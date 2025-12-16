from app.video_processor import read_video
from app.inference import run_inference

video_path = "data/raw/bottle-detection.mp4"

for i, frame in enumerate(read_video(video_path)):
    detections = run_inference(frame)
    print(f"Frame {i} detections: {detections}")
    if i == 3:
        break