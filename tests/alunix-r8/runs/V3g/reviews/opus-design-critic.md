fix

## persistence

**Partial pass.** Read this run: `house-physics.md`, `production-tells.md`, `gates.md`, `design/SKILL.md` (craft floor), `motion.md` (Durations, Scroll-linked, Choreography, Never Ship, Bans), `scroll/devices.md` § The engine, `design-catalogue/FEEDBACK.md` F-001..F-022, `TASTE.md`, `runs/V3g/EFFECTS.md`, `BYGGSPEC.md` (the V3f/V3g target: cell map § 3), `SHOWCASE-SPEC.md`, `RORELSE-SPEC.md`, `V3f/KEDJA.md` (how the lock was formed), and the whole of `index.html` (2074 lines).

Pixels captured fresh this run, headless and under `browser_lock.py`, against the current `index.html` (Sep 27 19:11). All were read:
- `shots/critic-opus/1440-001…024` (0.75-viewport steps through all 16 348 px);
- `shots/critic-opus/sheet390-0..2.png` (11 mobile slices at 390×844);
- `probe-tes-pinned-1440.png`;
- `lead-box-r6b/box-horai-40.png` (reused).

Measured with a DOM probe: pin offsets, iframe crop fraction, type sizes, link wrap and `will-change` count. `lead-r3-1440/` was **not** used. It predates R4–R6b and is stale.

**Fail on one input.** The lane lock is `aspensearch-com` (primary), with `cyphr-studio`, `exoape-com` and `area17-com` as motion loans (`V3f/KEDJA.md` L3–L9, `RORELSE-SPEC.md` 8–14). Those pages exist only as Inspo `get_screen` reads the V3f lead made. No `fold.webp` or capture is on disk, and I have no Inspo tool in this session. I could not open them. The ceiling lines below therefore judge the build against the lock's *written* principles only. A `ship` cannot be issued until `aspensearch-com` is captured at 1440 and read. There is no `BRIEF.md` for V3g; `BYGGSPEC.md` + `SHOWCASE-SPEC.md` stand in as brief and target.

Lane sentence (BYGGSPEC l.3–7): *"hela sidan är ETT kontinuerligt, hårt rutnät av celler i full bredd (0 gap, 1 px svarta skarvar, radie 0) … rutverket monterar sig självt"*. Motion principle (RORELSE-SPEC l.8): *"Allt rör sig i sin cell eller längs sin skarv, aldrig fritt över sidan."*

## fidelity

Screen by screen against BYGGSPEC § 3 + SHOWCASE-SPEC, 1440 unless noted.

