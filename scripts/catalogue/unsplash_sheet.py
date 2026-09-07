#!/usr/bin/env python3
"""unsplash_sheet.py — Unsplash sourcing for the contact-sheet method.

Three modes. The API path is the first choice; the scrape path is the fallback.

API search (needs UNSPLASH_ACCESS_KEY, see below):
  unsplash_sheet.py --api <out-dir> "<phrase>" ["<phrase>" ...]
                    [--per-page 30] [--orientation landscape|portrait|squarish]
      GET https://api.unsplash.com/search/photos per phrase. Writes
        <out-dir>/ids.json            [{id, phrase, loaded, photographer,
                                        photographer_url, html_url, width,
                                        height, color, alt, thumb}]
        <out-dir>/contact-sheet.html  the sheet to LOOK at (shoot it, read it)
      and prints the request count plus X-Ratelimit-Limit / -Remaining.

API download (the pick, after looking at the sheet):
  unsplash_sheet.py --download <id> [<id> ...] --to <dir> [--width 2200]
      Per id: GET /photos/<id> (metadata), GET /photos/<id>/download (the
      guideline's "trigger a download"), then urls.raw with
      &w=<width>&fm=webp&q=82&fit=max -> <dir>/<id>.webp. Appends
      {id, photographer, photographer_url, html_url, license} to
      <dir>/credits.json (merged if it exists). Prints size on disk per file.

API verify:
  unsplash_sheet.py --verify
      One GET /photos/random. Prints HTTP status, both rate-limit headers and
      the inferred app tier (50 -> demo, 5000 -> production). Non-200 exits 1.

Key resolution: UNSPLASH_ACCESS_KEY from the environment, else parsed from
~/.secrets/.env (KEY=VALUE, tolerant of BOM/CRLF). Set it with
scripts/keys.py. The key is never printed.

Scrape fallback (no key, the AB14 method):
  unsplash_sheet.py <out-dir> "<phrase>" ["<phrase>" ...]
  unsplash_sheet.py <out-dir> --ids-file <json>      {"phrase": ["id", ...]}
      Loads unsplash.com/s/photos/<phrase> with Playwright, pulls photo IDs out
      of the page, renders a contact sheet of images.unsplash.com/photo-<id>
      thumbnails and verifies each loads. unsplash.com returns 401/403 to
      headless Chromium (2026-09-04), so in practice: open the search page in
      the in-app Browser pane, pull IDs with one JS line, pass --ids-file.

The judgement (pick, then re-judge under the real scrim) stays with the reader.
"""
import argparse
import html
import json
import os
import re
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

PER_PHRASE = 12
API_BASE = "https://api.unsplash.com"
SECRETS_ENV = Path.home() / ".secrets" / ".env"
KEY_NAME = "UNSPLASH_ACCESS_KEY"
USER_AGENT = "anti-slop-design/unsplash_sheet.py (stdlib urllib)"
UTM = "utm_source=anti-slop-design&utm_medium=referral"
LICENSE = "Unsplash License"

_request_count = 0
_last_headers: dict = {}


# --------------------------------------------------------------------------- key
def parse_env_file(path: Path) -> dict:
    """KEY=VALUE parser tolerant of BOM, CRLF, comments, quotes. Values never leave this process."""
    if not path.exists():
        return {}
    out = {}
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        out[key.strip()] = value.strip().strip('"').strip("'")
    return out


def resolve_access_key() -> str | None:
    value = os.environ.get(KEY_NAME, "").strip()
    if value:
        return value
    value = parse_env_file(SECRETS_ENV).get(KEY_NAME, "").strip()
    return value or None


def require_access_key() -> str:
    key = resolve_access_key()
    if not key:
        print(f"error: {KEY_NAME} not set. Export it, or add it to {SECRETS_ENV} "
              f"(run scripts/keys.py). Falling back to the scrape path is the no-key option.",
              file=sys.stderr)
        sys.exit(2)
    return key


# --------------------------------------------------------------------------- http
def api_get(path: str, params: dict | None = None, key: str | None = None):
    """GET api.unsplash.com<path>. Returns (status, headers, body_bytes). Never raises on HTTP status."""
    global _request_count, _last_headers
    key = key or require_access_key()
    url = f"{API_BASE}{path}"
    if params:
        url += "?" + urlencode({k: v for k, v in params.items() if v is not None})
    req = Request(url, headers={
        "Authorization": f"Client-ID {key}",
        "Accept-Version": "v1",
        "User-Agent": USER_AGENT,
    })
    _request_count += 1
    try:
        with urlopen(req, timeout=30) as resp:
            status, headers, body = resp.status, dict(resp.headers), resp.read()
    except HTTPError as e:
        status, headers, body = e.code, dict(e.headers), e.read()
    _last_headers = headers
    return status, headers, body


def rate_headers(headers: dict) -> tuple:
    h = {k.lower(): v for k, v in headers.items()}
    return h.get("x-ratelimit-limit"), h.get("x-ratelimit-remaining")


def print_rate(headers: dict) -> None:
    limit, remaining = rate_headers(headers)
    print(f"API requests this run: {_request_count}   X-Ratelimit-Limit: {limit}   X-Ratelimit-Remaining: {remaining}")


