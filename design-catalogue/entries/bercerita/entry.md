---
title: "Bercerita"
url: https://bercerita.app/
source_url: https://bercerita.app/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "product-focused"
family: letter-mascot-bedtime-app
dna: "Kids' story app x 3D letter mascot"
register: other
grammar: continuous world
lane: "A children's story app where a green 3D letter 'B' with a face is the mascot: it sits in a lime space scene with kids reading, falls into a dark night sky as clouds rise, tumbles and sleeps under 'For Bedtime Moments', and drifts into a blue sky."
mode: persuade
traits: ["3D letter mascot with face", "lime space scene", "cloud edge transition to night", "mascot tumbling and changing expression", "3 pins"]
palette: ["#A6F2A0", "#CBF187", "#59C514", "#130C28", "#C5FDC7", "#8ED54D"]
type: ["Baloo 2"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The logo letter is a character that acts out the product's moment: from playful day to sleepy night. The transition is literal (clouds rise and the scene turns to night), and the mascot's expression changes with it.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Screenagers).

## What to borrow (principle)

- Turn the logo letter into a 3D mascot that acts out the use moment
- Change time of day as the chapter transition

## What to leave

- Little information beyond the mascot story
- Text small at the bottom

## Signature move

A 3D letter mascot that falls asleep as the scene turns to night.

## Motion

Intro: cream, lime loading screen with the mascot (~2 s), then the space scene. Scroll (3 pins, WebGL): mascot turns; clouds rise from the bottom into a night ground; mascot tumbles into the dark, eyes closing; 'For Bedtime Moments When Stories Linger Softly'; it rotates flat, then drifts into a blue sky with clouds.

Measured (`motion/probe.json`): GSAP 3.14.2; 3 pinned sections; WebGL canvas x1 (three.js); 3 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the continuous world grammar: a children's story app where a green 3D letter 'B' with a face is the mascot: it sits in a lime space scene with kids reading, falls into a dark night sky as clouds rise, tumbles and sleeps under 'For Bedtime Moments', and drifts into a blue sky. Type: Baloo 2.
Ground and ink from the measured palette (#A6F2A0, #CBF187, #59C514). Motion carries the page through
a 3D letter mascot that falls asleep as the scene turns to night. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D cartoon mascot and illustrated kids in a space scene

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D cartoon mascot and illustrated kids in a space scene

## Reference lock

Primary reference/direction: Bercerita — A children's story app where a green 3D letter 'B' with a face is the mascot: it sits in a lime space scene with kids reading, falls into a dark night sky as clouds rise, tumbles and sleeps under 'For Bedtime Moments', and drifts into a blue sky.
Preserve (3-5 traits): 3D letter mascot with face; lime space scene; cloud edge transition to night; mascot tumbling and changing expression; 3 pins.
Borrow only (1-2): Turn the logo letter into a 3D mascot that acts out the use moment; Change time of day as the chapter transition
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D cartoon mascot and illustrated kids in a space scene
Reject: Little information beyond the mascot story; Text small at the bottom
Token commitments: palette #A6F2A0, #CBF187, #59C514, #130C28, #C5FDC7, #8ED54D; type Baloo 2; engine GSAP + Lenis linked (never vendored).
