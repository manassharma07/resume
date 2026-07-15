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

  function shuffleResearchVisuals() {
    document.querySelectorAll(".research-visuals-grid").forEach((grid, gridIndex) => {
      const originalOrder = Array.from(grid.children);
      const shuffledOrder = originalOrder.slice();

      for (let index = shuffledOrder.length - 1; index > 0; index -= 1) {
        const randomIndex = Math.floor(Math.random() * (index + 1));
        [shuffledOrder[index], shuffledOrder[randomIndex]] = [shuffledOrder[randomIndex], shuffledOrder[index]];
      }

      const orderSignature = (items) => items.map((item) => item.getAttribute("data-lightbox") || "").join("|");
      const unchanged = shuffledOrder.length > 1 && shuffledOrder.every((item, index) => item === originalOrder[index]);
      let previousSignature = "";
      const storageKey = `research-visuals-order:${window.location.pathname}:${gridIndex}`;
      try {
        previousSignature = sessionStorage.getItem(storageKey) || "";
      } catch (error) {
        previousSignature = "";
      }

      if (unchanged || orderSignature(shuffledOrder) === previousSignature) {
        shuffledOrder.push(shuffledOrder.shift());
      }

      try {
        sessionStorage.setItem(storageKey, orderSignature(shuffledOrder));
      } catch (error) {
        // The randomized order still works when session storage is unavailable.
      }

      const fragment = document.createDocumentFragment();
      shuffledOrder.forEach((item) => fragment.appendChild(item));
      grid.appendChild(fragment);
    });
  }

  function setupLightbox() {
    const triggers = Array.from(document.querySelectorAll("[data-lightbox]"));
    if (!triggers.length) return;

    const lightbox = document.createElement("div");
    lightbox.className = "lightbox";
    lightbox.setAttribute("role", "dialog");
    lightbox.setAttribute("aria-modal", "true");
    lightbox.setAttribute("aria-hidden", "true");
    lightbox.setAttribute("aria-describedby", "lightbox-caption");
    lightbox.innerHTML = `
      <div class="lightbox-stage">
        <button class="lightbox-close" type="button" aria-label="Close viewer">&times;</button>
        <button class="lightbox-nav lightbox-prev" type="button" aria-label="Previous item">&#8249;</button>
        <div class="lightbox-media"></div>
        <button class="lightbox-nav lightbox-next" type="button" aria-label="Next item">&#8250;</button>
        <div class="lightbox-footer">
          <p class="lightbox-caption" id="lightbox-caption"></p>
          <p class="lightbox-counter" aria-live="polite"></p>
        </div>
      </div>`;
    document.body.appendChild(lightbox);

    const media = lightbox.querySelector(".lightbox-media");
    const caption = lightbox.querySelector(".lightbox-caption");
    const counter = lightbox.querySelector(".lightbox-counter");
    const close = lightbox.querySelector(".lightbox-close");
    const previous = lightbox.querySelector(".lightbox-prev");
    const next = lightbox.querySelector(".lightbox-next");
    let currentGroup = [];
    let currentIndex = 0;
    let lastTrigger = null;

    function groupFor(trigger) {
      const groupName = trigger.getAttribute("data-lightbox-group") || "default";
      return triggers.filter((item) => (item.getAttribute("data-lightbox-group") || "default") === groupName);
    }

    function captionFor(trigger) {
      const nestedMedia = trigger.querySelector ? trigger.querySelector("img, video") : null;
      return trigger.getAttribute("data-caption") || trigger.alt || (nestedMedia && nestedMedia.alt) || "Research visual";
    }

    function renderItem() {
      const trigger = currentGroup[currentIndex];
      if (!trigger) return;

      const activeVideo = media.querySelector("video");
      if (activeVideo) activeVideo.pause();
      media.replaceChildren();

      const src = trigger.getAttribute("data-lightbox") || trigger.currentSrc || trigger.src;
      const type = trigger.getAttribute("data-lightbox-type") || (/\.(mp4|m4v|webm)(\?.*)?$/i.test(src) ? "video" : "image");

      if (type === "video") {
        const video = document.createElement("video");
        video.src = src;
        const poster = trigger.getAttribute("data-poster");
        if (poster) video.poster = poster;
        video.controls = true;
        video.autoplay = true;
        video.playsInline = true;
        video.preload = "metadata";
        media.appendChild(video);
      } else {
        const image = document.createElement("img");
        image.src = src;
        image.alt = captionFor(trigger);
        media.appendChild(image);
      }

      caption.textContent = captionFor(trigger);
      counter.textContent = `${currentIndex + 1} / ${currentGroup.length}`;
      previous.hidden = currentGroup.length < 2;
      next.hidden = currentGroup.length < 2;
    }

    function showRelative(offset) {
      if (currentGroup.length < 2) return;
      currentIndex = (currentIndex + offset + currentGroup.length) % currentGroup.length;
      renderItem();
    }

    function closeLightbox() {
      const activeVideo = media.querySelector("video");
      if (activeVideo) activeVideo.pause();
      media.replaceChildren();
      lightbox.classList.remove("open");
      lightbox.setAttribute("aria-hidden", "true");
      document.body.classList.remove("lightbox-open");
      if (lastTrigger && typeof lastTrigger.focus === "function") lastTrigger.focus();
    }

    triggers.forEach((trigger) => {
      trigger.style.cursor = "zoom-in";
      trigger.addEventListener("click", () => {
        currentGroup = groupFor(trigger);
        currentIndex = currentGroup.indexOf(trigger);
        lastTrigger = trigger;
        renderItem();
        lightbox.classList.add("open");
        lightbox.setAttribute("aria-hidden", "false");
        document.body.classList.add("lightbox-open");
        close.focus();
      });
    });

    close.addEventListener("click", closeLightbox);
    previous.addEventListener("click", () => showRelative(-1));
    next.addEventListener("click", () => showRelative(1));
    lightbox.addEventListener("click", (event) => {
      if (event.target === lightbox) closeLightbox();
    });
    document.addEventListener("keydown", (event) => {
      if (!lightbox.classList.contains("open")) return;
      if (event.key === "Escape") closeLightbox();
      if (event.key === "ArrowLeft") showRelative(-1);
      if (event.key === "ArrowRight") showRelative(1);
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    updateThemeLabel();
    shuffleResearchVisuals();
    setupLightbox();
  });
})();
