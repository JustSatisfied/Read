import cv2
import easyocr

# 创建 EasyOCR 实例
reader = easyocr.Reader(['ch_sim', 'en'])  # 选择语言
# 读取图像
image = cv2.imread('screenshotpl.png')

# 获取图像的宽度和高度
height, width, _ = image.shape

# 裁剪掉右侧 45 个像素宽度的部分
cropped_image = image[:, 0:width - 46]

# 保存裁剪后的图像
cv2.imwrite('cropped_image.png', cropped_image)

number = reader.readtext('cropped_image.png')
print(number)
 
