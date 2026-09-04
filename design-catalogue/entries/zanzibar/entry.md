---
title: "Zanzibar (Framer template)"
url: https://zanzibar.framer.website
source_url: https://zanzibar.framer.website
captured: 2026-09-04
origin: raw-url
extract: ok
category: portfolio
category2: institutional
family: inverted-portrait-agency
dna: "Upside-down moody portrait hero x condensed serif agency wordmark"
register: cinematic dark
grammar: split stage
lane: "A dark maroon hero holds a deliberately inverted portrait photograph beside a two-column service list, then the page drops to a cream numbered-benefits section and a deep blue-green About panel with draped fabric photography"
mode: persuade
traits: ["inverted/upside-down hero portrait", "dark maroon photographic ground", "condensed serif display wordmark", "two-column service/outcome list", "numbered benefit list with dot icons", "outline pill CTA buttons", "cream content panel with accent photography", "small four-dot logo mark"]
palette: ["#FFFAF6", "#5A6967", "#294A5F", "#100C08", "#60221B", "#D9DAD5", "#9A9992", "#795E44"]
type: ["Libre Caslon Condensed Variable", "Inter"]
measured: designlang (confirmed)
kind: reference-style
source: claude
status: ready
raw: raw/f2f19a1d109dc9f8-zanzibar-framer-website.webp
---

## Why it works

This is a Framer marketplace template ("Buy Template" badge visible in the
capture), built to sell a creative-agency layout rather than one specific
studio — worth naming since it explains why the copy is generic ("Digital
marketing," "Brand Identity," "Creative Design") while the visual system is
doing all the actual persuasion. That system's one real idea is the hero: a
moody, dark maroon-toned portrait is flipped upside down relative to the
page's reading direction, so the subject's face reads sideways against the
wordmark. It's disorienting for a beat, then reads as confident art direction
rather than a template default — the kind of single deliberate break from
convention that makes an otherwise generic layout feel considered.

Around that image, a condensed serif display face (Libre Caslon Condensed)
sets the wordmark large and quiet, while a two-column list of service/outcome
pairs runs in a plain grotesque at small size to the image's right — service
name on the left, benefit phrase on the right, both in the same weight, so the
list reads as a single considered pairing rather than a hierarchy.

Below the fold, the palette breaks completely: cream ground, a numbered
benefits list with small dot-badge icons, and one accent photograph (a
backlit cocktail glass) that has no obvious connection to a branding agency's
services — a common template tell, image chosen for mood/colour fit rather
than for content relevance. The "About us" section shifts again to a deep
blue-green ground with wind-blown fabric photography, keeping the pattern of
one new colour world and one new image per section.

## What to borrow (principle)

- **Invert or flip one hero image deliberately** as the single break from
  expected convention — used once, it reads as intentional direction; used
  as a general habit it would just read as broken layout.
- **Pair service and outcome in two aligned columns at equal weight** instead
  of a hierarchy of headline-then-description — it reads as a considered
  one-to-one mapping rather than a feature list.
- **Change ground colour and photography together at each section boundary**
  so scrolling reads as moving through distinct rooms.
- **Use a condensed serif for a wordmark at generous scale** against dark,
  moody photography — the condensed width keeps a long name from overwhelming
  the image.

## What to leave

- The accent photography (cocktail glass, draped fabric) has no evident
  relationship to the agency's stated services — chosen for colour/mood match
  rather than content relevance, a common template-genre shortcut worth
  replacing with real work samples in production.
- Generic service copy ("Innovative Solutions," "Forward-thinking ideas") is
  template placeholder language, not brand voice — needs full rewriting before
  use.
- The "Buy Template" / "Made in Framer" badges are template-marketplace
  chrome, not brand content.

## Signature move

The hero portrait photograph deliberately inverted — the subject's face
reading upside down against the wordmark and nav — a single disorienting break
from convention used once, at maximum scale.

## Motion

(from designlang extract) The extract rates overall feel "responsive" with
confirmed scroll-linked behaviour, but the token set itself is nearly bare: a
single 400ms `md` duration on one ease-out curve
(`cubic-bezier(0.075, 0.82, 0.165, 1)`), applied to colour transitions. No
bespoke keyframe animations are defined — the only keyframe in the stylesheet
is Framer's built-in loading spinner. This matches the template's
generic-competence read above: just enough motion to feel alive (hover
colour changes) without investing in a signature choreography of its own.
(inferred from image) A "Scroll down" label sits in the hero footer, implying
a scroll-cued reveal into the next section; no pinned, parallax or
scroll-scrub behaviour is otherwise evident from the fold capture alone.

| kind | tokens |
|---|---|
| durations | md 400ms |
| easing | ease-out `cubic-bezier(0.075, 0.82, 0.165, 1)` (1×) |

## Brief

Build a creative-agency landing page anchored on one deliberately inverted or
otherwise disoriented hero photograph — flipped, mirrored, or unusually
cropped — paired with a condensed serif wordmark at generous scale. Beside the
image, list services and their outcomes in two aligned columns at equal type
weight, not as a headline-and-description hierarchy. Change both ground colour
and accent photography at each section boundary so the page reads as a
sequence of distinct rooms: dark and moody for the hero, cream and quiet for a
numbered-benefits section, a saturated accent colour (deep blue-green, forest,
oxblood) for an About section. Use outline pill buttons throughout, never
filled, to keep the surface quiet against the photography.

## Image recipe

Moody environmental portrait of [SUBJECT], warm dark maroon or deep-toned
lighting with strong shadow, shot from an unconventional angle (inverted,
tilted, or cropped tight) so the final composition reads as deliberately
art-directed rather than a straightforward headshot, shallow depth of field,
minimal retouching.

## Photo search

Unsplash first, Pexels second.
- "moody portrait dark red tone dramatic"
- "creative professional editorial portrait"
- "backlit glass drink moody photography"
- "fabric drape wind motion dark background"

## Reference lock

Primary reference/direction: Zanzibar (Framer template) — inverted moody
portrait hero, condensed serif wordmark, room-by-room colour shifts per
section.
Preserve (3-5 traits): one hero photograph deliberately flipped/inverted or
unconventionally cropped, used once at maximum scale; condensed serif
wordmark set generously against dark photography; two-column service/outcome
list at equal type weight; a distinct ground colour and accent photograph
change at every section boundary; outline (never filled) pill CTA buttons.
Borrow only (1-2): the numbered benefit list with small dot-badge icons; the
four-dot logo mark.
Role rules: the inverted/disoriented image treatment is used exactly once per
page, in the hero only; each section's accent photograph should relate to
actual brand content in production use, not be chosen for colour/mood alone.
Media strategy: photo:unsplash — moody, art-directed portrait and object
photography with strong colour identity per section; replace with real
client/work imagery before shipping a production site.
Reject: generic template placeholder copy in production use; filled CTA
buttons; repeating the inverted-image device more than once per page.
Token commitments: cream `#FFFAF5`, maroon-dark `#0F0203`, maroon-accent
`#60221B`, teal-deep `#294A5F`, sage `#5A6967`, stone `#9A9992`; display
"Libre Caslon Condensed Variable", body/UI "Inter".
