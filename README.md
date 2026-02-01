<div align="center">

# 🚨 Women Safety Analytics  
### *AI-Driven Behavioral Distress Recognition System*  
**HackNagpur Hackathon Project**

Protecting Women from Safety Threats using Real-Time AI Intelligence  

---

</div>

---

## 🌟 Overview

**Women Safety Analytics** is an intelligent, proactive safety system that automatically detects potential physical threats or distress situations using real-time video analytics and contextual artificial intelligence.

Unlike traditional safety applications that rely on manual SOS triggers, this system continuously monitors the environment, identifies dangerous behavior, and silently dispatches emergency alerts with location and incident context.

> 💡 Think of it as an **intelligent digital guardian** that works silently in the background and calls for help even when the victim cannot.

---

## 🎯 Key Objectives

- 🔍 Detect physical threats and distress situations in real time  
- 🚫 Remove dependency on manual panic button activation  
- 🧠 Minimize false alerts using multi-signal verification  
- 📢 Instantly notify emergency contacts and law enforcement  
- 🖥️ Provide centralized monitoring for authorities  
- 🔁 Continuously improve detection accuracy  

---

## 🏗️ System Architecture (High-Level)

The solution is composed of five intelligent layers:

1️⃣ Mobile Application Layer  
2️⃣ AI Processing Layer  
3️⃣ Verification & Decision Layer  
4️⃣ Alert & Communication Layer  
5️⃣ Admin & Analytics Layer  

Each layer operates independently yet communicates securely via APIs.

---

## 🧩 Component-Wise Solution Breakdown

---

### 📱 4.1 Mobile Application (User Side)

- User launches the app and selects **Start Journey**  
- App runs silently in background  
- Uses phone camera (screen-off / discreet mode)  
- Streams frames to backend or processes locally  

**Responsibilities**

- Camera access  
- GPS tracking  
- Secure data transmission  
- Receiving verification prompts  

---

### 🤖 4.2 Real-Time Threat Detection Engine

Powered by **YOLO Deep Learning Model**

Detects:

- Aggressive gestures  
- Struggle patterns  
- Abnormal body movements  

**Processing Pipeline**

1. Capture frame  
2. Resize & normalize  
3. Model inference  
4. Generate confidence score  

➡ If confidence exceeds threshold → **Potential threat flagged**

---

### 🔍 4.3 Multi-Signal Verification Layer

To reduce false positives:

- 🎤 Audio distress analysis  
- ❤️ Optional wearable heart-rate signals  
- ⏱️ Temporal consistency checks  

**Decision Logic**

- Multiple signals agree → Confirm threat  
- Ambiguous → Silent verification  
- No response → Escalate  

---

### 🚨 4.4 Automated SOS & Alert Dispatcher

When threat is confirmed:

- Collects GPS, timestamp, user ID, incident type  
- Sends alerts via:

  - 📩 SMS  
  - 📞 Call  
  - 🔔 Push Notification  

**Recipients**

- Emergency contacts  
- Nearest police station  

Includes **Google Maps Live Location Link**

---

### 🖥️ 4.5 Admin Dashboard & Control Room Panel

- 🗺️ Live alert map  
- 👤 Victim details  
- 📌 Incident status  
- 🚓 Dispatch & resolution controls  

---

### 📊 4.6 Post-Incident Learning Module

- Stores anonymized outcomes  
- Used for periodic model retraining  
- Improves accuracy over time  

---

## 🔁 System Workflow

1. User starts journey  
2. Camera analyzed continuously  
3. AI detects threat  
4. Verification layer confirms  
5. Alert dispatched  
6. Authorities respond  
7. Incident logged  
8. Model learns  

---

## 🧪 Technology Stack

| Layer | Technology |
|-----|-----------|
| AI Model | YOLO |
| Programming Language | Python |
| Video Processing | OpenCV |
| Dataset & Training | Roboflow |
| Alerts | Twilio API |
| Mobile App | Android / Flutter |
| Backend | Flask / FastAPI |
| Dashboard | React + Node.js |
| Database | MongoDB / PostgreSQL |

---

## 🔐 Security & Privacy

- 🔒 Encrypted communication  
- 🗂️ Minimal data storage  
- 🧑‍💻 Anonymized training data  
- 🔑 Role-based access control  

---

## 📈 Scalability

- Microservices architecture  
- Cloud deployment ready  
- Containerized services  
- City-wide expansion support  

---

## 🚀 Expected Outcomes

- Faster emergency response  
- Reduced assault severity  
- Increased confidence among women  
- Safer public environments  

---

## 🔮 Future Enhancements

- ⌚ Smartwatch integration  
- 📶 Offline edge inference  
- 👤 Facial recognition for repeat offenders  
- 🏛️ Government database integration  
- 🌍 Multilingual support  

---

## 👥 Team Details (HackNagpur)

| Name | Email |
|-----|------|
| Priyanshu Gupta | 23cse513.priyanshugupta@giet.edu |
| Aditya Sharma | as67jsr@gmail.com |
| Subrat Pandey | 23cse514.subratpandey@giet.edu |
| P Vamsi Krishna | mlwithkrishna@gmail.com |

---

## ✅ Conclusion

**Women Safety Analytics** represents a shift from reactive safety solutions to a **proactive, intelligent, and automated protection system**.

By combining real-time AI, contextual verification, and instant communication, the project aims to reduce response time, prevent escalation of violence, and help build safer cities.

---

