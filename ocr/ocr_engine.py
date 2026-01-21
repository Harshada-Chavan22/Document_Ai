# ocr/ocr_engine.py
from paddleocr import PaddleOCR
import cv2

ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en",
    det=True,
    rec=True,
    cls=True,
    enable_mkldnn=False   # 🔴 critical
)

def run_ocr(image_paths):
    print("[INFO] Running OCR")
    ocr_data = []

    for img_path in image_paths:
        img = cv2.imread(img_path)
        if img is None:
            continue

        result = ocr.ocr(img)

        if not result:
            continue

        for line in result:
            for word in line:
                bbox = word[0]
                text = word[1][0]
                conf = float(word[1][1])

                ocr_data.append({
                    "text": text,
                    "bbox": bbox,
                    "confidence": conf
                })

    return ocr_data
