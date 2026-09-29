#!/usr/bin/env python3
"""R6 runda 6 (F-019/F-022), fas 1b: 11 stegbilder (5 Calyx + 6 Horai) for
showcasens detaljcell - ANDRA passet, efter att de nya stegtexterna (COPY-
R6.md #8) satts in i index.html FORE detta pass, per leadens instruktion
(textbytet andrar textcellens hojd och darmed detaljcellens proportion).

Grundorsaken till fas 1's sju felaktiga utsnitt (mätt, inte gissat):
1. HORAI_ASPECT var en FORHANDSGISSNING (+15% pa dåvarande hojd, i tron att
   texten skulle krympa) - men Horais textcell var redan 178,5px INNAN
   copy-bytet (matt i verify_r6.py fore och efter: oforandrad), sa den
   gissade aspekten (1,2224) matchade ALDRIG den verkliga cellen (1,4058).
   object-fit:cover i den FEL bredare cellen skar da bort text som fanns i
   kallbilden men inte i den slutliga cellen - `object-position` styrde
   VILKEN kant som overlevde skarningen, vilket forklarar exakt de skarningar
   leaden rapporterade (H1 "H" borta, H4 "SANSAI"/"1480" skurna upptill,
   H5 "T" i "THE ROOM" borta).
2. Nagra bilder (H1, H2, H5) anvande en FAST klippbredd (600 CSS px, de
   gamla CALYX_CLIP_W/HORAI_CLIP_W-konstanterna) i stallet for malelementets
   egen matta bredd - om elementet var bredare an 600 px skars det rakt av,
   oavsett aspekt.
Fixen: en enda ASPECT-konstant matt direkt i den NYA (efter copy-bytet)
cellen for BADA casen (de rakade sammanfalla exakt: 599.578125 x
426.53125 CSS px, samma for Calyx och Horai), och en generell
"vax-till-aspekt"-algoritm (crop_for_elements) som VAXER den kortare sidan
for att na malformatet - den kan aldrig klippa ett element den fatt i sin
matt-lista, bara lagga till marginal.

Metod i ovrigt oforandrad: Playwright headless, viewport 1440 bred (hojd
per bild, se kommentarer), device_scale_factor=2, sajterna via servern
(port 3307). Dither: dither_variant() fran runs/V3f/dither.py, oforandrad.
"""
import importlib.util
import os
from playwright.sync_api import sync_playwright
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "assets", "steps")
BASE = "http://127.0.0.1:3307"

_dither_path = os.path.normpath(os.path.join(HERE, "..", "V3f", "dither.py"))
_spec = importlib.util.spec_from_file_location("v3f_dither", _dither_path)
_v3f_dither = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_v3f_dither)
dither_variant = _v3f_dither.dither_variant
GREY = _v3f_dither.GREY
BLACK = _v3f_dither.BLACK
WHITE = _v3f_dither.WHITE

# ---- the one, measured (not guessed) aspect - see module docstring §1.
# verify_r6.py, after the COPY-R6.md #8 text swap: both cases' detail cell
# is 599.578125 x 426.53125 CSS px at 1440x900.
CELL_W, CELL_H = 599.578125, 426.53125
ASPECT = CELL_W / CELL_H  # 1.40580...
OUT_W = 1200
OUT_H = round(OUT_W / ASPECT)  # 854
PAD_DEFAULT = 28  # CSS px in the SOURCE page's own coordinate space; see
# note in crop_for_elements() for why this is generous relative to the
# brief's "~20px in the cell" floor.

REVEAL_WAIT_MS = 2000


def crop_for_elements(bboxes, pad, aspect):
    """The one rule that replaces fas 1's per-image ad-hoc math: take the
    union bounding box of every element that must survive uncut, add `pad`
    CSS px on every side, then GROW (never shrink) the shorter dimension
    until the box matches `aspect` exactly. Every element in `bboxes`
    is therefore guaranteed to still be inside the final crop - the
    algorithm can only add margin, never remove content. Returns
    {x,y,w,h} in the same CSS-px coordinate space as the input boxes.

    `pad` is in the SOURCE page's coordinate space, which is usually more
    zoomed-in than the final ~600px-wide cell, so 28px here reads as
    comfortably more than the brief's "~20px in the cell" once the whole
    crop is scaled down to cell size - never less.
    """
    x0 = min(b["x"] for b in bboxes) - pad
    y0 = min(b["y"] for b in bboxes) - pad
    x1 = max(b["x"] + b["w"] for b in bboxes) + pad
    y1 = max(b["y"] + b["h"] for b in bboxes) + pad
    w, h = x1 - x0, y1 - y0
    cur_aspect = w / h
    if cur_aspect < aspect:
        new_w = h * aspect
        dx = (new_w - w) / 2
        x0 -= dx
        x1 += dx
        w = new_w
    else:
        new_h = w / aspect
        dy = (new_h - h) / 2
        y0 -= dy
        y1 += dy
        h = new_h
    return {"x": x0, "y": y0, "w": w, "h": h}


