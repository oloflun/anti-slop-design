---
title: "ChainGPT Labs - Web3 incubator"
url: https://labs.chaingpt.org/
source_url: https://labs.chaingpt.org/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: pixel-font-robot-incubator
dna: "Web3 incubator x a pixel font counter and a robot in a glass tube"
register: modern clean
grammar: chaptered editorial
lane: "An incubator on light grey: an orange screen with a pixel-font counter 000 to 100 that breaks into pixel blocks, 'BACKING TO...' in a pixel display font beside a white 3D column, partner logos, 'BEYOND CAPITAL' with a checklist, a little robot in a glass tube, 'INCUBATION', a portfolio of robot nodes connected by tubes, project cards with stats, media presence, testimonials, team, FAQ and news."
mode: persuade
traits: ["pixel display font", "orange counter loader", "white 3D props", "robot mascot in a tube", "grey UI cards", "orange accent buttons"]
palette: ["#E4E4E4", "#CBC8C7", "#997C6B"]
type: ["LabsAmiga", "RobotoMono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The pixel font and the robot mascot give a finance product a playful, consistent identity.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A pixel font counter that breaks into blocks as the intro

## What to leave

- Very long templated sections

## Signature move

A small robot in a glass tube beside 'INCUBATION' in pixel type.

## Motion

Intro: orange with a pixel counter (~2 s), the digits break into blocks that fly off. Wheel: the column rotates; titles type in pixel font; the tube moves down with the robot; nodes connect; cards slide in carousels.

Measured (`motion/probe.json`): GSAP 3.11.5; 8 ScrollTriggers; Lenis; WebGL canvas x1; 3 video; split text; smoothed scroll (median 141 px still travelling after input stops); entry gate: REJECT, close. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an incubator on light grey: an orange screen with a pixel-font counter 000 to 100 that breaks into pixel blocks, 'BACKING TO...' in a pixel display font beside a white 3D column, partner logos, 'BEYOND CAPITAL' with a checklist, a little robot in a glass tube, 'INCUBATION', a portfolio of robot nodes connected by tubes, project cards with stats, media presence, testimonials, team, FAQ and news. Type: LabsAmiga, RobotoMono.
Ground and ink from the measured palette (#E4E4E4, #CBC8C7, #997C6B). Motion carries the page through
a small robot in a glass tube beside 'INCUBATION' in pixel type. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D props, portraits

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D props, portraits

## Reference lock

Primary reference/direction: ChainGPT Labs - Web3 incubator — An incubator on light grey: an orange screen with a pixel-font counter 000 to 100 that breaks into pixel blocks, 'BACKING TO...' in a pixel display font beside a white 3D column, partner logos, 'BEYOND CAPITAL' with a checklist, a little robot in a glass tube, 'INCUBATION', a portfolio of robot nodes connected by tubes, project cards with stats, media presence, testimonials, team, FAQ and news.
Preserve (3-5 traits): pixel display font; orange counter loader; white 3D props; robot mascot in a tube; grey UI cards.
Borrow only (1-2): A pixel font counter that breaks into blocks as the intro
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D props, portraits
Reject: Very long templated sections
Token commitments: palette #E4E4E4, #CBC8C7, #997C6B; type LabsAmiga, RobotoMono; engine GSAP + Lenis linked (never vendored).
