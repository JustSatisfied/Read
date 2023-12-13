import pyautogui
import currentWindow
import random
import mouseMove
def userRandomMove():
   random_x=int(random.uniform(500,800))
   random_y= int(random.uniform(100,400))
   mouseMove.mouseMove(
     random_x,random_y,0,0)
   pyautogui.rightClick()

userRandomMove()