"""Measure the lit arched window aperture per frame of the push-in sequence.

    python track_window.py <frames_dir> <out_json> [--from N] [--sheet out.png]

Per frame: warm-bright mask (R>170, G>110, B<170, R-B>60) -> largest connected component
(via PIL ImageOps + simple flood fill on a downsampled grid) -> bbox in fractions of the
frame + the arch: top edge treated as a semicircle over the bbox width. Writes
{frame, x, y, w, h, arch: "top"} per frame from --from to the end, plus a contact sheet
with the boxes drawn for eyeballing.
"""
import sys, json, glob, argparse
from PIL import Image, ImageDraw
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("frames"); ap.add_argument("out"); ap.add_argument("--from", dest="start", type=int, default=60)
ap.add_argument("--sheet", default=None)
a = ap.parse_args()

files = sorted(glob.glob(a.frames + "/f*.webp"))
rows = []; tiles = []
for i, f in enumerate(files, start=1):
    if i < a.start: continue
    im = Image.open(f).convert("RGB"); W, H = im.size
    small = im.resize((W // 4, H // 4)); arr = np.asarray(small).astype(int)
    R, G, B = arr[..., 0], arr[..., 1], arr[..., 2]
    lum = (R * 299 + G * 587 + B * 114) // 1000
    mask = (lum > 105) & ((R - B) > 35) & (R > 140)
    # close the gaps across mullions/frames so the whole glazed aperture is one blob
    from PIL import ImageFilter
    m_img = Image.fromarray((mask * 255).astype("uint8")).filter(ImageFilter.MaxFilter(11)).filter(ImageFilter.MinFilter(7))
    mask = np.asarray(m_img) > 0
    # largest component by BFS
    h, w = mask.shape; seen = np.zeros_like(mask, bool); best = None
    for y in range(h):
        for x in range(w):
            if mask[y, x] and not seen[y, x]:
                stack = [(y, x)]; seen[y, x] = True; pts = []
                while stack:
                    cy, cx = stack.pop(); pts.append((cy, cx))
                    for ny, nx in ((cy-1,cx),(cy+1,cx),(cy,cx-1),(cy,cx+1)):
                        if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True; stack.append((ny, nx))
                if best is None or len(pts) > len(best): best = pts
    if not best:
        rows.append({"frame": i, "found": False}); continue
    ys = [p[0] for p in best]; xs = [p[1] for p in best]
    x0, x1, y0, y1 = min(xs)*4, (max(xs)+1)*4, min(ys)*4, (max(ys)+1)*4
    rows.append({"frame": i, "found": True, "x": round(x0/W, 4), "y": round(y0/H, 4),
                 "w": round((x1-x0)/W, 4), "h": round((y1-y0)/H, 4), "area": len(best)*16/(W*H)})
    if a.sheet and (i - a.start) % 5 == 0:
        d = ImageDraw.Draw(im); d.rectangle([x0, y0, x1, y1], outline=(0, 255, 0), width=6)
        d.text((x0+8, y0+8), f"f{i}", fill=(0, 255, 0))
        tiles.append(im.resize((480, int(H*480/W))))
json.dump({"frames_dir": a.frames, "note": "x,y,w,h as fractions of the frame; aperture = bbox with a semicircular top (arch)", "track": rows},
          open(a.out, "w", encoding="utf-8"), indent=1)
if a.sheet and tiles:
    cols = 4; rws = (len(tiles)+cols-1)//cols; tw, th = tiles[0].size
    sheet = Image.new("RGB", (cols*(tw+8)+8, rws*(th+8)+8), "#222")
    for k, t in enumerate(tiles): sheet.paste(t, (8+(k%cols)*(tw+8), 8+(k//cols)*(th+8)))
    sheet.save(a.sheet)
print(json.dumps([r for r in rows if r.get("found")][-6:], indent=0))
