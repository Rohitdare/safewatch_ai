import time
from collections import deque

class TemporalAlertEngine:
    def __init__(
        self,
        window_seconds=5,
        min_detections=3,
        cooldown_seconds=30
    ):
        self.window_seconds = window_seconds
        self.min_detections = min_detections
        self.cooldown_seconds = cooldown_seconds

        self.detection_buffer = deque()
        self.last_alert_time = 0

    def update(self, confidence):
        """
        Call this whenever a knife is detected.
        """
        current_time = time.time()

        # Add detection
        self.detection_buffer.append({
            "time": current_time,
            "confidence": confidence
        })

        # Remove old detections outside time window
        while self.detection_buffer and \
              current_time - self.detection_buffer[0]["time"] > self.window_seconds:
            self.detection_buffer.popleft()

        # Cooldown check
        if current_time - self.last_alert_time < self.cooldown_seconds:
            return None  # Changed False to None for consistency

        # Rule: enough detections?
        if len(self.detection_buffer) >= self.min_detections:
            self.last_alert_time = current_time

            count = len(self.detection_buffer)
            avg_confidence = sum(
                d["confidence"] for d in self.detection_buffer
            ) / count

            # Clear buffer after alert to prevent immediate re-triggering
            self.detection_buffer.clear()

            return {
                "count": count,
                "avg_confidence": avg_confidence
            }

        return None