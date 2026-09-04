---
title: "Beautiful™"
url: ""
source_url: ""
captured: 2026-09-04
origin: refero
extract: none
category: consumer-brand
category2: editorial
family: sunday-kitchen-cream
dna: "Domestic Sunday-morning lifestyle photography x rationed coral punctuation"
register: warm photographic
grammar: chaptered editorial
lane: "A cream-canvas kitchen-goods page where black-outlined pill nav and circular category icons float over warm product photography, one coral pill button per screen, and a single full-bleed coral banner interrupts the page once as its only loud moment"
mode: persuade
traits: ["cream canvas, never white", "one coral accent, one use per viewport", "999px pill buttons only", "1px black hairline as sole border language", "centred serif logo lockup", "tracked-out mono eyebrow labels"]
palette: ["#fff5e6", "#fa7864", "#dc8264", "#000000", "#e8e8e1", "#ffffff"]
type: ["GascogneTS", "Basis Grotesque Pro"]
kind: reference-style
source: anton
status: ready
refero: processed/Beautiful.md
---

## Why it works

Palette and type are read from Refero's extracted tokens. Cream linen `#fff5e6`
replaces white as the canvas everywhere — hero, about section, category row,
footer — which is what makes this read as a kitchen rather than a storefront
before a single product loads. Coral `#fa7864` is rationed to a strict "one moment
per viewport" rule: the filled hero button, the single full-bleed banner strip, and
nothing else. Every other surface stays black-on-cream, so the coral reads as
punctuation rather than branding-by-repetition.

Type performs the familiar editorial-vs-workhorse split, but with an inverted
tracking rule that is the real signature: Basis Grotesque Pro opens its
letter-spacing as size increases (0.019em at small sizes up to 0.031em at 21px),
which is the opposite of how most grotesques tighten at body size — the effect is
a calm, unhurried reading rhythm that matches the "warm kitchen" brief. GascogneTS
carries the editorial voice at weight 500 only, never bold, so emphasis always
comes from the serif switch or a size jump, never from weight.

Geometry enforces the same discipline as colour: buttons are always a full 999px
pill, cards are always 0px (square, borderless, defined only by the photography
inside them), and every interactive container gets a 1px black hairline instead of
elevation. That two-value radius system — pill or square, nothing between — keeps
"clickable" and "content" visually distinct without needing shadow to do the job.

## What to borrow (principle)

- **Cap a rationed accent to a literal one-per-screen rule.** "One coral moment per
  viewport maximum" is concrete enough to audit and keeps an accent from creeping
  into decoration.
- **Invert the tracking convention on purpose.** Opening letter-spacing as size
  grows (instead of the usual tightening) is a small, checkable choice that reads
  as calm rather than default.
- **Split radius into exactly two values tied to function.** Pill = clickable,
  square = content. No third radius value muddies the signal.
- **Let the black hairline replace both border and shadow.** One line weight
  (1px, pure black) doing all of nav, cards, and icon-circle duty keeps the system
  legible at a glance.
- **Centre the logo, flank it with function.** A dead-centre wordmark with nav
  pills on one side and utility icons on the other reads as considered rather than
  a default flex-row header.

## What to leave

- A 0px card radius paired with no border and no shadow means the product
  photography itself has to carry all the visual weight of "this is a card" —
  weak or inconsistent photography would collapse the grid instantly.
- The single coral banner strip depends on being genuinely singular; a second
  large coral surface anywhere else on the page would break the "exclamation
  point" reading described in the source.
- Positive letter-spacing at every body size is a deliberate anti-convention that
  will read as merely "loose" rather than "calm" without the warm cream canvas and
  serif pairing supporting it.

## Signature move

The coral banner strip: one full-bleed `#fa7864` band, roughly 120px tall, carrying
only centred white serif text with no padding container — the single large coral
surface on the entire page, positioned as a hard divider between the category grid
and the footer.

## Motion

No motion or interaction tokens are captured in the Refero export — the system is
described entirely in static component and layout terms. Inferred from the image
and the "flat, borderless-from-shadow" elevation philosophy: hover states most
likely swap the 1px black border to a filled black background (matching the
existing "quietest interactive elements" language for nav pills), and the hero
carousel arrows suggest a simple slide transition between hero images rather than
a scroll-driven or parallax effect. (inferred)

## Brief

Build a warm domestic kitchen-goods landing page. Canvas is cream linen `#fff5e6`
everywhere — never pure white; borders are 1px solid black on every interactive
element (nav pills, category circles, carousel arrows); cards have 0px radius and
no border, letting the product photography define the edge. Reserve coral `#fa7864`
for exactly one filled pill button per screen and the single full-bleed banner
strip; use terracotta `#dc8264` for outlined secondary CTAs. Centre a GascogneTS
serif logo in the header, flanked by black-bordered nav pills on the left and a
plain search icon on the right. Open with an asymmetric hero: 60% product
photography, 40% copy stack — tracked-out coral mono eyebrow label, GascogneTS
weight-500 headline at up to 52px, body copy in Basis Grotesque Pro with positive
letter-spacing, then one coral pill button. Add a horizontal row of circular
category icons (999px radius, black hairline) below. Keep 64px section gaps and no
shadows anywhere.

## Image recipe

Warm still-life or lifestyle photograph of [SUBJECT] — staged on a wooden
countertop or against a soft neutral wall, natural directional window light (not
studio-flat), styled with linen textiles and fresh botanicals or scattered
ingredients, high-key and slightly desaturated toward warm cream tones, no sterile
white-cyc background, no harsh flash.

## Photo search

Unsplash first, Pexels second.
- "kitchen countertop natural light warm styling"
- "ceramic kitchenware wooden counter lifestyle"
- "breakfast table linen natural light"
- "woman kitchen morning candid warm light"

## Reference lock

Primary reference/direction: Beautiful™ — warm cream kitchen-goods page, rationed
coral accent, editorial serif over a calm-tracked grotesque.
Preserve (3-5 traits): cream linen `#fff5e6` canvas everywhere, no pure white
background; coral `#fa7864` limited to one filled button and the single banner
strip per page; 1px solid black hairline as the only border/structure device, no
shadows; 999px pill radius on every button and icon circle, 0px on every card;
positive, size-scaling letter-spacing on all Basis Grotesque Pro text.
Borrow only (1-2): the tracked-out coral uppercase mono eyebrow label; the
handwritten signature sign-off as a humanizing one-off.
Role rules: coral never becomes a background surface outside the single banner;
GascogneTS never sets body copy or UI labels; Basis Grotesque Pro never goes bold;
logo stays centred, never flush-left.
Media strategy: photo:unsplash — warm, natural-light domestic still life and
lifestyle photography only; no studio white-cyc product shots, no 3D renders.
Reject: a second saturated accent colour; sharp corners on any clickable element;
drop shadows or elevation; bold body text; a left-aligned or asymmetric logo
lockup.
Token commitments: bg `#fff5e6`, divider `#e8e8e1`, card `#ffffff`, ink `#000000`,
ink-soft `#282828`, accent `#fa7864`, accent-outline `#dc8264`; display GascogneTS
weight 500 at 25-52px/leading 1.0-1.2; body Basis Grotesque Pro 400 at 10-21px with
0.019-0.031em tracking; radius 999px buttons/circles, 0px cards; page max-width
1200px, section gap 64px.
