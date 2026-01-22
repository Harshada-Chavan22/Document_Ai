def detect_signature_stamp(image_paths):
    """
    Stub detector for Signature & Stamp.
    Designed to be YOLO-compatible later.
    """

    # Default output
    signature = {
        "present": False,
        "bbox": None
    }

    stamp = {
        "present": False,
        "bbox": None
    }

    # Heuristic: assume last page bottom-right region
    # (common invoice layout)
    if image_paths:
        # Example bounding boxes (x1, y1, x2, y2)
        signature["present"] = True
        signature["bbox"] = [100, 400, 300, 480]

        stamp["present"] = True
        stamp["bbox"] = [350, 380, 520, 520]

    return signature, stamp
