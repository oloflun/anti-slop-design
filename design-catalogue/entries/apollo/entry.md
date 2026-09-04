---
title: "Apollo"
url: https://apolloworkspace.com
source_url: https://apolloworkspace.com
captured: 2026-09-04
origin: refero
extract: ok
category: hospitality
category2: editorial
family: brick-atelier-membership
dna: "Golden-hour brick photography x print-brochure membership copy"
register: warm photographic
grammar: chaptered editorial
lane: "A full-bleed golden-hour photograph of members walking through a brick archway carries an engraved whisper-thin serif wordmark, then the page settles onto a cream canvas of sharp 3px-radius, hairline-ruled two-column chapters"
mode: persuade
traits: ["47px engraved-thin serif hero", "3px radius everywhere, no pill buttons", "warm linen canvas, never white", "terracotta accent rationed to borders", "golden-hour lifestyle photography only", "uppercase wide-tracked section kickers"]
palette: ["#3c261c", "#e97451", "#4a43dd", "#f9f8f0", "#dddedf", "#fcede8"]
type: ["paradigm-pro", "MonaSans"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Apollo.md
raw: raw/d211379dfcd10faf-apolloworkspace-com.webp
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. Warm linen `#f9f8f0` stands in for white across the entire canvas, and
espresso `#3c261c` stands in for black — a page-wide warm shift that makes the
golden-hour brick photography feel like it belongs to the same light as the UI,
rather than sitting on top of a colder digital frame. Terracotta `#e97451` is
rationed hard: primary-action borders, the active nav underline, and the logo
monogram, never a filled surface — the "Do" list is explicit that it must never
become a large fill.

The typographic tension is the same whisper-vs-workhorse move seen across this
family of editorial sites: paradigm-pro at weight 300 only, used purely for the
hero display and a handful of brand-voice headings, against MonaSans's uppercase,
wide-tracked (0.07-0.1em) workhorse voice for everything structural — nav, section
kickers, body. The serif is deliberately restricted to 36-47px so it never has to
carry small text, which is where an ultra-light weight would fail.

A flat 3px radius on literally every interactive element and image — buttons,
cards, photos, inputs — rejects SaaS pill-button softness outright. Combined with
zero shadows and Ash Mist hairlines as the only structural device, the page reads
as a printed membership brochure rather than a software product, which matches the
brief: a physical, curated workspace, not a tech tool.

## What to borrow (principle)

- **Shift every neutral warm, uniformly.** Replacing both white and black with a
  single warm-shifted pair (linen, espresso) makes golden-hour or warm-toned
  photography read as native rather than composited.
- **Cap radius at one small value across every element type.** 3px everywhere —
  buttons, cards, images — rejects the "soft SaaS" register on sight and reads as
  print instead.
- **Ration the accent to structural marks only.** Terracotta on borders and
  underlines, never as a fill, keeps a warm accent from tipping into "loud."
  colour.
- **Reserve the display serif for a narrow size band.** Locking a whisper-weight
  face to 36-47px only avoids the legibility failure that comes from setting an
  ultra-light weight small.
- **Let uppercase wide-tracked kickers do the "magazine" work.** A 12px kicker at
  0.1em tracking above every section heading reads as an editorial index, not a
  UI label.

## What to leave

- Iris Ink `#4a43dd` as a "decorative headline only" colour is a fragile rule —
  one accidental reuse in body copy or a link would immediately read as a bug, not
  a feature, since it has no other role in the system.
- 3px radius on every element, including images, is a hard constraint that will
  visibly clash with any borrowed component using pill or fully-rounded geometry.
- The single architectural illustration described in the source (a painted
  building facade) is a bespoke, one-off asset — it isn't a repeatable pattern and
  shouldn't be treated as a template for future imagery.

## Signature move

The engraved-serif hero: paradigm-pro weight 300 at 47px with 0.08em positive
letter-spacing over a darkened full-bleed photograph — spaced out enough, and thin
enough, that the wordmark reads as etched into the image rather than typeset on
top of it.

## Motion

(from designlang extract) Feel reads as mixed, and the page is scroll-linked —
correcting the earlier read that no motion system exists. Two easing families do
distinct jobs: a standard `cubic-bezier(0.4, 0, 0.2, 1)` curve (25 uses) covers
colour, border and gradient-stop transitions at 150ms; a slower, named
"ease-editorial" curve `cubic-bezier(0.22, 1, 0.36, 1)` (3 uses) covers the same
properties at 300ms, giving hover/link states a softer, more decelerated finish
than plain UI chrome gets. A `max-height` transition at 300ms on the fast curve
points to at least one accordion/reveal panel. No keyframe animations are defined —
consistent with the flat, shadow-free print-brochure register, motion here lives
entirely in property transitions, not choreographed sequences. (observed in
capture) the flat 3px-radius system with no shadows and generous 68px section gaps
is consistent with simple crossfades between the hero photograph and the cream
content sections, with alternating text-left/image-right two-column reveals on
scroll rather than parallax.

| Token | Value | Easing |
|---|---|---|
| xs (UI chrome) | 150ms | `cubic-bezier(0.4, 0, 0.2, 1)` |
| md (reveal / accordion) | 300ms | `cubic-bezier(0.4, 0, 0.2, 1)` |
| md (editorial hover) | 300ms | `cubic-bezier(0.22, 1, 0.36, 1)` "ease-editorial" |

## Brief

Build a boutique-workspace membership page. Canvas is warm linen `#f9f8f0`
throughout — never pure white; ink is espresso `#3c261c` — never pure black.
Terracotta `#e97451` appears only on button borders, the active-nav underline and
the logo monogram. Cap every radius at 3px: buttons, cards, images, inputs alike.
Open full-bleed on a golden-hour lifestyle photograph with a dark Espresso nav bar
overlaid, an uppercase MonaSans eyebrow label, a paradigm-pro weight-300 hero
wordmark at 47px/0.08em tracking, and a ghost-outlined CTA. Below the hero, run
alternating two-column chapters (text ~40% width, photography ~45%, generous
gutters) with a MonaSans uppercase kicker, a MonaSans uppercase section heading,
18px body copy, and terracotta-dot bulleted feature lists. Keep 68px vertical gaps
between chapters and no shadows anywhere; Ash Mist `#dddedf` hairlines are the only
structural divider.

## Image recipe

Documentary lifestyle photograph of [SUBJECT] — people walking or working through a
warm brick or masonry setting, shot in genuine golden-hour light with long shadows
and warm highlight falloff, candid unposed body language, natural depth of field
with the background softly out of focus, no studio lighting, no cool colour
temperature anywhere in the frame.

## Photo search

Unsplash first, Pexels second.
- "golden hour brick archway people walking"
- "coworking space warm natural light interior"
- "entrepreneurs walking city street candid"
- "workspace desk warm afternoon light"

## Reference lock

Primary reference/direction: Apollo — golden-hour membership-brochure workspace
page, engraved whisper-thin serif hero, terracotta rationed to structural marks.
Preserve (3-5 traits): warm linen `#f9f8f0` canvas and espresso `#3c261c` ink,
never pure white or black; 3px radius on every element without exception; terracotta
`#e97451` restricted to borders, underlines and the monogram, never a fill;
paradigm-pro weight 300 restricted to 36-47px display only; Ash Mist `#dddedf`
hairlines as the sole structural divider, no shadows.
Borrow only (1-2): Iris Ink `#4a43dd` for a single brand-voice display heading; the
one painterly architectural illustration as a rare hand-crafted accent.
Role rules: terracotta never becomes a large fill; the display serif never sets
body text or UI labels; uppercase 0.07-0.1em tracking applies to all section
kickers and nav, never to body copy.
Media strategy: photo:unsplash — candid, golden-hour lifestyle photography of
people and brick/masonry interiors only; no studio product shots, no cool lighting.
Reject: pill buttons or radius above 3px on any element; drop shadows; Iris Ink in
body text or links; more than one accent colour active in a single view.
Token commitments: bg `#f9f8f0`, hairline `#dddedf`, accent `#e97451`, decorative
`#4a43dd`, ink `#3c261c`, hover-warm `#fcede8`; display paradigm-pro weight 300 at
36-47px/leading 0.95-0.97; body MonaSans 400 at 18px/leading 1.55; uppercase
kickers 0.07-0.1em tracking; radius 3px universal; page max-width 1200px, section
gap 68px.
