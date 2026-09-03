# `design critique`

Visual critique: the positive quality gate, judged on pixels.

Audit (`verbs/audit.md`) catches slop — named anti-patterns, structural
templates, gate violations. Critique is the other half: does this page read as
*good*, independent of whether it committed a named sin. A page can pass every
gate and still be flat, timid, or off-brand. Critique is where that gets
caught. Ported from [`upstream/designer-skills/visual-critique/`](../upstream/designer-skills/visual-critique/)
(seven `critique-*` skills + `/critique-screen`), adapted to this system's
tokens and register model in place of generic UI screens.

**Contract**
- **Reads:** the screenshots actually captured (fold, full page in slices,
  mobile 390) — `Read` each PNG so it enters context, never judge from code or
  memory. `DESIGN.md` if locked, or the tier-2 study notes / register table in
  [`house-physics.md`](../house-physics.md). The named references from Step 1b.
- **Does:** scores seven dimensions against what is on screen, each rated
  `pass` / `minor` / `major`, and runs the squint test and the composition
  contract.
- **Writes:** nothing. Critique is judgment, not code. Output is the fix list
  below, handed to a build or polish pass.
- **Human checks:** the assessment paragraph and the honest reference
  comparison are claims a reviewer should be able to verify by looking at the
  same screenshots — cite what you saw, not what a good page usually has.

---

## Inputs

Before scoring anything, confirm you actually have:

1. **The screenshots that were read** — fold (first viewport), full page in
   slices, and mobile at 390px. A dimension scored from source code instead of
   a captured, read image is not a visual critique; say so and mark it
   `not verified` rather than guessing from CSS.
2. **The direction document** — `DESIGN.md` if the project is Tier 0/locked,
   otherwise the lane phrase and register named in Step 1b/Step 2 of
   [`../../SKILL.md`](../../SKILL.md) (e.g. *"Tier 1 — warm photographic,
   deriving from the harbour-restaurant brand"*). This stands in for
   upstream's `mood.md`/`voice.md` — this system does not maintain those
   files. If neither exists, brand consistency is scored `N/A`, not invented.
3. **House physics** — [`house-physics.md`](../house-physics.md), the
   register's inventory, for what "good" looks like in this specific lane.

---

## The seven dimensions

Run in this order. For each: **Observation** (neutral, what is actually on
screen) → **Problem** (what is broken and why it matters) → **Fix** (specific,
actionable). Rate `pass` / `minor` / `major`.

### 1 · Hierarchy
- **Entry point** — one dominant element; does it match the primary goal?
- **Eye flow** — deliberate path (F/Z/register-appropriate), no dead ends.
- **Weight** — size differential ≥1.5× between adjacent hierarchy levels.
- **Emphasis** — exactly one primary emphasis zone; is it earned?

### 2 · Composition
- **Balance** — visual weight distributed on purpose, not by accident.
- **Whitespace** — macro air between sections, consistent micro-spacing.
- **Rhythm** — spacing intervals off a scale; repeated elements uniform.
- **Gestalt** — proximity, similarity, figure/ground, continuity, closure.

### 3 · Typography
- **Scale usage** — only defined steps; each step used for its role.
- **Readability** — measure capped 45–75ch; line-height by role (headings
  ~1.1, body 1.4–1.6, anything wrapping 3+ lines ≥1.4); contrast AA.
- **Consistency** — semantically equal elements share one treatment.
- **Token compliance** — every size/weight/family traces to a token, never a
  raw value improvised mid-render (gate 48, gate 59).

### 4 · Colour
- **Measured contrast pairs** — the rendered foreground against the ground it
  actually sits on, not the page background; state the ratio and the
  threshold it missed. Never report a ratio you didn't measure.
- **Palette coherence** — limited to the locked tokens; the one saturated
  accent stays at display scale, never fill on a small control.
- **Semantic use** — state never carried by colour alone; status hues
  consistent; interactive colour distinguishable from decorative.
- **CVD / forced-colours** — holds up for deuteranopia/protanopia and in a
  forced-colours environment.

### 5 · Affordance
- **Clickability** — controls read as controls; no false or missing
  affordances; hit area ≥44×44px on mobile (gate 62).
- **States** — default/hover/focus-visible/active/disabled/loading present
  and distinct; focus ring visible against its ground.
- **Single CTA** — one dominant action per view; primary filled, secondary
  ghost/outline, never two filled CTAs competing.
- **Discoverability** — nothing load-bearing hidden behind hover-only on a
  touch surface; empty states name a next action.

### 6 · Information density
- **Cognitive load** — how many decisions to complete the primary task; is
  anything present that doesn't serve it.
- **Priority** — the thing the user needs is above the fold and visually
  dominant; nothing critical buried in low-contrast secondary text.
- **Scanning pattern** — layout matches how it's actually read; labels
  aligned; numbers/dates formatted consistently.
- **Progressive disclosure** — complexity deferred where it should be,
  primary actions never hidden behind a disclosure to achieve this.

### 7 · Brand consistency
Compare against `DESIGN.md` if locked, or the named lane/register sentence
and house-physics inventory otherwise. **Never invent a `mood.md` or
`voice.md` to check against — if the project has neither a `DESIGN.md` nor a
stated lane, mark this dimension `N/A` and say why**, rather than inventing
brand rules that don't exist in this system.
- **Mood/register** — does the visual language match the named lane and the
  register table's fit (editorial print / cinematic dark / illustrated dark /
  modern clean / warm photographic / historical art)?
