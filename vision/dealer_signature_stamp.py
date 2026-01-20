# vision/dealer_signature_stamp.py

def detect_signature_stamp(image_paths):
    print("[INFO] Skipping YOLO detection (model not trained yet)")

    return {
        "signature": {
            "present": False,
            "bbox": None
        },
        "stamp": {
            "present": False,
            "bbox": None
        }
    }
