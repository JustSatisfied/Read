from pynput.keyboard import Key, Controller
import time
import pyautogui
import mouseMove

# 创建键盘控制器
keyboard = Controller()
 

email_icon=(1372,926)
select_icon=(477,468)
select_icon2=(627,467)
select_icon3=(700,1075)


def select_emial():
        i=0
        keyboard.press(Key.alt_l)
        keyboard.press('c')
# 模拟按住一段时间
        time.sleep(1)  # 这里模拟按住的时间，可以根据需要调整

# 释放按键
        keyboard.release('c')
        keyboard.release(Key.alt_l)
        mouseMove.mouseMove(email_icon[0],email_icon[1])
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        mouseMove.mouseMove(select_icon2[0],select_icon2[1])
        pyautogui.click()
        time.sleep(0.5)
        while i<5:
           i=i+1
           mouseMove.mouseMove(select_icon[0],select_icon[1])
           pyautogui.click()
           time.sleep(2)
           mouseMove.mouseMove(select_icon3[0],select_icon3[1])
           pyautogui.click()
        mouseMove.mouseMove(2100,1300)
        pyautogui.click()
        keyboard.press(Key.alt_l)
        keyboard.press('c')
# 模拟按住一段时间
        time.sleep(1)  # 这里模拟按住的时间，可以根据需要调整

# 释放按键
        keyboard.release('c')
        keyboard.release(Key.alt_l)
        

 