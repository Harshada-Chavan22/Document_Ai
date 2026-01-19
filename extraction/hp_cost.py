# extraction/hp_cost.py
import re

def extract_hp(ocr_data):
    for item in ocr_data:
        match = re.search(r"(\d+)\s*HP", item["text"], re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None

def extract_cost(ocr_data):
    for item in ocr_data:
        text = item["text"].lower()
        if "total" in text or "amount" in text:
            cost = re.sub(r"[^\d]", "", item["text"])
            if cost:
                return int(cost)
    return None
