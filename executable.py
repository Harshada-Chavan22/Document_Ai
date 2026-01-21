import os
import sys
import json
import time

# Disable problematic Paddle features (must be first)
os.environ["FLAGS_use_onednn"] = "False"
os.environ["FLAGS_enable_pir_api"] = "0"
os.environ["FLAGS_use_new_executor"] = "0"

from utils.pdf_to_image import pdf_to_images
from ocr.ocr_engine import run_ocr
from vision.dealer_signature_stamp import detect_signature_stamp


def main(pdf_path):
    start = time.time()

    images = pdf_to_images(pdf_path)
    ocr_data = run_ocr(images)
    print(f"[DEBUG] Number of OCR lines: {len(ocr_data)}")
    vision_data = detect_signature_stamp(images)
    
    output = {
        "doc_id": os.path.basename(pdf_path),
        "ocr_lines": ocr_data,
        "vision": vision_data,
        "confidence": round(min(1.0, len(ocr_data) / 50), 2),
        "processing_time_sec": round(time.time() - start, 2)
    }

    os.makedirs("output", exist_ok=True)
    with open("output/result.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("\n[SUCCESS] Output saved to output/result.json")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python executable.py <pdf_path>")
    else:
        main(sys.argv[1])
