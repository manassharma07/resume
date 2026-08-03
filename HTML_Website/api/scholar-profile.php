<?php
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store, max-age=0');
header('X-Content-Type-Options: nosniff');

const SCHOLAR_AUTHOR_ID = 'WYOEL94AAAAJ';
const REFRESH_INTERVAL = 86400; // One day.

$cacheFile = dirname(__DIR__) . '/data/scholar-metrics.json';
$lockFile = sys_get_temp_dir() . '/manas-scholar-metrics.lock';
$showDiagnostics = isset($_GET['diagnostics']) && $_GET['diagnostics'] === '1';

function fallbackMetrics(): array
{
    return [
        'author_id' => SCHOLAR_AUTHOR_ID,
        'citations' => 503,
        'h_index' => 8,
        'i10_index' => 8,
        'source' => 'Bundled fallback',
        'updated_at' => '2026-08-03T06:43:41Z',
    ];
}

function readMetrics(string $path): ?array
{
    if (!is_file($path)) {
        return null;
    }

    $contents = file_get_contents($path);
    if ($contents === false) {
        return null;
    }

    $metrics = json_decode($contents, true);
    if (!is_array($metrics)) {
        return null;
    }

    foreach (['citations', 'h_index', 'i10_index'] as $key) {
        if (!isset($metrics[$key]) || !is_int($metrics[$key]) || $metrics[$key] < 0) {
            return null;
        }
    }

    return $metrics;
}

function isFresh(?array $metrics): bool
{
    if ($metrics === null || !isset($metrics['updated_at'])) {
        return false;
    }

    $updatedAt = strtotime((string) $metrics['updated_at']);
    return $updatedAt !== false && (time() - $updatedAt) < REFRESH_INTERVAL;
}

function sendMetrics(?array $metrics, bool $stale = false, ?string $refreshError = null): void
{
    if ($metrics === null) {
        http_response_code(503);
        echo json_encode(['error' => 'Scholar metrics are temporarily unavailable']);
        exit;
    }

    $metrics['stale'] = $stale;
    if ($refreshError !== null) {
        $metrics['refresh_error'] = $refreshError;
    }
    echo json_encode($metrics, JSON_UNESCAPED_SLASHES);
    exit;
}

function parseNumber(string $value): ?int
{
    $digits = preg_replace('/[^0-9]/', '', $value);
    return $digits === null || $digits === '' ? null : (int) $digits;
}

function fetchScholarMetrics(): array
{
    if (!function_exists('curl_init')) {
        throw new RuntimeException('The PHP cURL extension is unavailable');
    }

    $url = 'https://scholar.google.com/citations?' . http_build_query([
        'user' => SCHOLAR_AUTHOR_ID,
        'hl' => 'en',
    ]);

    $curl = curl_init($url);
    if ($curl === false) {
        throw new RuntimeException('Could not initialize cURL');
    }

    curl_setopt_array($curl, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_CONNECTTIMEOUT => 3,
        CURLOPT_TIMEOUT => 8,
        CURLOPT_MAXREDIRS => 3,
        CURLOPT_ENCODING => '',
        CURLOPT_USERAGENT => 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        CURLOPT_HTTPHEADER => [
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language: en-US,en;q=0.9',
        ],
    ]);

    $html = curl_exec($curl);
    $status = (int) curl_getinfo($curl, CURLINFO_HTTP_CODE);
    $error = curl_error($curl);
    curl_close($curl);

    if (!is_string($html) || $status !== 200) {
        throw new RuntimeException('Google Scholar request failed: HTTP ' . $status . ' ' . $error);
    }

    if (stripos($html, 'unusual traffic') !== false || stripos($html, '/sorry/') !== false) {
        throw new RuntimeException('Google Scholar rate-limited the hosting server');
    }

    if (!preg_match('/<table\b[^>]*id=["\']gsc_rsb_st["\'][^>]*>(.*?)<\/table>/is', $html, $tableMatch)) {
        throw new RuntimeException('Google Scholar metrics table was not found');
    }

    $metrics = [];
    preg_match_all('/<tr\b[^>]*>(.*?)<\/tr>/is', $tableMatch[1], $rowMatches);
    foreach ($rowMatches[1] as $rowHtml) {
        preg_match_all('/<td\b[^>]*>(.*?)<\/td>/is', $rowHtml, $cellMatches);
        if (count($cellMatches[1]) < 2) {
            continue;
        }

        $label = strtolower(trim(html_entity_decode(strip_tags($cellMatches[1][0]), ENT_QUOTES | ENT_HTML5, 'UTF-8')));
        $valueText = html_entity_decode(strip_tags($cellMatches[1][1]), ENT_QUOTES | ENT_HTML5, 'UTF-8');
        $value = parseNumber($valueText);
        if ($value === null) {
            continue;
        }

        if ($label === 'citations') {
            $metrics['citations'] = $value;
        } elseif ($label === 'h-index') {
            $metrics['h_index'] = $value;
        } elseif ($label === 'i10-index') {
            $metrics['i10_index'] = $value;
        }
    }

    foreach (['citations', 'h_index', 'i10_index'] as $key) {
        if (!isset($metrics[$key])) {
            throw new RuntimeException('Google Scholar returned an incomplete metrics table');
        }
    }

    return [
        'author_id' => SCHOLAR_AUTHOR_ID,
        'citations' => $metrics['citations'],
        'h_index' => $metrics['h_index'],
        'i10_index' => $metrics['i10_index'],
        'source' => 'Google Scholar',
        'updated_at' => gmdate('Y-m-d\TH:i:s\Z'),
    ];
}

$cacheDirectory = dirname($cacheFile);
if (!is_dir($cacheDirectory)) {
    @mkdir($cacheDirectory, 0755, true);
}

$storedMetrics = readMetrics($cacheFile);
$cachedMetrics = $storedMetrics ?? fallbackMetrics();
if ($storedMetrics !== null && isFresh($storedMetrics) && !$showDiagnostics) {
    sendMetrics($storedMetrics);
}

$lockHandle = fopen($lockFile, 'c');
if ($lockHandle === false || !flock($lockHandle, LOCK_EX | LOCK_NB)) {
    if (is_resource($lockHandle)) {
        fclose($lockHandle);
    }
    sendMetrics($cachedMetrics, true);
}

try {
    // Another request may have refreshed the file before this lock was acquired.
    $latestMetrics = readMetrics($cacheFile);
    if (isFresh($latestMetrics) && !$showDiagnostics) {
        sendMetrics($latestMetrics);
    }

    $freshMetrics = fetchScholarMetrics();
    $encodedMetrics = json_encode($freshMetrics, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
    if ($encodedMetrics === false || file_put_contents($cacheFile, $encodedMetrics . PHP_EOL, LOCK_EX) === false) {
        throw new RuntimeException('Could not write the Scholar metrics cache');
    }

    sendMetrics($freshMetrics);
} catch (Throwable $error) {
    error_log('Scholar metrics refresh failed: ' . $error->getMessage());
    if ($storedMetrics === null && is_dir($cacheDirectory) && is_writable($cacheDirectory)) {
        $encodedFallback = json_encode($cachedMetrics, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
        if ($encodedFallback !== false) {
            @file_put_contents($cacheFile, $encodedFallback . PHP_EOL, LOCK_EX);
        }
    }
    sendMetrics($cachedMetrics, true, $showDiagnostics ? $error->getMessage() : null);
} finally {
    flock($lockHandle, LOCK_UN);
    fclose($lockHandle);
}
