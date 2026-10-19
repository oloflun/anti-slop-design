# 020 · Arkets geometri och utrop: 7 rem sant, arket klipps aldrig, A-glyfen syns, siffrorna byter ton, ett blått moment per skärm

- **Status**: TODO (R6, tillsammans med 019; samma fil, samma element)
- **Commit**: R5-läget av `runs/V3c/index.html`, md5 `fcbee8f1` (radnummer före 019:s omskrivning; byggaren gör 019 först och söker sedan på id, inte på rad)
- **Severity**: HIGH (H-33: ett falskt mått; H-35: arket klipps 900 till 1 340 px)
- **Category**: Cohesion (sanna mått) + Physicality (A-glyf) + Responsive (klippning)
- **Estimated scope**: 1 fil, ~15 rader CSS, 6 attributvärden, 1 ny `<path>`
- **Källor**: Astra 1, 4b, 5, 6, 7; design-critic 3, 6; heuristik 1 (klippning), 8 (tonbyte); design-perf 4 (fönsterbredd, delvis via 019); lead F-007 s-process-02/04/06

## Problem

1. **`7 rem` är falskt.** `#p-dim-gutter` spänner x 226 till 270 = 44 units; arkets skala
   är 880 units = 1 440 px, alltså 72 px = **4,5 rem**. H-33 tål inte ett falskt tal.
   Felet kommer ur plan 010 § Målbild s-process-03 (rättelse skriven där, fotnot).
2. **Arket klipps** mellan 900 och ~1 340 px bredd: `.process-sheet{width:880px;flex:none}`
   i ett bo som minst kräver 1 430 px; högerkanten mätt vid 1 204 (900), 1 325 (1024),
   1 335 (1180), 1 341 (1280); `1440`-siffran och `16:9`-ledaren försvinner, ingen
   scrollbar. `top:202px` och `height:495px` är 1440x900 som konstanter.
3. **A-glyfen syns inte** (`#p-mark`): `fill="#ffffff"` som presentationsattribut på den
   refererade pathen slår `fill:none`, och den ärvda 0,75 px-stroken skalas av
   `scale(0.031607)` till ~0,024 px.
4. **Utropen tänds ett fönster för sent** (siffrorna 0,35 mot stegfönster som slutar 0,37;
   `96 px` vid 0,55 = noll samexistens med steg 04) och **siffrorna byter aldrig till
   `--hair-ink`** i 06; de står blå i `proc-1440-06` och `-07`. Skärm 05 har därmed två
   auktoriteter (Calyx och den blå kedjan), TASTE § 4.8.
5. `.process-sheet .guide,.process-sheet .hatch{opacity:…}` (rad 783) träffar `#p-rev`
   (klass `hatch`), så revisionsfältet i 07 är permanent nedtonat till 0,35.

```html
<!-- index.html:1193-1198 - current -->
        <path id="p-opening" class="contour draw" pathLength="1"
              d="M 270 96 H 808 V 399 H 270 Z"/>
        <path id="p-dim-gutter" class="dimline draw" pathLength="1" d="M226 80 H270"
              marker-start="url(#p-arrow)" marker-end="url(#p-arrow)"/>
        <text id="p-c-gutter" class="callout" x="248" y="72" text-anchor="middle">7 rem</text>
<!-- index.html:1176-1177 - current -->
        <use id="p-mark" href="#alunix-mark-path"
             transform="translate(24,24) scale(0.031607) translate(-80,-400)"/>
```

```css
/* index.html:753-760 - current */
  .process-sheet .measure{font-family:var(--f-display);font-weight:700;
    font-size:44px;fill:var(--c-accent);font-variant-numeric:tabular-nums;
/* index.html:783 - current */
  .process-sheet .guide,.process-sheet .hatch{opacity:calc(1 - 0.65 * clamp(0,calc((var(--sc-ps,0) - 0.64) / 0.06),1));}
```

## Target

**A. Sant spaltmått.** Öppningen flyttas så att avståndet från 320-stationens hjälplinje
(x 195,6) till öppningens vänsterkant är 68,4 units = 111,9 px ≈ 7 rem (16 px rot).
Öppningen behåller 538x303 (16:9).

```html
<!-- target -->
        <rect id="p-open-rect" x="264" y="96" width="538" height="303"/>          <!-- i <clipPath> -->
        <image id="p-live-img" href="assets/demo-calyx-1440.webp" x="264" y="96" width="538" height="303" …/>
        <path id="p-opening" class="contour draw" pathLength="1" d="M 264 96 H 802 V 399 H 264 Z"/>
        <path id="p-dim-gutter" class="dimline draw" pathLength="1" d="M195.6 80 H264" …/>
        <text id="p-c-gutter" class="callout" x="229.8" y="72" text-anchor="middle">7 rem</text>
        <circle id="p-dot-169" class="leaddot" cx="802" cy="96" r="1"/>
        <path id="p-lead-169" class="leader draw" pathLength="1" d="M802 96 L829 110 H852"/>
        <text id="p-c-169" class="callout" x="852" y="104" text-anchor="end">16:9</text>
```

Kontroll: (264 − 195,6) · 1440/880 = 111,9 px; `16:9` = 538/303 = 1,7756 (16/9 = 1,7778,
inom en unit); `96 px` oförändrat (58,7 units · 1,636 = 96,06 px).

**B. Arket klipps aldrig.** Med 019:s grid (`minmax(0,880px)`, `width:100%; height:auto;
aspect-ratio:880/495`) skalar arket ned mellan 1 280 och 1 439 px (minst 760 px brett,
skala 0,86, hårlinje 0,65 px, utrop 10,4 px); under 1 280 gäller planschen 320x360. Mål:
arkets högerkant ≤ viewportbredd − `--rail-x` vid 1024, 1180, 1280, 1366, 1440.
`top` räknas ur `svh` (019: `max(24px, calc((100svh - 495px) / 2))`) så arket ligger
innanför vikningen vid 1366x640 (a11y fix 8: 24 + 495 = 519 < 640).

