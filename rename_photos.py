# rename_photos.py
import os


def transliterate(name: str) -> str:
    """Транслитерация кириллицы в латиницу"""
    translit = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
        ' ': '_', ',': '', '.': '', '/': '_', ':': '', ';': '', '"': '', "'": '', '?': '', '!': '', '—': '-'
    }
    return ''.join(translit.get(char.lower(), char.lower()) for char in name)


def rename_files_in_folder(folder_path: str):
    """Переименовывает все файлы в папке в латиницу"""
    if not os.path.exists(folder_path):
        print(f"Папка не найдена: {folder_path}")
        return

    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            name, ext = os.path.splitext(filename)
            new_name = transliterate(name) + ext
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)

            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print(f"✅ {filename} → {new_name}")
                except Exception as e:
                    print(f"❌ Ошибка при переименовании {filename}: {e}")


def main():
    photo_dirs = [
        "photos/mylo",
        "photos/probniki",
        "photos/svechi"
    ]

    for folder in photo_dirs:
        print(f"\n🔄 Обработка папки: {folder}")
        rename_files_in_folder(folder)

    print("\n🎉 Все фото успешно переименованы в латиницу!")


if __name__ == "__main__":
    main()