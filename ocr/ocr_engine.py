# ocr/ocr_engine.py
from paddleocr import PaddleOCR
import cv2

# OCR object (CPU, angle cls enabled)
ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en"
)

def run_ocr(image_paths):
    print("[INFO] Running OCR")
    ocr_data = []

    for img_path in image_paths:
        img = cv2.imread(img_path)

        if img is None:
            continue

        # ❌ DO NOT pass cls=True here
        result = ocr.ocr(img)

        if not result:
            continue

        for line in result[0]:
            bbox = line[0]
            text = line[1][0]
            conf = line[1][1]

            ocr_data.append({
                "text": text,
                "bbox": bbox,
                "confidence": conf
            })

    return ocr_data
