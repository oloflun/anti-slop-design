---
title: "Kononenko Architectural Bureau"
url: https://kononenkogroup.com/
source_url: https://kononenkogroup.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: ""
family: sketch-to-render-architecture
dna: "Architecture bureau x pencil sketch to render"
register: editorial print
grammar: chaptered editorial
lane: "An architecture bureau that counts up over white, opens on a building render, explains its process as pencil sketches drawing themselves into structures, then turns black for a ring of team photos orbiting the studio's numbers."
mode: persuade
traits: ["count-up loader at bottom-left", "pencil sketches drawn on scroll", "serif statements (light) over white", "project grid with drifting images", "black section with orbiting photo ring", "big serif counters (490+, 45+)"]
palette: ["#FFFFFF", "#A9AAAC", "#6C6559", "#C5C5C6", "#3C3933", "#898784"]
type: ["n", "h"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The process section shows the work the way architects actually start: line sketches draw themselves stroke by stroke as the reader scrolls, then turn into structure. The studio section switches to black and sets team photos in an orbit around each number, so statistics come with faces.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Artem Shcherban, Reksa Andhika).

## What to borrow (principle)

- Draw the process: sketches that build stroke by stroke with scroll before the finished render
- Orbit photos around a big number so a statistic has people attached
- Light serif statements over white for a calm, professional voice

## What to leave

- Counter loader is plain
- Long white stretches between sketches

## Signature move

Pencil sketches of buildings that draw themselves as you scroll through the process.

## Motion

Intro: counter 60 → 83 at bottom-left on white with a top progress line (~2 s), then the building render fills. Scroll (Lenis, ~120 px glide, SplitText, three.js): 'Systematic Clarity & Creativity'; render cards; services list; sketches draw progressively (structure, facade, perspective); project grid drifting; radial lines converge on 'Refined & Bold / Essential'; black studio section where a ring of team photos orbits '2011 Year of Foundation', '490+ completed projects', '45+ professionals'.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 120 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: an architecture bureau that counts up over white, opens on a building render, explains its process as pencil sketches drawing themselves into structures, then turns black for a ring of team photos orbiting the studio's numbers. Type: n, h.
Ground and ink from the measured palette (#FFFFFF, #A9AAAC, #6C6559). Motion carries the page through
pencil sketches of buildings that draw themselves as you scroll through the process. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — architectural renders in daylight, pencil sketches, team at work

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: architectural renders in daylight, pencil sketches, team at work

## Reference lock

Primary reference/direction: Kononenko Architectural Bureau — An architecture bureau that counts up over white, opens on a building render, explains its process as pencil sketches drawing themselves into structures, then turns black for a ring of team photos orbiting the studio's numbers.
Preserve (3-5 traits): count-up loader at bottom-left; pencil sketches drawn on scroll; serif statements (light) over white; project grid with drifting images; black section with orbiting photo ring.
Borrow only (1-2): Draw the process: sketches that build stroke by stroke with scroll before the finished render; Orbit photos around a big number so a statistic has people attached
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: architectural renders in daylight, pencil sketches, team at work
Reject: Counter loader is plain; Long white stretches between sketches
Token commitments: palette #FFFFFF, #A9AAAC, #6C6559, #C5C5C6, #3C3933, #898784; type n, h; engine GSAP + Lenis linked (never vendored).
