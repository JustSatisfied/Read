import ctypes
import time
import currentWindow
import pyautogui
currentWindow.activeWindows('地')

# 定义一些常量
MOUSEEVENTF_LEFTDOWN = 0x0002  # 左键按下
MOUSEEVENTF_LEFTUP = 0x0004  # 左键释放
MOUSEEVENTF_MIDDLEDOWN = 0x0020  # 中键按下
MOUSEEVENTF_MIDDLEUP = 0x0040  # 中键释放
MOUSEEVENTF_RIGHTDOWN = 0x0008  # 右键按下
MOUSEEVENTF_RIGHTUP = 0x0010  # 右键释放
pyautogui.moveTo(541, 803)
# 获取用户32.dll模块
user32 = ctypes.WinDLL('user32', use_last_error=True)

# 获取屏幕的宽度和高度（可以根据需要更改坐标）
click_x, click_y = 541, 803  # 示例中的坐标 (x, y)

# 等待一段时间以确保有足够的时间切换到您想要点击的窗口或位置


# 移动鼠标到指定位置
user32.SetCursorPos(click_x, click_y)

# 模拟鼠标左键单击
user32.mouse_event(MOUSEEVENTF_LEFTDOWN, click_x, click_y, 0, 0)
time.sleep(1)
user32.mouse_event(MOUSEEVENTF_LEFTUP, click_x, click_y, 0, 0)

user32.SetCursorPos(896, 696)

while True:
    user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 896, 696, 0, 0)
    time.sleep(1)
    user32.mouse_event(MOUSEEVENTF_LEFTUP, 896, 696, 0, 0)
