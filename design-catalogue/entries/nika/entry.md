---
title: "Nika - Creative and digital agency"
url: https://nika.agency/
source_url: https://nika.agency/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: agency-dark-column-wall
dna: "Silicon Valley agency x a dark wall of tilted project cards scrolling in columns"
register: cinematic dark
grammar: gallery/catalog
lane: "An agency: 'Good sh*t happens here' with award counts on black, then the whole screen becomes columns of portrait project cards scrolling at different speeds and wrapping, with a filter button."
mode: read
traits: ["award counts row", "columns of portrait cards", "different column speeds", "infinite wrap", "dimmed dark overlay", "filter button"]
palette: ["#151515", "#514B49", "#9AA198", "#3F2725"]
type: ["Space Grotesk", "BaseneueWide"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A wall of work as the home; the column parallax keeps it alive.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Columns of work at different speeds as the home

## What to leave

- Dark overlay dims the work

## Signature move

Columns of portrait project cards drifting at different speeds.

## Motion

Intro: black with the headline and counts (~1 s). Wheel (Lenis): columns move at different speeds and wrap.

Measured (`motion/probe.json`): GSAP 3.11.3; 4 ScrollTriggers; Lenis; ScrollSmoother; Barba page transitions; 121 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the gallery/catalog grammar: an agency: 'Good sh*t happens here' with award counts on black, then the whole screen becomes columns of portrait project cards scrolling at different speeds and wrapping, with a filter button. Type: Space Grotesk, BaseneueWide.
Ground and ink from the measured palette (#151515, #514B49, #9AA198). Motion carries the page through
columns of portrait project cards drifting at different speeds. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project thumbnails

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project thumbnails

## Reference lock

Primary reference/direction: Nika - Creative and digital agency — An agency: 'Good sh*t happens here' with award counts on black, then the whole screen becomes columns of portrait project cards scrolling at different speeds and wrapping, with a filter button.
Preserve (3-5 traits): award counts row; columns of portrait cards; different column speeds; infinite wrap; dimmed dark overlay.
Borrow only (1-2): Columns of work at different speeds as the home
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project thumbnails
Reject: Dark overlay dims the work
Token commitments: palette #151515, #514B49, #9AA198, #3F2725; type Space Grotesk, BaseneueWide; engine GSAP + Lenis linked (never vendored).
