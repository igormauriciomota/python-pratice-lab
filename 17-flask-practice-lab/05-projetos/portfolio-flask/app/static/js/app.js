document.addEventListener("DOMContentLoaded", () => {
  const sections = [...document.querySelectorAll("main section[id]")];
  const links = [...document.querySelectorAll(".portfolio-sidebar nav a")];

  // IntersectionObserver evita eventos de scroll executados a cada pixel.
  const observer = new IntersectionObserver((entries) => {
    const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (!visible) return;
    links.forEach((link) => link.classList.toggle("active", link.getAttribute("href") === `#${visible.target.id}`));
  }, { rootMargin: "-28% 0px -55%", threshold: [0.1, 0.35, 0.6] });
  sections.forEach((section) => observer.observe(section));

  const rail = document.querySelector(".project-rail");
  document.querySelector("[data-rail='prev']")?.addEventListener("click", () => rail?.scrollBy({ left: -400, behavior: "smooth" }));
  document.querySelector("[data-rail='next']")?.addEventListener("click", () => rail?.scrollBy({ left: 400, behavior: "smooth" }));
});
