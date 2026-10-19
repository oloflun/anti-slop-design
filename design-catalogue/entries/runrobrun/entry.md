---
title: "Run Rob Run"
url: https://www.runrobrun.com/
source_url: https://www.runrobrun.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: orange-pixel-runner-folio
dna: "Creative developer folio x 8-bit runner and orange slab"
register: modern clean
grammar: chaptered editorial
lane: "A developer folio where a pixel runner sprite starts the page, an orange blob morphs between the words CREATIVE and DEVELOPER, and an orange section of 'TOOLS' presents each experiment behind a pixel staircase that builds across the frame."
mode: persuade
traits: ["pixel running figure as loader", "morphing orange 3D blob hero", "extended heavy grotesque", "full orange section", "pixel staircase transitions", "numbered tool experiments 000–004"]
palette: ["#FC641B", "#DADADA", "#583424", "#C5B7B1", "#BE6B42"]
type: ["monumentHeading", "neueHeading", "neueralMono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A playful identity (a running pixel man) is kept consistent: he is the loader, he runs across the tools section, and the staircase of black pixel blocks that builds between experiments is his world. The orange ground takes over the second half so the experiments read as a separate lab.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Let the loader's character recur later in the page so the intro was a promise
- Pixel-block staircases as a section transition for a digital, playful brand
- Number experiments 000–004 like a lab log

## What to leave

- Headline words cropped at the edges
- Mixed systems (blob, pixels, photo) compete in the first half

## Signature move

An 8-bit runner who loads the page and later sprints across a staircase of pixel blocks.

## Motion

Intro: black with 'loading', a pixel runner silhouette animating in place, then a white wipe to 'CREATIVE / DEVELOPER' with an orange blob morphing (~2.5 s). Scroll (Lenis + ScrollSmoother, Draggable/Inertia, SplitText): the blob shrinks to a dot as two statement blocks slide in; portrait cards; services list with active black row; orange 'TOOLS' section where each experiment (Runman, Chroma Warp, Split Mask, Text Maze, Whale) enters behind a black pixel staircase that builds across.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; 4 video; smoothed scroll (median 44 px still travelling after input stops); entry gate: Play So Did We. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a developer folio where a pixel runner sprite starts the page, an orange blob morphs between the words CREATIVE and DEVELOPER, and an orange section of 'TOOLS' presents each experiment behind a pixel staircase that builds across the frame. Type: monumentHeading, neueHeading, neueralMono.
Ground and ink from the measured palette (#FC641B, #DADADA, #583424). Motion carries the page through
an 8-bit runner who loads the page and later sprints across a staircase of pixel blocks. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — playful developer experiments, pixel sprites, orange 3D blob

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: playful developer experiments, pixel sprites, orange 3D blob

## Reference lock

Primary reference/direction: Run Rob Run — A developer folio where a pixel runner sprite starts the page, an orange blob morphs between the words CREATIVE and DEVELOPER, and an orange section of 'TOOLS' presents each experiment behind a pixel staircase that builds across the frame.
Preserve (3-5 traits): pixel running figure as loader; morphing orange 3D blob hero; extended heavy grotesque; full orange section; pixel staircase transitions.
Borrow only (1-2): Let the loader's character recur later in the page so the intro was a promise; Pixel-block staircases as a section transition for a digital, playful brand
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: playful developer experiments, pixel sprites, orange 3D blob
Reject: Headline words cropped at the edges; Mixed systems (blob, pixels, photo) compete in the first half
Token commitments: palette #FC641B, #DADADA, #583424, #C5B7B1, #BE6B42; type monumentHeading, neueHeading, neueralMono; engine GSAP + Lenis linked (never vendored).
