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

## A/B isolation — how this verb is run

Ported from impeccable `critique.md` § Hard Invariants. The seven dimensions
below are one of two assessments, not the whole verb.

- **Assessment A — design review.** The dimensions, the squint test, the
  composition contract, the personas. Judged on the read images.
- **Assessment B — detector and browser evidence.**
  `node ~/.agents/skills/impeccable/scripts/detect.mjs --json <target>` plus
  what the rendered page actually reports (console errors, failed requests).

**Both are required, and they run as two isolated sub-agents whenever a Task
tool exists.** *"Running them inline in this context is 'possible' but is NOT
permitted; it is a degraded run."* The reason is stated in the same file and it
is the point of the whole arrangement: *"Assessment A must finish before
detector findings enter the parent synthesis context. Detector output is
deterministic, but it still anchors judgment."* A critic who has already read a
list of 14 mechanical findings will write a critique shaped by that list.

**The banner is not optional.** If A and B ran in one context for any reason,
the report's first line is:

```text
⚠️ DEGRADED: single-context (<reason>)
```

*"A silent degraded critique is a failed critique."* A dual-agent run declares
itself the same way: `Method: dual-agent (A: <agent-id> · B: <agent-id>)`.
A skipped detector is a failed run unless `detect.mjs` is missing or crashes
after a real attempt.

**Synthesis is weaving, not concatenation.** Say where the read and the detector
agree, where the detector caught what the read missed, and where a detector
finding is a false positive in this context.

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
- **Balance** — visual weight distributed on purpose, not by accident. Is the
  composition symmetrically or asymmetrically balanced, and *is the choice
  intentional*? Are heavy elements (dark fills, large images, dense text)
  offset by lighter ones? Does the layout tip — top-heavy, bottom-heavy,
  left-leaning? Is there a clear visual centre of gravity?
- **Whitespace** — macro air between sections, consistent micro-spacing. Does
  the whitespace *guide* attention, or does it fragment the layout into
  disconnected areas?
- **Rhythm** — spacing intervals off a scale; repeated elements uniform.
  Variety without chaos: a balance of repetition and differentiation, with
  section breaks that create a legible page cadence.
- **Gestalt** — proximity, similarity, figure/ground, continuity, closure.
  Related elements close together *and* unrelated ones clearly separated;
  elements that share a function share a treatment; alignment and flow lines
  lead the eye through the composition.
- **Anti-centre** — at a declared variance above 4 (the BRIEF.md dial), a
  centred hero or centred H1 section is a finding, not a preference. The
  alternatives upstream names are split-screen 50/50, left-aligned content with
  a right-aligned asset, asymmetric whitespace, or a scroll-pinned structure.
  Override: *"centered hero is OK for editorial / manifesto /
  launch-announcement briefs where the message itself is the design"* — which
  is the same carve-out gate 6's genre note already makes. This is the
  measurable form of "never converge": count the centred axes, don't intuit
  them.
- **Cohesion** — *"the overall composition feels cohesive — like one designer,
  not a committee."* Scan the full-page slices for the giveaway: three sections
  that each look like a competent solution to their own problem and share no
  spacing rhythm, no rule weight, no heading pattern.

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
  anything present that doesn't serve it. Score the eight-item checklist below.
- **One primary action** — *"One primary action per screen. If everything is
  important, nothing is."* (designpowers `cognitive-accessibility`.) A view with
  two equally weighted primary actions has not decided what it is for.
- **No hostile timing** — *"timed actions are hostile."* A countdown, an
  auto-advancing carousel that moves the thing being read, a session that
  expires mid-form: if a timeout is genuinely necessary, it warns before it
  expires and allows extension.
- **Input is preserved** — *"if a form submission fails, do not clear the
  fields."* Clearing a form on error is the single most expensive small defect
  a page can carry, because it converts one mistake into abandonment.
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

## Our extra checks

**Skeleton test.** From impeccable `bolder.md`: *"Strip the copy out of your
planned section and study the bare structure. Does the skeleton still say what
this section is and why it matters, through hierarchy and the system's devices
alone? If it only works once the words return, the boldness is in the text
size, not the design."* Run it on any section scored flat. The upstream
addendum matters as much as the test: *"a placeholder for an image or artifact
names a job, an anchor and a piece of evidence, not a cue to drop in a
decorative photo."*

