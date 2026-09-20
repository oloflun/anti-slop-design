fix

## persistence
Codex ran once (`gpt-6-astra`, reasoning medium, read-only, 24 attached images: P01 to P14 at 1440, `lead-r1/pris-1.png`, `P15-ref-1440.png`, `lead-r1/s--s12.png`, `s--s13.png`, and P01/P04/P07/P12/P13/P15 at 390; about 197k tokens, under ten minutes). It returned 16 parity lines and 9 findings. I checked every finding against the file and against a PNG, including my own Playwright captures (`?preview=process-05/06/07` at 1440, `process-01/02/04` at 390, wheel scroll from the top of the page through the stagger band and steps 05 to 07, `scrollTo(11700)` plus `elementsFromPoint`).

- **Survived: 8 of 9.** Several are merged below, so the list has 8 material_fixes.
- **Dropped: 1.** P05-390 said Hōrai's subtitle is clipped at the right edge. I could see it in `P05-390.png`, but I did not measure whether it comes from our host frame or from the site's own mobile layout, so I did not pass it on.
- **Lead finding (a), confirmed in all four parts:**
  - The loose "--" is the diacritics of Ö in the incoming "FÖRVALTNING". `elementsFromPoint(407,211)` at scrollY 11700 returns `H3.process-step-title` in band 07. Band 06 has its bottom at 184 px, band 07 sits at 184 to 400 px under the sheet, and `.process-stick` starts at 216 px. That leaves a 32 px slit where only the top of the glyphs shows.
  - The 768 guide crosses Calyx.
  - "16:9", "96 PX", "7 REM" and "1440" are cut at the sheet's edge.
- **Lead finding (b), confirmed and measured.** The milky film is the winning filter `brightness(0.6)` at index.html:1159 working on a paper-toned image. Asset against render in the opening, 1068x598 px:
  - p95 luminance 238 against 146, and maximum 255 against 153.
  - Mean chroma 21.0 against 13.2.
  - The Calyx paper header goes from (243,240,232) to (149,147,142).
  - The Calyx hero also carries a pale gradient at the bottom (visible in `assets/demo-calyx-1440-color.webp`), and the filter turns it grey.
- **s04 (empty frames after `scrollTo`) not reproduced with `mouse.wheel`.** At 100 px per 60 ms, Calyx is fully rendered at scrollY 3600. The dark Hōrai box there is the state before its reveal, which opens as an iris at 4200. I dismiss s04 as a `scrollTo` artefact.

## fidelity
The order point by point:
- **A to D achieved.** Price on the desk photo, address 46.1/28 px, process on `--c-drafting`, giant on black plate.
- **E achieved at 1440.** Measured at `?preview=process-06`: sheet 1168x657 (81 % vw), Calyx 1071x603, 84 % of the sheet. At 390 the sheet is 343 px (88 %, target 92 %).
- **F not achieved.** 07 draws nothing visible at 1440, 04 draws nothing at 390, 06 and 07 are the same image, and at 390 the process is still a paragraph under a small sheet.
- **G and H not achieved.** Rows below.

