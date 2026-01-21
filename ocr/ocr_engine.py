import os
os.environ["FLAGS_use_onednn"] = "0"

from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en')

def run_ocr(images):
    ocr_results = []
    for img in images:
        result = ocr.ocr(img)
        if result and len(result) > 0:
            ocr_results.extend(result[0])
    return ocr_results