A section that fails the skeleton test is usually one that *"quietly opts out of
the system's own strongest moves"* — the page has a motif, a display scale and a
structural device, and this section uses none of them. That diagnosis routes to
`bolder`, and the fix is amplification in the system's own vocabulary, never a
new colour, face, or primitive. Name the route in the fix list.

**Three litmus tests.** Image, card, brand — full text in
[`slop-test.md`](../slop-test.md) § Three litmus tests. The builder runs them on
their own output; here they are scored. Image test failures land under
Composition, card test failures under Composition, brand test failures under
Brand consistency. A litmus failure is at least P2: it means an element is on
the page carrying nothing.

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

## Common failure patterns per dimension

The upstream `critique-*` skills each close with a short list of what actually
goes wrong in that dimension. They were dropped in the first port; restored
here verbatim, 33 patterns across the seven dimensions. Read the list for the
dimension you are scoring *before* writing the observation — a named pattern is
a finding you can cite, and "the spacing feels off" is not.

**Hierarchy** — multiple competing primaries, nothing reads as most important ·
hierarchy flattening, levels too similar in size, weight or colour · false
emphasis, decorative elements outweighing functional ones · buried CTA, the
action visually quieter than the content around it.

**Composition** — equal-weight two-column layout with no clear
primary/secondary split · inconsistent padding, some components at 16px, others
at 20 or 24 with no system · orphaned elements floating without proximity to
their group · overcrowded sections adjacent to empty ones, creating
unintentional visual cliffs · competing horizontal rules and dividers that
multiply without adding structure.

**Typography** — scale drift, sizes nudged by 1–2px instead of moving to the
next defined step · line-height mismatches, display sizes with body line-height
and the reverse · alignment mixing, centred headings above left-aligned body
with no intentional justification · hardcoded font sizes because the token was
not found or not updated · over-use of bold, more than two weight levels active
on one screen diluting contrast.

**Colour** — link colour failing 4.5:1 against white once the underline is
removed · error states carried in red only, with no supporting icon or label ·
placeholder text at 40 % opacity failing contrast on light surfaces · one-off
hex values outside the token system · interactive and non-interactive elements
sharing one colour treatment.

**Affordance** — ghost buttons in low-contrast contexts where the border becomes
invisible · focus rings suppressed with `outline: none` and no replacement ·
multiple filled CTAs leaving the reader unsure which to press · edit and delete
hidden behind hover, *"inaccessible on touch and invisible until discovered by
accident"* · empty states that explain nothing and offer no path forward.

**Information density** — screens that show every available metric instead of
the most actionable · detail pages that inline all related objects instead of
linking · tables with 10+ columns where 3 do 90 % of the work · forms showing
all fields at once where a multi-step flow would reduce perceived complexity ·
content-heavy onboarding front-loading explanation before the reader has done
anything.

**Brand consistency** — hardcoded values drifting from tokens over time · copy
written without consulting voice guidelines, defaulting to generic UI language ·
imagery sourced outside the brand mood reference · inconsistent radius or shadow
values across components on the same screen.

**The fast path.** When the ask is functional rather than visual — a PM-led
review, a quick loop, "does this work" rather than "is this good" — run
dimensions **1, 5 and 6 only** (hierarchy, affordance, density): the three most
likely to block task completion. Say that you ran the fast path and which four
dimensions were not scored. This is upstream's `/critique-ux`, and it is a
declared narrowing, never a silent one.

---

## Scoring: heuristics, cognitive load, personas

These three run alongside the seven dimensions and give the critique a number
that survives between rounds.

**Nielsen 0–4, with honest `n/a`.** Score all ten heuristics 0–4 in a table with
a key issue per row. *"Be honest with scores. A 4 means genuinely excellent.
Most real interfaces score 20–32 out of 40."* Heuristics **7 (Flexibility and
Efficiency)** and **10 (Help and Documentation)** may be scored `n/a` on
Persuade and Experience surfaces — landing pages, campaigns, portfolios — as may
any heuristic that genuinely cannot apply. Write `n/a` with a one-line reason
and **renormalise the total to the applicable maximum**: 24/32, not 24/40.
*"Never print /40 over a partial set."* Read the band off the percentage when
the set is partial: 90 %+ excellent, 70 %+ good, 50 %+ acceptable, 30 %+ poor.

