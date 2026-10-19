---
title: "They Call Me Giulio - Creative Technologist"
url: https://www.theycallmegiulio.com/
source_url: https://www.theycallmegiulio.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: 3d-avatar-scroll-world
dna: "Creative technologist x 3D avatar walking through coloured worlds"
register: cinematic dark
grammar: continuous world
lane: "A WebGL folio behind an ENTER gate: a crouched 3D figure in a rain-soaked city, then the camera follows the figure through neon-lit worlds that change colour per project (cyan, blue, white, magenta, red), and ends in a dark grid 'room of memories' where visitors can add one."
mode: experience
traits: ["ENTER and sound gate", "one 3D avatar through every scene", "scene colour changes per project", "mono HUD labels and project years", "light streaks and particles", "interactive memory grid finale"]
palette: ["#01030B", "#201738", "#343B43", "#109BB6", "#470F58", "#426378"]
type: ["ubuntu-mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The avatar is the signature object and the colour shifts are the section breaks, so the project list becomes a walk through rooms rather than a grid; the memory room makes the visitor part of the ending.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Giulio Collesei).

## What to borrow (principle)

- Keep one figure on screen and change the world around it per section
- End with a room the visitor can add to

## What to leave

- Gate before any content
- Mono HUD text is hard to read

## Signature move

A 3D figure walking through neon worlds that change colour with each project.

## Motion

Intro: blurred loader with percent, ENTER gate (unlocked), the city scene with the crouched figure fades in (~3 s). Wheel (Lenis, ~100 px with spikes to ~400 px): the camera orbits the figure as it stands and dances; each project swaps the environment colour with light streaks; a close-up pass on the face transitions into the dark grid memory room.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; 6 video; smoothed scroll (median 87 px still travelling after input stops); entry gate: ENTER. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a WebGL folio behind an ENTER gate: a crouched 3D figure in a rain-soaked city, then the camera follows the figure through neon-lit worlds that change colour per project (cyan, blue, white, magenta, red), and ends in a dark grid 'room of memories' where visitors can add one. Type: ubuntu-mono.
Ground and ink from the measured palette (#01030B, #201738, #343B43). Motion carries the page through
a 3D figure walking through neon worlds that change colour with each project. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL avatar and environments, project thumbnails

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL avatar and environments, project thumbnails

## Reference lock

Primary reference/direction: They Call Me Giulio - Creative Technologist — A WebGL folio behind an ENTER gate: a crouched 3D figure in a rain-soaked city, then the camera follows the figure through neon-lit worlds that change colour per project (cyan, blue, white, magenta, red), and ends in a dark grid 'room of memories' where visitors can add one.
Preserve (3-5 traits): ENTER and sound gate; one 3D avatar through every scene; scene colour changes per project; mono HUD labels and project years; light streaks and particles.
Borrow only (1-2): Keep one figure on screen and change the world around it per section; End with a room the visitor can add to
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL avatar and environments, project thumbnails
Reject: Gate before any content; Mono HUD text is hard to read
Token commitments: palette #01030B, #201738, #343B43, #109BB6, #470F58, #426378; type ubuntu-mono; engine GSAP + Lenis linked (never vendored).
