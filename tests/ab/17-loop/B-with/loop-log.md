# Loop log — Florhuset Majorna (tests/ab/17-loop/B-with)

Start file: `tests/ab/17-loop/round0.html`, copied to `B-with/index.html`
and worked on in place. Two full rounds of the design chain's Step 5 loop,
real Playwright screenshots and real browser automation throughout — no
finding below was guessed from source code.

---

## Round 1 — visual critique

**Capture**: `round1-before/` — `shoot.py` (fold + full, 6741px total) and
`shoot_slices.py … p 8` (8× 1440×900 slices). All 8 slices plus the fold
were read (`Read` tool) before writing anything.

**What the pixels showed**
- Hero diptych: the left panel (dense floral macro) and right panel (a
  daisy field against open sky) claim equal 50% columns but do not carry
  equal visual weight — roughly the top two-thirds of the right panel is
  blank sky. Squint-test failure (an open column holding less weight than
  its width claims).
- Fetching the right panel's source image directly (`photo-1574684891174`)
  confirmed it's a daisy field shot from below — but its alt text described
  a flat-lay of cut flowers on a work table. Wrong, not just unlucky
  framing.
- The vow-knot signature move — the page's own stated emotional peak (act
  3, feeling-curve doc in the file's header) — rendered as a thin,
  small scribble on the sticky wedding stage, easy to miss next to the
  headline and photograph.
- Colour dimension measured directly from the page's own OKLCH tokens
  (Björn Ottosson OKLab→linear-sRGB matrices + WCAG luminance formula, not
  eyeballed): `korall` on `fog` = **3.71:1**, used by `.kicker`,
  `.ledger__meta`, `.split__list dt` at 10.5px regular — fails the 4.5:1 AA
  floor for text that size. Every other measured pair (display-scale
  korall-on-dark, stone/ink/dis body text) cleared its floor with margin.

**Fixes applied** (full write-up: `round1-critique.md`)
1. **P1, Colour** — added `--korall-onlight: oklch(50% 0.17 32)` (same
   hue/chroma, darker step — measured **5.67:1** on fog) and repointed
   `.kicker`, `.ledger__meta`, `.split__list dt` to it. Display-scale
   korall-on-dark usage untouched.
2. **P2, Composition + content accuracy** — corrected the hero right panel's
   alt text to describe what's actually shown, and added
   `transform: scale(2.05); transform-origin: 50% 92%` (same licensed
   photo, no new asset) so the visible crop favours the flower band over
   blank sky.
3. **P2, Hierarchy** — scaled the knot-wrap (`clamp(9rem,16vw,14rem)` →
   `clamp(13rem,22vw,20rem)`) and thickened the stroke (2.4px → 3.4px) so
   the signature move reads as a deliberate device.

P3 (heading `line-height: 0.98`, slightly tight vs the register's ~1.1
guidance) was logged but deliberately left unfixed — not required this
round.

---

## Round 2 — mechanical accessibility pass

**Capture**: `round2-before/` (same shoot.py + shoot_slices.py pattern) —
read to confirm Round 1's fixes rendered as intended (they did: visibly
darker labels, a much more legible knot, daisies filling more of the right
hero panel).

**Mechanical scripts, before → after**

| Script | Before | After |
|---|---|---|
| `a11y_scan.py` (axe, 1440×900 + 390×844) | **1 violation**: `color-contrast`, serious, 1.4.3 — a different `.ledger__row` text node flagged on each of 3 repeat runs (390×844 only); 41 passes | **0 violations**, 41 passes — confirmed clean across 3 repeat runs after the fix |
| `tab_walk.py` (≤60 stops) | 11 stops, **0 issues** | 11 stops, 0 issues (already clean, unchanged) |
| `reflow.py` | `overflow320: [img]`, `overflowZoom200: [img]`, `hiddenUnderReducedMotion: 1 [li]` | Same 2 `img` flags — **investigated, confirmed false positives** (see below); `li` flag's one genuinely-on-screen case resolved |
| `detect.mjs` | 1 warning: `overused-font` (Fraunces) | Unchanged — deliberate, documented choice, not an a11y defect |

**What the pixels + scripts showed, and what got fixed**

- The `color-contrast` violation was **flaky** — a different ledger row
  flagged each run. Root cause: the reveal system's mount-time
  immediate-reveal check (`top < viewport-height × 1.1`) didn't cover the
  ledger section, so it depended on an IntersectionObserver + a 1.2s
  transition with up to 360ms of per-row stagger delay — a large enough
  window for axe's fixed ~500ms-post-load sample to occasionally catch a
  row mid-fade (intermediate opacity = degraded contrast). Fixed by raising
  the immediate-reveal threshold to `× 3.0` and shortening the stagger
  (1.2s→0.5s duration, 90ms→40ms per-row delay step). **HIGH**, per the
  skill's escalation rule (contrast failures are never averaged down for
  being transient) — confirmed fixed across 3 repeat runs.
