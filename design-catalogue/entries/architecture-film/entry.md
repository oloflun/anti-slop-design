---
title: "Architecture.Film"
url: https://www.architecture.film/
source_url: https://www.architecture.film/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "luxury-craft"
family: architecture-film-reel-wordmark
dna: "Architecture film studio x a serif wordmark over a reel of building films"
register: warm photographic
grammar: filmic one-shot
lane: "An architectural film studio: the serif 'Architecture.Film' wordmark with an orange dot stays fixed at the left while full-bleed film clips of buildings (a green-clad housing block, a coastal house, an office interior, a white facade with grass, an aerial city, a party, a brick block) cut one after another behind it."
mode: experience
traits: ["fixed serif wordmark", "full-bleed architecture films", "orange dot accent", "aerial drone shots", "quiet cuts between clips", "no other content on the front"]
palette: ["#B0A8A3", "#271F1A", "#56473B", "#C4C1BF", "#7F6F65", "#E3E3E2"]
type: ["neue-haas-grotesk-display", "ivyora-display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The studio sells by showing; the fixed wordmark over a reel of their films is the whole argument.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Hold the wordmark still and cut films behind it

## What to leave

- No way to tell which project is which
- Nothing else on the page

## Signature move

A serif 'Architecture.Film' wordmark over a cut reel of buildings.

## Motion

Intro: the reel starts immediately with the wordmark. Wheel (virtual, Barba): each scroll step cuts to the next clip; the wordmark stays fixed.

Measured (`motion/probe.json`): GSAP 3.15.0; Barba page transitions; 10 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the filmic one-shot grammar: an architectural film studio: the serif 'Architecture.Film' wordmark with an orange dot stays fixed at the left while full-bleed film clips of buildings (a green-clad housing block, a coastal house, an office interior, a white facade with grass, an aerial city, a party, a brick block) cut one after another behind it. Type: neue-haas-grotesk-display, ivyora-display.
Ground and ink from the measured palette (#B0A8A3, #271F1A, #56473B). Motion carries the page through
a serif 'Architecture.Film' wordmark over a cut reel of buildings. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — architecture film

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: architecture film

## Reference lock

Primary reference/direction: Architecture.Film — An architectural film studio: the serif 'Architecture.Film' wordmark with an orange dot stays fixed at the left while full-bleed film clips of buildings (a green-clad housing block, a coastal house, an office interior, a white facade with grass, an aerial city, a party, a brick block) cut one after another behind it.
Preserve (3-5 traits): fixed serif wordmark; full-bleed architecture films; orange dot accent; aerial drone shots; quiet cuts between clips.
Borrow only (1-2): Hold the wordmark still and cut films behind it
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: architecture film
Reject: No way to tell which project is which; Nothing else on the page
Token commitments: palette #B0A8A3, #271F1A, #56473B, #C4C1BF, #7F6F65, #E3E3E2; type neue-haas-grotesk-display, ivyora-display; engine GSAP + Lenis linked (never vendored).
