(function () {
  const root = document.documentElement;
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme) {
    root.setAttribute("data-theme", savedTheme);
  }

  function updateThemeLabel() {
    const button = document.querySelector("[data-theme-toggle]");
    if (!button) return;
    const isLight = root.getAttribute("data-theme") === "light";
    button.textContent = isLight ? "Dark" : "Light";
    button.setAttribute("aria-label", isLight ? "Switch to dark theme" : "Switch to light theme");
  }

  window.toggleTheme = function toggleTheme() {
    const next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
    root.setAttribute("data-theme", next);
    localStorage.setItem("theme", next);
    updateThemeLabel();
  };

  function setupLightbox() {
    const triggers = document.querySelectorAll("[data-lightbox]");
    if (!triggers.length) return;

    const lightbox = document.createElement("div");
    lightbox.className = "lightbox";
    lightbox.setAttribute("role", "dialog");
    lightbox.setAttribute("aria-modal", "true");
    lightbox.innerHTML = '<button type="button" aria-label="Close image">x</button><img alt="">';
    document.body.appendChild(lightbox);

    const image = lightbox.querySelector("img");
    const close = lightbox.querySelector("button");

    function closeLightbox() {
      lightbox.classList.remove("open");
      image.removeAttribute("src");
      image.alt = "";
    }

    triggers.forEach((trigger) => {
      trigger.style.cursor = "zoom-in";
      trigger.addEventListener("click", () => {
        const src = trigger.getAttribute("data-lightbox") || trigger.currentSrc || trigger.src;
        image.src = src;
        image.alt = trigger.alt || "Expanded image";
        lightbox.classList.add("open");
      });
    });

    close.addEventListener("click", closeLightbox);
    lightbox.addEventListener("click", (event) => {
      if (event.target === lightbox) closeLightbox();
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") closeLightbox();
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    updateThemeLabel();
    setupLightbox();
  });
})();
