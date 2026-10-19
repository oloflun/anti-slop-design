---
title: "Vision (Doan Bao)"
url: https://vision.doanbao.com/
source_url: https://vision.doanbao.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "portfolio"
family: gesture-control-hud
dna: "3D car showcase x hand-gesture control HUD"
register: cinematic dark
grammar: live surface
lane: "An experiment that loads 000% → 095%, asks to 'initialize vision', then shows a green terminal HUD 'NEURAL_LINK_ESTABLISHED' with gesture cards (point, swipe, peace, rock, shaka) for controlling the 3D scene by hand through the webcam."
mode: experience
traits: ["huge percentage loader", "green terminal HUD", "gesture instruction cards with emoji hands", "webcam hand-tracking control", "black ground with scan lines"]
palette: ["#050505", "#666D68"]
type: []
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The interface teaches its own input: a set of gesture cards shows how to drive the scene with your hands, styled as a sci-fi HUD so the instructions feel like part of the experience.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Teach an unusual input with a small set of illustrated instruction cards

## What to leave

- Requires webcam; the scene stays behind the instruction screen headless
- Very small mono text

## Signature move

A green HUD of hand-gesture cards that teaches webcam control.

## Motion

Intro: '000%' → '055%' → '095%' with a status line (~2.5 s), 'INITIALIZE VISION'. Then: 'NEURAL_LINK_ESTABLISHED' fades in with gesture cards; scan lines drift; cards pulse in sequence. No scroll motion.

Measured (`motion/probe.json`): GSAP 3.14.2; 1 video; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: INITIALIZE VISION. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: an experiment that loads 000% → 095%, asks to 'initialize vision', then shows a green terminal HUD 'NEURAL_LINK_ESTABLISHED' with gesture cards (point, swipe, peace, rock, shaka) for controlling the 3D scene by hand through the webcam. Type: read from the captures.
Ground and ink from the measured palette (#050505, #666D68). Motion carries the page through
a green HUD of hand-gesture cards that teaches webcam control. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — HUD graphics, emoji hand icons, green on black

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: HUD graphics, emoji hand icons, green on black

## Reference lock

Primary reference/direction: Vision (Doan Bao) — An experiment that loads 000% → 095%, asks to 'initialize vision', then shows a green terminal HUD 'NEURAL_LINK_ESTABLISHED' with gesture cards (point, swipe, peace, rock, shaka) for controlling the 3D scene by hand through the webcam.
Preserve (3-5 traits): huge percentage loader; green terminal HUD; gesture instruction cards with emoji hands; webcam hand-tracking control; black ground with scan lines.
Borrow only (1-2): Teach an unusual input with a small set of illustrated instruction cards
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: HUD graphics, emoji hand icons, green on black
Reject: Requires webcam; the scene stays behind the instruction screen headless; Very small mono text
Token commitments: palette #050505, #666D68; type -; engine GSAP + Lenis linked (never vendored).
