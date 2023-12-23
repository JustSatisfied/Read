import transcation
import currentWindow
import cv2
import numpy as np

# 读取图像

currentWindow.activeWindows("地下城")


def screenMap():
    transcation.screen(1690, 131, 300, 32, "map")
    x1 = 0
    image = cv2.imread('screenshotmap.png')  # 替换为你的图像路径

# 定义浅蓝色的颜色范围（例如，假设浅蓝色在 HSV 颜色空间中的范围）
    lower_blue = np.array([90, 50, 50])   # 请根据实际情况调整下限
    upper_blue = np.array([130, 255, 255])  # 请根据实际情况调整上限

# 将图像转换为 HSV 颜色空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 创建蓝色区域的掩码
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

# 寻找轮廓
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 获取最大的轮廓（颜色集中区域）
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(max_contour)
        x1=x
        # 在图像上标记区域
        marked_image = image.copy()
        cv2.rectangle(marked_image, (x, y), (x + w, y + h),
                      (0, 255, 0), 2)  # 在图像上绘制矩形

        # 保存标记后的图像
        cv2.imwrite('marked_image.jpg', marked_image)  # 将标记后的图像保存为新文件
        print("The most concentrated light blue area coordinates: (x={}, y={}, w={}, h={})".format(
            x, y, w, h))
        print("A new image 'marked_image.jpg' has been created with the marked area.")
    else:
        print("No light blue area found.")
    return x1
