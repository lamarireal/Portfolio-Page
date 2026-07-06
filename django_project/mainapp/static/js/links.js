document.addEventListener('DOMContentLoaded', () => {
  const links = document.querySelectorAll('#links .links-list a');

  links.forEach(link => {
    if (link.classList.contains('contact-link')) {
      return;
    }

    link.setAttribute('target', '_blank');
    link.setAttribute('rel', 'noopener noreferrer');
  });

  const trigger = document.querySelector('#links .contact-link');
  const overlay = document.querySelector('#contact-modal-overlay');
  const modal = overlay?.querySelector('.contact-modal');
  const closeButton = overlay?.querySelector('.contact-close');

  if (!trigger || !overlay || !modal || !closeButton) {
    return;
  }

  const openModal = () => {
    overlay.classList.add('is-visible');
    overlay.setAttribute('aria-hidden', 'false');
    document.body.classList.add('modal-open');
  };

  const closeModal = () => {
    overlay.classList.remove('is-visible');
    overlay.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('modal-open');
  };

  trigger.addEventListener('click', event => {
    event.preventDefault();
    openModal();
  });

  closeButton.addEventListener('click', closeModal);

  overlay.addEventListener('click', event => {
    if (event.target === overlay) {
      closeModal();
    }
  });

  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && overlay.classList.contains('is-visible')) {
      closeModal();
    }
  });
});
