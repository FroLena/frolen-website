# convert_jpg_to_webp.py
import os
from PIL import Image


def convert_image(input_path: str, output_path: str):
    """Конвертирует изображение в WebP"""
    try:
        with Image.open(input_path) as img:
            # Конвертируем в RGB, если нужно (для WebP)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            # Сохраняем как WebP
            img.save(output_path, "WEBP", quality=85, method=6)
            print(f"✅ {input_path} → {output_path}")
    except Exception as e:
        print(f"❌ Ошибка {input_path}: {e}")


def main():
    photo_dirs = ["photos/mylo", "photos/probniki", "photos/svechi"]

    for folder in photo_dirs:
        if not os.path.exists(folder):
            print(f"Папка не найдена: {folder}")
            continue

        for filename in os.listdir(folder):
            if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
                input_path = os.path.join(folder, filename)
                name = os.path.splitext(filename)[0]
                output_path = os.path.join(folder, f"{name}.webp")
                convert_image(input_path, output_path)

    print("\n✨ Конвертация завершена!")


if __name__ == "__main__":
    main()