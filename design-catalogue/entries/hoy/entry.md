---
title: "Hoy"
url: https://www.hoy.se/
source_url: https://www.hoy.se/
captured: 2026-09-15
origin: raw-url
raw: ""
extract: ok
category: portfolio
category2: "playful"
family: flat-ground-chapters
dna: "Flat saturated ground chapters x one caps grotesk headline per section"
register: modern clean
grammar: chaptered editorial
lane: "A purple screen with one 3D word carousel, then chapter after chapter of one caps headline, one paragraph and one plate, alternating sides, while the whole ground jumps purple to cream to red; a pill nav floats at the bottom centre the whole way down"
mode: persuade
traits: ["three flat saturated grounds, purple cream red", "one caps grotesk headline per chapter, weight 400", "text and plate alternate sides chapter by chapter", "giant marquee headline as chapter divider", "floating pill nav bottom centre", "invert toggle top right", "outline pill buttons only", "hairline rules between chapters"]
palette: ["#5124AE", "#FCECBA", "#E5E7EB", "#000000"]
type: ["Circular", "Times New Roman"]
measured: designlang (palette and type from hoy-se-design-tokens.json; motion tokens from hoy-se-design-language.md, feel mixed, scroll-linked). The red ground of the app chapter and the plum and pale pink grounds of /tjanster/webbdesign are read off the captures (sampled #f84838, #783848, #f8d8e8), not in the extract's token list.
kind: reference-style
source: claude
status: ready
---

## Why it works

Hoy builds the whole page out of one chapter anatomy and lets the ground do the
chaptering. Every section is the same thing: a caps grotesk headline in a single weight
(400, 48 px on the home page, 132 px when it becomes a marquee), one paragraph in the same
face, one plate. What changes is which side the plate sits on, chapter by chapter, and
what colour the ground is. The home page runs purple, then cream, then red, three flat
grounds cut hard at full width, so the reader feels three acts without a single card or
shadow. On /tjanster/webbdesign the same trick runs plum to pale pink, once, with a
full-viewport photograph as the hinge.

The type never competes with the plates because it never gets heavy: cream on purple,
purple on cream, cream on red, always weight 400, always caps for the headline and
sentence case for the body. The plates are the only saturated, detailed thing on each
screen, so the eye lands on them first and reads the headline second. Hairline rules
mark the seam between chapters, and where the page wants a bigger beat it sets one
headline at marquee size ("UTVALDA PROJEKT", "WEBBDESIGN") and lets it run past the
right edge.

Two persistent pieces of chrome hold it together: a pill nav floating at the bottom
centre (Projekt, Tjänster, Kontakt, menu) that inverts its colours with the ground, and
an "Invert" toggle top right that swaps the whole palette. The hero is a four-slide
carousel where each slide changes the ground colour, so the first screen already
teaches the rule the rest of the page follows.

## What to borrow (principle)

- **Let the ground change material between acts, at full width, with a hard edge.**
  Three flat grounds are three chapters; no card is needed.
- **One chapter anatomy, alternated left and right**, so rhythm comes from mirroring,
  not from new components.
- **One type weight for everything and hierarchy by size and case.**
- **A giant headline that runs past the edge as a chapter divider.**
- **Chrome that inverts with the ground** instead of sitting on a fixed bar.

## What to leave

- The hero carousel that auto-advances and changes ground colour under the reader.
- Team photographs and "10 år", "20 år", "en av fem byråer": PRODUCT.md § absences.
- The "Invert" toggle: a novelty control that overlaps body copy at 390 (seen in the
  captures) and does no job for the visitor.
- The same anatomy nine times in a row: the mirroring carries it, but nothing on the page
  is not text-plus-plate, so the composition contract's "one moment that is not
  information" is never met.
- The `↗` glyph after every social link.

## Signature move

The ground jumps: purple to cream to red on the home page, plum to pale pink on the
service page, always full width, always a hard cut, with the floating pill nav inverting
its own colours at the same seam so the chrome belongs to whichever ground it is on.

## Motion

Feel "mixed", scroll-linked. One easing family, `cubic-bezier(0.4, 0, 0.2, 1)`, on 69
transitions, durations 150 to 500 ms. One keyframe in use, `slide-up-enter` (opacity), the
chapter reveal; `spin-vertically` and `rotate` are declared and drive the hero's word
carousel. The giant divider headlines carry a marquee dash that suggests horizontal
travel. Otherwise the page is quiet: no parallax, no pin, no scrub, and the ground cuts
are hard, not drifted. (from designlang extract, plus the captured slices)

| kind | tokens |
|---|---|
| durations | xs 150ms · sm 200ms · md 300ms · lg 500ms |
| easings | custom `cubic-bezier(0.4, 0, 0.2, 1)` |
| keyframes declared | `slide-up-enter` · `slide-up-leave` · `spin-vertically` · `rotate` |

## Brief

Build an agency page as a sequence of flat-ground chapters. Open on a saturated ground
with one caps word and a 3D object. Then run chapters of one caps headline, one short
paragraph and one plate, mirroring the plate's side each time, and cut the ground to a
new flat colour at full width every third chapter. Use one grotesk in one weight; make
hierarchy with size and case. Put a giant headline that runs past the right edge where
the page changes subject. Keep the nav as a floating pill at the bottom centre that
inverts with the ground. Close on the last ground with a short paragraph, one outline
button and the social links.

## Image recipe

Photograph or product still of [SUBJECT] framed as a plate with air on every side, true
colour, the plate being the most saturated and detailed thing on its screen; on the
hero, a soft 3D render of devices on a flat ground.

## Photo search

Unsplash first, Pexels second.
- "team working laptop loft office candid"
- "hand holding phone website mockup"
- "3d render devices flat background purple"

## Reference lock

Primary reference/direction: Hoy, flat-ground chapters where the ground colour, not a
card, marks each act.
Preserve (3-5 traits): three flat grounds cut at full width with hard edges; one chapter
anatomy (caps headline, paragraph, plate) mirrored left and right; one weight for all
type; a giant divider headline running past the edge; chrome that inverts with the
ground.
Borrow only (1-2): the full-width hard ground cut as the way to change act; the giant
divider headline as a chapter break.
Role rules: cream is type on purple and red, purple is type on cream; the plate is the
only detailed element per screen; buttons are outline pills only, never filled.
Media strategy: photo:unsplash for people, product screenshots as plates with air around
them, one 3D render on the hero.
Reject: cards, shadows, a fixed top bar, filled buttons, more than one type weight, an
auto-advancing hero carousel, a palette toggle.
Token commitments: purple `#5124AE`, cream `#FCECBA`, rule `#E5E7EB`, ink `#000000`;
red and plum grounds as read from the captures, sampled `#F84838` and `#783848`;
`Circular` 400 for every string, headlines caps 48px, marquee 132px with -2.64px
tracking, body 16px; radius 2px on plates and 9999px on pills only.
