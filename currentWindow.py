import pygetwindow as gw
import pyautogui
import win32gui
import win32con
import transcation
import win32gui

window_center_x = None
window_center_y = None


def getCurrentWindow(name):
    all_windows = gw.getAllWindows()
    target_window = None
    for window in all_windows:
        if name in window.title:
            target_window = window
            break
    return target_window

# 刷新607 1233


def activeWindows(name):
    matching_windows = []

    def enum_windows_callback(hwnd, lParam):
        if name.lower() in win32gui.GetWindowText(hwnd).lower():
            matching_windows.append(hwnd)
    win32gui.EnumWindows(enum_windows_callback, None)
    if matching_windows:
        window_handle = matching_windows[0]
        win32gui.ShowWindow(window_handle, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(window_handle)
        window_rect = win32gui.GetWindowRect(window_handle)
        window_x, window_y, window_width, window_height = window_rect
        window_center_x = window_x + window_width // 2
        window_center_y = window_y + window_height // 2
        pyautogui.moveTo(window_center_x, window_center_y, duration=1)
        # transcation.screen(1298, 392, 49, 38)
        # transcation.screen(1527, 392, 49, 38, "3")
        # transcation.screen(1740, 392, 49, 38, "4")
        # transcation.screen(1298, 470, 49, 38, "5")
        # transcation.screen(1527, 470, 49, 38, "6")
        # transcation.screen(1740, 470, 49, 38, "7")


def resetPosition(window_title):
    windows = []
    win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), windows)
    
    # 进行模糊匹配
    matching_windows = [hwnd for hwnd in windows if window_title.lower(
    ) in win32gui.GetWindowText(hwnd).lower()]

    if len(matching_windows) == 0:
        return None
    win32gui.SetWindowPos(matching_windows[0], 0, 0, 0, 0, 0, 0x0001)

def get_window_resolution(window_title):
    # 获取所有窗口列表
    windows = []
    win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), windows)
    
    # 进行模糊匹配
    matching_windows = [hwnd for hwnd in windows if window_title.lower(
    ) in win32gui.GetWindowText(hwnd).lower()]

    if len(matching_windows) == 0:
        return None

    # 获取匹配窗口的分辨率
    hwnd = matching_windows[0]
    window_rect = win32gui.GetClientRect(hwnd)
    width = window_rect[2] - window_rect[0]
    height = window_rect[3] - window_rect[1]

    return width, height


def getScreenSise():
    screen_width, screen_height = pyautogui.size()
    return screen_height, screen_width


def hight_map_coordinate(old_resolution, new_resolution, ):
    def map_coordinates(position):
        # 获取旧分辨率和新分辨率的宽高
        old_width, old_height = old_resolution
        new_width, new_height = new_resolution

    # 计算宽高比例
        width_ratio = new_width / old_width
        height_ratio = new_height / old_height

    # 计算新坐标
        new_x = int(position[0] * width_ratio)
        new_y = int(position[1] * height_ratio)

        return new_x, new_y

    return map_coordinates

resetPosition("命运方舟")