def crop_anchored(bboxes, pad, aspect, anchor, extra_span=0.0):
    """Same growth rule as crop_for_elements, but asymmetric: `anchor` is
    'top' or 'bottom' and fixes that edge in place, growing only toward the
    OTHER edge. Used for the wide, page-width rows (a photo pair's
    captions, a price-ledger row, a menu numeral-through-price line) where
    a symmetric grow would spill into the section above or below instead
    of into more of the SAME section's own content.
    `extra_span` (CSS px) pads the anchored edge outward before growth, for
    cases that want a bit more breathing room on the fixed side too."""
    x0 = min(b["x"] for b in bboxes) - pad
    x1 = max(b["x"] + b["w"] for b in bboxes) + pad
    y_top = min(b["y"] for b in bboxes) - pad
    y_bot = max(b["y"] + b["h"] for b in bboxes) + pad
    w = x1 - x0
    h_needed = w / aspect
    if anchor == "bottom":
        y1 = y_bot + extra_span
        y0 = y1 - h_needed
    else:
        y0 = y_top - extra_span
        y1 = y0 + h_needed
    return {"x": x0, "y": y0, "w": w, "h": y1 - y0}


def clamp_clip(x, y, w, h, page_w=1440):
    if x < 0:
        x = 0
    if x + w > page_w:
        x = max(0, page_w - w)
    if y < 0:
        y = 0
    return x, y, w, h


def shoot_rect(page, tmp_png, rect):
    """Capture an arbitrary CSS-px rect that may be TALLER than the current
    900px viewport, without resizing the viewport (which would inflate
    every `vh`-sized section on the page - calyx.html's hero is `h-[88vh]`,
    horai.html's hero/quote/room all use `vh` too - pushing content far
    down the document and defeating a taller viewport before it helps) and
    without a full-page screenshot (measured failing outright on horai.html:
    `Page.captureScreenshot: Unable to capture screenshot`, root-caused to
    its `.parallax{background-attachment:fixed}` sections).

    The proven method (tested standalone before wiring in, see
    scratchpad test_clip*.py): Playwright's ELEMENT screenshot
    (`locator.screenshot()`) captures beyond the viewport correctly - CDP's
    captureBeyondViewport applies to element screenshots even though plain
    `page.screenshot(clip=...)` silently clamps to the viewport (the exact
    bug this round's leaden review traced fas-1's cut content to). Drop an
    invisible, pointer-events:none marker <div> at the exact rect (position
    absolute, converted from the viewport-relative bbox coordinates to
    page-absolute with the current window.scrollY - never scrolls between
    measuring and shooting, so this conversion is exact), screenshot THAT
    element (it has no visual styling of its own, so the capture shows the
    real page content beneath it), then remove the marker."""
    x, y, w, h = clamp_clip(rect["x"], rect["y"], rect["w"], rect["h"])
    page.evaluate(f"""() => {{
        const old = document.getElementById('__probe_marker');
        if (old) old.remove();
        const m = document.createElement('div');
        m.id = '__probe_marker';
        m.style.position = 'absolute';
        m.style.left = '{x}px';
        m.style.top = ({y} + window.scrollY) + 'px';
        m.style.width = '{w}px';
        m.style.height = '{h}px';
        m.style.pointerEvents = 'none';
        m.style.margin = '0';
        m.style.zIndex = '2147483647';
        document.body.appendChild(m);
    }}""")
    page.locator("#__probe_marker").screenshot(path=tmp_png, timeout=15000)
    page.evaluate("() => { const m = document.getElementById('__probe_marker'); if (m) m.remove(); }")


