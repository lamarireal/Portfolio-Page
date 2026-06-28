document.addEventListener('DOMContentLoaded', () => {
  const items = document.querySelectorAll('#chronology .timeline-item');
  if (!items.length) return;

  const revealItem = (item) => {
    const rect = item.getBoundingClientRect();
    const isVisible = rect.top < window.innerHeight * 0.88;

    if (isVisible) {
      item.classList.add('is-visible');
    }
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
      }
    });
  }, {
    threshold: 0.2,
  });

  items.forEach((item) => {
    observer.observe(item);
    revealItem(item);
  });

  window.addEventListener('scroll', () => {
    items.forEach((item) => revealItem(item));
  }, { passive: true });
});
