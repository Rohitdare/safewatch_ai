import time
import cv2

from video.reader import VideoReader
from detection.detector import WeaponDetector

VIDEO_PATH = "data/test_video3.mp4"

# Initialize modules
reader = VideoReader(VIDEO_PATH, target_fps=1)
detector = WeaponDetector(confidence_threshold=0.30)

for frame in reader.read_frames():
    print("🟡 Processing frame...")
    detections = detector.detect(frame)
    
    if detections:
        print(f"🚨 WEAPON DETECTED at {time.strftime('%H:%M:%S')}")
        for d in detections:
            print(f"   - {d['class']} ({d['confidence']:.2f})")

        frame = detector.draw_detections(frame, detections)

    cv2.imshow("SafeWatch AI - Weapon Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()