SafeWatch AI is a real-time computer vision system that analyzes CCTV video feeds to identify potentially dangerous situations and escalate risk early to security personnel.

Instead of attempting unreliable “crime prediction,” SafeWatch focuses on early risk signals (e.g., a person holding a knife) and combines machine learning + temporal logic to reduce response time and human monitoring load.

This project is being built as:

🎯 A hackathon submission

🧩 A scalable foundation for future features

📁 A portfolio-ready, industry-aligned system

🎯 Problem Statement

Traditional CCTV systems are passive:

They record footage but do not analyze it in real time

Security staff must monitor multiple screens continuously

Critical events are often noticed too late

SafeWatch AI transforms CCTV from passive recording into an active risk escalation system.

💡 Solution Approach

Instead of detecting “crimes,” SafeWatch focuses on:

Early identification of high-risk visual signals
and escalating them for human review

Core Design Philosophy

Detection ≠ accusation

AI assists humans, it does not replace them

Reliability > hype

🧠 What the System Currently Detects (MVP)

✔ Person presence
✔ Knife detection (fine-tuned YOLOv8 model)
✔ Real-time frame processing
✔ Console-based alert logs

⚠️ Gun detection is intentionally excluded in MVP due to reliability issues in CCTV footage (documented limitation).

🏗️ System Architecture (High-Level)
Video Input (MP4 / CCTV)
        ↓
Frame Extraction (OpenCV)
        ↓
Object Detection (YOLOv8 – fine-tuned)
        ↓
Temporal Logic (next phase)
        ↓
Alert Engine
        ↓
Security Personnel / Dashboard

📂 Project Structure
safewatch-ai/
│
├── backend/
│   ├── app/
│   │   ├── main.py              # Entry point
│   │   ├── video/
│   │   │   └── reader.py        # Video ingestion & FPS control
│   │   ├── detection/
│   │   │   └── detector.py      # YOLOv8 inference logic
│   │   ├── datasets/
│   │   │   └── weapons/         # Training dataset (knife-focused)
│   │   └── scripts/
│   │       └── remap_labels.py  # Dataset label cleanup
│   │
│   ├── requirements.txt
│   └── .env
│
├── data/
│   └── test_video.mp4           # Test footage
│
├── runs/
│   └── detect/
│       └── safewatch_knife_v12/ # Trained model (best.pt)
│
└── README.md

⚙️ Environment Setup
1️⃣ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

2️⃣ Install Dependencies
pip install -r backend/requirements.txt


Key libraries:

OpenCV

Ultralytics (YOLOv8)

FastAPI (future backend)

Torch (CPU)

📹 Video Ingestion (Phase 1)

Video is read using OpenCV

FPS is intentionally downsampled (1–5 FPS) to reduce compute

Each frame is passed to the detection pipeline

This ensures:

Stable real-time performance

Predictable latency

🧠 Machine Learning (Phase 2)
Model

YOLOv8n

Fine-tuned on a knife-focused dataset

Classes:

0 → person

1 → knife

Why Knife-Only?

Knife detection is significantly more reliable than gun detection in CCTV

Gun datasets often suffer from label contamination

Industry systems rely on context + behavior, not gun-only detection

Model Used
runs/detect/safewatch_knife_v12/weights/best.pt


Metrics achieved (after ~2–3 epochs on CPU):

Precision ≈ 0.83

mAP@0.5 ≈ 0.81

Good enough for:

Hackathon demo

Real-time testing

Alert pipeline integration

🧪 Running the System

From project root:

venv\Scripts\activate
python backend/app/main.py


Expected output:

Video opened | Target FPS: 1
YOLOv8 model loaded
Processing frame...
[DETECTION] knife (0.62)
🚨 RISK EVENT DETECTED

🚨 Current Alert Behavior

Detection logs are printed to console

Knife detection triggers an immediate alert log

No dashboard yet (next phase)

🔜 What’s Coming Next (Planned)
Phase 3 — Temporal Alert Engine

Require knife detection across multiple frames

Reduce false positives

Severity scoring

Phase 4 — Context Awareness

Location-based rules

Person proximity logic

Phase 5 — UI & Notifications

Web dashboard

SMS / WebSocket alerts

⚠️ Known Limitations (Explicit & Honest)

Gun detection intentionally excluded (unreliable in CCTV)

No behavior understanding yet

Single-camera support in MVP

These are design decisions, not shortcomings.

🏆 Hackathon Positioning

SafeWatch AI is positioned as:

“A real-time risk escalation system that assists security teams by identifying high-risk visual signals in CCTV feeds and reducing response time.”

This framing is:

Technically honest

Judge-friendly

Scalable

👥 Team Collaboration Notes

If you’re joining this project:

Focus on logic, UI, or backend

ML core is already functional

Avoid retraining models unless necessary

Respect the “risk escalation, not crime prediction” philosophy

📜 License

This project is currently for educational and hackathon use.
Licensing will be finalized if productized.

🙌 Final Note

This is not a demo script.
This is a real system built with real constraints, designed to be extended responsibly.
