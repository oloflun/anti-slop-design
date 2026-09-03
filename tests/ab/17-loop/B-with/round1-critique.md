# Round 1 critique — Florhuset Majorna (B-with/index.html)

Inputs read: `round1-before/p--s00.png` through `p--s07.png` (viewport slices,
1440x900, covering the full 6741px page) and the fold screenshot. Direction:
lane "Sea-fog botanical ledger", register editorial print, grammar
gallery/catalog (per the file's own header comment — no separate `DESIGN.md`
exists for this test page, so brand consistency is scored against that
stated lane, not invented). The Colour dimension is backed by measured
contrast, computed directly from the page's own OKLCH token values
(`_oklch_contrast.py`, Björn Ottosson OKLab→linear-sRGB matrices, WCAG
relative-luminance formula) — not eyeballed.

## 1 · Hierarchy — minor

- **Entry point / eye flow**: hero h1 is the clear dominant element, matches
  the primary goal (same-day-binding promise); gallery/catalog scan order
  (hero → ledger → wedding → subscription → ateljé → close) reads as a
  deliberate walk, no dead ends. Pass.
- **Weight**: size differential between hierarchy levels clears 1.5x
  throughout (hero h1 vs body, ledger name vs desc). Pass.
- **Emphasis — problem**: the page's own feeling-curve doc names act 3
  (Bröllop) as the peak and the vow-knot as the signature move meant to carry
  it. In `p--s02`–`p--s04` the knot renders as a thin (2.4px stroke),
  small (clamp 9–14rem viewBox) coral scribble pinned to the right edge —
  next to a full-bleed photograph and a large headline it reads as
  incidental, not as the page's stated emotional peak. The single primary
  emphasis zone in that frame is still the headline/CTA block on the left;
  the knot does not yet earn co-equal billing.

## 2 · Composition — major

- **Balance — problem (major)**: the hero diptych's two panels claim equal
  50% columns, but they do not carry equal visual weight. Left panel
  (`photo-1487530811176`) is a dense floral macro edge-to-edge. Right panel
  (`photo-1574684891174`) is a daisy field shot from below — roughly the top
  two-thirds of that panel is near-uniform blue sky (confirmed by fetching
  the source image directly, not just the crop). This is the squint-test's
  named failure mode: an open column carrying less visual weight than its
  width claims — a hole, not a rail.
- **Alt-text accuracy — problem (feeds P2 below)**: that same image's alt
  text reads "Snittblommor och gröna blad utlagda för binderi, sett rakt
  uppifrån mot ett arbetsbord" (cut flowers laid out for binding, shot from
  directly above onto a work table). The actual photograph is a daisy field
  against open sky, shot from below. The alt text does not describe what is
  on screen — this compounds the visual-weight problem, it isn't a separate
  coincidence.
- **Whitespace / rhythm / gestalt**: macro section padding (`clamp(4rem,
  9vw, 8rem)`) and micro-spacing off the `--sp-*` scale are consistent
  throughout; hairline rows uniform. Pass.
- **Three-flat-text-sections check**: hero (image) → ledger (numbered list)
  → wedding (photo) → subscription (text + giant counter) → ateljékvällar
  (split image/text) → close (dark panel + table). No three consecutive
  plain-text sections. Pass.

## 3 · Typography — minor

- **Scale usage / token compliance**: every size traces to a `clamp()` step
  built off the declared tokens; no raw improvised value spotted in the
  captured screenshots. Pass.
- **Readability — observation**: heading `line-height: 0.98` is tighter than
  the register's own ~1.1 guidance. In `p--s00` the 4-line hero h1 is legible
  and not colliding, so this is a minor observation rather than a break —
  flagged as P3, not required this round.
- **Consistency**: kickers / ledger meta / split-list `dt` all share one
  mono treatment. Pass.

## 4 · Colour — major (measured)

Measured pairs (own token OKLCH values, WCAG contrast formula):

| Foreground | Ground | Ratio | Role | Verdict |
|---|---|---|---|---|
| korall `oklch(60% .17 32)` | fog `oklch(95% .014 200)` | **3.71:1** | `.kicker`, `.ledger__meta`, `.split__list dt` — 10.5px mono, not bold | **Fails AA** (needs 4.5:1 at this size) |
| korall | natt-2 (hero plate, ~88% natt mix) | 3.83:1 | hero accent-word, large display text | Passes (>=3:1 large-text floor) |
| korall | natt (wed-copy scrim) | 4.31:1 | wedding accent-word, large display text | Passes |
| stone `oklch(38% .016 210)` | fog | 8.64:1 | body copy / ledger desc | Passes, wide margin |
| ink `oklch(20% .02 215)` | fog | 15.66:1 | primary text | Passes |
| dis `oklch(80% .02 205)` | natt | 9.91:1 | on-dark kicker / body | Passes |
| fog | natt | 15.96:1 | hero h1 on dark plate | Passes |
| dis | natt-2 | 8.82:1 | hours table / close-foot | Passes |

