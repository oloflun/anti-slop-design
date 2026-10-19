---
title: "Mojo Studio - Content Creation Agency Paris"
url: https://mojostudio.co/
source_url: https://mojostudio.co/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: content-agency-stacking-colour-bars
dna: "Paris content agency x tilted 3D-shadow type and stacking coloured project bars"
register: other
grammar: chaptered editorial
lane: "A content agency: 'On y est (presque)' loader on beige concentric rings, 'Original nice content' with the middle word tilted in a blue/pink shadow, a video panel that grows to full screen with project thumbnails, a tilted 'Eclairee creative independante' and numbered project bars in mint, blue and pink that stack up as you scroll, ending with 'Besoin de contenus?'."
mode: persuade
traits: ["tilted type with offset coloured shadow", "concentric ring background", "video panel growing to full screen", "numbered colour bars stacking", "sparkle doodles", "Taxi page transitions"]
palette: ["#FDF8EC", "#ACA9A9", "#28252B", "#959291", "#C2C2BE"]
type: ["Unbounded", "Work Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The coloured project bars stack like a deck being dealt, giving each project its own colour and number without a grid.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Beaucoup Studio).

## What to borrow (principle)

- Stack project bars in alternating colours as you scroll
- Offset coloured shadow on one tilted word

## What to leave

- Cookie bar in every frame
- Small project captions

## Signature move

Numbered project bars in mint, blue and pink stacking over one another.

## Motion

Intro: beige rings with 'On y est (presque)' and sparkles (~1.5 s). Wheel (Lenis ~135 px glide): the tilted word wobbles; the video panel scales from a card to full screen with 'Decouvrir' following the cursor; the bars slide up and stick one below another; the closing headline tilts in.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; Taxi page transitions; 8 video; smoothed scroll (median 141 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a content agency: 'On y est (presque)' loader on beige concentric rings, 'Original nice content' with the middle word tilted in a blue/pink shadow, a video panel that grows to full screen with project thumbnails, a tilted 'Eclairee creative independante' and numbered project bars in mint, blue and pink that stack up as you scroll, ending with 'Besoin de contenus?'. Type: Unbounded, Work Sans.
Ground and ink from the measured palette (#FDF8EC, #ACA9A9, #28252B). Motion carries the page through
numbered project bars in mint, blue and pink stacking over one another. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — fashion and product video stills

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: fashion and product video stills

## Reference lock

Primary reference/direction: Mojo Studio - Content Creation Agency Paris — A content agency: 'On y est (presque)' loader on beige concentric rings, 'Original nice content' with the middle word tilted in a blue/pink shadow, a video panel that grows to full screen with project thumbnails, a tilted 'Eclairee creative independante' and numbered project bars in mint, blue and pink that stack up as you scroll, ending with 'Besoin de contenus?'.
Preserve (3-5 traits): tilted type with offset coloured shadow; concentric ring background; video panel growing to full screen; numbered colour bars stacking; sparkle doodles.
Borrow only (1-2): Stack project bars in alternating colours as you scroll; Offset coloured shadow on one tilted word
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: fashion and product video stills
Reject: Cookie bar in every frame; Small project captions
Token commitments: palette #FDF8EC, #ACA9A9, #28252B, #959291, #C2C2BE; type Unbounded, Work Sans; engine GSAP + Lenis linked (never vendored).
