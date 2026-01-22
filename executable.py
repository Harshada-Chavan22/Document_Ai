import sys
import json
import time
import os

from utils.pdf_to_image import pdf_to_images
from ocr.ocr_engine import run_ocr
from extraction.field_extractor import extract_fields
from vision.dealer_signature_stamp import detect_signature_stamp
from postprocess.confidence_scorer import compute_document_confidence


def main(pdf_path):
    start_time = time.time()

    # 1. PDF -> Images
    images = pdf_to_images(pdf_path)

    # 2. OCR
    ocr_data = run_ocr(images)
    print(f"[INFO] OCR lines received in executable: {len(ocr_data)}")

    # 3. Extract text fields
    fields = extract_fields(ocr_data)

    # 4. Signature & Stamp detection
    signature, stamp = detect_signature_stamp(images)

    # 5. Attach vision results to fields  ✅ CRITICAL
    fields["signature"] = signature
    fields["stamp"] = stamp

    # 6. Document confidence  ✅ MUST COME AFTER fields update
    doc_confidence = compute_document_confidence(ocr_data, fields)

    # 7. FINAL hackathon output (schema-safe)
    output = {
        "doc_id": os.path.splitext(os.path.basename(pdf_path))[0],
        "fields": {
            "dealer_name": fields.get("dealer_name"),
            "model_name": fields.get("model_name"),
            "horse_power": fields.get("horse_power"),
            "asset_cost": fields.get("asset_cost"),
            "signature": fields.get("signature"),
            "stamp": fields.get("stamp")
        },
        "confidence": doc_confidence,
        "processing_time_sec": round(time.time() - start_time, 2),
        "cost_estimate_usd": 0.002
    }

    # 8. Save JSON
    os.makedirs("output", exist_ok=True)
    with open("output/result.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("[SUCCESS] Output saved to output/result.json")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python executable.py <pdf_path>")
        sys.exit(1)

    main(sys.argv[1])
