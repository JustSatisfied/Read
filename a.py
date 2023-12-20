import transcation
import currentWindow
import pyautogui
currentWindow.activeWindows('地下城')
pyautogui.moveTo(1620, 1172, 0.4)
transcation.screen(1635, 1095, 85, 36, 'pl')
number = transcation.imgToNumber('screenshotpl.png')
print(number)
print(number.split('188')[0])