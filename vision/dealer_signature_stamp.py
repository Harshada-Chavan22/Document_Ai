# vision/dealer_signature_stamp.py
from ultralytics import YOLO

model = YOLO("models/best.pt")

def detect_signature_stamp(image_paths):
    signature = {"present": False, "bbox": None}
    stamp = {"present": False, "bbox": None}

    for img_path in image_paths:
        results = model(img_path)

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                bbox = box.xyxy[0].tolist()

                if cls == 0:
                    signature = {"present": True, "bbox": bbox}
                elif cls == 1:
                    stamp = {"present": True, "bbox": bbox}

    return {"signature": signature, "stamp": stamp}