- **Voice** — does visible copy match the tone the lane implies; any
  off-register apparatus (kicker microformat, grain, ledgers) borrowed from a
  register this page isn't in?
- **Token compliance** — every colour/font/radius on screen traces to the
  locked tokens or Tier 1/2 derivation; no demoted-skill hex (gate 60).

---

## Our two extra checks

**Squint test.** Blur the screenshot 5px (or genuinely squint). Two
questions: does the hierarchy still read with the content gone, and **is any
column carrying less visual weight than its width claims** — a rail or a
9-column block holding only a couple of whispered lines? An open column that
fails this is a hole, not a rail; the fix is to weight it (numeral, stat,
image, full-height rule) or close it. This is Step 5 point 2 of
[`../../SKILL.md`](../../SKILL.md), applied here as a composition check
rather than a build-verification step.

**Three-flat-text-sections contract.** From the composition contract in
[`../../SKILL.md`](../../SKILL.md) and the structural section of
[`house-physics.md`](../house-physics.md): scan the full-page slices for three
consecutive sections that are all plain text blocks with no anatomy variety —
no image, no ledger, no inversion, no grid-break. Three in a row is a fail
regardless of how good any single section is individually; flag it under
Composition and name the section range.

---

## Output

**1. Prioritised fix list**, P1/P2/P3, each tagged with its dimension:

- **P1 — Critical**: breaks usability, accessibility, brand compliance, or a
  named gate; fix before shipping.
- **P2 — Important**: degrades the read or creates inconsistency; fix this
  pass.
- **P3 — Polish**: minor refinement; address when capacity allows.

Each item: **Issue** (what's wrong) · **Dimension** (Hierarchy / Composition /
Typography / Colour / Affordance / Density / Brand) · **Fix** (the specific
change).

**2. One-paragraph assessment** naming the strongest dimension and the
weakest, in plain language a reviewer could check against the same
screenshots.

**3. The honest reference sentence.** State plainly whether this page beats
every reference named in Step 1b — not "stands up beside them." If you cannot
say it beats them, say what specifically the references still do better and
tag it into the fix list. This is the Exit bar's reference claim, restated as
critique's own closing line.

**Critique never edits.** It is a read on pixels, not a rewrite. Fixes named
here are a separate pass — hand the list to `build` or `polish`
([`../../SKILL.md`](../../SKILL.md) Step 0a), don't apply them inline.
