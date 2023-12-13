import currentWindow
import transcation
import time
import pyautogui
import mouseMove
import random
import os
import keyboard2
import user
currentWindow.activeWindows("命运方舟")

flag = 0


def buyGoods(price="10000", leavel=1, count="10"):
    press_random = random.uniform(0.5, 1)
    leval_ = (leavel-1)*70
    mouseMove.mouseMove(1575, 400+leval_, 35, 5)
    pyautogui.click()
    mouseMove.mouseMove(1839, 1152, 35, 5)
    pyautogui.click()
    mouseMove.mouseMove(1191, 690, 35, 5)
    pyautogui.click()
    pyautogui.press("backspace", presses=4)
    for c in list(count):
        pyautogui.press(c)
        time.sleep(press_random)
    mouseMove.mouseMove(1240, 730, 30)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press("backspace", presses=9)
    time.sleep(1)
    for p in list(price):
        pyautogui.press(p)
        time.sleep(press_random)
    mouseMove.mouseMove(1132, 1030, 30, 5)
    pyautogui.click()
    time.sleep(1)
    mouseMove.mouseMove(1136, 751, 30, 5)
    pyautogui.click()


def screenCut(leavel):
    for i in range(leavel):
        transcation.screen(1565, 400+(i*65), 35, 20, str(i+1))


def Transction():
    num1 = 10000
    num2 = 15000
    num3 = 100000
    time_random = random.uniform(3, 5)
    time.sleep(time_random)
    screenCut(3)
    imgNumber1 = transcation.imgToNumber('screenshot1.png')
    imgNumber2 = transcation.imgToNumber('screenshot2.png')
    imgNumber3 = transcation.imgToNumber('screenshot3.png')
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
    print(num1, num2, num3)
    if num1 <= 18:
        buyGoods("18", 1)
    if num2 <= 20:
        buyGoods("20", 2)
    if num3 <= 150:
        buyGoods("150", 3)

    os.remove("screenshot1.png")
    os.remove("screenshot2.png")
    os.remove("screenshot3.png")
    pyautogui.moveTo(545, 1150, 0.3)
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