| # | Screen | Holds | Drift | Class |
|---|---|---|---|---|
| 1 | Topline | Black logo cell, white ALUNIX cell, black mail cell, sticky | none | |
| 2 | Hero 2×2 (`1440-001..004`) | Quadrants, diagonal load, card on the ÖH/NH seam, flip scrubbed over +=220% | **48 px black band at 852–900 for the whole pin.** Pin start "top top" (l.1148) pins the calc(100svh-48px) stage under the topline; measured stageBottom 852 of 900. Same bug R7 fixed for the showcase (l.1733) | defect |
| 2b | Hero exit (`1440-004`) | h1 moves only in the last 25 % (reading rule met) | Lines exit at different yPercent (-16/-28/-40, l.1164) and collide inside their masks. The still frame shows "nutidens" and "visitkort" sliced into each other | defect (low) |
| 3 | Tes (`1440-005..008`) | Black full-width cell, 180 px white headline; lower grid 4+8 (spec 6+6, intentional); Hyperborea resolves dither → colour | **Pinned headline sits under the opaque topline.** Pin start "top top" (l.1194) puts h2 top at y=40 under a 48 px bar. Cap tops of D/f/t and the **ö diaeresis** are hidden for the whole 0.9 vh pin (`probe-tes-pinned-1440.png`). motion.md: "never the baseline" and only glyph parts "that do not carry the reading"; the diaeresis carries the reading. Protected effect in EFFECTS.md, and its own signature ("helt synlig") is not met | **defect, blocking** |
| 4 | Process (`1440-008..010`) | Grey sticky left, black right, 7 rows, mint progress on the seam | Spec "1px skarvar mellan": border-top 1px #000 on a #000 cell (l.214–215) is invisible, so the right half is one black plane and the rutverk dissolves there | defect |
| 5 | Exempelcase + picker (`1440-010..011`) | Word in a white cell, two choices | Picker inset by a 20 px black gutter (l.232 padding 0 20px 24px), so cells are no longer edge to edge (lane: 0 gap). Picker meta "Calyx / Florist, Stockholm" and the showcase head repeat each other **on the same screen** (`1440-011`). The picker thumbnail and the iframe's first frame are the same "Botanical architecture" image, stacked | defect |
| 6 | Showcase, Calyx (`1440-012..021`) | Pin created once, counter + mint track, 30 px h3 / 18 px body (F-019 met), crossfade, loupes | **The site is cropped to 61.6 % of its width.** Cover-scale (l.1491) into an 839×852 cell renders 1363 px wide. Every right column is cut: nav, "A bouquet is a conversa…", "Eleven cuttings, this week…", the **prices step 4 talks about** ("pris i högerkant", `1440-018`), "PHOTOGRAPHY:". On Hōrai the centred quote is severed mid-word ("COOKING IS A CONVE…", `lead-box-r6b/box-horai-40.png`). The site is supposed to be the main thing (F-019) | **defect, blocking (signature act)** |
| 6b | Case-colour head | Rust/lacquer fill only in the head (spec) | Text is ink #232323 on rust #9c5a3a = **2.95:1** and on lacquer #b23524 = **2.57:1**. The 13 px caption fails 4.5:1 and the 100 px name fails even 3:1. `.cell--rust/--lacquer` (l.71–72, paper text) exist but are unused; inline bg at l.727/770 | defect |
| 6c | Loupes | Step 4 "2 480 kr SEK", step 5 "atelier@calyx.se", Hōrai 料理は対話 are exactly the brief | Calyx 2 = wordmark over a blurred strip of flowers cut at the cell's bottom edge. Calyx 3 = a soft photo fragment parked in the top-right corner with the cream cell empty. Both break the R6b rule "rent komponerat, utan halva element i kanten". Sequential out-then-in (l.1678–1683) dips through an empty grey cell (`1440-017`) | defect (medium) |
| 7 | Pris (`1440-021..023`) | Tier-bento in cells, F-017 met (text 24 px < digits 44 px) | Spec "högerställda siffror": digits are left/bottom aligned. The 44 px price is lost in a 720×441 mint plane. Cells slide in from three directions by 14–18 % (l.1953–1955), leaving their seams (breaks the RORELSE principle). Lede narrates the page (see material_fixes 3) | defect |
| 8 | Kontakt (`1440-023..024`) | Mirrored quad, card handover, self-flip at 0.7 (protected) | **ÖH is an empty 720×450 white cell** (measured, 0 children, l.857) | defect |
| 9 | Footer | Giant ALUNIX, mail line | "Eller mejla oss…" follows no alternative. kontakt@alunix.se is on screen three times at once (`1440-024`) | defect (low) |
| M | Mobile 390 (`sheet390-*`) | Stack order, card fits, no horizontal overflow | Showcase iframe shows **27 % of the width and 52 % of the height** of a desktop render, mostly empty cream (`sheet390-1` panel 4, `sheet390-2` panel 1). Footer link wraps to 2 lines (measured, gate 49). Hero h1 is 40.7 px = 2.5× body (TASTE § 2.4 asks for ≥5×) | defect |

**Full finding list, ranked:**

