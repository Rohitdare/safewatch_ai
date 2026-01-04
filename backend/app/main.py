import time
import cv2
import json
import uuid


from pathlib import Path
from video.reader import VideoReader
from detection.detector import WeaponDetector
from alerts.temporal_engine import TemporalAlertEngine
from alerts.snapshot import save_snapshot
from alerts.severity import compute_severity



ALERTS_FILE = Path("backend/app/alerts/alerts.json")

def save_alert(alert: dict):
    if not ALERTS_FILE.exists():
        alerts = []
    else:
        content = ALERTS_FILE.read_text().strip()
        if not content:
            alerts = []
        else:
            alerts = json.loads(content)

    alerts.append(alert)
    ALERTS_FILE.write_text(json.dumps(alerts, indent=2))


# Configuration
temporal_engine = TemporalAlertEngine(
    window_seconds=5,
    min_detections=3,
    cooldown_seconds=30
)

VIDEO_PATH = r"D:\dipesh\sentipersonal\safewatch-ai\data\test_video (2).mp4"

# Initialize modules
reader = VideoReader(VIDEO_PATH, target_fps=1)
detector = WeaponDetector(confidence_threshold=0.30)

for frame in reader.read_frames():
    print("🟡 Processing frame...")
    detections = detector.detect(frame)

    for det in detections:
        # Check specifically for knives
        if det["class"] == "knife":
            print(f"🟡 Knife detected (conf={det['confidence']:.2f})")

            # Check if this detection triggers a temporal alert
            confirmed = temporal_engine.update(det["confidence"])

            # START of indented alert logic
            if confirmed:
                snapshot_path = save_snapshot(frame)

                severity = compute_severity(
                    detection_count=confirmed["count"],
                    avg_confidence=confirmed["avg_confidence"]
                )

                alert = {
                    "id": str(uuid.uuid4()),
                    "type": "knife_detected",
                    "severity": severity,
                    "confidence": round(confirmed["avg_confidence"], 2),
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "snapshot_path": snapshot_path
                }

                save_alert(alert)


                print("🚨 CONFIRMED RISK EVENT")
                print(f"🔴 Severity: {severity}")
                print(f"📸 Snapshot: {snapshot_path}")
            # END of indented alert logic

    # Visual feedback (This happens for every frame to keep the video moving)
    if detections:
        print(f"🚨 WEAPON DETECTED at {time.strftime('%H:%M:%S')}")
        for d in detections:
            print(f"   - {d['class']} ({d['confidence']:.2f})")
        
        # Draw boxes on the frame
        frame = detector.draw_detections(frame, detections)

    # Always show the frame
    cv2.imshow("SafeWatch AI - Weapon Detection", frame)

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()