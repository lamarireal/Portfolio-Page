document.addEventListener('DOMContentLoaded', () => {
  const links = document.querySelectorAll('#links .links-list a');
  links.forEach(a => a.setAttribute('target', '_blank'));
});
