import os
from PIL import Image
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:3305"
HERE = os.path.dirname(os.path.abspath(__file__))
SHOTS = [
    ("calyx", BASE + "/sites/calyx.html"),
    ("horai", BASE + "/sites/horai.html"),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    for name, url in SHOTS:
        page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
        page.goto(url, wait_until="networkidle", timeout=30000)
        page.wait_for_timeout(300)
        png_path = os.path.join(HERE, name + "-raw.png")
        page.screenshot(path=png_path)
        page.close()
        im = Image.open(png_path)
        # raw screenshot at dsf=2 is 2880x1800; downsample isn't needed, keep full res webp
        webp_path = os.path.join(HERE, name + "-1440.webp")
        im.save(webp_path, "WEBP", quality=82, method=6)
        os.remove(png_path)
        print(name, im.size, os.path.getsize(webp_path))
    browser.close()
