# Alunix r5 — V1 · Dokumentär band — build notes

Brief: `tests/alunix-concepts-r5/brief.md` (binding, all three variants) + `contract.md`'s
V1 row (binding). Starting point: `tests/alunix-concepts-r4/cells/M1-chain/index.html`
(Anton's chosen winner — "kontinuerlig grund, förskjutna spalter"), copied in and rebuilt
per r5's brief + contract, all copy kept verbatim except the lines brief.md itself changes.

## Reference lock (written before code)

**Tier 2** — direction is M1's own build (structure/copy/engine source, explicitly what to
keep or diverge from per contract.md's V1 row) plus three catalogue entries named in
contract.md's V1 row:

- `design-catalogue/entries/rre-ventures/entry.md` — **primary structural reference,
  carried over from M1 unchanged**. Preserve: one continuous, non-literal photograph
  (`k4-cabin-desk.webp`, fixed, grayscale, drift-tinted) running the full page as ground,
  alternately exposed and covered by opaque content panels. Nothing new borrowed here this
  round — M1 already built this device and V1 inherits it as-is.
- `design-catalogue/entries/creative-giants/entry.md` — for the hero panel's weight-300
  poster-scale headline sitting directly on an unlined cream ground. Preserve: "a light
  weight at poster scale reads as considered restraint" — ported from Creative Giants'
  84px Switzer-300 to `Er hemsida är nutidens visitkort` in Public Sans 300 here. Reject:
  Creative Giants' own bone-white `#fffef7` canvas and charcoal-gradient lettering — V1
  keeps M1's own `--c-paper` token and flat ink colour, the catalogue entry contributes the
  *weight discipline* only.
- `design-catalogue/entries/insign/entry.md` — for the tjänster grid's per-service tag.
  Preserve (scaled down hard): "assign one colour per category so the palette becomes
  navigation." Reject: Insign's own three fully saturated hues (chartreuse/lavender/orange)
  — that would add a second and third saturated accent, breaking the house rule of exactly
  ONE saturated accent at display scale. Adapted instead as three TINTS/SHADES of the one
  locked accent blue (`--tag-1` full strength, `--tag-2` a 55% white-mixed tint, `--tag-3`
  the existing `--c-accent-deep`), applied as a 2px underline beneath each service's index
  number. Same "navigate by colour" principle, one hue family, not three.

**Grammar**: unchanged from M1 — contract.md's "continuous world" in the loose sense
brief.md itself uses (one ground that never cuts), not the strict upstream grammar. See
M1's own NOTES.md for the full reasoning (M1's file, §Grammar note); not re-litigated here
since V1 is a structural remix of M1, not a fresh grammar pick.

**Structure differs from M1** on exactly the dimensions contract.md's V1 row assigns:

1. **Hero device.** M1: the Tidvatten iframe as one full-width interactive act. V1: a
   photo+cream-panel band — `k4-cabin-desk.webp` in colour, 62% right (cropped to the
   window-light triangle + desk lamp, `object-position:27% 34%`, measured against the raw
   asset), cream panel 38% left carrying the page's own headline + sub-line (verbatim,
   brief.md point 1), Public Sans 300, a hairline rule under the headline and a hairline
   border where the panel meets the photo.
2. **Blue block figure.** M1: a small 16:10 Hyperborea thumbnail beside the thesis text in
   a 2-column grid. V1: a full-width 16:6 strip *below* the thesis text, contained (never
   half outside — fixed-aspect `overflow:hidden` box, bleed-container sink capped well
   inside it), mono caption underneath reading the brief's own Hyperborea label.
3. **Offset stagger removed.** M1's signature device (`.col-right{margin-top:50vh}`) is
   gone. Brief.md's own instruction ("Högerspaltens 50vh-förskjutning ersätts av
   [innehåll]") reads as replacing the empty margin with real content, not keeping the
   margin — so col-right now starts flush under the hero (measured: hero bottom and
   `.stagger` top both sit at document y = 1721.5px, a 0px gap) and opens directly with the
   giant headline + ledger block that used to live in col-left.
4. **Content reassignment.** Col-left: console card → blue thesis block (with the
   Hyperborea strip) → Calyx frame. Col-right: giant headline + ledger → tjänster → Hōrai
   frame → price box. The "Utvalda projekt / Calyx…" mini-teaser that used to close M1's
   giant block was removed outright (not rewritten) — Calyx no longer follows it in the
   same column, and brief.md forbids new copy, so there was nothing to replace it with.
5. **Per-panel alternating reveal**, replacing M1's single reveal-per-close pattern: every
   one of the seven panels (console, thesis, Calyx, giant, tjänster, Hōrai, price) carries
   `data-sc-reveal`, alternating left/right/left/right/left/right/left in DOM order, per
   brief.md point 7 ("varje panel reveal växelvis left/right när den passerar").

**New construction this build**: the hero's signature move (cream panel growing 38%→100%
off the hero act's own `--sc-p`, bespoke JS, see §Signature move below); the full-width
Hyperborea strip and its contained bleed-sink; the alternating-reveal assignment; the
insign-derived tag shading; two frame-label blocks (kicker + line) added above the Calyx
and Hōrai frames, living inside the same wrapper the reveal already targets so they never
open a fresh gap of their own.