**Cognitive load, eight items.** Score dimension 6 against this checklist and
count the failures — *"0–1 failures = low cognitive load (good). 2–3 = moderate
(address soon). 4+ = high cognitive load (critical fix needed)."*

- **Single focus** — can the reader complete the primary task without
  distraction from competing elements?
- **Chunking** — is information in digestible groups (≤ 4 items per group)?
- **Grouping** — are related items visually grouped (proximity, borders, shared
  background)?
- **Visual hierarchy** — is it immediately clear what is most important?
- **One thing at a time** — can the reader focus on a single decision before the
  next?
- **Minimal choices** — ≤ 4 visible options at any decision point.
- **Working memory** — does the reader need to remember something from a
  previous screen to act on this one?
- **Progressive disclosure** — is complexity revealed only when needed?

The ceiling behind it: *"Humans can hold ≤ 4 items in working memory at once"*
(Miller, revised by Cowan 2001). 5–7 is pushing the boundary; 8+ and readers
skip, misclick, or abandon.

**Personas, chosen by surface type.** Walk the primary action as each and report
*specific* red flags — *"name the exact elements and interactions that fail each
persona. Don't write generic persona descriptions; write what broke for them."*
On a landing page the three are **mandatory**, because upstream's selection
table names them for marketing surfaces (first impressions, trust, mobile):

- **Jordan (confused first-timer)** — icon-only navigation, jargon with no
  explanation, no visible help, ambiguous next step after an action, no
  confirmation that something worked. *"Is the first action obviously clear
  within 5 seconds?"*
- **Riley (deliberate stress tester)** — long strings, empty states, unexpected
  input, refresh mid-flow, features that look like they work and silently do
  not, error handling that leaves the UI broken.
- **Casey (distracted mobile user)** — thumb zone, state preserved across an
  interruption, slow connection, tap targets ≥ 44×44 and not crowded, heavy
  assets on every view.

Alex (power user) and Sam (accessibility-dependent) are the dashboard and
data-heavy picks; Sam's ground is covered more rigorously by
`Skill(a11y-audit)`, so cite that rather than re-deriving it here.

**Trend, not just a score.** Persist the report and read the last five runs so
the number means something:

```bash
node ~/.agents/skills/impeccable/scripts/critique-storage.mjs write "<target>" <body-file>
node ~/.agents/skills/impeccable/scripts/critique-storage.mjs trend "<target>" 5
```

Print one line after the report: `Trend for <slug> (last 5 runs): 24 → 28 → 32 →
29 → 32 (out of 40)`. When the runs used different applicable maxima, print each
score with its own denominator (`24/32 → 30/40`) and say plainly that the runs
scored different heuristic sets, so the line is not like-for-like. First run for
a slug: say so, no trend yet. This is fire-and-forget — a storage failure prints
an error and never blocks the critique.

---

## When the target is a change, not a screen

A branch, a PR, or an uncommitted diff is a different job, and three upstream
rules keep it honest. (Scope resolution itself belongs to
[`review.md`](review.md) § 1; these are the critique-side traps.)

**Read the removed side.** `removed-signals.md` lists what to look for on the
`-` side of a hunk, because a regression is invisible in the post-change state.
A row is a lead, never a finding: route it to its owner and report it only once
that owner confirms the interface got worse.

| Removed | Owner | What to check |
|---|---|---|
| `aria-label`, `aria-labelledby`, `aria-describedby`, `aria-live`, `role=` | a11y | Control or region lost its accessible name, description, or announcement |
| `alt=`, `<label`, `for=`, `scope=` | a11y | Image, field, or table cell lost its programmatic association |
| `<button>`, `<a>`, `<nav>`, `<main>`, `<ul>` replaced by `div`/`span` | a11y | Keyboard and AT behaviour traded for styling |
| `:focus-visible`, `:focus`, `outline`, `tabindex` | a11y | Focus indicator gone, or the element left the tab order |
| Logical properties swapped for `left`/`right` | layout | Direction-aware layout dropped |
| `lang=`, `dir=` | typography | Language metadata or text direction dropped |
| `text-wrap`, `line-clamp`, `overflow-wrap`, `tabular-nums`, `font-feature-settings` | typography | Text rendering, wrapping, or numeral alignment silently changed |
| A colour token swapped for a literal, or for a lighter token | colour | The rendered contrast pair may now fail; measure it |
| A user-facing string deleted or shortened | writing | A label, error, or empty state lost the information it carried |

