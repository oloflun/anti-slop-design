from playwright.sync_api import sync_playwright
import sys

URL = "http://127.0.0.1:8795/tests/alunix-r8/runs/V3d/index.html"

HEADING_SEL = "h1, h2, h3, .ts, .statement, .close-mailto"

SWEEP_JS = """
(sel) => {
  // Box-shorthand-aware inset() parser (1/2/3/4-token forms - a fixed-count
  // parser silently mis-skips 1- and 2-token serializations, see V3d R8-9
  // lore). Returns {top,right,bottom,left} in px, or null if not inset()/none.
  function parseInset(clipPath, w, h) {
    const m = /^inset\\(([^)]+)\\)/.exec(clipPath);
    if (!m) return null;
    const raw = m[1].trim().split(/\\s+/);
    function val(tok, base) { return tok.endsWith('%') ? parseFloat(tok)/100*base : parseFloat(tok); }
    let top, right, bottom, left;
    if (raw.length === 1) { top = right = bottom = left = val(raw[0], h); }
    else if (raw.length === 2) { top = bottom = val(raw[0], h); right = left = val(raw[1], w); }
    else if (raw.length === 3) { top = val(raw[0], h); right = left = val(raw[1], w); bottom = val(raw[2], h); }
    else { top = val(raw[0], h); right = val(raw[1], w); bottom = val(raw[2], h); left = val(raw[3], w); }
    return { top, right, bottom, left };
  }
  const headings = Array.from(document.querySelectorAll(sel));
  const hits = [];
  for (const el of headings) {
    const cs = getComputedStyle(el);
    if (parseFloat(cs.opacity) < 0.05) continue;
    let rect = el.getBoundingClientRect();
    if (rect.width <= 0 || rect.height <= 0) continue;
    // Restrict to the visible sub-rect after clip-path on the element itself
    // OR any ancestor (e.g. .cs h3 - the clip-path sits on the .cs <li>
    // parent, not the h3 - several stacked in the same grid cell; only the
    // unclipped slice is a real on-screen presence. Plan 057 Verification B2).
    let clipped = false;
    let node = el, depth = 0;
    while (node && node.nodeType === 1 && depth < 8) {
      depth++;
      const ncs = node === el ? cs : getComputedStyle(node);
      const nrect = node.getBoundingClientRect();
      const inset = parseInset(ncs.clipPath, nrect.width, nrect.height);
      if (inset) {
        const vTop = Math.max(rect.top, nrect.top + inset.top);
        const vBottom = Math.min(rect.bottom, nrect.bottom - inset.bottom);
        const vLeft = Math.max(rect.left, nrect.left + inset.left);
        const vRight = Math.min(rect.right, nrect.right - inset.right);
        rect = { top: vTop, bottom: vBottom, left: vLeft, right: vRight };
        clipped = true;
      }
      node = node.parentElement;
    }
    if (clipped && (rect.left >= rect.right || rect.top >= rect.bottom)) continue; // fully clipped
    const vw = window.innerWidth, vh = window.innerHeight;
    const left = Math.max(0, rect.left), right = Math.min(vw, rect.right);
    const top = Math.max(0, rect.top), bottom = Math.min(vh, rect.bottom);
    if (left >= right || top >= bottom) continue;
    for (let iy = 0; iy < 3; iy++) {
      for (let ix = 0; ix < 3; ix++) {
        const px = left + (right-left) * (ix+0.5)/3;
        const py = top + (bottom-top) * (iy+0.5)/3;
        const hitEl = document.elementFromPoint(px, py);
        if (!hitEl) continue;
        const isDescendant = el === hitEl || el.contains(hitEl);
        if (!isDescendant) {
          hits.push({ heading: el.tagName + '.' + el.className, px: Math.round(px), py: Math.round(py), hitTag: hitEl.tagName, hitCls: hitEl.className });
        }
      }
    }
  }
  return hits;
}
"""

def sweep(pg, width, height, step=20):
    pg.set_viewport_size({"width": width, "height": height})
    pg.goto(URL)
    pg.wait_for_timeout(600)
    total_h = pg.evaluate("document.documentElement.scrollHeight")
    all_hits = []
    y = 0
    frame = 0
    while y <= total_h:
        pg.evaluate("window.scrollTo(0, " + str(y) + ")")
        pg.wait_for_timeout(20)
        hits = pg.evaluate(SWEEP_JS, HEADING_SEL)
        for h in hits:
            h["scrollY"] = y
            h["frame"] = frame
        all_hits.extend(hits)
        y += step
        frame += 1
    return all_hits, frame

if __name__ == "__main__":
    inject_old = "--inject-old" in sys.argv
    widths = [(1920,930),(1440,900),(768,1024),(390,844)]
    with sync_playwright() as p:
        b = p.chromium.launch()
        for w,h in widths:
            pg = b.new_page(viewport={"width": w, "height": h})
            if inject_old:
                pg.goto(URL)
                pg.add_style_tag(content="""
                  .process{ margin-top:-100svh !important; }
                  .chapter-hold{ height:calc(200svh + 40svh) !important; }
                  .process-chapter{ position:sticky !important; top:0 !important; height:100svh !important; min-height:auto !important; }
                """)
            hits, frames = sweep(pg, w, h)
            print(w, "x", h, "inject_old=", inject_old, ": frames=", frames, "hits=", len(hits))
            if hits:
                for hh in hits[:5]:
                    print("  ", hh)
            pg.close()
        b.close()
