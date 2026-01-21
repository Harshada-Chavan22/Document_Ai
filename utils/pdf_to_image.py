from pdf2image import convert_from_path
import os

POPPLER_PATH = r"C:\Users\harsh\Downloads\Release-25.12.0-0\poppler-25.12.0\Library\bin"

def pdf_to_images(pdf_path):
    print(f"[INFO] Converting PDF to images: {pdf_path}")

    images = convert_from_path(
        pdf_path,
        dpi=200,
        poppler_path=POPPLER_PATH
    )

    os.makedirs("data/images", exist_ok=True)
    image_paths = []

    for i, img in enumerate(images):
        path = f"data/images/page_{i+1}.jpg"
        img.save(path, "JPEG")
        image_paths.append(path)

    print(f"[DEBUG] Total images created: {len(image_paths)}")
    return image_paths
