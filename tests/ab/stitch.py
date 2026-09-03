"""Side-by-side stitch of two full-page PNGs, top-aligned, white gap between."""
import sys
from PIL import Image

def main(a_path, b_path, out_path, gap=24):
    a = Image.open(a_path).convert("RGB")
    b = Image.open(b_path).convert("RGB")
    w = a.width + gap + b.width
    h = max(a.height, b.height)
    canvas = Image.new("RGB", (w, h), "white")
    canvas.paste(a, (0, 0))
    canvas.paste(b, (a.width + gap, 0))
    canvas.save(out_path)
    print("wrote", out_path, canvas.size)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
