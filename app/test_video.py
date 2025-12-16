from app.video_processor import read_video

video_path = "data/raw/bottle-detection.mp4"

for i, frame in enumerate(read_video(video_path)):
    print(f"Frame {i} shape: {frame.shape}")

    if i == 5:
        break