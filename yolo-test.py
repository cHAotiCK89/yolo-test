from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

results = model("testphotos/test-1.jpg",save=True)