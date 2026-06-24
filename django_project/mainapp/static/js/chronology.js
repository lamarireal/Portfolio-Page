document.addEventListener('DOMContentLoaded', () => {
  const el = document.querySelector('#chronology .chronology-list');
  if (!el) return;
  // Placeholder: replace with actual timeline rendering
  if (el.children.length === 0) {
    const p = document.createElement('p');
    p.textContent = 'No items yet. Add chronology entries in the template or via context.';
    el.appendChild(p);
  }
});
