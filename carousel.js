// carousel.js - Логика карусели для популярных товаров

document.addEventListener('DOMContentLoaded', function () {
  const carousel = document.getElementById('featuredProductsCarousel');
  const prevBtn = document.getElementById('carouselPrev');
  const nextBtn = document.getElementById('carouselNext');
  const products = carousel.querySelectorAll('.product');
  const totalProducts = products.length;

  // Проверяем, нужно ли вообще показывать карусель
  if (totalProducts <= 3) {
    // Если товаров 3 или меньше, скрываем стрелки
    prevBtn.style.display = 'none';
    nextBtn.style.display = 'none';
    return; // Выходим из функции, карусель не нужна
  }

  let currentIndex = 0;
  const visibleProducts = 3; // Сколько товаров показывать за раз

  function updateCarousel() {
    // Рассчитываем сдвиг: ширина одного элемента * его индекс
    // Учитываем gap (1.8rem) между элементами
    const productWidth = products[0].offsetWidth;
    const gapValue = parseFloat(getComputedStyle(carousel).gap) || 0; // Получаем gap из CSS
    const totalShift = (productWidth + gapValue) * currentIndex;

    carousel.style.transform = `translateX(-${totalShift}px)`;

    // Обновляем состояние кнопок
    prevBtn.disabled = currentIndex === 0;
    nextBtn.disabled = currentIndex >= totalProducts - visibleProducts;
  }

  // Обработчики кликов по кнопкам
  prevBtn.addEventListener('click', function () {
    if (currentIndex > 0) {
      currentIndex--;
      updateCarousel();
    }
  });

  nextBtn.addEventListener('click', function () {
    if (currentIndex < totalProducts - visibleProducts) {
      currentIndex++;
      updateCarousel();
    }
  });

  // Инициализация карусели
  updateCarousel();

  // Обработка изменения размера окна (для адаптивности)
  window.addEventListener('resize', updateCarousel);
});
