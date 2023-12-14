import currentWindow
import transcation
import time
import pyautogui
import mouseMove
import random
import os
import keyboard2
import user
from datetime import datetime

now = datetime.now()
currentWindow.activeWindows("命运方舟")

flag = 0


def buyGoods(price="10000", leavel=1, count="10"):
    press_random = random.uniform(0.5, 1)
    leval_ = (leavel-1)*70
    mouseMove.mouseMove(1575, 432+leval_, 35, 5)
    pyautogui.click()
    mouseMove.mouseMove(1839, 1175, 35, 5)
    pyautogui.click()
    mouseMove.mouseMove(1191, 728, 35, 5)
    pyautogui.click()
    pyautogui.press("backspace", presses=4)
    for c in list(count):
        pyautogui.press(c)
    mouseMove.mouseMove(1240, 769, 30)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press("backspace", presses=9)
    time.sleep(0.5)
    for p in list(price):
        pyautogui.press(p)
    mouseMove.mouseMove(1132, 1078, 30, 5)
    pyautogui.click()
    priceError()
    mouseMove.mouseMove(1136, 770, 30, 5)
    pyautogui.click()


def screenCut(leavel):
    for i in range(leavel):
        transcation.screen(1565, 432+(i*65), 37, 26, str(i+1))


def priceError():
    transcation.screen(1068, 710, 40, 30, "b")
    n = transcation.imgToNumber('screenshotb.png')
    try:
        num1 = int(n)
        pyautogui.moveTo(1159, 901, 0.3)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(1307, 230, 0.3)
        pyautogui.click()
        return num1
    except ValueError:
        print(n)
        return 3


def Transction():
    num1 = 10000
    num2 = 15000
    num3 = 100000
    time_random = random.uniform(3, 4)
    time.sleep(time_random)
    screenCut(4)
    imgNumber1 = transcation.imgToNumber('screenshot1.png')
    imgNumber2 = transcation.imgToNumber('screenshot2.png')
    imgNumber3 = transcation.imgToNumber('screenshot3.png')
    imgNumber4 = transcation.imgToNumber('screenshot4.png')
    try:
        num1 = int(imgNumber1)
    except ValueError:
        print(ValueError)

    try:
        num2 = int(imgNumber2)
    except ValueError:
        print(ValueError)
    try:
        num3 = int(imgNumber3)
    except ValueError:
        print(ValueError)
    try:
        num4 = int(imgNumber4)
    except ValueError:
        print(ValueError)
    print(num1, num2, num3, num4)
    print(num3 <= 99)
    if now.minute > 4:
        if num3 <= 99:
            buyGoods("99", 3, "20")
        elif num4 <= 150:
            buyGoods("150", 4)
        elif num2 <= 23:
            buyGoods("23", 2)
        elif num1 <= 21:
            buyGoods('21', 1)
    else:
        if num3 <= 99:
            buyGoods("99", 3, "30")
    try:
        os.remove("screenshot1.png")
        os.remove("screenshot2.png")
        os.remove("screenshot3.png")
        os.remove("screenshot4.png")
        os.remove("screenshotb.png")
    except FileNotFoundError:
        print(FileNotFoundError)
    pyautogui.moveTo(545, 1183, 0.3)
    pyautogui.click()


keyboard2.openTransction()
while True:
    flag = flag+1
    print(flag)
    if flag % 10 == 0:
        random_ = int(random.uniform(1, 3))
        if random_ == 2:
            keyboard2.keyboardRandom()
    else:
        Transction()
