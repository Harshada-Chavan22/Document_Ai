import sys
import json
import time
import os

from vision.dealer_signature_stamp import detect_signature_stamp
from utils.pdf_to_image import pdf_to_images
from ocr.ocr_engine import run_ocr
from extraction.field_extractor import extract_fields

def main(pdf_path):
    start_time = time.time()

    # 1. PDF -> Images
    images = pdf_to_images(pdf_path)

    # 2. OCR
    ocr_data = run_ocr(images)
    print(f"[INFO] OCR lines received in executable: {len(ocr_data)}")

    # 3. Field Extraction
    fields = extract_fields(ocr_data)

    signature, stamp = detect_signature_stamp(images)

    # 4. Final Output Object  ✅ THIS WAS MISSING BEFORE
    output = {
    "doc_id": os.path.basename(pdf_path),
    "fields": {
        "dealer_name": fields["dealer_name"],
        "dealer_match_score": fields["dealer_match_score"],
        "model_name": fields["model_name"],
        "horse_power": fields["horse_power"],
        "asset_cost": fields["asset_cost"],
        "signature": signature,
        "stamp": stamp
    },
    "processing_time_sec": round(time.time() - start_time, 2)
}


    # 5. Save JSON
    os.makedirs("output", exist_ok=True)
    with open("output/result.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("[SUCCESS] Output saved to output/result.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python executable.py <pdf_path>")
        sys.exit(1)

    main(sys.argv[1])
