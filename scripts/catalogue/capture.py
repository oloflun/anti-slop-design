#!/usr/bin/env python3
"""capture.py <url|file> <slug>

Captures a page with Playwright and writes, under design-catalogue/entries/<slug>/:
  shot.webp        full-page capture (desktop 1440, longest edge <= 2200px)
  fold.webp        first viewport 1440x900
  shot.png         lossless copy of fold (<=1440 wide) for vision
  slices/NN.webp    viewport-height slices of the full page (max 12)
"""
import sys
import os
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

VIEWPORT_W = 1440
VIEWPORT_H = 900
MAX_LONG_EDGE = 2200
MAX_SLICES = 12
MAX_SCROLL_STEPS = 60


def resolve_url(target: str) -> str:
    if target.startswith("http://") or target.startswith("https://") or target.startswith("file://"):
        return target
    p = Path(target)
    if p.exists():
        return p.resolve().as_uri()
    return target


def save_webp(png_bytes: bytes, dest: Path, max_long_edge: int | None = None):
    from io import BytesIO
    img = Image.open(BytesIO(png_bytes)).convert("RGB")
    if max_long_edge:
        w, h = img.size
        long_edge = max(w, h)
        if long_edge > max_long_edge:
            scale = max_long_edge / long_edge
            img = img.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, "WEBP", quality=82, method=6)
    return img.size


def main():
    if len(sys.argv) != 3:
        print("usage: capture.py <url|file> <slug>", file=sys.stderr)
        sys.exit(1)
    target, slug = sys.argv[1], sys.argv[2]
    url = resolve_url(target)

    root = Path(__file__).resolve().parent.parent.parent
    out_dir = root / "design-catalogue" / "entries" / slug
    slices_dir = out_dir / "slices"
    out_dir.mkdir(parents=True, exist_ok=True)
    slices_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": VIEWPORT_W, "height": VIEWPORT_H}, device_scale_factor=1)
        try:
            page.goto(url, wait_until="networkidle", timeout=60000)
        except Exception:
            # ponytail: sites with long-polling never reach networkidle; settle on load instead.
            page.goto(url, wait_until="load", timeout=60000)
        page.wait_for_timeout(1200)

        # Dismiss cookie banners (they sat in the fold of insign/nglm). Decline first, accept second.
        for sel in ["button:has-text('Neka')", "button:has-text('Decline')", "button:has-text('Reject')",
                    "button:has-text('Avvisa')", "button:has-text('Acceptera')", "button:has-text('Accept')",
                    "button:has-text('Godkänn')", "[id*='cookie'] button", "[class*='cookie'] button"]:
            try:
                btn = page.locator(sel).first
                if btn.is_visible(timeout=400):
                    btn.click(timeout=1500)
                    page.wait_for_timeout(400)
                    break
            except Exception:
                continue

        # Scroll through once to trigger reveal animations / lazy loads.
        total_height = page.evaluate("document.body.scrollHeight")
        y = 0
        # ponytail: hard step cap. Pages whose scrollHeight grows as you scroll
        # (sticky scroll-scrub sections, infinite lists) never terminate otherwise.
        for _ in range(MAX_SCROLL_STEPS):
            if y >= total_height:
                break
            page.evaluate(f"window.scrollTo(0, {y})")
            page.wait_for_timeout(150)
            y += VIEWPORT_H
            total_height = page.evaluate("document.body.scrollHeight")
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_timeout(300)

        # Fold (first viewport)
        fold_png = page.screenshot(type="png")
        save_webp(fold_png, out_dir / "fold.webp")

        # shot.png: lossless copy of fold, <=1440 wide
        from io import BytesIO
        fold_img = Image.open(BytesIO(fold_png)).convert("RGB")
        if fold_img.width > 1440:
            scale = 1440 / fold_img.width
            fold_img = fold_img.resize((1440, int(fold_img.height * scale)), Image.LANCZOS)
        fold_img.save(out_dir / "shot.png", "PNG")

        # Full page shot
        full_png = page.screenshot(type="png", full_page=True)
        save_webp(full_png, out_dir / "shot.webp", max_long_edge=MAX_LONG_EDGE)

        # Slices: viewport-height slices of the full page, capped at MAX_SLICES
        total_height = page.evaluate("document.body.scrollHeight")
        num_slices = min(MAX_SLICES, max(1, -(-total_height // VIEWPORT_H)))
        for i in range(num_slices):
            y = i * VIEWPORT_H
            page.evaluate(f"window.scrollTo(0, {y})")
            page.wait_for_timeout(200)
            slice_png = page.screenshot(type="png")
            save_webp(slice_png, slices_dir / f"{i:02d}.webp")

        browser.close()

    print(f"captured {slug} -> {out_dir}")


if __name__ == "__main__":
    main()
