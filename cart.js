// cart.js — корзина для ФроЛен ЕКБ с анимацией прыжка кнопки

let cart = JSON.parse(localStorage.getItem('cart')) || [];

function updateCartCount() {
  const count = cart.reduce((sum, item) => sum + item.quantity, 0);
  const badge = document.getElementById('cart-count');
  if (badge) badge.textContent = count;
}

document.addEventListener('DOMContentLoaded', () => {
  // Обновляем счётчик корзины
  updateCartCount();

  // Обработчик кнопок "В корзину"
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

      // --- Код для анимации и визуальной обратной связи ---
      // Добавляем класс анимации
      button.classList.add('bounce-animation');
      // Изменяем цвет фона
      button.style.backgroundColor = '#d35400';

      // Удаляем класс анимации и сбрасываем цвет после завершения анимации
      setTimeout(() => {
        button.classList.remove('bounce-animation');
        // Сброс цвета фона, если он не был изменен другим способом
        if (button.style.backgroundColor === 'rgb(211, 84, 0)') { // Проверяем, не изменился ли цвет
            button.style.backgroundColor = '';
        }
      }, 500); // 500ms - длительность анимации
      // --- Конец кода для анимации ---
    });
  });
});
