from PIL import Image, ImageDraw
from pathlib import Path

BASE = Path(r"C:\Users\Anton L\anti-slop-design")
OURS = BASE / "tests/alunix-r8/runs/V3d/shots/r1/preview"
REF = BASE / "tests/alunix-r8/runs/V3c/shots/fasA"
OUT = BASE / "tests/alunix-r8/runs/V3d/shots/r1/par"
OUT.mkdir(parents=True, exist_ok=True)

ROWS = [
    ("P01", "front-1440.png", "hoy-1440/hoy-webb-1440--s00.png", "front-390.png", "hoy-390/hoy-home-390--s00.png"),
    ("P02", "back-1440.png", "hoy-1440/hoy-home-1440--s00.png", "back-390.png", "hoy-390/hoy-home-390--s00.png"),
    ("P03", "thesis-1440.png", "hoy-1440/hoy-home-1440--s01.png", "thesis-390.png", "hoy-390/hoy-home-390--s01.png"),
    ("P04", "ledger-1440.png", "hoy-1440/hoy-webb-1440--s03.png", "ledger-390.png", "hoy-390/hoy-webb-390--s02.png"),
    ("P05", "horai-band-1440.png", "insign-1440/insign-1440--s04.png", "horai-band-390.png", "insign-390/insign-390--s07.png"),
    ("P06", "process-chapter-1440.png", "hoy-1440/hoy-home-1440--s03.png", "process-chapter-390.png", "hoy-390/hoy-home-390--s03.png"),
    ("P07", "process-01-1440.png", "hoy-1440/hoy-home-1440--s03.png", "process-01-390.png", "hoy-390/hoy-webb-390--s00.png"),
    ("P08", "process-02-1440.png", "hoy-1440/hoy-webb-1440--s08.png", "process-02-390.png", "hoy-390/hoy-webb-390--s08.png"),
    ("P09", "process-03-1440.png", "hoy-1440/hoy-home-1440--s06.png", "process-03-390.png", "hoy-390/hoy-home-390--s05.png"),
    ("P10", "process-04-1440.png", "hoy-1440/hoy-home-1440--s07.png", "process-04-390.png", "hoy-390/hoy-home-390--s06.png"),
    ("P11", "process-05-1440.png", "hoy-1440/hoy-webb-1440--s07.png", "process-05-390.png", "hoy-390/hoy-webb-390--s05.png"),
    ("P12", "process-06-1440.png", "hoy-1440/hoy-webb-1440--s01.png", "process-06-390.png", "hoy-390/hoy-webb-390--s01.png"),
    ("P13", "process-07-1440.png", "hoy-1440/hoy-webb-1440--s10.png", "process-07-390.png", "hoy-390/hoy-webb-390--s09.png"),
    ("P14", "principer-1440.png", "hoy-1440/hoy-webb-1440--s04.png", "principer-390.png", "hoy-390/hoy-webb-390--s02.png"),
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
    d.text((4, h + 4), f"{out_path.stem}  (our | ref: {ref_path.name})", fill="black")
    sheet.save(out_path)
    print("wrote", out_path)

for rid, our1440, ref1440, our390, ref390 in ROWS:
    o1 = OURS / our1440
    r1 = REF / ref1440
    o3 = OURS / our390
    r3 = REF / ref390
    if o1.exists() and r1.exists():
        compose(o1, r1, OUT / f"{rid}-1440.png")
    else:
        print("MISSING 1440", rid, o1.exists(), r1.exists())
    if o3.exists() and r3.exists():
        compose(o3, r3, OUT / f"{rid}-390.png")
    else:
        print("MISSING 390", rid, o3.exists(), r3.exists())

# P15
p15_1440_a = BASE / "tests/alunix-r8/runs/V3d/shots/r1/slices-1440/v3d-r1-1440--s15.png"
p15_1440_b = BASE / "tests/alunix-r8/runs/V3d/shots/r1/slices-1440/v3d-r1-1440--s16.png"
if p15_1440_a.exists() and p15_1440_b.exists():
    imga = Image.open(p15_1440_a).convert("RGB")
    imgb = Image.open(p15_1440_b).convert("RGB")
    stacked = Image.new("RGB", (imga.width, imga.height + imgb.height), "white")
    stacked.paste(imga, (0, 0))
    stacked.paste(imgb, (0, imga.height))
    stacked.save(OUT / "P15-ours-1440.png")
    ref_a = REF / "hoy-1440/hoy-home-1440--s08.png"
    ref_b = REF / "hoy-1440/hoy-home-1440--s09.png"
    ra = Image.open(ref_a).convert("RGB")
    rb = Image.open(ref_b).convert("RGB")
    refstack = Image.new("RGB", (ra.width, ra.height + rb.height), "white")
    refstack.paste(ra, (0, 0))
    refstack.paste(rb, (0, ra.height))
    refstack.save(OUT / "P15-ref-1440.png")
    compose(OUT / "P15-ours-1440.png", OUT / "P15-ref-1440.png", OUT / "P15-1440.png")

p15_390 = BASE / "tests/alunix-r8/runs/V3d/shots/r1/slices-390/v3d-r1-390--s13.png"
p15_390_ref = REF / "insign-390/insign-390--s10.png"
if p15_390.exists() and p15_390_ref.exists():
    compose(p15_390, p15_390_ref, OUT / "P15-390.png")

print("done")
