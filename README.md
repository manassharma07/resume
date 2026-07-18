# My Resume

The resume webpage is created via Streamlit

## Automatic Google Scholar metrics

The HTML website renders cached citation metrics immediately. On page load, `HTML_Website/scholar-metrics.js` asynchronously calls `HTML_Website/api/scholar-metrics.php`. The request does not block the page.

The PHP endpoint uses only built-in PHP and cURL functionality available on GoDaddy Linux Web Hosting. It returns `HTML_Website/data/scholar-metrics.json` immediately while the file is less than three days old. When the cache expires, the next page view refreshes it from the public Google Scholar profile and writes the new values to that JSON text file. Concurrent visitors continue receiving the old cache while one refresh is running.

Deployment notes:

1. Upload the `api`, `data`, and `scholar-metrics.js` additions with the rest of `HTML_Website`.
2. Ensure the `data` directory is writable by PHP. The normal GoDaddy owner permissions generally handle this; `755` is the usual directory permission.
3. Open `/api/scholar-metrics.php` on the live domain once. It should return JSON containing `citations`, `h_index`, and `i10_index`.

If Scholar temporarily rate-limits the server or changes its HTML, the endpoint returns the last valid cache and the HTML fallback remains visible.
