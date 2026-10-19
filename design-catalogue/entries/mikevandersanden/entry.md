---
title: "Mike van der Sanden - Personal Project Platform"
url: https://mikevandersanden.com/
source_url: https://mikevandersanden.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: ascii-orange-playground
dna: "Designer's experiments platform x ASCII art and orange pixel blocks"
register: cinematic dark
grammar: chaptered editorial
lane: "A personal playground: an orange header 'Challenging the limits of visual comfort, feeding the inherent drive to create', a black section with an ASCII-art rendering behind a short story, featured cases (a pixel type tool, a building facade, math curves, cats on grids) and a footer where orange pixel blocks dance over a grey wave."
mode: read
traits: ["orange and black", "ASCII art rendering", "pixel block footer animation", "case cards for experiments", "serif headline", "small mono meta"]
palette: ["#101010", "#FF4C0B", "#D8CAD9", "#9D604D", "#8A3F26", "#CD4C1E"]
type: ["Suisse Intl", "PP Woodland"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The ASCII art and the dancing pixel footer show the experiments as the brand; it is a playground, not a sales page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- An ASCII rendering as a background texture

## What to leave

- Footer animation dominates the capture

## Signature move

Orange pixel blocks dancing over a grey wave in the footer.

## Motion

Intro: orange header slides up from black (~1 s). Wheel (native): the ASCII art resolves; cases slide up; the footer blocks animate continuously.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x1 (three.js); 4 video. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a personal playground: an orange header 'Challenging the limits of visual comfort, feeding the inherent drive to create', a black section with an ASCII-art rendering behind a short story, featured cases (a pixel type tool, a building facade, math curves, cats on grids) and a footer where orange pixel blocks dance over a grey wave. Type: Suisse Intl, PP Woodland.
Ground and ink from the measured palette (#101010, #FF4C0B, #D8CAD9). Motion carries the page through
orange pixel blocks dancing over a grey wave in the footer. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — ASCII art, experiment screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: ASCII art, experiment screenshots

## Reference lock

Primary reference/direction: Mike van der Sanden - Personal Project Platform — A personal playground: an orange header 'Challenging the limits of visual comfort, feeding the inherent drive to create', a black section with an ASCII-art rendering behind a short story, featured cases (a pixel type tool, a building facade, math curves, cats on grids) and a footer where orange pixel blocks dance over a grey wave.
Preserve (3-5 traits): orange and black; ASCII art rendering; pixel block footer animation; case cards for experiments; serif headline.
Borrow only (1-2): An ASCII rendering as a background texture
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: ASCII art, experiment screenshots
Reject: Footer animation dominates the capture
Token commitments: palette #101010, #FF4C0B, #D8CAD9, #9D604D, #8A3F26, #CD4C1E; type Suisse Intl, PP Woodland; engine GSAP + Lenis linked (never vendored).
