from paddleocr import PaddleOCR
import cv2
import time

ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en",
    enable_mkldnn=False,
    det_db_thresh=0.3,
    det_db_box_thresh=0.5
)

def run_ocr(image_paths):
    print("[INFO] Running OCR")
    ocr_data = []

    for img_path in image_paths:
        print("[DEBUG] Processing image:", img_path)

        img = cv2.imread(img_path)
        if img is None:
            print("[ERROR] Image read failed")
            continue

        # 🔽 RESIZE IMAGE (CRITICAL)
        h, w = img.shape[:2]
        if max(h, w) > 1200:
            scale = 1200 / max(h, w)
            img = cv2.resize(img, (int(w * scale), int(h * scale)))

        print("[DEBUG] Image resized, starting OCR inference...")
        start = time.time()

        result = ocr.ocr(img)

        print(f"[DEBUG] OCR finished in {round(time.time() - start, 2)} sec")

        if not result:
            print("[WARN] Empty OCR result")
            continue

        page = result[0]

        texts = page.get("rec_texts", [])
        scores = page.get("rec_scores", [])
        boxes = page.get("rec_polys", [])

        print("[DEBUG] Lines detected:", len(texts))

        for t, s, b in zip(texts, scores, boxes):
            print("   →", t)
            ocr_data.append({
                "text": t.strip(),
                "confidence": float(s),
                "bbox": b.tolist()
            })

    print("[FINAL DEBUG] OCR_DATA LENGTH:", len(ocr_data))
    return ocr_data
