(function () {
  "use strict";

  const metricTargets = document.querySelectorAll("[data-scholar-metric]");
  if (!metricTargets.length) return;

  const metricKeys = new Set(["citations", "h_index", "i10_index"]);
  const numberFormatter = new Intl.NumberFormat("en-US");

  function isMetric(value) {
    return Number.isSafeInteger(value) && value >= 0;
  }

  function renderMetrics(data) {
    metricTargets.forEach((target) => {
      const key = target.getAttribute("data-scholar-metric");
      if (!metricKeys.has(key) || !isMetric(data[key])) return;
      target.textContent = numberFormatter.format(data[key]);
    });

    const updatedAt = new Date(data.updated_at);
    if (Number.isNaN(updatedAt.getTime())) return;

    const formattedDate = updatedAt.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric"
    });
    document.querySelectorAll("[data-scholar-updated]").forEach((target) => {
      target.textContent = `last refreshed ${formattedDate}`;
    });
  }

  async function loadMetrics() {
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), 9000);

    try {
      const metricsUrl = new URL("api/scholar-metrics.php", document.baseURI);
      const response = await fetch(metricsUrl, {
        cache: "no-store",
        credentials: "same-origin",
        signal: controller.signal
      });
      if (!response.ok) throw new Error(`Scholar metrics request failed: ${response.status}`);
      renderMetrics(await response.json());
    } catch (error) {
      // Keep the server-rendered fallback values when the cache cannot be loaded.
    } finally {
      window.clearTimeout(timeout);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", loadMetrics, { once: true });
  } else {
    loadMetrics();
  }
})();
