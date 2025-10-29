// filter-sort.js - Логика фильтрации и сортировки товаров

document.addEventListener('DOMContentLoaded', function () {
  const productsContainer = document.getElementById('products-container');
  const productCards = productsContainer.querySelectorAll('.product');
  const filterInputs = document.querySelectorAll('input[name="price"], input[name="type"]');
  const sortSelect = document.getElementById('sort-select');

  // --- Функция обновления отображения ---
  function updateDisplay() {
    const activeFilters = {
      price: [],
      type: []
    };

    // Собираем активные фильтры
    filterInputs.forEach(input => {
      if (input.checked) {
        if (input.name === 'price') {
          activeFilters.price.push(input.value);
        } else if (input.name === 'type') {
          activeFilters.type.push(input.value);
        }
      }
    });

    // Сортировка
    let sortedCards = Array.from(productCards); // Создаём копию массива карточек
    const sortValue = sortSelect.value;

    if (sortValue === 'price-asc') {
      sortedCards.sort((a, b) => parseFloat(a.dataset.price) - parseFloat(b.dataset.price));
    } else if (sortValue === 'price-desc') {
      sortedCards.sort((a, b) => parseFloat(b.dataset.price) - parseFloat(a.dataset.price));
    } else if (sortValue === 'name-asc') {
      sortedCards.sort((a, b) => a.querySelector('h3').textContent.localeCompare(b.querySelector('h3').textContent));
    } else if (sortValue === 'name-desc') {
      sortedCards.sort((a, b) => b.querySelector('h3').textContent.localeCompare(a.querySelector('h3').textContent));
    }
    // 'default' - оставляем порядок как есть в HTML

    // Очищаем контейнер и добавляем отсортированные карточки
    productsContainer.innerHTML = '';
    sortedCards.forEach(card => {
      productsContainer.appendChild(card);
    });

    // --- Фильтрация ---
    // После сортировки применяем фильтры
    sortedCards.forEach(card => {
      const cardPrice = parseFloat(card.dataset.price);
      const cardTypes = card.dataset.type ? card.dataset.type.split(' ') : [];

      let showCard = true;

      // Проверяем фильтр по цене
      if (activeFilters.price.length > 0) {
        let priceMatch = false;
        for (const filter of activeFilters.price) {
          if (filter === 'under200' && cardPrice < 200) {
            priceMatch = true;
            break;
          } else if (filter === '200to300' && cardPrice >= 200 && cardPrice <= 300) {
            priceMatch = true;
            break;
          } else if (filter === 'over300' && cardPrice > 300) {
            priceMatch = true;
            break;
          }
        }
        if (!priceMatch) {
          showCard = false;
        }
      }

      // Проверяем фильтр по типу
      if (activeFilters.type.length > 0) {
        let typeMatch = false;
        for (const filter of activeFilters.type) {
          if (cardTypes.includes(filter)) {
            typeMatch = true;
            break;
          }
        }
        if (!typeMatch) {
          showCard = false;
        }
      }

      // Показываем или скрываем карточку
      card.style.display = showCard ? '' : 'none';
    });
  }

  // --- Обработчики событий ---
  filterInputs.forEach(input => {
    input.addEventListener('change', updateDisplay);
  });

  sortSelect.addEventListener('change', updateDisplay);

  // Инициализация
  updateDisplay();
});
