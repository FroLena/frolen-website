// cart.js — корзина для ФроЛен ЕКБ

let cart = JSON.parse(localStorage.getItem('cart')) || [];

function updateCartCount() {
  const count = cart.reduce((sum, item) => sum + item.quantity, 0);
  const badge = document.getElementById('cart-count');
  if (badge) badge.textContent = count;
}

document.addEventListener('DOMContentLoaded', () => {
  // Обновляем счётчик корзины
  updateCartCount();

  // Обработчик кнопок "Заказать"
  document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', () => {
      const id = button.dataset.id;
      const name = button.dataset.name;
      const price = parseFloat(button.dataset.price);
      const image = button.dataset.image;

      const existing = cart.find(item => item.id === id);
      if (existing) {
        existing.quantity += 1;
      } else {
        cart.push({ id, name, price, image, quantity: 1 });
      }

      localStorage.setItem('cart', JSON.stringify(cart));
      updateCartCount();

    });
  });
});
