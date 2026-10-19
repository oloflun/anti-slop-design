---
title: "Kumon Malaysia - 30th Anniversary"
url: https://kumonmalaysia.com/30anniversary
source_url: https://kumonmalaysia.com/30anniversary
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "playful"
family: anniversary-path-timeline
dna: "Children's tutoring brand x a white 3D path climbing through 30 years"
register: cinematic dark
grammar: continuous world
lane: "An anniversary microsite: a sky-blue year counter 2023 to 2025, '30 years of empowering the future generation' over a classroom photo, then a white 3D path that zigzags up into the dark with year markers, record cards (Malaysia Book of Records), a 'Memory Vault' photo carousel, a Pixar-style kid in VR goggles at a futuristic station for 'Project Blueprint', skill labels, a video and 'Past, present & future' with a join button."
mode: experience
traits: ["white 3D path through time", "year counter loader", "record cards with stats", "photo memory vault", "3D character in a future city", "gold and blue accents"]
palette: ["#82D0F5", "#01060A", "#313E43", "#D5EFFA"]
type: ["Black Future"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The path is the anniversary made literal: thirty years as a road you climb, ending in the future scene.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Optimize Tech Solutions).

## What to borrow (principle)

- A path object that carries the timeline

## What to leave

- Dim text over dark images
- Long dark middle

## Signature move

A white 3D path zigzagging up through thirty years.

## Motion

Intro: sky blue with a year counter rolling up (~2 s). Wheel (1 pin): the path draws forward as the camera follows it and year markers pass; cards pop up beside it; the vault carousel slides; the future city fades in with the character; skill labels highlight; the closing panel fades over the classroom.

Measured (`motion/probe.json`): GSAP 3.9.1/3.12.5; 1 ScrollTriggers; 1 pinned sections. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: an anniversary microsite: a sky-blue year counter 2023 to 2025, '30 years of empowering the future generation' over a classroom photo, then a white 3D path that zigzags up into the dark with year markers, record cards (Malaysia Book of Records), a 'Memory Vault' photo carousel, a Pixar-style kid in VR goggles at a futuristic station for 'Project Blueprint', skill labels, a video and 'Past, present & future' with a join button. Type: Black Future.
Ground and ink from the measured palette (#82D0F5, #01060A, #313E43). Motion carries the page through
a white 3D path zigzagging up through thirty years. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D path, classroom photography, 3D character

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D path, classroom photography, 3D character

## Reference lock

Primary reference/direction: Kumon Malaysia - 30th Anniversary — An anniversary microsite: a sky-blue year counter 2023 to 2025, '30 years of empowering the future generation' over a classroom photo, then a white 3D path that zigzags up into the dark with year markers, record cards (Malaysia Book of Records), a 'Memory Vault' photo carousel, a Pixar-style kid in VR goggles at a futuristic station for 'Project Blueprint', skill labels, a video and 'Past, present & future' with a join button.
Preserve (3-5 traits): white 3D path through time; year counter loader; record cards with stats; photo memory vault; 3D character in a future city.
Borrow only (1-2): A path object that carries the timeline
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D path, classroom photography, 3D character
Reject: Dim text over dark images; Long dark middle
Token commitments: palette #82D0F5, #01060A, #313E43, #D5EFFA; type Black Future; engine GSAP + Lenis linked (never vendored).
