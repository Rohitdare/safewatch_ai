import cv2
import time

class VideoReader:
    def __init__(self, video_path, target_fps=1):
        self.video_path = video_path
        self.target_fps = target_fps
        self.cap = cv2.VideoCapture(video_path)

        if not self.cap.isOpened():
            raise Exception("❌ Unable to open video source")

        # Original FPS of video
        self.original_fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_interval = int(self.original_fps / self.target_fps)

        if self.frame_interval <= 0:
            self.frame_interval = 1

        print(f"✅ Video opened | Original FPS: {self.original_fps} | Target FPS: {self.target_fps}")

    def read_frames(self):
        frame_count = 0

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("📴 End of video stream")
                break

            if frame_count % self.frame_interval == 0:
                yield frame  # Send frame forward

            frame_count += 1

        self.cap.release()
