---
title: "AMANATION - creator management"
url: https://www.amanation-official.com/
source_url: https://www.amanation-official.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "playful"
family: illustrator-agency-image-in-text
dna: "Tokyo creator agency x illustrations inline in the headline and a spinning cube"
register: modern clean
grammar: chaptered editorial
lane: "A creator management company: a counter on black, a spinning cube of illustrations on white, 'We create the next generation of entertainment with creators' with small illustrations set inline between words, a giant black 'A' wipe, a dark rounded panel with the mission, a creator grid of illustration styles, topics on dark grey and an orange footer with a line portrait."
mode: persuade
traits: ["inline illustrations in the headline", "spinning illustration cube", "giant letter wipe", "dark rounded panels", "creator illustration grid", "orange footer"]
palette: ["#FFFFFF", "#222222", "#E7E1E2", "#90888A"]
type: ["heisei-kaku-gothic-std", "neulis-sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Putting the creators' art inside the headline shows the product (creators) in the sentence itself.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Set small artworks inline in the headline
- A giant letter as the wipe to the next section

## What to leave

- Small Japanese text

## Signature move

Illustrations set inline between the words of 'We create the next generation of entertainment'.

## Motion

Intro: black with a counter (~2 s), the cube spins on white. Wheel: headline lines fill with inline images popping in; a giant 'A' sweeps across as a wipe; the dark panel rises; the grid assembles; topics scroll; the orange footer rises.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 123 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a creator management company: a counter on black, a spinning cube of illustrations on white, 'We create the next generation of entertainment with creators' with small illustrations set inline between words, a giant black 'A' wipe, a dark rounded panel with the mission, a creator grid of illustration styles, topics on dark grey and an orange footer with a line portrait. Type: heisei-kaku-gothic-std, neulis-sans.
Ground and ink from the measured palette (#FFFFFF, #222222, #E7E1E2). Motion carries the page through
illustrations set inline between the words of 'We create the next generation of entertainment'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: illustration

## Reference lock

Primary reference/direction: AMANATION - creator management — A creator management company: a counter on black, a spinning cube of illustrations on white, 'We create the next generation of entertainment with creators' with small illustrations set inline between words, a giant black 'A' wipe, a dark rounded panel with the mission, a creator grid of illustration styles, topics on dark grey and an orange footer with a line portrait.
Preserve (3-5 traits): inline illustrations in the headline; spinning illustration cube; giant letter wipe; dark rounded panels; creator illustration grid.
Borrow only (1-2): Set small artworks inline in the headline; A giant letter as the wipe to the next section
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: illustration
Reject: Small Japanese text
Token commitments: palette #FFFFFF, #222222, #E7E1E2, #90888A; type heisei-kaku-gothic-std, neulis-sans; engine GSAP + Lenis linked (never vendored).