Upstream's table carries one further row, covering two removed media features.
**F-011 (2026-09-07): the `prefers-reduced-motion` half of that row does not apply here — a build with no rm branch is correct in this system, so its removal is never a finding.**
The `prefers-contrast` half of the row stands and is routed to accessibility as
upstream has it.

Check the **equivalent replacements** before routing anything, *"or the report
fills with refactors reported as regressions"*: `aria-label` giving way to
`aria-labelledby` pointing at visible text; an explicit `role` dropped because
the element became the native equivalent; `outline` replaced by a `box-shadow`
ring that still meets the focus rule; `tabindex="0"` dropped from something now
natively focusable; a literal replaced by a token that measures the same pair; a
physical property replaced by its logical counterpart; a string moved into the
translation catalogue rather than deleted.

**Two exclusion traps under-exclude silently.** `*.lock` catches `yarn.lock` and
`Cargo.lock` but *not* `package-lock.json` or `pnpm-lock.yaml`. And `**` needs
glob magic: without it `*` never crosses `/`, so `**/dist/**` excludes
`packages/a/dist/` and misses a root-level `dist/`. Run the diff with and
without the pathspecs and confirm the count dropped by exactly the files you
named. Two exceptions stay in scope even though they look like assets: a **font
file** added or swapped is a typography change, and an **image** added to a
component is a UI and accessibility change through its `alt` and its outline.

**Hold the change to its stated intent.** Read the title, body, linked issue and
commit messages, then review whether the interface delivers what they claim.
*"This is what surfaces the incomplete change, because a surface review inspects
the states that are present, and here the point is the ones that are absent"*:

- a new variant, size, or theme applied to some states but not all — hover,
  focus, active, disabled, loading, selected;
- a new user-facing string with no entry in the translation catalogue;
- a new component with no empty, loading, error, disabled, or narrow-width state;
- a control added to one surface but not to the siblings that already carry its
  peers.

*"Do not report scope creep. Whether a change does too much is a process
question, not an interface one."*

**Evidence, not taste.** The bar for reporting is evidence; the bar for a clean
verdict is that you inspected what you claim to have inspected. *"A short report
from a real inspection beats a long one padded to look thorough."* Press hard on
the triggers, leave deliberate project choices alone — *"a density, radius, or
voice you merely disagree with is not a finding."* And keep the two sides
symmetric: **do not report a code-level finding from appearance alone, or a
visual finding from source alone** when runtime behaviour decides the result.
Every finding cites what it was read from.

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

**2. Craft gap table.** One row per element where the build and the locked
direction disagree — the format designpowers uses so a craft finding is as
checkable as a contrast ratio:

| Element | Expectation (lock / register) | Current state | Gap |
|---|---|---|---|
| [element] | [what the reference lock or register calls for] | [what is on screen] | [the specific difference] |

*"Evaluate craft, not just compliance."* The sentence upstream offers as the
model for this verdict is worth copying in shape (re-punctuated to keep gate 75
clean): *"This meets the plan requirements but the execution is flat."* Then the
defects, named: the shadows are uniform, the spacing has no rhythm, and the
colour usage does not match the restrained palette. Three named defects, one
verdict. "It doesn't feel right" is not a finding; name the gap.

If no reference lock exists for this build, say so in one line — craft is then
judged against the register table and house physics only, and the table's
Expectation column says which.

**3. One-paragraph assessment** naming the strongest dimension and the
weakest, in plain language a reviewer could check against the same
screenshots.

**4. The honest reference sentence.** State plainly whether this page beats
every reference named in Step 1b — not "stands up beside them." If you cannot
say it beats them, say what specifically the references still do better and
tag it into the fix list. This is the Exit bar's reference claim, restated as
critique's own closing line.

**Critique never edits.** It is a read on pixels, not a rewrite. Fixes named
here are a separate pass — hand the list to `build` or `polish`
([`../../SKILL.md`](../../SKILL.md) Step 0a), don't apply them inline.
