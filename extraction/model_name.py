# extraction/model_name.py
import re

def extract_model_name(ocr_data):
    pattern = r"[A-Za-z]+\s\d+\sDI"

    for item in ocr_data:
        match = re.search(pattern, item["text"])
        if match:
            return match.group()

    return None
