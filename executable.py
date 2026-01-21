import os

# 🔴 MUST be set before Paddle is imported
os.environ["FLAGS_use_onednn"] = "False"
os.environ["FLAGS_enable_pir_api"] = "0"
os.environ["FLAGS_use_new_executor"] = "0"

import sys

from utils.pdf_to_image import pdf_to_images
from ocr.ocr_engine import run_ocr
from extraction.hp_cost import extract_hp, extract_cost
from extraction.model_name import extract_model_name
from vision.dealer_signature_stamp import detect_signature_stamp
from postprocess.validation import validate_fields
from postprocess.confidence import compute_confidence
from utils.save_json import save_json

def main(pdf_path):
    images = pdf_to_images(pdf_path)
    ocr_data = run_ocr(images)

    model = extract_model_name(ocr_data)
    hp = extract_hp(ocr_data)
    cost = extract_cost(ocr_data)

    vision = detect_signature_stamp(images)
    fields = validate_fields(None, model, hp, cost, vision)
    confidence = compute_confidence(fields, vision)

    result = {
        "doc_id": pdf_path,
        "fields": fields,
        "confidence": confidence
    }

    save_json(result)
    print("[SUCCESS] Output saved to output/result.json")

if __name__ == "__main__":
    main(sys.argv[1])