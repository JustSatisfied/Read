from pynput.mouse import Listener
import pyautogui
import pytesseract
from PIL import Image
 
def on_click(x, y, button, pressed):
    if pressed:
        print(f"鼠标点击位置：X={x}, Y={y}")


# with Listener(on_click=on_click) as listener:
#     listener.join()


def screen(x, y, width, height, name=""):
    # 截取指定区域的图像
 
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    
# 保存截图
    screenshot.save('screenshot'+name+".png")

def  imgToNumber(file_name): 
# 打开图像文件
  img = Image.open(file_name)  # 替换为你的图像文件名

# 配置 Tesseract OCR，只识别数字
  custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'

# 使用 Tesseract 进行文字识别
  text = pytesseract.image_to_string(img, config=custom_config)
 
  return text


 