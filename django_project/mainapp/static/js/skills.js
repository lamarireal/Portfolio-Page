/*
   ===================================
   JavaScript файл для раздела Skills
   Интерактивность и анимации плашек навыков
   ===================================
*/

document.addEventListener('DOMContentLoaded', () => {
  initSkillsBadges();
});

function initSkillsBadges() {
  const skillBadges = document.querySelectorAll('.skill-badge');
  
  if (skillBadges.length === 0) return;

  /* Для больших экранов: стартуем анимацию при видимости раздела */
  const skillsSection = document.querySelector('#skills');
  if (!skillsSection) return;

  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px'
  };

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        /* Раздел в видимости - активируем анимации */
        enableSkillsAnimation();
        sectionObserver.unobserve(entry.target);
      }
    });
  }, observerOptions);

  sectionObserver.observe(skillsSection);

  /* Для мобильных: применяем анимации сразу */
  if (window.innerWidth <= 768) {
    enableSkillsAnimation();
  }
}

function enableSkillsAnimation() {
  const skillBadges = document.querySelectorAll('.skill-badge');
  
  skillBadges.forEach((badge, index) => {
    /* Перезапускаем анимацию для видимого эффекта */
    badge.style.animation = 'none';
    setTimeout(() => {
      badge.style.animation = '';
    }, 10);
  });
}

/* Добавляем поддержку сенсорных устройств для hover эффекта */
if (window.matchMedia('(hover: none)').matches) {
  document.addEventListener('touchstart', function() {}, false);
}

