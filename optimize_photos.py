# optimize_photos.py
import os
from PIL import Image

PHOTO_DIRS = ["photos/mylo", "photos/probniki", "photos/svechi"]
MAX_WIDTH = 1000
QUALITY = 85

def optimize_image(input_path: str, output_path: str):
    try:
        with Image.open(input_path) as img:
            # Конвертируем в RGB, если нужно (для WebP)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            # Уменьшаем размер
            img.thumbnail((MAX_WIDTH, MAX_WIDTH), Image.Resampling.LANCZOS)
            # Сохраняем как WebP
            img.save(output_path, "WEBP", quality=QUALITY, method=6)
            print(f"✅ {input_path} → {output_path}")
    except Exception as e:
        print(f"❌ Ошибка {input_path}: {e}")

def main():
    for folder in PHOTO_DIRS:
        if not os.path.exists(folder):
            print(f"Папка не найдена: {folder}")
            continue

        for filename in os.listdir(folder):
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                input_path = os.path.join(folder, filename)
                name = os.path.splitext(filename)[0]
                output_path = os.path.join(folder, f"{name}.webp")
                optimize_image(input_path, output_path)

    print("\n✨ Оптимизация завершена! Теперь обнови generate_site.py для использования .webp")

if __name__ == "__main__":
    main()