def fit_to_target(png_path, target_w, target_h):
    """Final exact-size normalisation: RESIZE ONLY, never crop.
    crop_for_elements()/crop_anchored() already match `aspect` by
    construction for almost every image, so this is a no-op stretch in
    practice - but a couple of images (C5's colophon clamp) deliberately
    accept a slightly-off aspect rather than risk this step cropping real
    content off the side, which is exactly the bug leaden traced fas-1's
    cut numerals/prices to (a downstream crop-to-aspect step eating
    content an upstream step had already measured safe). A few px of
    non-uniform stretch is never visible at this scale; a clipped word is."""
    im = Image.open(png_path).convert("RGB")
    im = im.resize((target_w, target_h), Image.LANCZOS)
    im.save(png_path)


def save_color_and_dither(png_path, case, n, ink, paper):
    fit_to_target(png_path, OUT_W, OUT_H)
    im = Image.open(png_path).convert("RGB")
    color_out = os.path.join(OUT_DIR, f"{case}-{n}.webp")
    im.save(color_out, "WEBP", quality=82, method=6)

    w, h = im.size
    scale = 900 / max(w, h)
    dith_src = im.resize((int(w * scale), int(h * scale)), Image.LANCZOS) if scale < 1 else im
    dithered = dither_variant(dith_src, ink, paper)
    dither_out = os.path.join(OUT_DIR, f"{case}-{n}-dither.webp")
    dithered.save(dither_out, "WEBP", lossless=True, quality=100, method=6)
    print("wrote", color_out, os.path.getsize(color_out))
    print("wrote", dither_out, os.path.getsize(dither_out))


def wait_reveal(page, selector_js):
    page.evaluate(f"""() => {{
        const el = {selector_js};
        if (el) el.scrollIntoView({{behavior:'instant', block:'center'}});
    }}""")
    page.wait_for_timeout(REVEAL_WAIT_MS)


def get_bbox(page, selector_js):
    return page.evaluate(f"""() => {{
        const el = {selector_js};
        if (!el) return null;
        const r = el.getBoundingClientRect();
        return {{x: r.x, y: r.y, w: r.width, h: r.height}};
    }}""")


def last_line_bbox(page, selector_js):
    """The bounding box of the LAST wrapped text line of an element, via
    Range.getClientRects() (one rect per physical line box) - used so a
    "include at most the last line above" crop can't accidentally include
    a partial line."""
    return page.evaluate(f"""() => {{
        const el = {selector_js};
        const range = document.createRange();
        range.selectNodeContents(el);
        const rects = Array.from(range.getClientRects());
        const r = rects[rects.length - 1];
        return {{x: r.x, y: r.y, w: r.width, h: r.height}};
    }}""")


