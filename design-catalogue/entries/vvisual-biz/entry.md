---
title: "VISUALBUSINESS"
url: https://www.vvisual.biz/
source_url: https://www.vvisual.biz/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "luxury-craft"
family: numbered-photo-grid-agency
dna: "Model and image agency x a sparse numbered photo grid"
register: modern clean
grammar: gallery/catalog
lane: "A visual agency on white: a grid of numbered slots that fill one by one with fashion and editorial photos at small size, leaving many slots empty, scrolling down to a dense text footer."
mode: read
traits: ["numbered grid slots", "small photos with lots of white", "fashion photography", "tiny type", "dense footer"]
palette: ["#FCFBFC", "#0A0F10", "#55443D", "#C6D2D5", "#768A89", "#B2A89F"]
type: ["Neue Montreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The sparse numbered grid feels like a contact sheet; restraint lets the photos look curated.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Number every grid slot, leave some empty

## What to leave

- Tiny type

## Signature move

A sparse numbered grid of fashion photos on white.

## Motion

Intro: white with numbers (~1 s), photos pop into slots. Wheel: the grid scrolls; photos fade in as slots enter.

Measured (`motion/probe.json`): GSAP 3.12.7; Taxi page transitions; WebGL canvas x1; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a visual agency on white: a grid of numbered slots that fill one by one with fashion and editorial photos at small size, leaving many slots empty, scrolling down to a dense text footer. Type: Neue Montreal.
Ground and ink from the measured palette (#FCFBFC, #0A0F10, #55443D). Motion carries the page through
a sparse numbered grid of fashion photos on white. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — fashion photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: fashion photography

## Reference lock

Primary reference/direction: VISUALBUSINESS — A visual agency on white: a grid of numbered slots that fill one by one with fashion and editorial photos at small size, leaving many slots empty, scrolling down to a dense text footer.
Preserve (3-5 traits): numbered grid slots; small photos with lots of white; fashion photography; tiny type; dense footer.
Borrow only (1-2): Number every grid slot, leave some empty
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: fashion photography
Reject: Tiny type
Token commitments: palette #FCFBFC, #0A0F10, #55443D, #C6D2D5, #768A89, #B2A89F; type Neue Montreal; engine GSAP + Lenis linked (never vendored).