- `reflow.py`'s `hiddenUnderReducedMotion` flag on `#wedFacts li`: direct
  inspection at the 3 checkpoints (0%, 50%, 100% of page scroll) showed
  only **1 of 3** facts visible at the one checkpoint where the wedding
  section is genuinely on-screen (50%) — the progressive-reveal thresholds
  (0.15/0.4/0.65) meant the full set was only simultaneously visible for
  the last 29% of the 220vh scroll-pin range. **MEDIUM** — fixed by
  fronting the thresholds to 0.05/0.12/0.20 (full set now visible for ~74%
  of the range). Re-check: all 3 facts on at the 50% checkpoint. The
  remaining flag at the 0%/100% checkpoints is a verified false positive —
  `reflow.py`'s hidden-element check excludes horizontally off-canvas
  elements but not vertically off-screen ones, and at those two checkpoints
  the wedding section is genuinely 2448px below / 3393px above the
  viewport (confirmed via `getBoundingClientRect`), not visible to anyone.
- `reflow.py`'s `img` overflow at 320px and 200% zoom: traced to the Round
  1 hero-crop fix (`transform: scale(2.05)`) expanding the image's own
  bounding rect beyond its container — but `document.documentElement.
  scrollWidth === clientWidth` at both breakpoints (checked directly),
  confirming the parent's `overflow: hidden` clips it and no real
  horizontal scroll exists. Verified false positive (the script's geometry
  check doesn't walk up for a clipping ancestor); no fix applied.
- Applying SKILL.md passes 2–6 (not just re-running scripts) surfaced four
  more real findings the mechanical tools don't check for directly:
  1. **HIGH, 1.1.1** — fetched the other 3 photographs' source images
     directly and found 2 more alt-text mismatches beyond the one caught in
     Round 1: the wedding photo (an outdoor ceremony aisle) was captioned
     as "a set table"; the ateljékvällar photo (a finished tulip bouquet in
     a jar) was captioned as "hands binding stems." Both rewritten to
     describe what's actually shown.
  2. **MEDIUM, 1.3.1** — `.hours-table` had scoped row headers but no
     `<caption>`. Added `<caption class="sr-only">Öppettider</caption>`.
  3. **MEDIUM, 2.4.6/1.3.1** — the "Besök oss" close section had no heading
     at all (address was a plain `<p>`). Promoted to `<h2>` — zero visual
     change, since styling is class-based, not tag-based.
  4. **MEDIUM, 1.4.4 (spirit)** — 10 selectors sitewide set `font-size` in
     raw px (10/10.5/11/12px). Converted to rem equivalents so these labels
     scale with a user's base font-size preference, not just page zoom
     (which already passed reflow.py's 200% check).

Full findings table with Before/After/Why/WCAG/Who and coverage table:
`round2-audit.md`. **Verdict: Approve** — both HIGH and all four MEDIUM
findings fixed and reconfirmed; the two remaining `reflow.py` flags are
documented false positives, not silently dropped; `forced-colors` and
actual-AT testing are marked "not verified" rather than assumed clean.

**Final capture**: `final/` — `shoot.py` + `shoot_slices.py … p 8`, all 8
slices read. Confirmed: darker kicker/meta/dt labels, the enlarged knot,
the recropped hero panel (daisies now dominate over sky), all 3 wed-facts
visible together at the same mid-scroll frame that used to show only 1,
and both the caption and h2 changes are visually silent as intended.

**Reveal/scroll rules** (10-line Playwright check, `page.on('console')` +
a post-load DOM check, 1440×900, 1200ms wait matching `shoot.py`):
- Every `[data-reveal]` / `.split__figure` element carries `is-revealed` at
  capture time — **0 elements left un-revealed**.
- **0 console messages**, **0 `[scrollcraft]` warnings** (expected — this
  page never loads the vendored scroll-choreography engine at all, per its
  own header comment's MOTION ENGINE NOTE).

---

## Net changes to `index.html` across both rounds

- New token `--korall-onlight` (measured 5.67:1 on fog), applied to 3
  small-text selectors.
- Hero right-panel image: corrected alt text + crop reframe.
- Vow-knot: enlarged + thickened.
- Reveal system: immediate-reveal threshold `×1.1 → ×3.0`; ledger stagger
  transition `1.2s/90ms-steps → 0.5s/40ms-steps`; wed-facts thresholds
  `0.15/0.4/0.65 → 0.05/0.12/0.20`.
- 2 more alt-text corrections (wedding, ateljékvällar photos).
- New `.sr-only` utility + `<caption>` on the hours table.
- `.close-address` promoted from `<p>` to `<h2>`.
- 10 selectors' `font-size` converted from px to rem.

Deliberately left unfixed (named, not silently dropped — see
`round1-critique.md` P3 and `round2-audit.md`'s LOW rows): heading
line-height 0.98; the static non-sticky nav bar (explicit registry-
fingerprint decision); the hero-plate's 88%-opaque scrim under
`prefers-reduced-transparency`; no `prefers-color-scheme` fork; the
Fraunces "overused font" warning.
