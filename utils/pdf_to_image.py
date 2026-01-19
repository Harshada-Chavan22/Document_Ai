# utils/pdf_to_image.py
from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path):
    print(f"[INFO] Converting PDF to images: {pdf_path}")

    images = convert_from_path(pdf_path, dpi=300)

    os.makedirs("data/images", exist_ok=True)
    image_paths = []

    for i, img in enumerate(images):
        path = f"data/images/page_{i+1}.jpg"
        img.save(path, "JPEG")
        image_paths.append(path)

    return image_paths
