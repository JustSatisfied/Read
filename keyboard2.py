import pyautogui
import random
import mouseMove
import time
keyboardRandomList = ['I', 'L', 'K']


def keyboardRandom():
    keybord = random.choice(keyboardRandomList)
    pyautogui.press(keybord)
    time.sleep(1)
    pyautogui.press(keybord)


def openTransction():
    mouseMove.mouseMove(2141, 1326, 30, 0)
    pyautogui.click()
    mouseMove.mouseMove(2064, 994, 30, 0)
    pyautogui.click()
    mouseMove.mouseMove(632, 330, 30, 0)
    pyautogui.click()
   


def closeTransction():
    mouseMove.mouseMove(1627, 196, 0, 0)
    pyautogui.click()


 