- **P01 fold: does not hold.** 1440 holds (headline ~120 px, card 62 % vw). At 390 the headline is ~35 px against the reference's ~80 px display word, with ~150 px of empty photo between nav and headline (P01-390). Gap: `.hero-headline` (index.html:357) at least 46 px at 390, and the stage raised.
- **P02 card back: does not hold.** "ALUNIX" on the plate is ~60 px (1440) and ~40 px (390) inside a card that sits under the unchanged headline. The reference's one word owns the middle at ~160 px. Gap: the display word on the back at ≥ 100 px at 1440, and the outer headline yields as the back arrives (`--sc-ps`).
- **P03 thesis band: does not hold.** Hyperborea is ~20 % vw (P03-1440, 315 to 517 of 992) against the reference's ~44 %, the blue headline is ~48 px against ~80 px, and the black giant weighs more than the thesis beside it. Gap: `.panel-thesis` (607) gets an interval of its own with the image ≥ 40 % vw.
- **P04 giant, inverted: does not hold.** The inversion is right, but "VI BYGGER ERT VARUMÄRKE." at ~88 px shares the viewport with the blue panel and the Calyx frame (P04-1440, the whole left half). The reference owns an empty field. Gap: `.panel-giant` (790) / `#giant-section` (829) gets a viewport interval where the black plate is alone. The heading size stays.
- **P05 Hōrai band: holds at 1440.** Two works side by side. 390 was not judged (the finding was dropped, see persistence), so the row stays open.
- **P06 chapter screen: does not hold.** "Från samtal till lanserad sida." at 104 px holds the size, but the band for 01 (168 px number, title, paragraph) takes the lower third of the same screen (P06-1440, y 470 to 600). The same happens at 390 plus a sliver of the sheet. Gap: `.process-lead` margin-bottom (910) ≥ 1 viewport minus the title, so the chapter is presented alone.
- **P07 step 01: does not hold.** 1440 holds: an empty sheet at 81 % vw, one scene. At 390 the sheet covers the step's paragraph. Measured at `?preview=process-01`: stick 548 to 894 px over the paragraph at 506 to 724 px (material_fixes 2).
- **P08 step 02: does not hold.** 1440 holds: the 320/768/1440 chain in 44 px accent reads at a distance. At 390 a fragment of step 01 sits above the sheet, because the stick only sticks after its 202 px margin (stick at 49 px at `process-02`).
- **P09 step 03: holds level** at both widths. One chapter per screen, the 16:9 opening and 7 REM readable.
- **P10 step 04: does not hold.** At 1440 the change from 03 is a 54-unit hatch in the margin. At 390 the drawing is identical to 03 (index.html:1189 hides `#p-hatch,#p-ledgers,#p-dim-row,#p-c-row`, all of step 04's additions). The band changes, the scene does not.
- **P11 step 05: does not hold.**
  - Calyx is ~52 % of the sheet (meets the plan).
  - "96 PX" is cut to "6 PX" at the left edge, "16:9" at the right edge, and "1440" against the right edge (P11-1440; `wheel` capture as well).
  - The image is grey at `brightness(0.6)`, so the arrival of the material has no impact.
- **P12 step 06: does not hold.** The size passes at 1440 (84 %, 1071x603). Still:
  - The image carries the milky film (fixes 3).
  - The 768 guide cuts through it (fixes 4).
  - The 16:9 leader hangs out at the top right.
  - It reads as a greyed image on a sheet, not as the reference's image that owns the screen.
  - At 390 Calyx is ~56 % of the sheet, with air left round it.
- **P13 step 07: does not hold.** At 1440 it is pixel-identical to 06 apart from the band text. 07's only drawing (the revision field) sits at x −296, y 935 (`getBoundingClientRect` at `?preview=process-07`), outside the sheet at 134 to 1306 / 223 to 882. The band's note "Revisionsfältet fylls" points at something that is not visible.
- **P14 How we think: does not hold.** The two columns hold. The body is 17 px (1133) against the table's ~20 px, and at 390 "Hur vi tänker" falls to an 11 px kicker (P14-390).
- **P15 price + contact: holds level.** Statement in display scale, prices in display figures, address 46.1 px as the subordinate action, everything on the same photo (`pris-1.png`, P15-390).
- **P16 whole page: does not hold.** Seven process screens on the same drafting ground. 06, 07 and the coda (`.process-steps::after`, 929) show the same unchanged image three times in a row, and 01 to 04 add little mass.

## ceiling
- **Engine and shim:** n/a. The process moves read `--kN`/`--cam` out of `--sc-ps`, and nothing uses raw `--sc-p`. F-011 respected.
- **References:** hoy gives every chapter a whole viewport with one dominant element (hoy-home s03, hoy-webb s01). Our band plus sheet reaches that at 1440 for 01 to 03. It is broken by the camera's overflow (05 to 07), by the identical 06/07, and on mobile by the overlap.

## material_fixes
1. **Step 07 draws nothing at 1440.** `g[data-step="07"]` (index.html:1630 to 1635) sits inside `#p-cam`. At `--cam` 1 the transform (1103 to 1104) gives x′ = 1.5x − 359.5, so the revision field at 24..84 / 439..493 lands at −323..−233 / 535..616, outside the viewBox. Move the group out of `#p-cam` (after `</g><!-- /#p-cam -->`), or give it coordinates that land in the sheet at `--cam` 1. Expected: at `?preview=process-07`, `#p-title`'s rect lies inside `.process-sheet`'s rect, and 07 is visibly different from 06.
2. **Mobile: the sheet covers the step text.** Cause: `.process-stick` keeps the desktop rule's `margin-top:var(--band-h)` (922, computed 202.56 px at 390), and both it and `.process-steps` stay in `grid-area:1/1`. The mobile block (1177 to 1180) resets neither. Target: in `@media (max-width:767px)`, `.process-stick{margin-top:0;grid-area:auto}` and `.process-steps{grid-area:auto}` (separate rows), then measure `--sheet-h`/anchors again. Expected: at `?preview=process-01..07`, 390, the stick has top 0 and never overlaps `.process-p` (today 548 over 506..724).
3. **The milky film on Calyx in 05 to 07.** `.process-sheet .p-live{filter:… brightness(0.6)}` (1158 to 1159) caps every white at 153/255 and grey-shades the paper header and the pale bottom gradient. Target: `brightness(calc(0.6 + 0.4 * var(--k6)))`, so the dimming only belongs to the drawing phase (05). Measured the same way as in persistence, at `process-06`: p95 luminance ≥ 220 and the paper header ≥ (225,222,214). The lamp risk (P12) is met by the image's size of 84 % of the sheet, not by the dimming.
4. **The camera leaves cut annotations and a guide over the product.** From `--k5` onwards, `#p-c-row`, `#p-dim-row`, `#p-lead-169`, `#p-c-169`, `#p-c-gutter`, `#p-dim-gutter`, `.measure` and `#p-dim-width` get the opacity `calc(1 - clamp(0, var(--cam) * 4, 1))` (gone before `--cam` 0.25). Alternatively they can sit in an unscaled layer outside `#p-cam`. `#p-guides` (1034) gets `opacity:calc((1 - var(--k5)) * (1 - 0.65 * var(--k6)))`, because it paints after the image (1589 after 1559). Expected: at `process-05/06/07` and in wheel captures between them, no label or leader is cut by the sheet's edge, and no dashed line crosses Calyx.
5. **The ticker slit shows glyph fragments ("--").** At scrollY 11700 (1440), band 06 has its bottom at 184, band 07's `.process-step-title` lies at 184+ and `.process-stick` starts at 216. The 32 px slit between them shows only the Ö's diacritics. Target: the rising band shows no ink until it has cleared the sheet's top edge. For example, `.step-band` on `li:not(:first-child)` gets `clip-path:inset(max(0px, calc(var(--band-h) - …)) 0 0)`. An equivalent is to let the stick start at 0 with `padding-top:var(--band-h)` under an opaque band N. Expected: no frame between two bands shows a partial glyph from the next band.
6. **The chapter screen and the stagger band do not own their viewports (P03, P04, P06).** P06: `.process-lead` margin-bottom (910) at least `calc(100svh - <the title block's height>)`, so "Från samtal till lanserad sida." stands alone before band 01 enters. P04: `.panel-giant` gets an interval in `.stagger` where the black plate fills ≥ 80 % of the viewport width without the blue panel or a frame visible beside it. P03: the Hyperborea image ≥ 40 % vw in the thesis interval.
7. **Steps 04, 06 and 07 are not separate scenes.** At 390, 1189 hides all of 04's drawing. Show `#p-hatch`/`#p-dim-row`/`#p-c-row` in mobile coordinates (the viewBox is 320x300), so that 04 visibly changes the sheet. At 1440, with fix 1 in place, 07 needs a visible event (the revision field in the sheet's lower left corner, in the unscaled frame). The coda `.process-steps::after` (929) either goes, or holds a scene that differs from 07.
8. **Mobile and body-text scale (P01, P14, E at 390).** `.hero-headline` ≥ 46 px at 390 (357). `.principles .ledger--plain .ledger-body p` 20 px at ≥ 900 (1133), and `.principles > .kicker-sans` ≥ 32 px at 390. The mobile sheet gets a 16 px inset of its own instead of `--rail-x` (1179): 358 px = 92 % vw, the plan's E target.

## keep
- The price and address as one closing on the same desk photo, with the address at 46.1/28 px under an 86 px statement (P15 holds).
- The black giant plate with `--frame-line`, and the drafting ground `--c-drafting`: three dark materials, not one.
- The desktop sheet at 81 % vw and Calyx at 84 % of the sheet, 1071x603 at `process-06`. The size is right and must not be scaled back when fixes 3 and 4 are made.
- Band plus sticky sheet as the scene form at ≥ 768 (P07 to P09 at 1440 hold), with number and title lit via `--k` (without opacity on the text).
- Calyx sticky beside Hōrai in the stagger band: two live sites side by side, no hole where the price used to be.
- All motion reads `--sc-ps` via `--kN`/`--cam`. The engine, the shim and the `@property` registration are untouched. F-011 respected.