| Sev | Finding | Gate / rule | Evidence |
|---|---|---|---|
| HIGH | Showcase site cropped to 61.6 % width (1440) / 27 % (390) | F-019 "sajten är huvudsaken"; F-007 signature act | l.1491; `1440-014,-015,-018,-019`; `box-horai-40` |
| HIGH | Tes headline under the topline for the whole pin, diaeresis hidden | motion.md reading rule; EFFECTS signature "helt synlig" | l.1194; `probe-tes-pinned-1440.png` |
| HIGH | Pris lede narrates the page: "det ni just har sett … varje rad nedan" | F-018, gate 99 | l.830; `1440-022` |
| HIGH | Case-head text 2.95:1 / 2.57:1 | WCAG 1.4.3; house-physics "every muted tone needs a value per ground" | l.727, 770; `1440-012` |
| HIGH | Footer link wraps to two lines at 390 | gate 49 (hard floor) | l.904; measured lines = 2 |
| MED | Hero pin leaves a 48 px black band for ~2 screens | lane (cells meet the edge) | l.1148; `1440-002..004` |
| MED | Kontakt ÖH empty | house-physics "every open column carries weight"; F-022 | l.857; `1440-023` |
| MED | Process rows lose their seams (black on black) | lane "1 px skarvar"; house-physics "hairlines separate" | l.214–215; `1440-009` |
| MED | Picker: 20 px gutter; name/caption shown twice; same image twice | lane 0 gap; gate 99 (repeat identification) | l.232, 694–704 vs 727–729; `1440-011` |
| MED | "Vår process:" kicker + paraphrase line "Webbdesign, design och system. Allt på ett ställe." ("webbdesign, design" also repeats itself) | gate 99, gate 70 | l.625, 627 |
| MED | Loupes Calyx 2 and 3 are fragment crops; the crossfade dips through empty | R6b rule; house-physics "art direction by render" | `1440-015`, `-016`, `-017` |
| MED | Pris price at 44 px in a 441 px mint plane, left-aligned (spec: right) | house-physics § Ledger (display-scale price, right-aligned); BYGGSPEC § 3.8 | l.425, 410; `1440-022` |
| MED | Six reveal profiles (0.55/0.6/0.7/0.75/0.8 s, power2/3/4, stagger .012–.08). Pris slides 60–100 px | house-physics "a page picks one profile … never a third set"; "a rise past 24 px reads as a slide" | l.1126, 1182, 1204, 1213, 1286, 1939, 1950–1955 |
| MED | Reveals re-hide on scroll-up (toggleActions with reverse) | house-physics: re-hiding is a defect | l.1205, 1214, 1287, 1931, 1940, 1951 (l.1183 is the protected tes rise: leave it to Anton) |
| MED | "Boka ett möte" goes to #kontakt, i.e. to itself; the primary action books nothing | gate 99 test "enable an action" | l.882 |
| MED | Mobile hero h1 40.7 px (2.5× body) | TASTE § 2.4 / § 4.6 (≥5×) | l.33, 562; `sheet390-0` |
| LOW | Text-colour tween on process titles/numbers | motion.md Bans (text-colour transitions) | l.1265–1267 |
| LOW | 730 resting will-change (tile spans + picker img) | motion.md Bans; gate 93 | l.239, 508; measured |
| LOW | back.out(1.4) overshoot on the card drop-in | motion.md Bans (overshoot) | l.1127 |
| LOW | body overflow-x: hidden | gate 34 (clip, never hidden) | l.52 |
| LOW | Only 2 stock photos fill 6 image slots (stage-pool ×4, cabin-desk ×2); the NV cabin dither is illegible noise | TASTE § 4.3 | `1440-001`, `-009` |
| LOW | Copy cadence: 7 of 11 step bodies open "Vi + past verb". Process copy is stiff: "samt", "initialt underlag", trailing "mobilen först". Tes line 3 "Vi hjälper er att synas på rätt sätt." is the page's one generic sentence (copy facit, so flag, don't rewrite unasked) | copy-gate | l.639–669, 608, 737–785 |
| LOW | "Asian Fusion" (caption) vs "Asian fusion-koncept" (alt) | consistency | l.703, 772 vs 700 |

## ceiling

