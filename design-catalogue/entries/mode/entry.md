---
title: "Mode"
url: https://mode.com
source_url: https://mode.com
captured: 2026-09-04
origin: refero
extract: ok
category: product-focused
category2: editorial
family: sage-greenhouse-bi
dna: "Botanical-editorial SaaS canvas x tight-tracked serif display headlines"
register: modern clean
grammar: split stage
lane: "A pale sage canvas replaces sterile SaaS white behind a tightly-tracked serif headline and a documentary photo of a real team, with depth built entirely from a sage-to-forest-to-chartreuse colour stack instead of shadows"
mode: persuade
traits: ["56-96px serif display, single weight, negative tracking", "sage canvas, never pure white", "one chartreuse accent, one filled button only", "4px radius interactive, 16px radius surfaces", "zero shadow, colour-stack depth", "documentary human photography, no stock"]
palette: ["#eef2e3", "#fcfcfc", "#000000", "#043f2e", "#c8f169", "#2a6f2b"]
type: ["Grenette", "Graphik"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Mode.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. Pale sage `#eef2e3` replaces the default SaaS white as the page canvas,
with true white (`#fcfcfc`) reserved strictly for elevated cards — a distinction
the source calls out as deliberate, not a fallback. Depth is built from a
three-layer colour stack (sage → forest → chartreuse) rather than shadow: each
layer is both a surface and a hierarchy signal, so "how dark is this section"
doubles as "how important is this content."

Grenette, a custom serif, is locked to display sizes 36px and above at a single
weight (400) with aggressive negative tracking that intensifies with scale
(-0.72px at 36px down to -2.98px at 96px) — the source is explicit that this
serif/sans contrast at large sizes is the signature and must never be broken by
setting Graphik at display size instead. Graphik itself is reserved for
everything functional, with positive tracking (0.06em) turning small uppercase
text into eyebrow labels.

Chartreuse `#c8f169` is fenced to exactly one job: it is "the only filled button
color in the system," never a decorative wash, never a second accent alongside
Vivid Green (which is fenced off in turn to data-visualization only). Combined
with a strict two-radius rule (4px for every interactive control, 16px for every
card and large surface, nothing between), the whole interface reads as warm and
intellectual rather than corporate — "BI without the corporate coldness," as the
source puts it.

## What to borrow (principle)

- **Replace default white with a warm, named canvas colour.** Distinguishing
  "page background" from "elevated card background" with two different near-
  white values gives elevation meaning without a shadow.
- **Lock a serif to a strict size floor, one weight only.** Grenette never
  appearing below 36px, and never bolding, keeps the serif's "editorial
  authority" from being diluted into a body-text role it can't carry.
- **Increase negative tracking with size, not just leading.** Progressive
  tightening (-0.72px to -2.98px) is what keeps a 96px serif headline from
  reading as merely stretched.
- **Fence the single accent colour to one component type.** Chartreuse existing
  only as the filled-CTA background — never a wash, never a second badge colour
  — keeps the "singular chromatic punctuation" claim actually true.
- **Split radius into exactly two values by role.** 4px for anything clickable,
  16px for anything that contains — an easy, auditable rule with no exceptions.

## What to leave

- A dedicated data-visualization-only accent (Vivid Green) alongside the primary
  action accent (Chartreuse) is a subtle distinction that's easy to blur under
  product pressure — a chart accidentally reusing the CTA colour would break the
  "one accent, one job" contract silently.
- Grenette's display-only restriction (never below 36px) requires genuine
  editorial discipline in a growing product; feature teams will be tempted to
  reach for the serif at smaller sizes for "brand feel" and need a firm no.
- The photography rule — "documentary, human, never staged stock" — is a real
  production cost; a team without access to genuine team photography will
  default to stock that breaks the register immediately.

## Signature move

The forest stat card: a Deep Forest `#043f2e` card holding a single large metric
(e.g. "8.2K") in Paper White, with its label set in Chartreuse — the one place
the accent colour is used as text rather than a fill, and the densest, most
information-forward card in an otherwise airy system.

## Motion

(from designlang extract) Feel reads as springy, correcting the earlier "no
motion tokens" read — this is a genuinely animated product page. A plain `ease`
curve carries the bulk of interactions (102 uses) across five duration steps
from 150ms to 1s, but a true spring/overshoot curve, `cubic-bezier(0.75, 0,
0.29, 1.01)`, also appears (3 uses) — the source of the "springy" feel rating,
most likely on a card or button press-state. A `scroll` keyframe (slide-x
transform, 2 uses) drives at least one horizontally-scrolling strip, separate
from the third-party Calendly-widget bounce keyframe also present in the
stylesheet (not brand motion). (observed in capture) the live capture shows a
dismissible top announcement banner and a hero composed of overlapping sage and
forest card shapes; the primary CTA's documented hover behaviour (chartreuse
darkening toward Forest Mid) is a colour shift, not movement — consistent with
depth staying in the colour stack even while other elements on the page do move.

