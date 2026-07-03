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
document.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => document.body.classList.add('animated-bg'), 100);
  initSmoothScroll();
  initActiveNavigation();
  initTopNavAnimation();
  initTitleAnimation();
});

function initTitleAnimation() {
  const intro = document.querySelector('.intro');
  if (!intro) return;
  requestAnimationFrame(() => setTimeout(() => intro.classList.add('visible'), 200));
}

function initTopNavAnimation() {
  const nav = document.querySelector('.nav-menu');
  if (!nav) return;
  nav.classList.add('init-anim');
  nav.addEventListener('animationend', () => nav.classList.remove('init-anim'), { once: true });
}

function initSmoothScroll() {
  const navLinks = document.querySelectorAll('.nav-menu a, .side-nav a');
  navLinks.forEach(link => link.addEventListener('click', function(e) {
    const href = this.getAttribute('href');
    if (href && href.startsWith('#')) {
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }));
}

function initActiveNavigation() {
  const sections = document.querySelectorAll('.main-screen, section');
  const navLinks = document.querySelectorAll('.nav-menu a, .side-nav a');
  const threshold = window.innerHeight * 0.25;

  function update() {
    let current = 'home';
    const pos = window.pageYOffset + threshold;
    sections.forEach(s => { if (pos >= s.offsetTop) current = s.getAttribute('id'); });
    navLinks.forEach(link => link.classList.toggle('active', link.getAttribute('href') === '#' + current));
    document.body.classList.toggle('scrolled', window.pageYOffset > 80);
  }

  window.addEventListener('scroll', update);
  update();
}
