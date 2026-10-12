# My Resume

The resume webpage is created via Streamlit

## Automatic Google Scholar metrics

The HTML website renders cached citation metrics immediately. On page load, `HTML_Website/scholar-metrics.js` asynchronously calls `HTML_Website/api/scholar-profile.php`. The request does not block the page.

The PHP endpoint uses only built-in PHP and cURL functionality available on GoDaddy Linux Web Hosting. It returns `HTML_Website/data/scholar-metrics.json` immediately while the file is less than three days old. When the cache expires, the next page view refreshes it from the public Google Scholar profile and writes the new values to that JSON text file. Concurrent visitors continue receiving the old cache while one refresh is running.

Deployment notes:

1. Upload the `api`, `data`, and `scholar-metrics.js` additions with the rest of `HTML_Website`.
2. Ensure the `data` directory is writable by PHP. The normal GoDaddy owner permissions generally handle this; `755` is the usual directory permission.
3. Open `/api/scholar-profile.php` on the live domain once. It should return JSON containing `citations`, `h_index`, and `i10_index`.

If it returns cached values with `"stale": true`, open `/api/scholar-profile.php?diagnostics=1` to see the safe refresh error. The diagnostic response does not expose credentials because this implementation does not use any.

If Scholar temporarily rate-limits the server or changes its HTML, the endpoint returns the last valid cache and the HTML fallback remains visible.

## Conference photos in Google Images

The gallery links to dedicated photo pages for ICMS 2026, TURBOMOLE Oxford 2024, and research posters. These pages include images in the original HTML, visible captions, descriptive alternative text, responsive WebP previews, and structured data connecting the content to Manas Sharma. The full image URLs are listed in `HTML_Website/sitemap.xml`.

Upload all of `HTML_Website`, including the three new HTML pages, `album.css`, the `assets/gallery/optimized/search-previews` directory, and the updated sitemap. After deployment, use Google Search Console to submit `https://manas.bragitoff.com/sitemap.xml` and request indexing for:

- `https://manas.bragitoff.com/gallery.html`
- `https://manas.bragitoff.com/icms-2026.html`
- `https://manas.bragitoff.com/turbomole-oxford-2024.html`
- `https://manas.bragitoff.com/research-posters.html`

Use URL Inspection to check that Google can retrieve each page and its images. Google controls indexing and rankings; these changes improve discoverability without guaranteeing placement. Photographs are associated with their subject and conference, without assigning unverified photographer credits or licenses.

Google's guidance: [image SEO](https://developers.google.com/search/docs/appearance/google-images), [image sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps), and [requesting a recrawl](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl).
