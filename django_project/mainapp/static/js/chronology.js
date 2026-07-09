document.addEventListener('DOMContentLoaded', () => {
  const chronology = document.querySelector('#chronology');
  const items = document.querySelectorAll('#chronology .timeline-item');
  if (!items.length) return;
  const toggle = document.querySelector('#chronology .chronology-toggle');
  const extraItems = document.querySelectorAll('#chronology .timeline-item--extra');

  if (chronology && extraItems.length) {
    chronology.classList.add('has-hidden-items');
  }

  if (toggle && !extraItems.length) {
    toggle.classList.add('is-hidden');
  }

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

  if (toggle && chronology && extraItems.length) {
    const label = toggle.querySelector('span');
    const showLabel = toggle.dataset.showLabel;
    const hideLabel = toggle.dataset.hideLabel;
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const followToggleDuringCollapse = (anchorTop) => {
      if (prefersReducedMotion) {
        toggle.scrollIntoView({ block: 'center' });
        return;
      }

      const startedAt = performance.now();
      const duration = 760;

      const keepAnchor = (now) => {
        const currentTop = toggle.getBoundingClientRect().top;
        const delta = currentTop - anchorTop;

        if (Math.abs(delta) > 0.5) {
          window.scrollBy({ top: delta, behavior: 'auto' });
        }

        if (now - startedAt < duration) {
          requestAnimationFrame(keepAnchor);
        }
      };

      requestAnimationFrame(keepAnchor);
    };

    toggle.addEventListener('click', () => {
      const toggleTopBeforeChange = toggle.getBoundingClientRect().top;
      const isExpanded = chronology.classList.toggle('is-expanded');
      toggle.dataset.expanded = String(isExpanded);
      if (label) label.textContent = isExpanded ? hideLabel : showLabel;

      if (isExpanded) {
        extraItems.forEach((item, index) => {
          window.setTimeout(() => item.classList.add('is-visible'), index * 70);
        });
      } else {
        extraItems.forEach((item) => item.classList.remove('is-visible'));
        followToggleDuringCollapse(toggleTopBeforeChange);
      }
    });
  }
});
