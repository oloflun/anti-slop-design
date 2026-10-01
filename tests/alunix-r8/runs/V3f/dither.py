#!/usr/bin/env python3
"""V3f dither generator.

Floyd-Steinberg 1-bit dither for the rutverket cell grid. Source images
are downscaled to roughly a third of their long edge, dithered to 1-bit,
then scaled back up with NEAREST so the dots read as physical print grain
at cell size. Two ink variants are produced per source: black dots on the
--grey ground (for light cells) and white dots on black (for dark cells).
Output is lossless WebP, kept small because the source data is 1-bit.
"""
import os
from PIL import Image

SRC_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..",
                        "tests", "alunix-concepts-r3", "build", "assets")
SRC_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "..", "..", "..", "alunix-concepts-r3", "build", "assets"))
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "dither")

IMAGES = {
    "k1-stage-pool": "k1-stage-pool.webp",
    "k4-cabin-desk": "k4-cabin-desk.webp",
    "demo-hyperborea": "demo-hyperborea.webp",
    "demo-calyx": "demo-calyx.webp",
    "demo-horai": "demo-horai.webp",
}

GREY = (0xd9, 0xd9, 0xd9)
BLACK = (0x00, 0x00, 0x00)
WHITE = (0xff, 0xff, 0xff)


def dither_variant(im, ink, paper):
    """Return an RGB image: 1-bit Floyd-Steinberg dither, ink on paper."""
    w, h = im.size
    small = im.convert("L").resize((max(1, w // 3), max(1, h // 3)), Image.LANCZOS)
    bw = small.convert("1", dither=Image.FLOYDSTEINBERG)
    big = bw.resize((w, h), Image.NEAREST)
    out = Image.new("RGB", (w, h), paper)
    ink_layer = Image.new("RGB", (w, h), ink)
    out.paste(ink_layer, mask=big.point(lambda p: 255 if p == 0 else 0))
    return out


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for name, fname in IMAGES.items():
        path = os.path.join(SRC_DIR, fname)
        if not os.path.exists(path):
            print("MISSING", path)
            continue
        im = Image.open(path).convert("RGB")
        # cap long edge at 900 for a fast, print-grain dither
        w, h = im.size
        scale = 900 / max(w, h)
        if scale < 1:
            im = im.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

        on_grey = dither_variant(im, BLACK, GREY)
        on_black = dither_variant(im, WHITE, BLACK)

        p1 = os.path.join(OUT_DIR, f"{name}-dither-grey.webp")
        p2 = os.path.join(OUT_DIR, f"{name}-dither-black.webp")
        on_grey.save(p1, "WEBP", lossless=True, quality=100, method=6)
        on_black.save(p2, "WEBP", lossless=True, quality=100, method=6)
        print("wrote", p1, os.path.getsize(p1))
        print("wrote", p2, os.path.getsize(p2))


if __name__ == "__main__":
    main()