**C. A-glyfen som egen bana.** `<use>` ersätts av en egen `<path id="p-glyph" class="draw"
pathLength="1" transform="translate(24,24) scale(0.031607) translate(-80,-400)" d="…">`
med `d` kopierad ordagrant från rad 931 (`#alunix-mark-path`), och:

```css
  .process-sheet #p-glyph{fill:none;stroke:var(--hair-ink);stroke-width:23.7;
    stroke-linejoin:miter;}
```

23,7 units i pathens eget rum · 0,031607 = 0,75 px på skärmen (`--contour-hair`). Dash-
draw fungerar på en `<path>` (pathLength stöds), så glyfen ritas som konturen, i steg 01
efter `#p-outline` (andel `[0.5,1]` av `--k1`). Ingen opacitetston.

**D. Utropen i sitt eget steg, siffrorna byter ton.** Med 019:s ankring: siffrorna `--p-t`
från `--k2` andel 0,75 (tänds medan 02 står i mitten); `7 rem` från `--k3` andel 0,55,
`16:9` från `--k3` 0,85 (med `#p-dot-169`); `96 px` från `--k4` 0,8; `A` från `--k7` 0,85.
Tonbytet:

```css
  .process-sheet .measure{…;
    fill:color-mix(in srgb, var(--c-accent), var(--hair-ink) calc(100% * var(--k6)));
    transform:scale(calc(1 - 0.7273 * var(--k6)));}
```

Vid `--k6` = 1 (steg 06 i mitten) är kedjan 12 px och `--hair-ink`; vid steg 07 finns inget
blått i arket (H-33: ett blått moment per skärm, inte ett kvarglömt). Skärm 05: siffrorna är
fortfarande accent men Calyx är skärmens auktoritet; critic 05-driften löses av att `--k5`:s
fyllning når 1 medan siffrorna redan har haft sin skärm (02 till 04); `.measure` får
dessutom `opacity` 1 → 0,7 över `--k5` så att kedjan viker när bilden landar (TASTE § 4.8),
utan att försvinna.

**E. Selektorn snävas.** Rad 783 → `#p-guides,#p-ledgers,#p-hatch{opacity:calc(1 - 0.65 *
var(--k6));}`. `#p-rev` (revisionsfältets skraffering) berörs inte och står i full ton i 07.

## Repo conventions to follow

- Måttsiffrornas `transform-box:fill-box` och origin (rad 758-760) står.
- `color-mix` finns redan på sidan (`--hair-ink`, ordscrubben rad ~660).
- Markörernas snäpp-opacitet (rad 740-747) gäller även `#p-glyph` via `.draw`.
- Ledgerrad i `BRIEF.md`: "spaltmåttet rättat till 7 rem genom att öppningen flyttas
  6 units; källa Astra fynd 5, plan 010 § Rättelse".

## Steps

1. Efter 019: byt de sju attributvärdena i Target A (clipPath-rect, image, `#p-opening`,
   `#p-dim-gutter`, `#p-c-gutter`, `#p-dot-169`, `#p-lead-169`, `#p-c-169`).
2. Ersätt `<use id="p-mark">` med `<path id="p-glyph">` enligt Target C; ta bort
   `.process-sheet #p-mark{…}` (rad 794-796) och lägg `#p-glyph`-regeln.
3. Skriv om `.measure` (rad 753-760) och rad 783 enligt Target D/E; utropens `--p-t`
   enligt Target D:s andelar.
4. Mät arkets högerkant vid 1024, 1180, 1280, 1366 och 1440 (`document.querySelector(
   '.process-sheet').getBoundingClientRect().right`) och skriv talen i NOTES.md.
5. Mät `7 rem`: `(264 - 195.6) * sheetWidthPx / 880` vid 1440 = 111,9 px.

## Boundaries

- `96 px`-måttet, liggarraderna och skrafferingens geometri rörs inte.
- Inga nya utrop, ingen text i SVG utöver de sex sanna måtten och `A`.
- Matchar inte id:na `p-opening`, `p-dim-gutter`, `p-c-gutter`, `p-mark`, `p-dot-169`,
  `p-lead-169`, `p-c-169`, `p-open-rect`, `p-live-img` eller `alunix-mark-path` (rad 931):
  STOPPA.

## Verification

- **Mekaniskt:** de fem högerkantsmätningarna ≤ viewport − 86 (1440) respektive − rail;
  `motion_probe --track "#p-glyph:stroke-dashoffset"` inte DEAD; `a11y_scan.py` 0;
  `reflow.py` vid 1024 och 1280 utan overflow (lägg till dessa bredder i körningen).
- **Skärmbilder:** `?preview=process-01` visar konturen **och** A-glyfen (0,75 px kontur
  uppe till vänster); `process-02` visar 320 · 768 · 1440 i accent; `process-03` visar
  `7 rem` mellan hjälplinjen vid 195,6 och öppningens kant; `process-04` visar `96 px`;
  `process-06` visar siffrorna 12 px i `--hair-ink`; `process-07` visar `A` i full ton;
  en bild vid 1280x800 och en vid 1366x640 med hela arket i bild.
- **Feel check:** i steg 01 ritas konturen och sedan glyfen som två drag av samma penna;
  när Calyx fylls (05) viker siffrorna; efter 06 finns inget blått i arket.
- **Done when:** H-33 (sanna mått, ett blått moment per skärm) och H-35 (arket helt vid
  1024/1280/1366) bockade; plan 010 § Rättelse hänvisar hit.
