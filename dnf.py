import currentWindow
from pynput.keyboard import Key, Controller
import time
import random
import pyautogui
import transcation
import easyocr
import cv2
from enum import Enum
import dnfMap
# 创建 EasyOCR 实例
reader = easyocr.Reader(['ch_sim', 'en'])  # 选择语言

# 读取图像中的文本


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


currentWindow.activeWindows('地下城')
currentWindow.resetPosition("地下城")
keyboard = Controller()
random_fengbao = random.uniform(5, 10)
icon_fengbao = (489-random_fengbao, 166-random_fengbao)
current_status = USER_LOCATION.ROOM
cureent_Map_position = 0
inital_pl = 134


def getBack():
    transcation.screen(1540, 278, 300, 38, 'back')
    back = reader.readtext('screenshotback.png')
    print("回" in back[0][1])
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


def userMoveRight(st=0.3, ed=0.3):
    random_ = random.uniform(st, ed)
    keyboard.press(Key.right)
    time.sleep(0.2)            # 按住上箭头键一秒钟（可根据需要调整）
    keyboard.release(Key.right)
    time.sleep(0.2)
    keyboard.press(Key.right)
    time.sleep(random_)
    keyboard.release(Key.right)
    time.sleep(0.2)       # 按住上箭头键一秒钟（可根据需要调整） # 释放上箭头键


def userMove(st, ed):
    random_ = random.uniform(st, ed)
    keyboard.press(Key.down)   # 按下上箭头键
    keyboard.press(Key.right)
    time.sleep(random_)            # 按住上箭头键一秒钟（可根据需要调整）
    keyboard.release(Key.down)  # 释放下箭头键
    keyboard.release(Key.right)  # 释放上箭头键
    time.sleep(0.2)


def skillRandom(randomSkill, time2=0.2):
    time_ = random.uniform(0, time2)
    skill = random.choice(randomSkill)
    keyboard.press(skill)
    time.sleep(time_)
    keyboard.release(skill)
    time.sleep(0.2)


def getMap(n):
    time.sleep(0.4)
    map_ = dnfMap.screenMap()
    while map_ == 12+(n*36) and map != 0:
        userMoveRight()
        map_ = dnfMap.screenMap()
    if n == 5:
        time.sleep(14)
        if getBack() == True:
            pyautogui.keyDown('f2')
            pyautogui.keyUp('f2')


def one():
    global cureent_Map_position
    global inital_pl
    inital_pl = inital_pl-1
    cureent_Map_position = 1

    userMove(0.2, 0.2)
    userMoveRight(0.3, 0.3)
    getMap(0)


def two():
    global cureent_Map_position
    global inital_pl
    inital_pl = inital_pl-1
    userMove(0.25, 0.25)
    skillRandom(['a'])
    userMoveRight(1.5, 1.8)
    getMap(1)


def three():
    print("进入")
    global inital_pl
    inital_pl = inital_pl-1
    userMove(0.1, 0.15)
    userMoveRight(0.2, 0.4)
    skillRandom([Key.alt])
    userMoveRight(1, 1.5)
    getMap(2)


def four():
    global inital_pl
    inital_pl = inital_pl-1
    skillRandom(["s"], 1.5)
    userMoveRight(1, 1.5)
    getMap(3)


def five():
    global inital_pl
    inital_pl = inital_pl-1
    userMoveRight(0.1, 0.15)
    userMove(0.2, 0.25)
    skillRandom(['f'], 1.5)
    userMoveRight(1, 1.5)
    getMap(4)


def six():
    global inital_pl
    inital_pl = inital_pl-1
    userMove(0.15, 0.2)
    skillRandom(['h'], 0.5)
    userMoveRight(1.5, 1.5)
    getMap(5)


def getProp():
    keyboardEnter('3')
    i = 0
    while i < 10:
        i = i+1
        keyboardEnter('x')


if inital_pl <= 188:
    skillRandom([Key.ctrl])
    one()
    two()
    three()
    four()
    five()
    six()
