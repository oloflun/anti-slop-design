---
title: "SSTR — Friction Reduction Systems"
url: https://sstr.tech/en/
source_url: https://sstr.tech/en/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "institutional"
family: orange-drill-pipe-engineering
dna: "Drilling equipment maker x technical HUD and 3D drill string"
register: cinematic dark
grammar: chaptered editorial
lane: "An oilfield-equipment page with a signal-orange loader block, data charts of torque reduction, then a long pinned scene where a 3D drill string bends through the borehole and each orange component lights up as its spec text appears."
mode: persuade
traits: ["signal orange on charcoal", "percentage loader in an orange block", "dotted data curves with big negative percentages", "3D drill pipe bending through a borehole", "components highlighted one by one", "caps technical copy"]
palette: ["#17191A", "#DAC5C0", "#46302D"]
type: ["Abc Monument Grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Engineering proof is told along the product itself: the camera travels down a 3D drill string and each tool along it turns orange as its function is stated, so the spec sheet becomes a tour of the object. Data charts before it give the numbers (−48%, −23 T) as dotted curves.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Travel along the product in 3D and highlight each part as its spec is read
- Show results as large signed numbers beside dotted curves
- One signal colour reserved for the part being discussed

## What to leave

- Long pinned scene (~10 viewports) of similar frames
- Very small caps body

## Signature move

A 3D drill string where each component turns orange as the camera reaches it.

## Motion

Intro: orange block top-left with '// SSTR' and a percentage 21 → 92 (~2 s). Scroll (Lenis, ~150 px glide, 8 ScrollTriggers, Barba, SplitText, three.js): hero; 'From well data to verified field results' with three equipment icons; dotted curves for torque and hook load with big numbers; drilling rig illustration; pinned 3D sequence where the drill pipe bends down the borehole and each tool (FRS, Transfer X1, X6, X3, PDC bit) is highlighted orange with its text.

Measured (`motion/probe.json`): GSAP 3.15.0; 8 ScrollTriggers; Lenis; Barba page transitions; WebGL canvas x1 (three.js); 3 video; smoothed scroll (median 141 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: an oilfield-equipment page with a signal-orange loader block, data charts of torque reduction, then a long pinned scene where a 3D drill string bends through the borehole and each orange component lights up as its spec text appears. Type: Abc Monument Grotesk.
Ground and ink from the measured palette (#17191A, #DAC5C0, #46302D). Motion carries the page through
a 3D drill string where each component turns orange as the camera reaches it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — technical 3D renders of industrial equipment on charcoal, one signal orange

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: technical 3D renders of industrial equipment on charcoal, one signal orange

## Reference lock

Primary reference/direction: SSTR — Friction Reduction Systems — An oilfield-equipment page with a signal-orange loader block, data charts of torque reduction, then a long pinned scene where a 3D drill string bends through the borehole and each orange component lights up as its spec text appears.
Preserve (3-5 traits): signal orange on charcoal; percentage loader in an orange block; dotted data curves with big negative percentages; 3D drill pipe bending through a borehole; components highlighted one by one.
Borrow only (1-2): Travel along the product in 3D and highlight each part as its spec is read; Show results as large signed numbers beside dotted curves
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: technical 3D renders of industrial equipment on charcoal, one signal orange
Reject: Long pinned scene (~10 viewports) of similar frames; Very small caps body
Token commitments: palette #17191A, #DAC5C0, #46302D; type Abc Monument Grotesk; engine GSAP + Lenis linked (never vendored).
