/*
   ===================================
   JavaScript файл для главной страницы портфолио
   Содержит функциональность и интерактивность
   ===================================
*/

/*
   Функция инициализации страницы
   Выполняется при загрузке документа
*/
document.addEventListener('DOMContentLoaded', function() {
  // Анимация фона после загрузки
  setTimeout(() => {
    document.body.classList.add('animated-bg');
  }, 100);

  initSmoothScroll();
  initActiveNavigation();
  initScrollAnimation();
});

/*
   Функция для плавной прокрутки страницы к якорям
   Улучшает пользовательский опыт навигации
*/
function initSmoothScroll() {
  // Находим все ссылки в навигации
  const navLinks = document.querySelectorAll('.nav-menu a');
  
  // Добавляем обработчик события клика для каждой ссылки
  navLinks.forEach(link => {
    link.addEventListener('click', function(event) {
      // Получаем значение атрибута href
      const href = this.getAttribute('href');
      
      // Проверяем, является ли это якорем (начинается с #)
      if (href && href.startsWith('#')) {
        // Отменяем стандартное поведение ссылки
        event.preventDefault();
        
        // Получаем элемент, на который указывает якорь
        const targetElement = document.querySelector(href);
        
        // Если элемент существует, прокручиваем к нему плавно
        if (targetElement) {
          targetElement.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      }
    });
  });
}

/*
   Функция для обновления активной ссылки в меню при прокрутке
   Показывает, какой раздел сейчас видим на экране
*/
function initActiveNavigation() {
  // Находим все секции на странице
  const sections = document.querySelectorAll('section');
  
  // Находим все ссылки в навигации
  const navLinks = document.querySelectorAll('.nav-menu a');
  
  // Добавляем обработчик события прокрутки
  window.addEventListener('scroll', function() {
    // Переменная для хранения текущей секции
    let currentSection = '';
    
    // Проходим по каждой секции
    sections.forEach(section => {
      // Получаем позицию секции относительно верхней части экрана
      const sectionTop = section.offsetTop;
      
      // Если прокруткa выше или на уровне этой секции, то это текущая секция
      if (window.pageYOffset >= sectionTop - 50) {
        currentSection = section.getAttribute('id');
      }
    });
    
    // Убираем класс активной ссылки со всех ссылок
    navLinks.forEach(link => {
      link.classList.remove('active');
      
      // Если это ссылка на текущую секцию, добавляем класс active
      if (link.getAttribute('href') === '#' + currentSection) {
        link.classList.add('active');
      }
    });
  });
}

/*
   Функция для анимации элементов при прокрутке страницы
   Элементы появляются с анимацией, когда они попадают в видимую область
*/
function initScrollAnimation() {
  // Находим все элементы, которые должны анимироваться
  const elementsToAnimate = document.querySelectorAll('.skill-card, .project-card');
  
  // Создаем объект IntersectionObserver для отслеживания видимости элементов
  const observer = new IntersectionObserver(function(entries) {
    // Проходим по каждому элементу, который попал в видимую область
    entries.forEach(entry => {
      // Если элемент видим
      if (entry.isIntersecting) {
        // Добавляем класс анимации
        entry.target.classList.add('animate');
        
        // Прекращаем наблюдение за этим элементом (анимация произойдет только раз)
        observer.unobserve(entry.target);
      }
    });
  }, {
    // Параметры observer'а
    threshold: 0.1 // Срабатывает, когда 10% элемента видимо
  });
  
  // Начинаем наблюдение за всеми элементами
  elementsToAnimate.forEach(element => {
    observer.observe(element);
  });
}
