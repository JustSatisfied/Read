from ultralytics import YOLO

model = YOLO('./best.pt')

result = model('./c.jpg')
print(result[0].boxes)
