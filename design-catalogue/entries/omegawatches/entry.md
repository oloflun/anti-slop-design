---
title: "Omega x ClearSpace - removing debris from space"
url: https://www.omegawatches.com/clearspace
source_url: https://www.omegawatches.com/clearspace
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "luxury-craft"
family: space-mission-scrollytelling
dna: "Watch brand mission story x a satellite over Earth and the camera descending through debris"
register: cinematic dark
grammar: filmic one-shot
lane: "A brand story: 'CLEARSPACE x OMEGA' small on black, 'The quest to remove debris from space' over a satellite above the Earth's limb with the sun, the camera turning past the satellite into sunrise, 'Since the birth of the first watch on the moon, humankind has launched well over 6,400 rockets' over Earth filling the screen, debris pieces drifting with small captions, the Earth dimming to black and a thin crescent at the end."
mode: experience
traits: ["3D Earth and satellite", "camera turning into sunrise", "captions floating over the globe", "thin display caps", "cookie dialog at start", "long dark passage"]
palette: ["#080A16", "#363E54", "#18253C", "#6E7894"]
type: ["omegact", "Austin Italic"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One continuous camera move from the satellite down to the planet and out again gives the mission the scale it needs.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Immersive Garden).

## What to borrow (principle)

- Make the whole page one camera move around a single object

## What to leave

- Long stretch of near-black frames
- Cookie dialog over the hero

## Signature move

A satellite above the Earth's limb with the sun rising behind it.

## Motion

Intro: black with the logos (~2 s), the cookie dialog. Wheel (Lenis, pinned WebGL): the camera orbits the satellite into the sunrise; the Earth fills the frame; captions fade in and out at points on the globe; the scene darkens; a crescent appears.

Measured (`motion/probe.json`): GSAP 3.14.2; WebGL canvas x1 (three.js); split text; smoothed scroll (median 42 px still travelling after input stops); entry gate: REJECT ALL. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a brand story: 'CLEARSPACE x OMEGA' small on black, 'The quest to remove debris from space' over a satellite above the Earth's limb with the sun, the camera turning past the satellite into sunrise, 'Since the birth of the first watch on the moon, humankind has launched well over 6,400 rockets' over Earth filling the screen, debris pieces drifting with small captions, the Earth dimming to black and a thin crescent at the end. Type: omegact, Austin Italic.
Ground and ink from the measured palette (#080A16, #363E54, #18253C). Motion carries the page through
a satellite above the Earth's limb with the sun rising behind it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL Earth, satellite

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL Earth, satellite

## Reference lock

Primary reference/direction: Omega x ClearSpace - removing debris from space — A brand story: 'CLEARSPACE x OMEGA' small on black, 'The quest to remove debris from space' over a satellite above the Earth's limb with the sun, the camera turning past the satellite into sunrise, 'Since the birth of the first watch on the moon, humankind has launched well over 6,400 rockets' over Earth filling the screen, debris pieces drifting with small captions, the Earth dimming to black and a thin crescent at the end.
Preserve (3-5 traits): 3D Earth and satellite; camera turning into sunrise; captions floating over the globe; thin display caps; cookie dialog at start.
Borrow only (1-2): Make the whole page one camera move around a single object
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL Earth, satellite
Reject: Long stretch of near-black frames; Cookie dialog over the hero
Token commitments: palette #080A16, #363E54, #18253C, #6E7894; type omegact, Austin Italic; engine GSAP + Lenis linked (never vendored).