def json_or_none(body: bytes):
    try:
        return json.loads(body.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return None


def api_errors(body: bytes) -> str:
    data = json_or_none(body)
    if isinstance(data, dict) and "errors" in data:
        return "; ".join(str(e) for e in data["errors"])
    return body[:200].decode("utf-8", "replace")


def fetch_ok(url: str) -> bool:
    """Same check the scrape path makes: does a GET of the thumbnail come back 2xx?"""
    try:
        with urlopen(Request(url, headers={"User-Agent": USER_AGENT}), timeout=30) as resp:
            return 200 <= resp.status < 300
    except (HTTPError, URLError, OSError):
        return False


def fetch_bytes(url: str) -> bytes:
    with urlopen(Request(url, headers={"User-Agent": USER_AGENT}), timeout=120) as resp:
        return resp.read()


def with_utm(url: str | None) -> str | None:
    if not url:
        return url
    return f"{url}{'&' if '?' in url else '?'}{UTM}"


# --------------------------------------------------------------------------- sheet
def write_sheet(out: Path, phrases: list, rows: list) -> None:
    """Each row needs id, phrase, loaded, thumb; photographer is optional (API path)."""
    figs = []
    for r in rows:
        credit = f"<br>{html.escape(r['photographer'])}" if r.get("photographer") else ""
        figs.append(
            f'<figure><img src="{html.escape(r["thumb"])}" alt="">'
            f'<figcaption>{html.escape(r["id"])}<br>{html.escape(r["phrase"])}'
            f'{"" if r["loaded"] else " · FAILED"}{credit}</figcaption></figure>')
    page = ("<!doctype html><meta charset='utf-8'><title>contact sheet</title><style>"
            "body{margin:0;padding:24px;background:#111;color:#eee;font:12px system-ui}"
            ".grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}"
            "figure{margin:0;background:#1c1c1c;border:1px solid #333}"
            "figure img{display:block;width:100%;height:220px;object-fit:cover;background:#444}"
            "figcaption{padding:6px 8px;font:11px ui-monospace,Consolas,monospace;color:#aaa}"
            f"</style><h1>{html.escape(' · '.join(phrases))} ({len(rows)} candidates)</h1>"
            f"<div class='grid'>{chr(10).join(figs)}</div>")
    (out / "contact-sheet.html").write_text(page, encoding="utf-8")


def thumb_url(pid: str) -> str:
    return f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w=600&q=70"


# --------------------------------------------------------------------------- API modes
def cmd_api(argv: list) -> None:
    ap = argparse.ArgumentParser(prog="unsplash_sheet.py --api")
    ap.add_argument("out")
    ap.add_argument("phrases", nargs="+")
    ap.add_argument("--per-page", type=int, default=30)
    ap.add_argument("--orientation", choices=["landscape", "portrait", "squarish"])
    a = ap.parse_args(argv)
    key = require_access_key()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)

    rows = []
    for ph in a.phrases:
        status, headers, body = api_get("/search/photos", {
            "query": ph, "per_page": max(1, min(a.per_page, 30)), "orientation": a.orientation}, key)
        if status != 200:
            print(f"error: HTTP {status} for {ph!r}: {api_errors(body)}", file=sys.stderr)
            print_rate(headers)
            sys.exit(1)
        for p in (json_or_none(body) or {}).get("results", []):
            user = p.get("user") or {}
            rows.append({
                "id": p["id"], "phrase": ph, "loaded": None,
                "photographer": user.get("name"),
                "photographer_url": with_utm((user.get("links") or {}).get("html")),
                "html_url": with_utm((p.get("links") or {}).get("html")),
                "width": p.get("width"), "height": p.get("height"),
                "color": p.get("color"), "alt": p.get("alt_description"),
                "thumb": (p.get("urls") or {}).get("small"),
            })
    for r in rows:
        r["loaded"] = bool(r["thumb"]) and fetch_ok(r["thumb"])
    (out / "ids.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    write_sheet(out, a.phrases, rows)
    ok = sum(1 for r in rows if r["loaded"])
    print(f"{len(rows)} candidates, {ok} load -> {out / 'contact-sheet.html'}")
    print_rate(_last_headers)


def merge_credits(path: Path, entry: dict) -> None:
    credits = []
    if path.exists():
        try:
            credits = json.loads(path.read_text(encoding="utf-8-sig"))
        except ValueError:
            credits = []
        if not isinstance(credits, list):
            credits = []
    credits = [c for c in credits if not (isinstance(c, dict) and c.get("id") == entry["id"])]
    credits.append(entry)
    path.write_text(json.dumps(credits, indent=2, ensure_ascii=False), encoding="utf-8")


def cmd_download(argv: list) -> None:
    ap = argparse.ArgumentParser(prog="unsplash_sheet.py --download")
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--to", required=True)
    ap.add_argument("--width", type=int, default=2200)
    a = ap.parse_args(argv)
    key = require_access_key()
    dest = Path(a.to); dest.mkdir(parents=True, exist_ok=True)

    failed = 0
    for pid in a.ids:
        status, headers, body = api_get(f"/photos/{pid}", key=key)
        if status != 200:
            print(f"error: HTTP {status} for /photos/{pid}: {api_errors(body)}", file=sys.stderr)
            failed += 1
            continue
        photo = json_or_none(body) or {}
        status, headers, body = api_get(f"/photos/{pid}/download", key=key)
        if status != 200:
            print(f"error: HTTP {status} for /photos/{pid}/download: {api_errors(body)}", file=sys.stderr)
            failed += 1
            continue
        raw = (photo.get("urls") or {}).get("raw")
        if not raw:
            print(f"error: no urls.raw for {pid}", file=sys.stderr)
            failed += 1
            continue
        image_url = f"{raw}{'&' if '?' in raw else '?'}w={a.width}&fm=webp&q=82&fit=max"
        target = dest / f"{pid}.webp"
        try:
            target.write_bytes(fetch_bytes(image_url))
        except (HTTPError, URLError, OSError) as e:
            print(f"error: image fetch failed for {pid}: {e}", file=sys.stderr)
            failed += 1
            continue
        user = photo.get("user") or {}
        merge_credits(dest / "credits.json", {
            "id": pid,
            "photographer": user.get("name"),
            "photographer_url": with_utm((user.get("links") or {}).get("html")),
            "html_url": with_utm((photo.get("links") or {}).get("html")),
            "license": LICENSE,
        })
        print(f"{target}  {target.stat().st_size / 1024:.0f} KB  ({user.get('name')})")
    print_rate(_last_headers)
    if failed:
        sys.exit(1)


def verify(key: str | None = None) -> tuple:
    """One GET /photos/random. Returns (status, limit, remaining, tier, errors_text)."""
    status, headers, body = api_get("/photos/random", key=key)
    limit, remaining = rate_headers(headers)
    tier = {"50": "demo", "5000": "production"}.get(str(limit), "unknown")
    return status, limit, remaining, tier, ("" if status == 200 else api_errors(body))


def cmd_verify(argv: list) -> None:
    argparse.ArgumentParser(prog="unsplash_sheet.py --verify").parse_args(argv)
    key = require_access_key()
    status, limit, remaining, tier, errors = verify(key)
    print(f"HTTP {status}   X-Ratelimit-Limit: {limit}   X-Ratelimit-Remaining: {remaining}   tier: {tier}")
    if status != 200:
        print(f"error: {errors}", file=sys.stderr)
        sys.exit(1)


# --------------------------------------------------------------------------- scrape fallback (unchanged)
def scrape_ids(page, phrase: str) -> list[str]:
    page.goto(f"https://unsplash.com/s/photos/{quote(phrase)}", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(2500)
    for _ in range(3):
        page.mouse.wheel(0, 1800)
        page.wait_for_timeout(700)
    html_src = page.content()
    ids = []
    for m in re.finditer(r"images\.unsplash\.com/photo-([0-9]{13}-[0-9a-f]{12})", html_src):
        if m.group(1) not in ids:
            ids.append(m.group(1))
    return ids[:PER_PHRASE]


def cmd_scrape(argv: list) -> None:
    from playwright.sync_api import sync_playwright  # only the scrape path needs it

    out = Path(argv[0]); out.mkdir(parents=True, exist_ok=True)
    # ponytail: unsplash.com returns 401/403 to headless Chromium (2026-09-04). The working path is
    # the in-app Browser pane: open the search page there, pull IDs with one JS line, and pass them
    # in as `--ids-file <json>` ({"phrase": ["id", ...]}); headless is then only used to verify loads.
    rows = []
    if argv[1] == "--ids-file":
        data = json.loads(Path(argv[2]).read_text(encoding="utf-8"))
        phrases = list(data)
        for ph, ids in data.items():
            for pid in ids[:PER_PHRASE]:
                rows.append({"id": pid.replace("photo-", ""), "phrase": ph, "loaded": None})
    else:
        phrases = argv[1:]
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        for ph in ([] if rows else phrases):
            for pid in scrape_ids(page, ph):
                rows.append({"id": pid, "phrase": ph, "loaded": None})
        # verify each thumbnail actually loads (grey box = dead ID)
        for r in rows:
            resp = page.request.get(thumb_url(r["id"]))
            r["loaded"] = resp.ok
        browser.close()
    (out / "ids.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    write_sheet(out, phrases, [dict(r, thumb=thumb_url(r["id"])) for r in rows])
    ok = sum(1 for r in rows if r["loaded"])
    print(f"{len(rows)} candidates, {ok} load -> {out / 'contact-sheet.html'}")


# --------------------------------------------------------------------------- entry
def main():
    argv = sys.argv[1:]
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__, file=sys.stderr)
        sys.exit(0 if argv else 1)
    mode, rest = argv[0], argv[1:]
    if mode == "--api":
        cmd_api(rest)
    elif mode == "--download":
        cmd_download(rest)
    elif mode == "--verify":
        cmd_verify(rest)
    else:
        if len(argv) < 2:
            print(__doc__, file=sys.stderr)
            sys.exit(1)
        cmd_scrape(argv)


if __name__ == "__main__":
    main()
