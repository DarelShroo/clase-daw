document.addEventListener('DOMContentLoaded', () => {
  const sections = document.querySelectorAll('section');

  const reveal = () => {
    const triggerBottom = window.innerHeight * 0.85;
    sections.forEach((section) => {
      const boxTop = section.getBoundingClientRect().top;
      if (boxTop < triggerBottom) {
        section.classList.add('show');
      }
    });
  };

  window.addEventListener('scroll', reveal);
  reveal();
});
