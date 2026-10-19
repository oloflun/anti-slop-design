from PIL import Image, ImageDraw
from pathlib import Path

BASE = Path(r"C:\Users\Anton L\anti-slop-design")
OURS = BASE / "tests/alunix-r8/runs/V3d/shots/r3/ours"
REF = BASE / "tests/alunix-r8/runs/V3c/shots/fasA"
OUT = BASE / "tests/alunix-r8/runs/V3d/shots/r3"
OUT.mkdir(parents=True, exist_ok=True)

ROWS = [
    ("P02", "back-1440.png", "hoy-1440/hoy-home-1440--s00.png", "back-390.png", "hoy-390/hoy-home-390--s00.png"),
    ("P03", "thesis-1440.png", "hoy-1440/hoy-home-1440--s01.png", "thesis-390.png", "hoy-390/hoy-home-390--s01.png"),
]

def compose(ours_path, ref_path, out_path):
    a = Image.open(ours_path).convert("RGB")
    b = Image.open(ref_path).convert("RGB")
    h = min(a.height, b.height)
    aw = int(a.width * h / a.height)
    bw = int(b.width * h / b.height)
    a2 = a.resize((aw, h))
    b2 = b.resize((bw, h))
    gap = 24
    label_h = 22
    sheet = Image.new("RGB", (aw + gap + bw, h + label_h), "white")
    sheet.paste(a2, (0, 0))
    sheet.paste(b2, (aw + gap, 0))
    d = ImageDraw.Draw(sheet)
    d.text((4, h + 4), f"{out_path.stem}  (ours | ref: {ref_path.name})", fill="black")
    sheet.save(out_path)
    print("wrote", out_path)

for rid, our1440, ref1440, our390, ref390 in ROWS:
    compose(OURS / our1440, REF / ref1440, OUT / f"{rid}-1440.png")
    compose(OURS / our390, REF / ref390, OUT / f"{rid}-390.png")
print("done")
