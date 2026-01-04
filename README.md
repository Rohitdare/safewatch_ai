🛡️ SafeWatch AI

Real-Time CCTV Risk Escalation System

🚀 Overview

SafeWatch AI is a real-time computer vision system that transforms traditional CCTV feeds into an active risk-escalation pipeline.

Instead of attempting unreliable “crime prediction,” SafeWatch focuses on early detection of high-risk visual signals (e.g., a person holding a knife) and combines machine learning, temporal logic, and severity reasoning to alert security teams faster and more reliably.

This project was built as:

🏆 A hackathon submission

🧩 A scalable system foundation

💼 A portfolio-ready, industry-aligned project

🎯 Problem Statement

Traditional CCTV systems are passive:

They only record footage

Operators must monitor screens continuously

Critical incidents are often noticed too late

SafeWatch AI augments CCTV with intelligence, enabling early warnings and faster human response without making unrealistic AI claims.

💡 Solution Philosophy

Detection ≠ Accusation
AI assists humans — it does not replace them

SafeWatch focuses on:

Risk escalation, not crime prediction

Explainable rules, not black-box claims

Reliability over hype

🧠 What SafeWatch AI Does (MVP)

✔ Real-time video ingestion
✔ Person & knife detection (YOLOv8, GPU-accelerated)
✔ Temporal confirmation (multi-frame persistence)
✔ Severity classification (LOW / MEDIUM / HIGH)
✔ Frame snapshot capture for evidence
✔ REST API (FastAPI)
✔ Live dashboard (HTML + JS)

⚠️ Gun detection is intentionally excluded in the MVP due to poor reliability in CCTV environments — this is a documented and deliberate design decision.

🏗️ System Architecture (High Level)
CCTV / Video Feed
        ↓
Frame Sampling (OpenCV)
        ↓
Object Detection (YOLOv8 + CUDA)
        ↓
Temporal Alert Engine
        ↓
Severity & Context Logic
        ↓
Snapshot Capture
        ↓
Alert Storage (JSON)
        ↓
FastAPI Backend
        ↓
Web Dashboard / API Consumers


⚙️ Tech Stack
Layer	Technology
Computer Vision	OpenCV
ML Framework	PyTorch (CUDA-enabled)
Object Detection	YOLOv8 (Ultralytics)
Backend API	FastAPI
Frontend	HTML + JavaScript
Acceleration	NVIDIA CUDA
Storage	JSON (hackathon-safe)
🧪 How the System Works
1️⃣ Detection

YOLOv8 detects persons and knives in video frames.

2️⃣ Temporal Confirmation

A single detection is treated as noise.
An alert is triggered only if detections persist across multiple frames within a time window.

3️⃣ Severity Scoring

Severity is computed using:

Detection count

Average confidence

Severity	Meaning
LOW	Weak / brief signal
MEDIUM	Persistent risk
HIGH	Persistent + high confidence
4️⃣ Snapshot Evidence

When a risk is confirmed, the exact frame is saved as visual proof.

5️⃣ Alert Exposure

Alerts are:

Stored persistently (alerts.json)

Served via REST API

Displayed on a live dashboard

▶️ Running the Project
1️⃣ Activate Environment
venv\Scripts\activate

2️⃣ Start Detection Pipeline
python backend/app/main.py

3️⃣ Start API & Dashboard
uvicorn backend.app.api:app --reload

4️⃣ Open Dashboard
http://127.0.0.1:8000

🌐 API Endpoints
Endpoint	Description
GET /alerts	List all alerts
GET /alerts/{id}	Alert details
GET /alerts/{id}/snapshot	Snapshot image
GET /docs	Swagger API docs
⚠️ Known Limitations (Honest & Intentional)

No gun detection in MVP (data unreliability)

No behavior or intent inference

Single-camera pipeline

JSON storage instead of DB (hackathon-appropriate)

These are design trade-offs, not oversights.

🔮 Roadmap

Person-weapon proximity logic

Pose estimation for aggression cues

Multi-camera support

Database persistence

Real-time WebSocket alerts

Mobile notifications

🏆 Hackathon Positioning

SafeWatch AI is positioned as:

A real-time CCTV risk escalation system that assists security teams by identifying persistent high-risk visual signals and reducing response time.

This framing is:

Technically honest

Industry-aligned

Judge-friendly

👥 Team Collaboration

ML core is complete

Backend is modular

Frontend can be extended independently

Clear separation of concerns

📜 License

This project is currently intended for educational and hackathon use.

🙌 Final Note

SafeWatch AI is not a demo script —
it is a real system built with real constraints, designed to be extended responsibly.
