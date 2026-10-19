---
title: "Phantom Studios - Technology Creative Agency"
url: https://www.phantom.land/
source_url: https://www.phantom.land/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: curved-grid-work-wall-agency
dna: "London tech-creative agency x a curved wall of project tiles"
register: cinematic dark
grammar: gallery/catalog
lane: "An agency home on black: the name, then a grid of dozens of project tiles bent onto a curved surface like the inside of a cylinder, the centre tile enlarged and highlighted, the wall drifting as you move and scroll."
mode: experience
traits: ["curved cylinder grid of tiles", "centre tile enlarged", "black ground", "filter and nav pill", "drag/scroll to pan", "dense work wall"]
palette: ["#000000", "#908785", "#F5EBD6", "#C4C7BC", "#443734", "#873E33"]
type: ["Helvetica Now", "ballinger-mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Bending the grid onto a curve gives a dense archive depth and makes browsing physical.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Bend the work grid onto a curved surface

## What to leave

- Hard to read individual projects

## Signature move

A wall of project tiles bent onto a curved surface around the viewer.

## Motion

Intro: black with the name (~2 s), cookie declined, the wall fades in with a fisheye curve. Scroll/drag: the wall pans; the tile in the centre scales and brightens.

Measured (`motion/probe.json`): GSAP 3.14.2; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Decline. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the gallery/catalog grammar: an agency home on black: the name, then a grid of dozens of project tiles bent onto a curved surface like the inside of a cylinder, the centre tile enlarged and highlighted, the wall drifting as you move and scroll. Type: Helvetica Now, ballinger-mono.
Ground and ink from the measured palette (#000000, #908785, #F5EBD6). Motion carries the page through
a wall of project tiles bent onto a curved surface around the viewer. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project thumbnails

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project thumbnails

## Reference lock

Primary reference/direction: Phantom Studios - Technology Creative Agency — An agency home on black: the name, then a grid of dozens of project tiles bent onto a curved surface like the inside of a cylinder, the centre tile enlarged and highlighted, the wall drifting as you move and scroll.
Preserve (3-5 traits): curved cylinder grid of tiles; centre tile enlarged; black ground; filter and nav pill; drag/scroll to pan.
Borrow only (1-2): Bend the work grid onto a curved surface
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project thumbnails
Reject: Hard to read individual projects
Token commitments: palette #000000, #908785, #F5EBD6, #C4C7BC, #443734, #873E33; type Helvetica Now, ballinger-mono; engine GSAP + Lenis linked (never vendored).