def run_calyx(browser, tmp_dir):
    # ---------------------------------------------------------------- C1
    # Fas 1b fix: h1 alone (no kicker - briefen sa "annars racker h1", och
    # kickern "No. 042" sitter i en helt annan kolumn langt till hoger,
    # vilket tvingade ett mycket bredare - och dartill fel-formaterat -
    # utsnitt). Hela h1 ("Botanical architecture, from Stockholm.", tre
    # rader) med generos marginal in i fotot runt om.
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page.set_default_timeout(15000)
    page.goto(f"{BASE}/sites/calyx.html", wait_until="load")
    page.evaluate("() => document.fonts.ready")
    page.wait_for_timeout(300)
    wait_reveal(page, "document.querySelector('h1')")
    h1 = get_bbox(page, "document.querySelector('h1')")
    rect = crop_for_elements([h1], PAD_DEFAULT, ASPECT)
    shoot_rect(page, os.path.join(tmp_dir, "calyx-1.png"), rect)
    page.close()

    # ---------------------------------------------------------------- C2
    # Fas 1b fix: hela #studio-brodstycket ("Calyx is a two-sister
    # atelier...", tre HELA rader) plus - om det ryms utan att klippa -
    # citatets sista rad ovanfor (via Range.getClientRects, aldrig en
    # gissad radhojd). Storre an fas 1 (mindre marginal runt sjalva
    # stycket relativt dess bredd).
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page.set_default_timeout(15000)
    page.goto(f"{BASE}/sites/calyx.html", wait_until="load")
    page.evaluate("() => document.fonts.ready")
    page.wait_for_timeout(300)
    wait_reveal(page, "document.querySelector('#studio')")
    info = page.evaluate("""() => {
        const bp = document.querySelectorAll('#studio p')[2];
        const quote = document.querySelectorAll('#studio p')[1];
        const r = bp.getBoundingClientRect();
        const qr = quote.getBoundingClientRect();
        return {body: {x:r.x,y:r.y,w:r.width,h:r.height}, quoteBottom: qr.y + qr.height};
    }""")
    # leaden 2026-09-27, tredje passet: aven med BARA brodstycket som
    # mast-inkludera-element racker den symmetriska vaxten uppat langt in
    # i citatets rader (bred, kort text tvingar mycket extra hojd). Klamp
    # toppen till strax under citatets EGNA underkant - aldrig ovanfor -
    # och lat den uteblivna hojden ga nedat i stallet (tomt, sakert papper).
    rect = crop_for_elements([info["body"]], PAD_DEFAULT, ASPECT)
    min_top = info["quoteBottom"] + 16
    if rect["y"] < min_top:
        rect["y"] = min_top
    shoot_rect(page, os.path.join(tmp_dir, "calyx-2.png"), rect)
    page.close()

    # ---------------------------------------------------------------- C3
    # Fas 1b: markningarna storre/lasbara var huvudfelet (orsak: fel
    # ASPECT-konstant lat cover-beskarningen krympa dem ytterligare - se
    # moduldokstrangen). Ramen i sig (fotoparets nedre del + BADA
    # figcaption-raderna) var redan nara ratt enligt leaden - bottom-
    # ankrad vid den senare bildtextens underkant, full bredd over bada
    # fotona, men med den KORREKTA aspekten skars inget bort langre och
    # texten blir markbart storre eftersom ingen cover-krympning sker.
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page.set_default_timeout(15000)
    page.goto(f"{BASE}/sites/calyx.html", wait_until="load")
    page.evaluate("() => document.fonts.ready")
    page.wait_for_timeout(300)
    wait_reveal(page, "document.querySelectorAll('.duo')[1]")
    band = page.evaluate("""() => {
        const figs = Array.from(document.querySelectorAll('.duo'));
        const caps = figs.map(f => f.querySelector('figcaption'));
        const fr = figs.map(f => f.getBoundingClientRect());
        const cr = caps.map(c => c.getBoundingClientRect());
        return {
            x: Math.min(...fr.map(r => r.x)),
            w: Math.max(...fr.map(r => r.x + r.width)) - Math.min(...fr.map(r => r.x)),
            capTop: Math.min(...cr.map(r => r.y)),
            capBottom: Math.max(...cr.map(r => r.y + r.height)),
        };
    }""")
    caps_bbox = {"x": band["x"], "y": band["capTop"], "w": band["w"], "h": band["capBottom"] - band["capTop"]}
    rect = crop_anchored([caps_bbox], PAD_DEFAULT, ASPECT, anchor="bottom")
    shoot_rect(page, os.path.join(tmp_dir, "calyx-3.png"), rect)
    page.close()

    # ---------------------------------------------------------------- C4
    # Fas 1b fix: bara listan, INGET fotopar. Top-ankrad vid forsta radens
    # egen kant (numeral+namn+pris, full bredd), vaxer nedat genom fler
    # HELA rader - aldrig uppat mot fotoparet ovanfor. Klipp av vid en
    # radgrans (aldrig mitt i en rad) sa numret/priset for varje synlig
    # rad star helt.
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page.set_default_timeout(15000)
    page.goto(f"{BASE}/sites/calyx.html", wait_until="load")
    page.evaluate("() => document.fonts.ready")
    page.wait_for_timeout(300)
    wait_reveal(page, "document.querySelectorAll('#index li')[1]")
    rows = page.evaluate("""() => {
        const lis = Array.from(document.querySelectorAll('#index li'));
        return lis.map(li => { const r = li.getBoundingClientRect(); return {x:r.x,y:r.y,w:r.width,h:r.height}; });
    }""")
    row0 = rows[0]
    # leaden 2026-09-27, andra passet: den tidigare radgrans-klampningen
    # andrade `rect["h"]` EFTER att crop_anchored redan matchat ASPECT
    # exakt - det fick fit_to_target (som bara litar pa att aspekten
    # redan stammer) att se en for BRED bild och skara bort sidorna,
    # exakt dar numeralen och priset sitter. Utan klampning (mattest
    # fristaende, se scratchpad test_real.py): alla fyra rader ryms redan
    # naturligt inom den aspekt-korrekta hojden, med lite fotot darunder
    # kvar osynligt - ingen klampning behovs alls.
    rect = crop_anchored([row0], PAD_DEFAULT, ASPECT, anchor="top")
    shoot_rect(page, os.path.join(tmp_dir, "calyx-4.png"), rect)
    page.close()

    # ---------------------------------------------------------------- C5
    # Fas 1b fix: samma mal (mailto-raden + adresskickern), men top-ankrad
    # vid rutans EGEN overkant (inte symmetriskt vaxande uppat) sa
    # paragrafen ovanfor ("...the light, the meal...") aldrig kommer med
    # ens till halva raden.
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page.set_default_timeout(15000)
    page.goto(f"{BASE}/sites/calyx.html", wait_until="load")
    page.evaluate("() => document.fonts.ready")
    page.wait_for_timeout(300)
    wait_reveal(page, "document.querySelector('#commission')")
    info = page.evaluate("""() => {
        const a = document.querySelector('#commission a[href^="mailto"]');
        const w = a.parentElement;
        const r = w.getBoundingClientRect();
        const colophon = document.querySelector('#commission .border-t');
        const cr = colophon ? colophon.getBoundingClientRect() : null;
        return {wrap: {x:r.x,y:r.y,w:r.width,h:r.height}, colophonTop: cr ? cr.top : null};
    }""")
    rect = crop_anchored([info["wrap"]], PAD_DEFAULT, ASPECT, anchor="top")
    # leaden 2026-09-27, andra passet: vaxten nedat racker in i colophon-
    # raden ("Photography: Linn Berggren" osv) under den morka sektionen -
    # leaden bad uttryckligen om INGEN footer. Klamp botten till strax
    # ovanfor colophon-linjens egen topp. Bredden ror vi ALDRIG (den ar
    # satt av mailto-radens egen bredd + marginal - att krympa den for att
    # tvinga tillbaka aspekten är precis den sorten sidoklipp som skar av
    # numeralen/priset i C4/H4 forra passet). En liten kvarvarande
    # aspektskillnad far fit_to_target() bara stracka bort (resize-only
    # nu), aldrig skara bort.
    if info["colophonTop"] is not None:
        max_bottom = info["colophonTop"] - 12
        if rect["y"] + rect["h"] > max_bottom:
            rect["h"] = max_bottom - rect["y"]
    shoot_rect(page, os.path.join(tmp_dir, "calyx-5.png"), rect)
    page.close()


