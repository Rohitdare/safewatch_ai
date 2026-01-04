from ultralytics import YOLO
import cv2

class WeaponDetector:
    def __init__(self, confidence_threshold=0.45):
        self.confidence_threshold = confidence_threshold
        
        self.model = YOLO(
            r"D:\dipesh\sentipersonal\safewatch-ai\runs\detect\safewatch_knife_v12\weights\best.pt"
        )


        # COCO class names we care about
        self.weapon_classes = ["knife", "gun"]

        print("✅ YOLOv8 model loaded successfully")

    def detect(self, frame):
        # Indented this block to belong to the detect method
        results = self.model(frame, verbose=False)
        detections = []

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls)
                class_name = self.model.names[cls_id]
                confidence = float(box.conf)

                # 🔍 LOG EVERYTHING FIRST
                print(f"[RAW DETECTION] class={class_name}, conf={confidence:.2f}")
                print(f"[DEBUG] cls_id={cls_id}, class={class_name}, conf={confidence:.2f}")


                if confidence >= self.confidence_threshold:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    detections.append({
                        "class": class_name,
                        "confidence": confidence,
                        "bbox": (x1, y1, x2, y2)
                    })

        return detections

    def draw_detections(self, frame, detections):
        # Indented this block to belong to the draw_detections method
        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            label = f"{det['class']} {det['confidence']:.2f}"

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )

        return frame