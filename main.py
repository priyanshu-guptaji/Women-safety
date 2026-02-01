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

try:
    while True:
        success, img = cap.read()
        if not success:
            break

        results = model(img, stream=True)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])
                confidence_percentage = math.ceil(confidence * 100) / 100
                print("Confidence --->", confidence_percentage)

                if confidence_percentage > confidence_threshold:
                    cls = int(box.cls[0])
                    class_name = classNames[cls] if cls < len(classNames) else "unknown"

                    # Draw bounding box
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                    cv2.putText(img, class_name, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                    if not alert_triggered:
                        print("🚨 SOS ALERT TRIGGERED")
                        alert_triggered = True
                        alert_time = time.time()

                        # Save the alert image
                        image_path = "alert_frame.jpg"
                        cv2.imwrite(image_path, img)

                        # --- Twilio: Make Voice Call ---
                        try:
                            response = VoiceResponse()
                            response.say("SOS alert triggered. Immediate assistance needed.")
                            call = client.calls.create(
                                to=to_phone_number,
                                from_=twilio_phone_number,
                                twiml=response.to_xml()
                            )
                            print("📞 Twilio Call SID:", call.sid)
                        except Exception as e:
                            print("❌ Error calling via Twilio:", e)

                        # --- Telegram: Send Image ---
                        try:
                            with open(image_path, "rb") as photo:
                                photo_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
                                photo_res = requests.post(photo_url, data={"chat_id": TELEGRAM_CHAT_ID}, files={"photo": photo})
                                print("Telegram photo status:", photo_res.status_code)
                        except Exception as e:
                            print("❌ Error sending image:", e)

                        # --- Telegram: Send Location ---
                        try:
                            location_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendLocation"
                            loc_res = requests.post(location_url, data={
                                "chat_id": TELEGRAM_CHAT_ID,
                                "latitude": latitude,
                                "longitude": longitude
                            })
                            print("Telegram location status:", loc_res.status_code)
                        except Exception as e:
                            print("❌ Error sending location:", e)

                        # --- Telegram: Send Text Message ---
                        try:
                            message = f"🚨 SOS Alert: '{class_name}' detected with {confidence_percentage*100:.1f}% confidence."
                            text_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
                            text_res = requests.post(text_url, data={
                                "chat_id": TELEGRAM_CHAT_ID,
                                "text": message
                            })
                            print("Telegram message status:", text_res.status_code)
                        except Exception as e:
                            print("❌ Error sending text:", e)

        cv2.imshow('Webcam', img)

        # Auto-exit after cooldown
        if alert_triggered and (time.time() - alert_time > cooldown_seconds):
            print("✅ Alert sent. Exiting after 30 seconds cooldown.")
            break

        if cv2.waitKey(1) == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