def run_horai(browser, tmp_dir):
    # ---------------------------------------------------------------- H1
    # Fas 1b fix: hela ordet HORAI (fast klippbredd 600px i fas 1 var
    # smalare an ordet sjalvt, ~968px - darav det avhuggna "H"). Nu matt
    # dynamiskt mot elementets egen bredd, med luft in i det morka fotot.
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page.set_default_timeout(15000)
    page.goto(f"{BASE}/sites/horai.html", wait_until="load")
    page.evaluate("() => document.fonts.ready")
    page.wait_for_timeout(300)
    hero = get_bbox(page, "document.querySelector('#hero-title')")
    rect = crop_for_elements([hero], 36, ASPECT)
    shoot_rect(page, os.path.join(tmp_dir, "horai-1.png"), rect)
    page.close()

    # ---------------------------------------------------------------- H2
    # Fas 1b fix: briefens eget reservlage - kanji+rubrik HELA, INGET av
    # brodtexten (som i fas 1 klipptes mitt i ett ord eftersom den fasta
    # 600px-bredden racker in i lede-kolumnen till hoger). Bara
    # stampkolumnen den hor ihop med.
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page.set_default_timeout(15000)
    page.goto(f"{BASE}/sites/horai.html", wait_until="load")
    page.evaluate("() => document.fonts.ready")
    page.wait_for_timeout(300)
    wait_reveal(page, "Array.from(document.querySelectorAll('h2')).find(h => h.textContent.includes('HOUSE'))?.parentElement")
    info = page.evaluate("""() => {
        const h2 = Array.from(document.querySelectorAll('h2')).find(h => h.textContent.includes('HOUSE'));
        const col = h2.parentElement;
        const lede = document.getElementById('house-lede');
        const r = col.getBoundingClientRect();
        const lr = lede.getBoundingClientRect();
        return {col: {x:r.x,y:r.y,w:r.width,h:r.height}, ledeX: lr.x};
    }""")
    # leaden 2026-09-27, tredje passet: kolumnen (smal, hog) tvingar via
    # aspekten en bredd som INTE ryms fore lede-kolumnen oavsett var
    # rektangeln star - att bara skjuta den at vanster hjalper inte nar
    # bredden i sig ar for stor. Fast bredd = det sakra utrymmet (fran
    # sidkanten till strax fore lede), fast hojd = kolumnens egen utstrackning
    # + marginal (rors aldrig) - fit_to_target() strackar (aldrig skar) till
    # slutaspekten, sa kolumnen star hel aven om den blir nagot bredare i
    # cellen an i kallan.
    col, ledeX = info["col"], info["ledeX"]
    safe_right = ledeX - 20
    x0 = max(0, col["x"] - PAD_DEFAULT)
    rect = {"x": x0, "y": col["y"] - PAD_DEFAULT, "w": safe_right - x0, "h": col["h"] + 2 * PAD_DEFAULT}
    shoot_rect(page, os.path.join(tmp_dir, "horai-2.png"), rect)
    page.close()

    # ---------------------------------------------------------------- H3
    # Fas 1b fix: meningen centrerad med luft (ingen fast bredd som kan
    # hamna asymmetriskt) - bredd matt mot textens egen box, generos
    # marginal, symmetriskt vaxande at bada hall.
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page.set_default_timeout(15000)
    page.goto(f"{BASE}/sites/horai.html?preview=quote", wait_until="load")
    page.evaluate("() => document.fonts.ready")
    page.wait_for_timeout(2200)
    # leaden 2026-09-27, tredje passet: bade 700ms och 700+300ms missade
    # meningens FORSTA rad - `?preview=quote` andrar `transform:scale()` via
    # en 200ms setTimeout, och att bara mata om #quote-text sjalvt racker
    # inte om just den elementets rapporterade box andras nagra ms efter
    # matningen. Mater i stallet mot kickern (ovanfor) och byline (nedanfor)
    # - bada enklare opacitet-overgangar utan transform, klara langt fore
    # 2200ms - och later crop_for_elements VAXA fran DERAS union, som
    # garanterat omsluter meningen mellan dem oavsett dess egen exakta box.
    info = page.evaluate("""() => {
        const rect = el => { const r = el.getBoundingClientRect(); return {x:r.x,y:r.y,w:r.width,h:r.height}; };
        return {kicker: rect(document.querySelector('#quote-kicker')), author: rect(document.querySelector('#quote-author')), quote: rect(document.querySelector('#quote-text'))};
    }""")
    rect = crop_for_elements([info["kicker"], info["author"], info["quote"]], 50, ASPECT)
    shoot_rect(page, os.path.join(tmp_dir, "horai-3.png"), rect)
    page.close()

    # ---------------------------------------------------------------- H4
    # Fas 1b: samma ram som fungerade visuellt i fas 1 (numeral+namn+pris
    # top-ankrat, vaxer nedat) - felet var enbart ASPECT-konstanten (se
    # moduldokstrangen), inte kompositionen. Klipp av vid menyartikelns
    # egen radgrans om vaxten skulle na in i nasta rad.
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page.set_default_timeout(15000)
    page.goto(f"{BASE}/sites/horai.html", wait_until="load")
    page.evaluate("() => document.fonts.ready")
    page.wait_for_timeout(300)
    wait_reveal(page, "Array.from(document.querySelectorAll('article')).find(a => a.textContent.includes('SANSAI'))")
    articles = page.evaluate("""() => {
        return Array.from(document.querySelectorAll('article')).map(a => {
            const r = a.getBoundingClientRect();
            return {x:r.x,y:r.y,w:r.width,h:r.height};
        });
    }""")
    top_row = page.evaluate("""() => {
        const a = Array.from(document.querySelectorAll('article')).find(x => x.textContent.includes('SANSAI'));
        const numeral = a.children[0];
        const priceCol = a.children[2];
        const nr = numeral.getBoundingClientRect();
        const pr = priceCol.getBoundingClientRect();
        const x = nr.x;
        const w = (pr.x + pr.width) - nr.x;
        return {x, y: nr.y, w, h: nr.height};
    }""")
    # leaden 2026-09-27, andra passet: samma bugg som C4 - klampningen
    # andrade hojden EFTER att crop_anchored redan traffat ASPECT, vilket
    # fick fit_to_target skara sidorna (numeralen, priset). Utan klampning
    # rymdes bade meny 1 OCH meny 2 helt i den aspekt-korrekta hojden i den
    # tidigare fristaende matningen - ingen klampning behovs.
    rect = crop_anchored([top_row], PAD_DEFAULT, ASPECT, anchor="top")
    shoot_rect(page, os.path.join(tmp_dir, "horai-4.png"), rect)
    page.close()

    # ---------------------------------------------------------------- H5
    # Fas 1b fix: "THE ROOM" klipptes ("HE ROOM") eftersom fas 1s fasta
    # 600px-klipp centrerades pa fel punkt och inte tackte rubrikens egen
    # vansterkant. Nu: rubriken + inledande brodtextrader som mast-inkludera
    # element, symmetriskt vaxande, sa bada star hela.
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page.set_default_timeout(15000)
    page.goto(f"{BASE}/sites/horai.html", wait_until="load")
    page.evaluate("() => document.fonts.ready")
    page.wait_for_timeout(300)
    wait_reveal(page, "Array.from(document.querySelectorAll('h2')).find(h => h.textContent.includes('ROOM'))")
    els = page.evaluate("""() => {
        const h2 = Array.from(document.querySelectorAll('h2')).find(h => h.textContent.includes('ROOM'));
        const col = h2.parentElement; // the text column (jp glyph, h2, two <p>s)
        const ps = col.querySelectorAll('p');
        const firstP = ps[1]; // ps[0] is the jp glyph "部屋", ps[1] the real descriptive paragraph
        const secondP = ps[2]; // the italic closing line - must NOT be partially shown
        const rect = el => { const r = el.getBoundingClientRect(); return {x:r.x,y:r.y,w:r.width,h:r.height}; };
        return {h2: rect(h2), p: rect(firstP), secondPTop: secondP ? rect(secondP).y : null};
    }""")
    rect = crop_for_elements([els["h2"], els["p"]], PAD_DEFAULT, ASPECT)
    # leaden 2026-09-27, andra passet: vaxten nedat racker in i den andra
    # (kursiva) paragrafen och klipper dess sista rad ("...at half past
    # six."). Klamp botten till strax fore den paragrafens egen topp -
    # bredden ror vi aldrig (se C5-kommentaren om varfor).
    if els["secondPTop"] is not None:
        max_bottom = els["secondPTop"] - 16
        if rect["y"] + rect["h"] > max_bottom:
            rect["h"] = max_bottom - rect["y"]
    shoot_rect(page, os.path.join(tmp_dir, "horai-5.png"), rect)
    page.close()

    # ---------------------------------------------------------------- H6
    # Bra i fas 1 - oforandrad komposition, bara den nu korrekta ASPECT-
    # konstanten (var redan ratt av en slump i fas 1 eftersom "TO BOOK"-
    # blocket satt lagom centrerat, men matt konsekvent med samma metod
    # som ovrigt denna runda).
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page.set_default_timeout(15000)
    page.goto(f"{BASE}/sites/horai.html", wait_until="load")
    page.evaluate("() => document.fonts.ready")
    page.wait_for_timeout(300)
    wait_reveal(page, "Array.from(document.querySelectorAll('p')).find(p => p.textContent.trim() === 'TO BOOK').parentElement")
    wrap = page.evaluate("""() => {
        const label = Array.from(document.querySelectorAll('p')).find(p => p.textContent.trim() === 'TO BOOK');
        const r = label.parentElement.getBoundingClientRect();
        return {x:r.x,y:r.y,w:r.width,h:r.height};
    }""")
    rect = crop_for_elements([wrap], PAD_DEFAULT, ASPECT)
    shoot_rect(page, os.path.join(tmp_dir, "horai-6.png"), rect)
    page.close()


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp_dir = os.path.join(HERE, ".make_steps_tmp")
    os.makedirs(tmp_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            run_calyx(browser, tmp_dir)
            run_horai(browser, tmp_dir)
        finally:
            browser.close()

    for n in range(1, 6):
        save_color_and_dither(os.path.join(tmp_dir, f"calyx-{n}.png"), "calyx", n, BLACK, GREY)
    for n in range(1, 7):
        save_color_and_dither(os.path.join(tmp_dir, f"horai-{n}.png"), "horai", n, WHITE, BLACK)

    print("done ->", OUT_DIR)


if __name__ == "__main__":
    main()
