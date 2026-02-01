import torch
import cv2
import math
from ultralytics import YOLO
import time
import requests
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

# ----------------- Telegram Bot Credentials -----------------
TELEGRAM_BOT_TOKEN = "8519823990:AAHlFrIh_xS5kLIQajSi5CfXgDlgzgBHZec"  # Replace this
TELEGRAM_CHAT_ID = "6015607235"

# ----------------- Twilio Credentials -----------------
account_sid = 'AC37b166b74540119cdbdb2fa952122a05'
auth_token = '523658817112799e27bc97da392dd3dc'
twilio_phone_number = '+1 575 900 5699'
to_phone_number = '+916201203734'  # Your mobile number
client = Client(account_sid, auth_token)

# ----------------- Static Location -----------------
latitude = 19.0483
longitude = 83.8322

# ----------------- YOLOv8 Model Setup -----------------
classNames = ["abuse", "attack", "chain snatching", "harash", "none", "rape", "women-men-knife-gun"]
# model = YOLO("C:/Users/vamsi/Desktop/women/women-safe-cam/runs/detect/train3/weights/best.pt")
model = YOLO('yolov8n.pt')

confidence_threshold = 0.50

# ----------------- Webcam Setup -----------------
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
cv2.namedWindow('Webcam', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Webcam', 1280, 720)

alert_triggered = False
alert_time = 0
cooldown_seconds = 30

