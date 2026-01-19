# vision/dealer_signature_stamp.py

def detect_signature_stamp(images):
    return {
        "signature": {"present": False, "bbox": None},
        "stamp": {"present": False, "bbox": None}
    }
