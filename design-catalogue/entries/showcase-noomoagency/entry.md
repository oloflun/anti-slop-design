---
title: "Noomo Showcase 2025"
url: https://showcase.noomoagency.com/
source_url: https://showcase.noomoagency.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: blue-glow-type-wall-showcase
dna: "Immersive 3D agency x glowing justified type wall"
register: cinematic dark
grammar: live surface
lane: "An agency year-review that loads by stretching the 'noomo' wordmark like taffy (0% → 55%), then sets a full-width justified statement in mixed weights over a blue glow, with small 3D scenes and spheres embedded between the words."
mode: experience
traits: ["stretching wordmark loader", "full-width justified statement in mixed weights", "3D vignettes embedded in the text", "blue radial glow that switches off", "starfield ground"]
palette: ["#000000", "#010080", "#BBBED9", "#5E5B9C", "#010339", "#13105F"]
type: ["GTAmericaMonoRegular", "ppneuemontreal-book", "ppneuemontreal-medium"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The loader is the logo itself stretching its 'oo' into a long bar as the percentage climbs, so loading is a brand animation. The hero is one sentence set edge to edge, with tiny 3D scenes living inside it, and the blue glow turns off to show the type alone.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Noomo).

## What to borrow (principle)

- Stretch part of the wordmark as the progress bar
- Embed small 3D vignettes inside a justified statement
- Switch a coloured glow off to change the mood of the same frame

## What to leave

- Virtual scroll; the statement does not progress under the wheel in captures
- Text-heavy hero

## Signature move

The 'oo' of the wordmark stretching into a progress bar.

## Motion

Intro: 0% → 40% → 55% with 'noomo' at the bottom stretching its middle into a long rounded bar (~2.5 s). Hero: the statement sets in with embedded 3D objects (spheres, frames) moving; the blue glow pulses then switches off. ScrollSmoother present; wheel did not advance in capture.

Measured (`motion/probe.json`): GSAP 3.14.2; ScrollSmoother; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: an agency year-review that loads by stretching the 'noomo' wordmark like taffy (0% → 55%), then sets a full-width justified statement in mixed weights over a blue glow, with small 3D scenes and spheres embedded between the words. Type: GTAmericaMonoRegular, ppneuemontreal-book, ppneuemontreal-medium.
Ground and ink from the measured palette (#000000, #010080, #BBBED9). Motion carries the page through
the 'oo' of the wordmark stretching into a progress bar. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — small 3D object vignettes, chrome spheres, on starfield black

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: small 3D object vignettes, chrome spheres, on starfield black

## Reference lock

Primary reference/direction: Noomo Showcase 2025 — An agency year-review that loads by stretching the 'noomo' wordmark like taffy (0% → 55%), then sets a full-width justified statement in mixed weights over a blue glow, with small 3D scenes and spheres embedded between the words.
Preserve (3-5 traits): stretching wordmark loader; full-width justified statement in mixed weights; 3D vignettes embedded in the text; blue radial glow that switches off; starfield ground.
Borrow only (1-2): Stretch part of the wordmark as the progress bar; Embed small 3D vignettes inside a justified statement
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: small 3D object vignettes, chrome spheres, on starfield black
Reject: Virtual scroll; the statement does not progress under the wheel in captures; Text-heavy hero
Token commitments: palette #000000, #010080, #BBBED9, #5E5B9C, #010339, #13105F; type GTAmericaMonoRegular, ppneuemontreal-book, ppneuemontreal-medium; engine GSAP + Lenis linked (never vendored).
