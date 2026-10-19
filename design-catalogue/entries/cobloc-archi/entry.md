---
title: "Cobloc"
url: https://www.cobloc.archi/
source_url: https://www.cobloc.archi/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: ""
family: blur-block-letters-architecture
dna: "Architecture firm x building-block letters and velocity blur"
register: warm photographic
grammar: chaptered editorial
lane: "An architecture firm whose name is spelled in simple geometric blocks (c o / b l o c) that rearrange like building pieces, on peach and warm grey grounds, with the whole page blurring while it moves and sharpening when it stops."
mode: persuade
traits: ["logo built from geometric blocks that rearrange", "velocity blur on the whole page", "peach / warm grey / dark grounds", "mono + serif (Ivory) type", "project images floating with drift"]
palette: ["#FAF2DC", "#FFDDB1", "#CEBBA1"]
type: ["DM Mono", "Funnel Sans", "Ivory LL"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The name is literally built: c-o-b-l-o-c set as blocks (circle, bar, half-disc) that later scatter and re-stack as an illustration of what building means. Motion is felt as blur: the page softens while it is moving and comes into focus at rest, which makes stopping feel like arriving.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Build the wordmark from basic geometric pieces that can rearrange later
- Blur by scroll velocity so rest equals focus

## What to leave

- Captures are nearly all blurred: velocity blur makes the page hard to read while scrolling
- Cookie banner over every frame

## Signature move

The letters c-o-b-l-o-c as building blocks that scatter and re-stack.

## Motion

Intro: the blocks assemble into 'co / bloc' on light grey (~2 s), ground warms to peach. Scroll (Barba, SplitText, Draggable, WebGL x2): the whole viewport blurs while moving; a greeting sets in over the faded blocks; the blocks drift apart and re-stack as a small sculpture; project images float on peach and dark bands.

Measured (`motion/probe.json`): GSAP 3.13.0; Barba page transitions; WebGL canvas x2 (three.js); smoothed scroll (median 115 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: an architecture firm whose name is spelled in simple geometric blocks (c o / b l o c) that rearrange like building pieces, on peach and warm grey grounds, with the whole page blurring while it moves and sharpening when it stops. Type: DM Mono, Funnel Sans, Ivory LL.
Ground and ink from the measured palette (#FAF2DC, #FFDDB1, #CEBBA1). Motion carries the page through
the letters c-o-b-l-o-c as building blocks that scatter and re-stack. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — architectural photography in warm light, terracotta, olive trees

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: architectural photography in warm light, terracotta, olive trees

## Reference lock

Primary reference/direction: Cobloc — An architecture firm whose name is spelled in simple geometric blocks (c o / b l o c) that rearrange like building pieces, on peach and warm grey grounds, with the whole page blurring while it moves and sharpening when it stops.
Preserve (3-5 traits): logo built from geometric blocks that rearrange; velocity blur on the whole page; peach / warm grey / dark grounds; mono + serif (Ivory) type; project images floating with drift.
Borrow only (1-2): Build the wordmark from basic geometric pieces that can rearrange later; Blur by scroll velocity so rest equals focus
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: architectural photography in warm light, terracotta, olive trees
Reject: Captures are nearly all blurred: velocity blur makes the page hard to read while scrolling; Cookie banner over every frame
Token commitments: palette #FAF2DC, #FFDDB1, #CEBBA1; type DM Mono, Funnel Sans, Ivory LL; engine GSAP + Lenis linked (never vendored).
