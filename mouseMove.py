import pyautogui
import random
import currentWindow


def randomMouseMove():
    count_random = int(random.uniform(0, 2))
    for i in range(count_random):
        position_random_x = random.uniform(0, 1546)
        posiiton_random_y = random.uniform(0, 1000)
        count_move_random = random.uniform(0.3, 0.8)
        pyautogui.moveTo(position_random_x,
                         posiiton_random_y, count_move_random)


def mouseMove(x, y, floatx=0, floaty=0):
    move_random = random.uniform(0.3, 0.8)
    float_random_x = random.uniform(0, floatx)
    float_random_y = random.uniform(0, floaty)
    randomMouseMove()
    pyautogui.moveTo(x-float_random_x,y-float_random_y, move_random)
