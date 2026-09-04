#!/usr/bin/env python3
"""_refero_image.py <slug> <processed_image_path> [second_image_path]

Ad-hoc helper for the refero catalogue pass (not part of the standing pipeline).
Copies/resizes a processed/ image into entries/<slug>/:
  shot.webp   longest edge <= 2200, quality 82
  fold.webp   resize width to 1440, then top 900px crop (or full height if shorter)
  shot-2.webp optional second image, same longest-edge treatment as shot.webp
"""
import sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent.parent
MAX_LONG_EDGE = 2200
FOLD_W = 1440
FOLD_H = 900


def save_shot(src: Path, dest: Path):
    img = Image.open(src).convert("RGB")
    w, h = img.size
    long_edge = max(w, h)
    if long_edge > MAX_LONG_EDGE:
        scale = MAX_LONG_EDGE / long_edge
        img = img.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, "WEBP", quality=82, method=6)
    return img.size


def save_fold(src: Path, dest: Path):
    img = Image.open(src).convert("RGB")
    w, h = img.size
    if w != FOLD_W:
        scale = FOLD_W / w
        img = img.resize((FOLD_W, max(1, int(h * scale))), Image.LANCZOS)
        w, h = img.size
    crop_h = min(FOLD_H, h)
    img = img.crop((0, 0, w, crop_h))
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, "WEBP", quality=82, method=6)
    return img.size


def main():
    if len(sys.argv) < 3:
        print("usage: _refero_image.py <slug> <img1> [img2]", file=sys.stderr)
        sys.exit(1)
    slug = sys.argv[1]
    img1 = Path(sys.argv[2])
    out_dir = ROOT / "design-catalogue" / "entries" / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    shot_size = save_shot(img1, out_dir / "shot.webp")
    fold_size = save_fold(img1, out_dir / "fold.webp")
    print(f"{slug}: shot.webp {shot_size}, fold.webp {fold_size}")

    if len(sys.argv) > 3:
        img2 = Path(sys.argv[3])
        shot2_size = save_shot(img2, out_dir / "shot-2.webp")
        print(f"{slug}: shot-2.webp {shot2_size}")


if __name__ == "__main__":
    main()
