import currentWindow
from pynput.keyboard import Key, Controller
import time
import random
import pyautogui
import transcation
from ultralytics import YOLO
import easyocr
import cv2
from enum import Enum
import dnfMap
import cv2
import requests
import numpy as np

# 创建 EasyOCR 实例
reader = easyocr.Reader(['ch_sim', 'en'])  # 选择语言
currentWindow.activeWindows('地下城')
currentWindow.resetPosition("地下城")
# 读取图像中的文本

userModel = YOLO('./user.pt')


class USER_LOCATION(Enum):
    ROOM = 1
    FENNG = 2


keyborad_distance = {
    "a": 0,
    "s": 1,
    "d": 2,
    "f": 3,
    "g": 4,
    "h": 5,
}
keyboard = Controller()
random_fengbao = random.uniform(5, 10)
icon_fengbao = (489-random_fengbao, 166-random_fengbao)
current_status = USER_LOCATION.ROOM
cureent_Map_position = 0
inital_pl = 134


def getBack():
    transcation.screen(1540, 278, 300, 38, 'back')
    back = reader.readtext('screenshotback.png')

    return "回" in back[0][1]


def getSkillCD(key):
    number = 0
    distance = keyborad_distance[key]*70
    transcation.screen(772+distance, 1132, 25, 32, "skill")
    imgNumber = transcation.imgToNumber('screenskill.png')
    try:
        number = int(imgNumber)
    except ValueError:
        print(ValueError)
    return number


# inital_value = int(getPL())


# def screenPL(inital=0):
#     number = getPL()
#     print(number, 'i', inital_value)
#     if int(number) != inital:
#         homeMove(0.2, 0.25)
#         time.sleep(1)
#         screenPL(inital)
#     return number

key_ = {
    "up": Key.up,
    "down": Key.down,
    "right": Key.right,
    "left": Key.left,
}

MonsterList = [1.0, 4.0, 5.0, 6.0]


def keyboardEnter(key):
    random_ = random.uniform(0.1)
    keyboard.press("x")
    time.sleep(random_)
    keyboard.release("x")


def homeMove(st=1, ed=2):
    keyboard.press(Key.right)
    random_ = random.uniform(st, ed)
    time.sleep(random_)
    keyboard.release(Key.right)


def enterFengbao():
    pyautogui.moveTo(icon_fengbao[0], icon_fengbao[1], 0.5)
    time.sleep(0.25)
    keyboard.press(Key.enter)
    time.sleep(0.25)
    keyboard.release(Key.enter)

    # 按住上箭头键一秒钟（可根据需要调整） # 释放上箭头键


def userMove(key_):
    keyboard.press(key_)
    time.sleep(0.05)
    keyboard.release(key_)
    time.sleep(0.05)
    keyboard.press(key_)
    if key_ == Key.right or key_ == Key.left:
        time.sleep(0.25)
    else:
        time.sleep(0.1)
    keyboard.release(key_)


def skillRandom(randomSkill):
    skill = random.choice(randomSkill)
    keyboard.press(skill)
    time.sleep(0.1)
    keyboard.release(skill)


def dnfScreen():
    transcation.screen(0, 0, 1920, 1200, 'DNF')


def getTag(model):

    return model[0].boxes.cls.tolist()


def getFirstTag(model):
    if len(model[0].boxes.cls) > 0:
        return model[0].boxes.cls[0].tolist()
    return 2


def getPosition(model, index):
    return model[0].boxes.xyxy[index].tolist()


def getModelX(model, tag):
    list = getTag(model)
    if tag in list:
        index_of = list.index(tag)
        return getPosition(model, index_of)[2]


def getModelY(model, tag):
    list = getTag(model)
    if tag in list:
        index_of = list.index(tag)
        return getPosition(model, index_of)[3]


def isHaveMonster(model):
    print(model[0].boxes)
    tagList = getTag(model)
    for element in MonsterList:
        if element in tagList:
            return True
    return False


def recentMonster(model, UserX):
    MonsterList = [1.0, 4.0, 5.0, 6.0]
    tagList = getTag(model)
    min = 999999
    i = 0
    for element in MonsterList:
        if element in tagList:
            index_of = tagList.index(element)
            x_ = getPosition(model, index_of)[2]
            distance_x = abs(UserX-x_)
            if min > distance_x:
                min = MonsterList[index_of]
    return min


def isHaveChuansong(model):
    if 3.0 in getTag(model):
        return True
    return 1


source = "screenshotDNF.png"

# // 0 BOSS 1 4 5 GUAIWU  wupin 6  7jinzhi

random_skill = ['a', 's', 'd', 'f', 'q', 'w', 'e', 'r', 't']

# 初始化 YOLOv8n 模型
model = YOLO('./best.pt')

# 打开视频流
cap = cv2.VideoCapture('http://127.0.0.1:5000/')  # 将视频流的 URL 作为参数传递

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    source = "screenshotDNF.png"
# // 0 BOSS 1 4 5 GUAIWU  wupin 6  7jinzhi
    random_skill = ['a', 's', 'd', 'f', 'q', 'w', 'e', 'r', 't']
    userResult = userModel.track(frame, persist=True)
    result = model.track(frame, persist=True)
    tagList = getTag(result)
    User = getFirstTag(userResult)
    if User != 2:
        print(
            len(getTag(result)) == 0,
            isHaveMonster(result),
            isHaveChuansong(result) and all(
                element == 3.0 for element in getTag(result)) and User,
            '------'
        )
        UserX = getModelX(userResult, User)
        UserY = getModelY(userResult, User)
        # if User == 2:
        #     print('进入1')
        #     userMove(key_['right'], 0.3)
        #     continue
        if len(getTag(result)) == 0:
            print('进入2')
            userMove(key_['right'])
            continue
        if isHaveMonster(result) and User != 2:
            print(result[0].boxes)
            Monster = recentMonster(result, UserX)
            MonsterY = getModelY(result, Monster)
            MonsterX = getModelX(result, Monster)
            if MonsterY and MonsterX:
                print('进入1234')
                if UserY-y < -25:
                    userMove(key_["down"])
                elif UserY-y > 25:
                    userMove(key_["up"])
                if UserX-MonsterX > 300:
                    userMove(key_["left"])
                elif UserX-MonsterX < -300:
                    userMove(key_['right'])
                skillRandom([random.choice(random_skill)])
                continue
            else:
                userMove(key_['right'])
        if isHaveChuansong(result) and all(element == 3.0 for element in getTag(result)) and User == 0.0:
            indices_of_sevens = [index for index,
                                 value in enumerate(tagList) if value == 3.0]
            print(indices_of_sevens)
            array_ = []
            for i in indices_of_sevens:
                y = getPosition(result, i)[3]
                x = getPosition(result, i)[2]
                if y > 600 and y < 1100 and x > 1400:
                    array_.append(i)
            if len(array_) == 0:
                userMove(key_['right'])
                continue
            i = array_[0]
            print('进入3')
            y = getPosition(result, i)[3]
            x = getPosition(result, i)[2]
            if y > 600 and y < 1100:
                print("进入4")
                if UserY-y < 0:
                    userMove(key_["down"])
                else:
                    userMove(key_["up"])
                if UserX-x > 0:
                    userMove(key_["left"])
                else:
                    userMove(key_['right'])
            continue

    # 释放资源
cap.release()
cv2.destroyAllWindows()
