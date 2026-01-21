from paddleocr import PaddleOCR
import cv2

ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en",
    enable_mkldnn=False
)

def run_ocr(image_paths):
    print("[INFO] Running OCR")

    for img_path in image_paths:
        print("[DEBUG] Reading image:", img_path)
        img = cv2.imread(img_path)

        if img is None:
            print("[ERROR] Image could not be read")
            continue

        result = ocr.ocr(img)

        print("\n========== RAW OCR OUTPUT ==========")
        print(result)
        print("===================================")

        break  # only first image for debug

    return []
