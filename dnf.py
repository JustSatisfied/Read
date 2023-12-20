import currentWindow
from pynput.keyboard import Key, Controller
import time
import random
import pyautogui
import transcation
import easyocr

# 创建 EasyOCR 实例
reader = easyocr.Reader(['ch_sim', 'en'])  # 选择语言

# 读取图像中的文本


currentWindow.activeWindows('地下城')
currentWindow.resetPosition("地下城")
keyboard = Controller()
random_fengbao = random.uniform(5, 10)
icon_fengbao = (489-random_fengbao, 166-random_fengbao)


def getPL():
    pyautogui.moveTo(1620, 1172, 0.4)
    transcation.screen(1635, 1095, 85, 38, 'pl')
    number = reader.readtext('screenshotpl.png')
    print(number)
    return number[0][1][:3]


inital_value = int(getPL())

print(inital_value)


def screenPL(inital=0):
    number = getPL()
    print(number, 'i', inital_value)
    if int(number) != inital:
        homeMove(0.2, 0.25)
        time.sleep(1)
        screenPL(inital)
    return number


def keyboardEnter(key):
    random_ = random.uniform(0.1)
    keyboard.press("x")
    time.sleep(random_)
    keyboard.release("x")


def homeMove(st=1, ed=2):
    keyboard.press(Key.right)
    random_ = random.uniform(st, ed)
    time.sleep(random_)
    keyboard.release(Key.right)    # 按下上箭头键


def enterFengbao():
    pyautogui.moveTo(icon_fengbao[0], icon_fengbao[1], 0.5)
    time.sleep(0.25)
    keyboard.press(Key.enter)
    time.sleep(0.25)
    keyboard.release(Key.enter)


def userMoveRight(st, ed):
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


def one():
    global inital_value
    userMoveRight(0.4, 0.8)
    inital_value = inital_value-1
    screenPL(inital_value)


def two():
    global inital_value
    userMoveRight(0.2, 0.4)
    userMove(0.25, 0.3)
    skillRandom(['g', 'a'])
    userMoveRight(1.5, 1.8)
    inital_value = inital_value-1
    screenPL(inital_value)


def three():
    global inital_value
    userMoveRight(0.2, 0.4)
    
    skillRandom([Key.alt])
    userMoveRight(1, 1.5)
    inital_value = inital_value-1
    screenPL(inital_value)


def four():
    global inital_value
    userMoveRight(0.2, 0.4)
    skillRandom(['s'], 1.5)
    userMoveRight(1, 1.5)
    inital_value = inital_value-1
    screenPL(inital_value)


def five():
    global inital_value
    userMoveRight(0.2, 0.4)
     
    skillRandom(['e'], 1.5)
    userMoveRight(1, 1.5)
    inital_value = inital_value-1
    screenPL(inital_value)


def six():
    global inital_value
    userMove(0.15, 0.2)
    skillRandom(['h'], 0.5)
    userMoveRight(1, 1.5)
    inital_value = inital_value-1
    screenPL(inital_value)


def getProp():
    keyboardEnter('3')
    i = 0
    while i < 10:
        i = i+1
        keyboardEnter('x')


skillRandom([Key.ctrl])
one()
two()
three()
four()
five()
six()


while inital_value != 0:
    skillRandom([Key.ctrl])
    one()
    two()
    three()
    four()
    five()
    six()
    time.sleep(10)
    getProp()
    keyboardEnter('F2')
    time.sleep(3)