- `aspensearch-com`: **could not open.** Inspo-only reference with no capture on disk and no Inspo tool this session. Read against its written principle ("cellen som enhet, allt rör sig i sin cell"), this build **förlorar** where Aspen is strongest: cells stay whole and nothing leaves its seam. Here the pris cells slide 60–100 px out of place, the process column melts into one black plane, the picker floats on a gutter, and a live site is cropped inside its cell. Verdict provisional until captured.
- `cyphr-studio`: **could not open.** Against the written loan (grid resolve between flat and photo): **står sig bredvid**. The dither → colour tile resolve on tes, process and kontakt is real and reversible. The R6b diagonal wave in the loupes is cleaner than a random checkerboard. Cyphr presumably lets the resolve land on a whole image, not on fragment crops.
- `exoape-com` (motion loan): **could not open.** Monumental type cut by the edge was deliberately dropped in R5 for legibility, which is correct. Against the loan: **står sig bredvid** on scale (180 px tes, 200 px Exempelcase). But the pinned tes headline being cut by the *topline* is not the Exoape move. That is a bug.
- `area17-com` (motion loan): **could not open.** "Type moves over a still photo field": **förlorar**. No section on the page holds a still photo field with type moving over it. The closest, kontakt NV, has no type on it.

## material_fixes

1. Showcase iframe shows the whole site width. Desktop: scale = wrap.w/1440 (0.583 at 1440) and iframe height = wrap.h/scale (≈1461 px), so visible width fraction goes 0.616 → **1.00**. Mobile: render the example at its own responsive width (iframe width 390, scale 1), not a 27 % crop of 1440 (F-019, F-007; l.1491, l.256).
2. Tes pin start "top top" → **"top top+=48"**, as R7 did for the showcase. Headline glyph tops go from y=40 to **≥ 88 px** and the diaeresis shows for the whole pin. This restores the protected effect's own signature, so the lead must name it in the brief (EFFECTS.md; l.1194).
3. Rewrite the pris lede with no reference to the page. Cut "Med bra design menar vi det ni just har sett. Den nivån får ni på varje rad nedan". Either let "Alla har rätt till bra design." stand alone, or say something about the offer (F-018, gate 99; l.830).
4. Case-head text colour ink → paper: rust **2.95 → 5.3:1**, lacquer **2.57 → 6.1:1**. Use the existing .cell--rust / .cell--lacquer (l.71–72, 727, 770).
5. Hero pin start "top top" → **"top top+=48"**: black band 48 → **0 px** for the whole +=220% (l.1148). Footer link at 390: no-wrap on the address, or break before it as plain text. Clickable lines 2 → **1** (gate 49; l.904).
6. Kontakt ÖH gets content (the image or the headline, mirroring the hero): empty quadrants 1 → **0**. Process rows: seam colour #000 → #333 on black so the 7 row boundaries show at 1 px (house-physics "hairlines separate"; l.857, 214).
7. One reveal profile for all non-protected section reveals: **14 px / 620 ms / --ease-out / 30–80 ms stagger, play once, no reverse**. Pris slide 60–100 px → **14 px**, cells never leave their seam (house-physics § Structural; RORELSE l.8; l.1204–1214, 1286, 1931–1955).
8. Pris digits to display scale and right-aligned: 44 → **clamp(64px, 6.7vw, 96px)** at 1440; "Pris vid förfrågan" one step smaller (≈48 px). Drop the picker's duplicated meta, which removes 2 duplicate strings per screen, and the 20 px gutter → **0** (house-physics § Ledger, F-017, BYGGSPEC § 3.8; l.425, 232, 694–704).

## keep

Keep these unchanged:
- the hero 2×2 with the card flipping across the seam;
- the 180 px white tes headline with its char rise and pin, and the Hyperborea screen resolving from raster to colour;
- the showcase mechanism: one pin, crossfading 30 px/18 px text box, counter and mint track;
- the loupes that are pure detail ("2 480 kr SEK", "atelier@calyx.se", 料理は対話);
- the showcase step copy, which explains decisions in plain Swedish ("Med en lista räcker det att skriva om en rad");
- radius 0 everywhere, two families (Geist 500 / Geist Mono), zero em-dashes, arrows and middle dots, zero shadowed cards;
- the kontakt card handover that self-flips at 0.7.
