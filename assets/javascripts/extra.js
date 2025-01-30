// document.addEventListener('DOMContentLoaded', function() {
//     const sections = document.querySelectorAll('.section');
//     const navItems = document.querySelectorAll('.md-tabs__item');
  
//     function changeLinkState() {
//       let index = sections.length;
//       while(--index && window.scrollY + 50 < sections[index].offsetTop) {}
//       navItems.forEach((link) => link.classList.remove('md-tabs__item--active'));
//       navItems[index].classList.add('md-tabs__item--active');
//     }
  
//     changeLinkState();
//     window.addEventListener('scroll', changeLinkState);
//   });
  
//   function scrollToNextSection(currentSection) {
//     const sections = document.querySelectorAll('.section');
//     const currentIndex = Array.from(sections).indexOf(currentSection);
//     if (currentIndex < sections.length - 1) {
//       sections[currentIndex + 1].scrollIntoView({ behavior: 'smooth' });
//     }
//   }

document.addEventListener('DOMContentLoaded', function () {
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.content, .feature-item').forEach(element => {
    observer.observe(element);
  });
});