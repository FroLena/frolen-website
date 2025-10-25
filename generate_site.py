# generate_site.py
import os
from data.products import CATEGORIES

# HTML-шаблон
HTML_HEADER = '''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>ФроЛен ЕКБ — Натуральное мыло ручной работы</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    body { background: #fdf6f0; color: #333; line-height: 1.6; }
    header { text-align: center; padding: 2rem 1rem; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
    h1 { font-size: 2.2rem; color: #5d4037; margin-bottom: 0.5rem; }
    .subtitle { color: #8d6e63; font-size: 1.1rem; }
    .container { max-width: 1200px; margin: 2rem auto; padding: 0 1rem; }
    .category { margin-bottom: 3rem; }
    .category h2 { font-size: 1.8rem; color: #5d4037; margin-bottom: 1.5rem; padding-bottom: 0.5rem; border-bottom: 2px solid #d7ccc8; }
    .products { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.5rem; }
    .product { background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.08); transition: transform 0.2s; }
    .product:hover { transform: translateY(-4px); }
    .product img { width: 100%; height: 200px; object-fit: cover; background: #efebe9; }
    .product-info { padding: 1rem; }
    .product h3 { font-size: 1.2rem; margin-bottom: 0.5rem; color: #4e342e; }
    .price { font-weight: bold; color: #5d4037; font-size: 1.1rem; margin: 0.5rem 0; }
    .desc { font-size: 0.95rem; color: #666; margin-bottom: 1rem; }
    .btn { display: inline-block; background: #8d6e63; color: white; text-decoration: none; padding: 0.6rem 1rem; border-radius: 6px; font-weight: 500; transition: background 0.2s; }
    .btn:hover { background: #6d4c41; }
    footer { text-align: center; padding: 2rem 1rem; background: white; margin-top: 3rem; border-top: 1px solid #eee; }
    @media (max-width: 600px) {
      .products { grid-template-columns: 1fr; }
      h1 { font-size: 1.8rem; }
      h2 { font-size: 1.5rem; }
    }
  </style>
</head>
<body>

<header>
  <h1>🌿🧼 ФроЛен ЕКБ</h1>
  <p class="subtitle">Натуральное мыло и свечи ручной работы</p>
</header>

<div class="container">
'''

HTML_FOOTER = '''
</div>

<footer>
  <p>Хотите заказать или уточнить детали?</p>
  <a href="https://t.me/frolen_ekb" class="btn" target="_blank">📩 Написать в Telegram</a>
  <p style="margin-top: 1rem; font-size: 0.9rem; color: #888;">
    Доставка по Екатеринбургу • Натуральный состав • Ручная работа
  </p>
</footer>

</body>
</html>
'''


def get_photo_path(category_name: str, product_name: str) -> str:
    # Транслитерация кириллицы в латиницу
    def transliterate(name: str) -> str:
        translit = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
            'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
            'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
            'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
            ' ': '_', ',': '', '.': '', '/': '_', ':': '', ';': '', '"': '', "'": '', '?': '', '!': '', '—': '-'
        }
        return ''.join(translit.get(char.lower(), char.lower()) for char in name)

    category_folder_map = {
        "🌸 Мыло": "mylo",
        "🌿 Пробники и аксессуары": "probniki",
        "🕯️ Свечи": "svechi"
    }

    folder = category_folder_map.get(category_name, "unknown")

    safe_name = transliterate(product_name)

    for ext in [".webp", ".jpg", ".jpeg", ".png"]:
        photo_path = os.path.join("photos", folder, f"{safe_name}{ext}")
        if os.path.exists(photo_path):
            return photo_path.replace("\\", "/")

    return f"https://via.placeholder.com/300x200/e0d3c5/5d4037?text={safe_name}"


def generate_product_html(category_name: str, product: dict) -> str:
    img_src = get_photo_path(category_name, product["name"])
    return f'''
      <div class="product">
        <img src="{img_src}" alt="{product['name']}">
        <div class="product-info">
          <h3>{product['name']}</h3>
          <div class="price">{product['price']} ₽</div>
          <p class="desc">{product['desc']}</p>
        </div>
      </div>
    '''


def generate_category_html(category_name: str, products: list) -> str:
    products_html = "\n".join(generate_product_html(category_name, p) for p in products)
    return f'''
  <section class="category">
    <h2>{category_name}</h2>
    <div class="products">
{products_html}
    </div>
  </section>
    '''


def main():
    html_parts = [HTML_HEADER]

    for category_name, products in CATEGORIES.items():
        html_parts.append(generate_category_html(category_name, products))

    html_parts.append(HTML_FOOTER)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write("".join(html_parts))

    print("✅ Файл index.html успешно сгенерирован!")
    print("📁 Убедитесь, что папка 'photos' находится рядом с index.html.")


if __name__ == "__main__":
    main()