**Reject** (unchanged from M1, restated): a second FIXED background photograph — the hero
band's colour photo is a foreground content element inside its own section, not a second
page-wide fixed layer; transform/opacity applied to an `<iframe>` tag or any of its
ancestors while on screen (both frame wrappers stay static/full-box/no-bleed, verified by a
150px-step scroll sweep, see §Verification); a third saturated hue anywhere on the page;
dashes in visible text; invented numbers beyond the three prices brief.md itself supplies.

## Decision ledger

| Decision | Source | Role | Why |
|---|---|---|---|
| Hero = photo 62% / cream panel 38%, not the Tidvatten frame | contract.md V1 row | hero | Literal instruction; also the clearest way to differ from M1 on the hero-device fingerprint dimension |
| Hero photo = `k4-cabin-desk.webp`, colour, `object-position:27% 34%` | brief.md point 1 + measured against the raw asset (Read tool, `_assets/k4-cabin-desk.webp`) | hero framing | The raw photo's window-light triangle and desk lamp sit in the left-third, upper-half of the frame; this crop keeps both in view at a wide band aspect instead of centring on the (duller) right wall |
| Used the r3-build's already-downsized copy of the same file (`r3/build/assets/k4-cabin-desk.webp`, 42KB, 733×1100) instead of the raw pool asset (827KB) | Step 5b imagery pipeline ("downsize, re-encode, vendor") | perf | The raw pool asset intermittently failed to load under the dev server's single-threaded concurrency (`ERR_CONNECTION_RESET`, reproduced 3×); the pre-optimized copy loads reliably and is the correct choice per the pipeline regardless |
| Cream panel width driven by bespoke JS reading the hero act's own `--sc-p`, tall (184vh) wrapper + `position:sticky` (plain CSS) inner stage, growth domain hardcoded to `[0.352, 0.648]` **— superseded, round 2: act height 130vh, domain `[0.4348,0.5652]`, cap 55%, see below** | contract.md V1 signature-move cell | signature move | The domain is not guessed: for a flow act with height `h` (in 100vh units) and a `vh`-tall sticky stage, sticky ENGAGES at `p = 1/(h+1)` and RELEASES at `p = h/(h+1)`; with `h=1.84` that was `0.352`/`0.648`, independent of actual viewport pixels — derived algebraically, then confirmed live (see §Verification). Round 1's 100% cap is what round 2 fixed |
| Hyperborea demoted from an interactive-feeling side card to a full-width 16:6 contained strip | contract.md V1 row ("aldrig halvt utanför") | blue block figure | Literal instruction; `overflow:hidden` fixed-aspect box + bleed-sink capped at 56px (well under the box's own real clip budget) guarantees it never bleeds past the block edge |
| Thesis rise/sink motion pair reused from M1's own mechanism (local-mode headline rise, act-mode strip sink), rebuilt from scratch in this file's JS (a generic `data-motion` engine, not just the hero's own `paintHero()`) | brief.md point 7 ("text och bild i olika riktningar minst i en akt") | opposite-direction proof | First draft of this file only wired up `paintHero()` and left the `data-motion` attributes unhandled — caught by a live numeric check (all `transform` values reading `none`) before shipping, see §What was tried and fixed |
| Offset stagger (`.col-right{margin-top:50vh}`) removed; right column starts flush under hero | brief.md point 2 ("Ingen tom lucka under heron... ersätts av...") | layout | Literal instruction; measured hero-bottom to `.stagger`-top gap = 0px |
| "Utvalda projekt" mini-teaser removed from the giant block, not rewritten | brief.md's no-new-copy rule + Calyx no longer follows the giant block in the same column | compliance | Nothing to replace it with that wouldn't be new copy; removing was the only compliant option |
| Insign's 3-hue service-band device scaled down to 3 shades of the one locked accent | house-physics.md "exactly ONE saturated accent" vs. contract.md's insign citation | craft/compliance | Reconciles the two: keeps the "navigate by colour" principle without adding a second or third saturated hue |
| Frame labels (`Exempelsida` kicker + line) live inside the same wrapper the reveal targets | brief.md point 3 (labelling) + brief.md point 2 (≤8vh gaps) | compliance | A separate label section above each frame would have opened its own gap; nesting it inside the existing `.frame-block` avoids that entirely (measured gap = 0px either side) |
| `.calyx-block .frame-label .k-mono` recoloured from the 60%-opacity mute tone to solid ink | `a11y_scan.py` first pass (1 violation, `color-contrast`, serious) | a11y fix | Measured 4.4:1 on the block's `#e9e5da` ground, under the 4.5:1 floor for 11px text; solid ink measures 8.7:1 |
| Mobile hero logo gets a small cream backing chip, not left as bare dark-fill ink **— superseded, round 2: logo lives inside the panel on every breakpoint now, no chip needed, see below** | visual check against `shots/mobile-390--fold.png` | craft fix | On mobile the logo sat over the photo (stacked layout, not the cream panel); dark ink directly on the mid-brown wood photo was low-contrast decoration. Round 2 moved the logo into the panel's own flow entirely, which removes the over-photo case (and the clipping/scribble defect) on every breakpoint at once |
| Full-page desktop screenshot hand-composited with sticky-aware sampling, not `full_page=True` | Same class of Playwright bug M1's own NOTES.md documented, reproduced here (see §Capture-methodology notes) | verification | `full_page=True` renders the sticky hero stage once at rest and leaves the remaining ~756px of its tall wrapper blank |

### Round 2 fix pass (Anton's pixel review, three defects)

| Decision | Source | Role | Why |
|---|---|---|---|
| Logo moved from an absolutely-positioned, `translateY(-50%)`-straddling element on `.hero-stage` to a normal-flow first child of `#heroPanel`, height `clamp(48px,5vw,72px)` (≈72px at 1440), no blend mode, fill unchanged (`#14171a` = `--c-ink`) | Anton: "logo is a black scribble... clipped by the top bar" | hero / a11y-adjacent craft fix | The old rule sat the mark half above `.hero-stage`'s own `overflow:hidden` top edge (clipped) and half inside the topline's translucent dark scrim (unreadable) — moving it into the panel's own normal flow puts it on plain cream, fully inside the panel's bounds, below the topline in both DOM order and screen position, so nothing clips or collides with it. The old mobile-only cream backing chip (row above, now superseded) is gone too — the logo never sits over the photo any more, on any breakpoint, so it needs no chip |
| Panel growth cap lowered from 100% to 55% (`HERO_W_MAX`); hero act height cut from 184vh to 130vh; growth domain constants recomputed from `[0.352,0.648]` to `[0.4348,0.5652]` to match | Anton: "the panel growth creates a whole empty viewport... big empty areas" | signature move | At a 100% cap the panel fully covered the photo, so mid-scroll the screen was 100% cream + headline (zero photo) for a real stretch — measured as a whole extra viewport of bare cream. Live sweep after the fix (see §Hero signature move, updated) shows panel width plateaus at exactly 55.0% and photo fraction never drops below 45.0% at any sampled 300px step through the act, comfortably inside the brief's own 40% floor. Act height 130vh keeps the whole hero (including its sticky travel) at 1.3 viewport heights, under the 1.4 ceiling |
| Both columns end within 4vh of each other: `.stagger` changed from `align-items:flex-start` to `align-items:stretch`, `.col` is now itself a flex column (`display:flex;flex-direction:column`), `.calyx-block` (col-left's last item) gets `flex:1;min-height:90vh;display:flex;flex-direction:column` with `.calyx-block .frame-box{flex:1}` so the iframe area itself (not just blank space under the label) absorbs the extra height; reset to `flex:none;min-height:0` on mobile so the single-column stack isn't forced to carry a spare 90vh | Anton: "the columns end a viewport apart... a full screen of bare ground bottom-left" — same device r3 used (`.calyx-frame{flex:1}` there) | layout | `align-items:stretch` makes both columns share the taller column's (col-right's) height; `flex:1` on the shorter column's own last item is what lets it consume the resulting leftover space instead of the ground showing through. Live measurement: `colLeftBottom === colRightBottom` (0.0px diff) at both 1440×900 and 1280×800, well inside the ≤0.04×innerHeight ceiling (36.0px and 32.0px respectively) |

## Feeling curve (written before building)

1. **Arrival, grounded in a real room.** The hero band opens on the desk photo (window
   light, drafting lamp, a cap reading "501") with the headline in a plain cream panel
   beside it — no chrome, no scrim, a documentary photograph doing the work M1's Tidvatten
   frame used to do. Caused by: the 62/38 photo/panel split, full colour, no filter.
2. **Attention, the panel takes the room.** Scrolling through the hero's own extra height,
   the cream panel visibly widens — the same headline that started cramped at 38% now
   spans the full band at 100%, the photo fully covered. Caused by: the bespoke
   `--sc-p`-driven width grow, the page's signature move.
3. **Release, back into the grid.** The panel holds at 100% through the hero's remaining
   scroll life, then the whole band scrolls away and the console card and giant headline
   appear side by side, flush, no gap. Caused by: the sticky stage un-sticking, the removed
   50vh offset.
4. **Weight, two speeds in one act.** In the blue thesis block, "Det första intrycket är
   digitalt." visibly climbs ahead of the scroll while the Hyperborea strip beneath it
   settles lower in its own frame — the required opposite-direction pair, now on real
   photography rather than a small thumbnail. Caused by: local-mode text rise vs. act-mode
   image sink.
5. **Peak: the giant headline lands where the offset used to be empty.** "VI BYGGER ERT
   VARUMÄRKE." kinetic-splits into view directly under the hero with no run-up, the ledger
   stags in below it — the exact spot M1's own layout left bare for a whole viewport height.
   Caused by: the kinetic reveal + ledger stagger landing in the space the removed offset
   used to waste.
6. **Two lives out of step.** Left column settles inside the real Calyx site; right,
   slightly ahead by content weight, is already past Hōrai and into the price box. Caused
   by: two independent columns of different natural heights, same as M1.
7. **Close, uneven, resolved anyway.** Calyx simply stops; the price box, further down on
   the right, lands still — kontakt@alunix.se the last line before the shorter left column's
   remaining height shows bare grayscale ground. Caused by: two independent endings, the
   ground absorbing the difference (inherited from M1, unchanged).

**Peak:** act 2/3 (the hero panel's own growth to 100%, immediately followed by the giant
headline landing with no run-up where M1's offset used to leave a bare gap) — the largest
single structural change from M1, and the moment that proves the "ersätts av innehåll, inte
tomrum" instruction actually happened.

**Tell-someone sentence:** "It's the site where the text panel in the photo slowly eats the
whole picture as you scroll, until the headline you started reading small is suddenly the
entire width of the screen — and then it just lets go and the rest of the page catches up."

**Signature move:** the cream panel growing from 38% to 100% width, driven off the hero
act's own `--sc-p` (not a kit parameter — a page-authored script reading a plain `flow`
act's published progress and writing a custom-property width), holding at full width
through the act's release before the section scrolls away into the grid below.

## Devices per act (target: ≥4 families, never the same one twice running)

DOM order (col-left panels precede col-right panels; the two are visually interleaved by
the flex row, not by DOM position):

1. `act-hero` — bespoke width-grow (signature move, off `--sc-p`, not a kit device) +
   **parallax** (`-1.2`, hero photo) + `drift` stop 1.
2. `panel-open` (left) — **reveal** (`left`) + `flow`-adjacent rise (`data-motion`, console
   card as one block).
3. `panel-thesis` (left) — **reveal** (`right`) + bespoke **rise/sink pair** (headline
   local-mode rise, Hyperborea strip act-mode sink — opposite-direction proof) + `drift`
   stop 2.
4. `calyx-block` (left, close) — **reveal** (`left`). Frame itself static, full box, no
   bleed, no transform (verified, see below).
5. `panel-giant` (right, opens directly under hero) — **kinetic** (`lines`, the giant
   headline) + **flow+in** (ledger, staggered) + rise (`data-motion`, headline+sub).
6. `panel-services` (right) — **reveal** (`left`) + **flow+in** (section head + 3 services,
   staggered) + rise (`data-motion`, statement) + `drift` stop 3.
7. `horai-block` (right) — **reveal** (`right`). Frame itself static, full box, no bleed,
   no transform.
8. `price` (right, close) — **reveal** (`left`), otherwise static (unchanged house lesson
   from M1/r3: "the close should rest").

Families used: bespoke signature move, parallax, reveal, kinetic, flow+in, cue-adjacent
rise/sink (6, counting the bespoke `data-motion` rise/sink mechanism as its own family per
brief.md's explicit ask for it). No two consecutive acts in DOM order repeat the same
primary family: signature-move+parallax → reveal → reveal+rise/sink → reveal → kinetic+in →
reveal+in → reveal → reveal.

## Device table per act (per viewport)

| Act | Desktop (≥900px) | Mobile (<900px) |
|---|---|---|
| act-hero | photo 62% / cream panel 38%→100% (sticky-driven grow), logo straddles top edge | stacks: photo (52vh) then panel (auto height, full width), no grow (script gated off `<=900px`), logo gets a cream backing chip |
| panel-open | dark console card, kicker row + wordmark + body + service list + CTA | same, stacked, full width |
| panel-thesis | text block, then full-width 16:6 Hyperborea strip below it, mono caption | same, single column, strip still full width of the panel |
| calyx-block | label (kicker+line) then iframe, min-height 64vh, static/full-box | label then iframe, min-height 60vh |
| panel-giant | giant kinetic headline, 3-row ledger | stacked, ledger single column |
| panel-services | 3-col services grid, tag-shaded index numbers | single column |
| horai-block | label then iframe, min-height 64vh, static/full-box | label then iframe, min-height 60vh |
| price | static, padded | static, padded, full width |

## Fingerprint row (vs. M1, contract's own ≤2/6 shared ceiling within this cell's own use of M1's grammar)

| Dimension | M1 | V1 | Shared? |
|---|---|---|---|
| Grammar | continuous world (loose) | continuous world (loose) — inherited, not a fingerprint axis for this remix | Yes (by design, all three r5 variants share M1's grammar) |
| Hero device | full-width Tidvatten iframe, single act | photo 62% / cream panel 38%→100%, no iframe | No |
| Act-sequence shape | full-width act, then 50vh-offset stagger, independent close heights | full-width hero band, then flush (no offset) stagger, independent close heights | No |
| Blue-block figure | small 16:10 side-by-side thumbnail | full-width 16:6 contained strip below the text | No |
| Signature move | the 50vh offset itself + the ground's drift | the cream panel's own scroll-driven grow (38%→55%, round 2 fix; round 1 shipped 38%→100%) | No |
| Close pattern | Calyx + price box, deliberately unsynced | Calyx + price box, deliberately unsynced (inherited) | Yes (inherent to the shared copy/asset constraint, same as M1 vs r3) |

Shared: 2/6 (grammar and close pattern, both structurally inherited rather than a V1
choice) — the four remaining dimensions (hero device, act-sequence shape, blue-block
figure, signature move) are exactly the four contract.md's V1 row assigns as this variant's
own axes of difference, all four differ.

## Gap measurement (JS, every panel-to-panel gap per column, brief's own ≤8vh ceiling)

Measured live via Playwright (`getBoundingClientRect()` on consecutive panels within each
`#colLeft`/`#colRight`), at rest (scrollY 0, geometry is scroll-position-independent since
gaps come from padding/margin, not motion):

**Desktop 1440×900** (innerHeight 900, so 8vh = 72px):

| Column | From | To | px | vh |
|---|---|---|---|---|
| left | panel-open | panel-thesis | 0 | 0.00 |
| left | panel-thesis | calyx-block | 0 | 0.00 |
| right | panel-giant | panel-services | 0 | 0.00 |
| right | panel-services | horai-block | 0 | 0.00 |
| right | horai-block | price | 0 | 0.00 |

**Mobile 390×844** (innerHeight 844, so 8vh = 67.5px) — same panels, same result:

| Column | From | To | px | vh |
|---|---|---|---|---|
| left | panel-open | panel-thesis | 0 | 0.00 |
| left | panel-thesis | calyx-block | 0 | 0.00 |
| right | panel-giant | panel-services | 0 | 0.00 |
| right | panel-services | horai-block | 0 | 0.00 |
| right | horai-block | price | 0 | 0.00 |

All panels are adjacent siblings with no margin between them (each panel supplies its own
padding), so every measured gap is exactly 0px — comfortably inside the ≤8vh ceiling. The
hero-to-stagger gap (not a same-column pair, but the other half of brief.md point 2's
"ingen tom lucka under heron") measured 0px as well: hero bottom and `.stagger` top both
sit at document y = 1721.5px.

**Round 2 re-check:** all gaps above re-measured 0px at both breakpoints after the round 2
fixes (the `align-items:stretch`/`calyx-block flex:1` change only affects where each
column's own bottom lands, not the spacing between panels inside a column). The
hero-to-stagger boundary moved with the shorter 130vh act, but the gap itself is still
exactly 0px: hero bottom and `.stagger` top now both sit at document y = 1235.5px (was
1721.5px under the old 184vh act).

## Hero signature move — measured, not asserted

**Round 2 (current): panel width + photo-visible fraction at every 300px scroll step through
the act (desktop 1440×900, motion on, live Playwright sweep):**

| scrollY | panel width | panel % | photo visible % |
|---|---|---|---|
| 0 | 547.2px | 38.0% (rest) | 62.0% |
| 300 | 780.5px | 54.2% | 45.8% |
| 600 | 792.0px | 55.0% (capped) | 45.0% |
| 900 | 792.0px | 55.0% (held) | 45.0% |
| 1200 | 792.0px | 55.0% (held) | 45.0% |
| 1500 | 792.0px | 55.0% (held) | 45.0% |
| 1800 | 792.0px | 55.0% (held, released) | 45.0% |

Same sweep at 1280×800: panel plateaus at exactly 704.0px = 55.0% of 1280, photo-visible
floor 45.0% throughout — both viewports clear the brief's 40% floor with 5 points to spare
at every sampled step, not just at rest or full-grow. Growth domain recomputed for the new
130vh act height (100vh-units `h=1.3`): sticky engages at `p=1/(h+1)=0.4348`, releases at
`p=h/(h+1)=0.5652`; `HERO_W_MAX=55` replaces the old 100% ceiling in `pct = 38 +
(HERO_W_MAX-38)*g`. Act height 130vh / 900px viewport = 1.3, under the 1.4 ceiling (and
1280×800: 1040px/800 = 1.3, same ratio, confirms the vh-based CSS height holds the ratio
across viewports as designed).

**Round 1 (superseded, kept for the record): live `--sc-p` and panel width readings at five
scrollY positions through the 184vh act, 100% cap:**

| scrollY | `--sc-p` | panel width | panel % |
|---|---|---|---|
| 0 | 0.3265 | 547.2px | 38.0% (rest) |
| 414 | 0.4885 | 941.6px | 65.4% |
| 745 | 0.6180 | 1414.4px | 98.2% |
| 1076 | 0.7475 | 1440.0px | 100.0% (held) |
| 1490 | 0.9094 | 1440.0px | 100.0% (held, before release) |

This is exactly what produced the defect: full-width panel means 0% of the photo is
visible for the whole 1076→1490+ dwell, which reads as a screen of bare cream. Round 2's
55% cap and shorter act fix this directly, per the table above.

## What was tried and fixed before verification passed

1. **Hero photo intermittently failed to load** (`net::ERR_CONNECTION_RESET`) when pointed
   at the raw, un-downsized pool asset (`/tests/alunix-concepts/_assets/k4-cabin-desk.webp`,
   827KB) under the dev server's single-threaded concurrency. Fixed by switching to the
   already-optimized copy of the same photo the r3 build vendored
   (`/tests/alunix-concepts-r3/build/assets/k4-cabin-desk.webp`, 42KB, same crop/composition)
   — the correct choice per Step 5b's own imagery pipeline regardless of the load failure.
2. **Growth domain miscalibrated on the first pass.** Initially guessed `[0.02, 0.46]` for
   the panel's grow window; live measurement showed the panel already at ~85% width on a
   cold page load (scrollY 0), because a flow act's `--sc-p` is not zero at document load
   when the act sits near the top of the page. Root-caused algebraically (see §Hero
   signature move above) and replaced with the derived constants `[0.352, 0.648]`.
3. **The `data-motion` rise/sink engine was missing entirely on the first pass** — only the
   hero's own `paintHero()` was wired into the scroll handler; the thesis headline/strip
   and the console/giant/services rise wrappers carried `data-motion` attributes that
   nothing read. Caught by a live numeric check (`getComputedStyle(...).transform` reading
   `'none'` at every one of 5 sampled scrollY positions) before it reached the screenshot
   review stage. Fixed by rebuilding the generic engine (mirroring M1's own mechanism) and
   wiring it into the same `schedule()`/freeze/unfreeze hooks as the hero script.
4. **`a11y_scan.py` found one contrast violation** (`.frame-label .k-mono` on the Calyx
   block's `#e9e5da` ground, measured 4.4:1 against a 4.5:1 floor) — fixed by using solid
   ink instead of the 60%-opacity mute tone for that specific 11px label; re-scan came back
   clean (0 violations).
5. **Mobile hero logo low-contrast** — dark-ink logo mark sits over the photo on the mobile
   stacked layout (not the cream panel, which is where it sits on desktop); fixed with a
   small cream backing chip + shadow, matching the mark's own visibility on desktop.
6. **The full-page desktop composite screenshot duplicated the hero content twice**, then
   (after a first fix) duplicated the panel-open/thesis section once, both from the same
   root cause: naive overlapping-slice tiling doesn't work for a `position:sticky` region,
   because its visible content doesn't translate with scroll the way ordinary flow content
   does. Fixed by giving the composite script sticky-aware handling: sample exactly `ceil
  (region_height / vh) + 1` frames evenly across the region's own release window (never
   past it), each pasted into an equal, non-overlapping share of the region's real document
   height. See §Capture-methodology notes below for why this was needed at all.

### Round 2 fix pass (Anton's pixel review)

7. **Logo clipped/scribbled.** Root cause: `.hero-logo` was `position:absolute;top:0;
   transform:translateY(-50%)` on `.hero-stage`, straddling document y=0 of the stage — the
   top half fell outside `.hero-stage{overflow:hidden}` and got clipped, the visible bottom
   half sat inside the topline's translucent dark scrim (`rgba(6,7,9,.62)` fading out),
   reading as a small illegible mark. Fixed by moving the logo into `#heroPanel`'s own normal
   flow (first child, before the `<h1>`) — no absolute positioning, no clipping ancestor, no
   overlap with the topline (which is above it in both DOM order and screen position on
   every breakpoint). Confirmed by screenshot: the mark now renders as the full compass/X
   glyph at ~66px height, solid ink, fully inside the cream panel.
8. **Whole empty viewport of bare cream mid-hero.** Root cause: the panel grew to 100% width,
   so once fully grown the photo was 0% visible — for a real stretch of scroll (the domain's
   `[0.618,0.648]` tail plus the sticky hold) the screen showed only cream + headline, no
   photo, no visual variety. Confirmed with a live 300px-step sweep of panel-width vs.
   scrollY (see §Hero signature move, "Round 1" table) before fixing. Fixed by capping growth
   at 55% (`HERO_W_MAX`) and cutting the act from 184vh to 130vh; re-swept after the fix (see
   "Round 2" table, same section) — photo-visible floor is now 45% at every sampled step,
   never drops toward 0.
9. **Columns ending a viewport apart at the page bottom.** Root cause: `.stagger` used
   `align-items:flex-start`, so each column's height was purely its own content height —
   col-left (console → thesis → Calyx) came up shorter than col-right (giant → tjänster →
   Hōrai → price), and the shared fixed `.ground` photo showed through the gap on the left.
   Fixed the same way r3 fixed the identical problem: `align-items:stretch` on `.stagger` so
   both columns share the taller column's height, `.col` itself becomes a flex column, and
   `.calyx-block` (col-left's own last item) gets `flex:1;min-height:90vh` (plus
   `.frame-box{flex:1}` inside it so the iframe area, not dead space under the label, is what
   grows) to absorb the difference. Verified live: `colLeftBottom === colRightBottom` (0.0px
   diff) at both 1440×900 and 1280×800.
10. **Hand-composited screenshot showed an apparent "duplicate" of the desk photo right below
    the first fold, after the round 2 hero-height change.** Investigated as a possible new
    regression before ruling it out: live `getBoundingClientRect()` measurement at scrollY=900
    confirmed the hero-stage's *released* (post-sticky) resting position is `document [335.5,
    1235.5]`, not `[65.5, 965.5]` as a naive symmetric read of the sticky mechanics would
    suggest — a sticky child locks at the *bottom* of its long containing block once released,
    not the top, so its resting box legitimately overlaps into the second 900px-tall capture
    tile. Both frames are individually correct (confirmed live in the Browser pane at several
    scrollY values); the "duplicate" look is purely an artifact of tiling a naive one-shot-per-
    viewport composite across that boundary. A first attempt at finer (150px-strip) slicing to
    avoid the boundary introduced a *worse* artifact (ghosted/doubled text throughout the page,
    from reveal-transition frames not yet settled at the smaller per-strip wait). Settled on
    the original 900px-tile method with a longer 400ms settle wait per tile — clean everywhere
    except that one hero/stagger seam, which is now documented here as a known capture quirk,
    same class as the `blankBands` note below, not a page defect (`scroll_verify.py`, the
    actual verification tool, independently reports zero blank bands this round).

## Capture-methodology notes (not page defects)

- **Round 1 (superseded): `scroll_verify.py`'s `blankBands` check reported one band,
  966px→1722px (756px), at both motion-on and `--reduced-motion`**, root-caused to the same
  `full_page=True` + sticky-element artifact M1's own NOTES.md documented. **Round 2: this
  band is gone — `scroll_verify.py` now reports `blankBands: []` at both motion-on and
  `--reduced-motion`, at 1440×900 and 390×844.** The shorter 130vh act plus the 55% growth
  cap leaves no scroll range where the sticky region's own `full_page=True` mis-layout could
  produce a large enough blank gap to trip the detector — a side effect of fixing defect #2,
  not a separate fix.
- **Round 2: the hand-composited `shots/desktop-1440--full.png` still shows one seam** where
  the released hero-stage's resting position (document `[335.5,1235.5]`, see fix #10 above)
  straddles the boundary between the first two 900px capture tiles. Confirmed as a capture
  artifact, not a page defect, the same three ways as round 1's note: (1) a live scroll sweep
  in the Browser pane shows correct, continuous content at every scrollY tested; (2) the
  mobile composite (hero not sticky there) has no such seam; (3) `scroll_verify.py`'s own
  `blankBands` check — an independent tool, not the hand-rolled composite script — reports
  zero blank bands this round, at every configuration tested.
- **Round 1 (superseded): `scroll_verify.py --reduced-motion` reported one expected
  `deadScroll` entry (300px→600px, diff 0.0)**, because two scroll positions both landed
  inside the 184vh act's long sticky dwell and the panel (held at rest width under reduced
  motion) produced byte-identical frames. **Round 2: `deadScroll: []`** at both motion-on and
  `--reduced-motion` — the shorter 130vh act's sticky dwell is narrow enough that no two
  adjacent 300px-step samples land inside it and produce identical frames any more. Not a
  design change to the reduced-motion behaviour itself (the panel still holds at 38% rest
  width under reduced motion, confirmed live, see §Verification results) — purely a
  side effect of the shorter act height changing which sample pairs happen to coincide.

## Skills loaded, in order

1. `Skill(design)` — front door; Step 0 (page scope, full build), Step 1 (pre-flight — no
   `DESIGN.md` in `tests/alunix-concepts-r5/`), Step 1b (reference lock above: M1's own
   file + three catalogue entries read in full), Step 2 (Tier 2 — M1 + catalogue are the
   stated direction), Step 2b (feeling curve, device list, fingerprint row above — bake-off
   skipped, this is a task-assigned single direction per contract.md, not an open
   exploration), Step 4 (build), Step 5 (verify, this document).
2. No copywriting/copy-editing/humanizer chain run — brief.md and contract.md both state
   the copy is verbatim (either from M1, or the exact new lines brief.md itself supplies:
   the hero headline/sub, the three demo-site labels, the three price rows). The copy
   gate's own scope note ("any user-facing string being *written*") does not apply to text
   that is dictated verbatim by the brief and only placed, not authored.

## Verification results (round 2, after the three pixel-review fixes)

- **Shots regenerated** (Playwright, hand-rolled composite script, see fix #10): desktop
  1440×900 fold (`shots/desktop-1440--fold.png`) + hand-composited full page
  (`shots/desktop-1440--full.png`, sticky-aware, real document height 3863px — down from
  4349px, tracking the shorter 130vh hero act), mobile 390×844 fold
  (`shots/mobile-390--fold.png`) + full (`shots/mobile-390--full.png`, real document height
  4671px), `shots/motion-0..4.png` re-shot through the thesis panel's opposite-direction pair.
- **`scroll_verify.py`** (desktop 1440×900, motion on): `deadScroll: []`, `cuesNeverFull:
  []`, `unrevealed: []`, `contrastUnderMedia: []`, `notes: []`, **`blankBands: []`** —
  positions 0 through 2963 in 300px steps (shorter than round 1's 0–3449 sweep, tracking the
  shorter document).
- **`scroll_verify.py`** (mobile 390×844, motion on): all five arrays clean including
  `blankBands: []`, positions 0 through 3827.
- **`scroll_verify.py --reduced-motion`** (desktop 1440×900): all five arrays clean including
  `deadScroll: []` and `blankBands: []` — both round 1's documented "expected" entries are
  gone this round, see §Capture-methodology notes for why.
- **`a11y_scan.py`:** 0 violations, 28 passes, 2 incomplete (axe's own "needs manual review"
  bucket, not a failure) — re-ran after the round 2 fixes, still clean (the logo move and
  column flex changes touched no colour/contrast surface).
- **Overflow:** `document.documentElement.scrollWidth === window.innerWidth` at both 1440
  (`1440 === 1440`) and 390 (`390 === 390`), checked after a full scripted scroll-through to
  the document's own bottom, not just at rest.
- **Console:** no `[scrollcraft]` warnings across a full 300px-step scroll sweep at both 1440
  and 390. Only messages present: `cdn.tailwindcss.com` production-use notices originating
  inside the Calyx/Hōrai iframes' own pages (outside this build's scope, same as every prior
  Alunix round).
- **Iframes:** two present (Calyx, Hōrai — Hyperborea is a static photo strip in this
  variant, not a frame, per contract.md's V1 row), both with real `title` attributes matching
  their visible labels (`Calyx, florist i Stockholm`; `Hōrai, Asian fusion-koncept`). Both
  re-verified static/full-box/no-transform across a full 200px-step scroll sweep of the
  entire document at both 1440 and 390 — zero instances of a non-`none` `transform` on either
  iframe or any of its ancestors, at any scroll position, at either breakpoint.
- **Gaps:** every panel-to-panel gap in both columns, both breakpoints, re-measured 0px — see
  §Gap measurement above. Well inside the ≤8vh ceiling. (Unaffected by the round 2 fixes —
  the `align-items:stretch`/`flex:1` change only alters where the *columns' own bottoms* land,
  not the spacing between panels within a column.)
- **Column-bottom alignment (new gate, round 2):** live measurement, both required
  viewports — `|colLeftBottom − colRightBottom|`: **0.0px** at 1440×900 (ceiling
  0.04×900=36.0px) and **0.0px** at 1280×800 (ceiling 0.04×800=32.0px). Both PASS with large
  margin.
- **Hero growth cap (new gate, round 2):** live 300px-step sweep, both required viewports —
  panel width plateaus at exactly 55.0% of the band width at both 1440×900 and 1280×800;
  photo-visible fraction never drops below 45.0% at any sampled step (floor required: 40%).
  Hero act height: 1170px/900 = 1.3 at 1440×900, 1040px/800 = 1.3 at 1280×800 — both under
  the 1.4 viewport-height ceiling. See §Hero signature move above for the full table.
- **Logo (new check, round 2):** renders as the full glyph at `clamp(48px,5vw,72px)` (66px at
  1440 fold, exact 72px only once 5vw reaches that value above ~1440px), solid ink, no
  clipping, no overlap with the topline bar, on both the desktop fold screenshot and the
  mobile full composite — confirmed by direct visual read of both.
- **Motion proof (`shots/motion-0..4.png`), re-shot after the fixes:** the thesis headline's
  `translate3d` y-offset moves -19.8px → -32.9px → -46.0px → -59.1px → -72.2px (local mode,
  still climbing across this sampled range, not yet saturated) while the Hyperborea strip's
  offset moves 7.3px → 10.6px → 13.8px → 17.1px → 20.4px (act mode) — opposite signs
  throughout at every frame, unaffected by the round 2 fixes (the `data-motion` engine was
  not touched).
- **Reduced motion:** `prefers-reduced-motion: reduce` emulated via a real Playwright
  browser context. All five sampled `[data-motion]` elements report computed `transform:
  none` at scrollY 2000; all seven `[data-sc-reveal]` elements report `clip-path: none`;
  the one `[data-sc-parallax]` element reports `transform: none`; the hero panel's computed
  width is `547.188px` (= 38%, unchanged, no growth); `__scFreezeMotion`/
  `__scUnfreezeMotion` are `undefined` in this branch, confirming both the bespoke hero
  script and the `data-motion` engine are gated out entirely, not just zeroed per frame.
- **Motion proof (`shots/motion-0..4.png`, scrollY computed live from the thesis panel's
  own document position, so the pair stays on screen at every frame):** the thesis headline
  wrapper's `translate3d` y-offset moves -80.0px → -80.0px → -80.0px → -80.0px → -80.0px
  (local mode, capped at 80px, already saturated by the first sampled frame — the headline
  leads the scroll fast, by design) while the Hyperborea strip's offset moves 23.6px →
  29.1px → 34.6px → 40.0px → 45.5px (act mode, uncapped in this range, ceiling 56px) —
  opposite signs throughout (headline risen and holding, strip still sinking), both fully
  inside their own boxes at every frame, confirmed by reading `getBoundingClientRect()`
  directly (not just the transform values) at every sampled position.
- **Hero signature move:** see §Hero signature move above — five-point live table, growth
  domain derived algebraically and confirmed matching measured behaviour.

## Not achieved / deviations from a literal reading

- The mono caption under the Hyperborea strip and the Calyx/Hōrai frame labels both use
  the exact copy brief.md point 3 supplies (`Exempelsida: Hyperborea, konferens i Lund`,
  `Calyx, florist i Stockholm`, `Hōrai, Asian fusion-koncept`) but are laid out as kicker +
  line (two visual rows) rather than a single run-on sentence with a colon — read as the
  more literal interpretation of "benämns med kicker + rad" (labelled WITH a kicker + a
  line), not a deviation.
- Nothing else identified as unachieved against brief.md or contract.md's V1 row.