| Token | Value | Easing |
|---|---|---|
| xs | 150ms | `ease` |
| sm | 200ms | `ease` |
| md | 350ms | `ease` |
| lg | 500ms | `ease` |
| xl | 1s | `ease` |
| spring/overshoot | — | `cubic-bezier(0.75, 0, 0.29, 1.01)` |

## Brief

Build a business-intelligence product marketing page. Canvas is pale sage
`#eef2e3` — never pure white; elevated cards and the nav bar use paper white
`#fcfcfc`. Deep Forest `#043f2e` carries dark sections and stat cards; Chartreuse
Lime `#c8f169` is the only filled-button colour in the entire system, with Forest
Mid as its hover state. Set every headline 36px and above in Grenette serif,
weight 400 only, tracking tightening from -0.72px at 36px to -2.98px at 96px;
keep Graphik for all body, nav, and UI text, with 0.06em positive tracking on
uppercase eyebrow labels. Radius is either 4px (buttons, inputs, tags) or 16px
(cards, images, stat blocks) — nothing between. Open with a two-column hero: a
Grenette headline plus a Deep Forest stat card on one side, a sage-matted
documentary photograph of a real team on the other, a filled chartreuse "Try for
free" button paired with a ghost "Request demo" button. Alternate sage and white
section bands with 56-80px gaps below. No box-shadow anywhere — depth comes only
from the colour stack.

## Image recipe

Documentary photograph of [SUBJECT] — real people at desks or collaborating over
screens, candid unstaged body language, warm natural window light, genuine office
or workspace setting, no posed corporate stock composition, no colour overlay or
duotone treatment, presented uncropped within a 16px-radius sage-matted frame.

## Photo search

Unsplash first, Pexels second.
- "team collaborating desk candid natural light"
- "coworkers reviewing screen office documentary"
- "data analyst workspace candid"
- "colleagues meeting table natural light"

## Reference lock

Primary reference/direction: Mode — botanical-editorial BI product page, tight-
tracked serif display, single chartreuse accent on a sage/forest colour stack.
Preserve (3-5 traits): pale sage `#eef2e3` canvas distinct from paper-white
`#fcfcfc` elevated cards; Grenette serif locked to 36px+ at weight 400 only,
tracking tightening with size; Chartreuse `#c8f169` as the sole filled-button
colour, never a decorative wash; radius fixed at 4px (interactive) or 16px
(surfaces), nothing between; zero box-shadow, depth from the sage → forest →
chartreuse colour stack only.
Borrow only (1-2): the Deep Forest stat card with chartreuse label text; the
dismissible top announcement banner pattern.
Role rules: Grenette never sets text below 36px or above weight 400; Vivid Green
stays confined to data-visualization, never a UI accent; more than one
chromatic accent never appears in a single viewport.
Media strategy: photo:unsplash — warm, candid, documentary workplace photography
only; no staged stock, no duotone or colour-overlay treatment.
Reject: pure white as page background; a bold or italic Grenette headline; a
second filled-button colour; box-shadow on any card or button; radius values
outside {4px, 16px}.
Token commitments: bg `#eef2e3`, card `#fcfcfc`, accent `#c8f169`, accent-hover
`#2a6f2b`, dataviz `#78c51c`, ink `#000000`, forest `#043f2e`; display Grenette
400 at 36-96px/leading 0.90-1.10/-0.72px to -2.98px tracking; body Graphik
400-600 at 12-18px; radius 4px buttons/inputs/tags, 16px cards/surfaces; page
max-width 1200px, section gap 56-80px.
