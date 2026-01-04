import cv2
import os
import time

SNAPSHOT_DIR = "backend/app/alerts/snapshots"

def save_snapshot(frame):
    """
    Saves a frame snapshot to disk and returns file path.
    """
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"alert_{timestamp}.jpg"
    filepath = os.path.join(SNAPSHOT_DIR, filename)

    cv2.imwrite(filepath, frame)

    return filepath