- **Problem**: every small (10.5px, regular-weight) mono label that sets
  korall directly on the fog ground — the section kickers, the ledger's
  season meta line, the ateljékvällar `dt` labels — measures 3.71:1, under
  the 4.5:1 AA floor for text this size. This is systemic (three selectors,
  every instance on the page), not a one-off.
- **Palette coherence / semantic use / CVD**: accent stays single-hue,
  display-scale-or-price only, never a fill or a control — consistent with
  the locked token commitments. The contrast failure above also compounds
  under CVD (low luminance contrast is harder before hue confusion is even
  a factor). Pass on coherence, fail on the measured pair above.

## 5 · Affordance — pass

CTAs read as typeset links (arrow + korall underline), consistent across
all five instances, none competing (exactly one per section). Hover/
focus-visible states present and distinct; nav links and CTA links both
clear the 44px hit-area floor. Nothing load-bearing sits behind hover-only
(the pointer-tilt mark is `aria-hidden`, decorative).

## 6 · Information density — pass

Ledger's five rows (name/desc/season/price) match a catalog register's
expected load; primary value prop is above the fold and dominant; prices
are right-aligned tabular-nums for consistent scanning; nothing critical is
buried behind a disclosure.

## 7 · Brand consistency — pass

Cold fog/petrol palette and Fraunces+Space Mono pairing match the stated
lane ("Sea-fog botanical ledger," not Calyx's warm-cream default). Voice is
terse, museum-label-register Swedish, no off-register apparatus (no grain
overlay, no blanket reveal-everything script) visible in the captured
slices. Token traceability confirmed for everything scored above; full
mechanical confirmation deferred to Round 2's `detect.mjs` pass.

## Squint test

At a blur, the hairline ledger, the dark close panel, and the hero headline
all still read as distinct shapes — hierarchy survives. The one column that
fails the "does this width earn its weight" question is the hero's right
panel, per Composition above (cited once, not double-counted).

## Three-flat-text-sections contract

Not triggered — see Composition.

---

## Fix list

**P1 — Critical**
1. **Issue**: `.kicker`, `.ledger__meta`, `.split__list dt` set korall on
   fog at 10.5px/regular — measured 3.71:1, fails WCAG AA's 4.5:1 floor.
   **Dimension**: Colour. **Fix**: add a per-ground darker accent step
   (`--korall-onlight`, same hue/chroma, lower lightness — measured to clear
   AA) for these three small-text-on-fog roles, following the project's own
   "every muted tone needs a value per ground, measured twice" rule (the
   same pattern already used for `--dis` vs `--stone`). Leave the
   display-scale korall-on-dark usages untouched — they already clear the
   3:1 large-text floor.

**P2 — Important**
1. **Issue**: hero right panel image (`photo-1574684891174`) is a daisy
   field against open sky, but its alt text describes a flat-lay of cut
   flowers on a work table — factually wrong, and it also explains why the
   panel reads as visually empty next to the left panel's dense macro.
   **Dimension**: Composition (+ compounds a content-accuracy problem).
   **Fix**: correct the alt text to describe what is actually shown, and
   reframe the crop (scale/reposition, same licensed photo, no new asset)
   so the visible portion favours the flower band over blank sky — closing
   the squint-test weight gap without inventing a fifth image ID.
2. **Issue**: the vow-knot signature move (page's own stated peak) is too
   small/thin to read as the primary emphasis zone of its section.
   **Dimension**: Hierarchy. **Fix**: scale the knot-wrap and thicken the
   stroke so it holds its own against the headline and photograph, without
   creating two competing emphasis zones.

**P3 — Polish (not required this round)**
1. Heading `line-height: 0.98` is tighter than the register's ~1.1
   guidance; legible today, worth nudging toward ~1.02–1.05 in a later pass.

## Assessment

Strongest dimension is Affordance/Density: the CTA system, focus states,
hit areas and information pacing are disciplined and true to the
editorial-print register, with no card-grid or generic-pill-button
regression anywhere in the captured slices. Weakest is Colour, where a
small but real and systemic accessibility gap (accent-on-fog labels at
3.71:1, under the 4.5:1 floor) undercuts an otherwise measured palette,
compounded by a Composition problem in the hero's unequal diptych halves —
which turns out to be tied to an inaccurate alt text on the same image —
and a signature move that does not yet carry the visual weight the page's
own feeling-curve document claims for it.

## Honest reference sentence

Against Calyx (the primary structural reference), this page does not yet
beat it: Calyx's kicker/ledger apparatus ships at a resolved, measured
contrast, while this build's identical apparatus currently fails AA at
small size, and its hero column balance and signature-move weighting are
still short of Calyx's discipline. Closing the P1 and P2 items above is
what would close that gap.
