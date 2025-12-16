from app.model import model

def run_inference(frame):
    results = model(frame)

    detections = []

    for r in results:
        for box in r.boxes:
            detections.append({
                "class_id": int(box.cls),
                "confidence": float(box.conf),
            })
    
    return detections