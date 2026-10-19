---
title: "Pablo Miguez - Web Designer and Creative Frontend Developer"
url: https://pablomiguez.dev/
source_url: https://pablomiguez.dev/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: wide-gothic-dev-folio
dna: "Spanish frontend developer x wide gothic display and horizontal card rail"
register: cinematic dark
grammar: chaptered editorial
lane: "A developer folio on black in a wide gothic display face: name then 'DEV' scaling up as the loader, a Frontend / Motion / Creative marquee, a manifesto that fills in, a pinned horizontal rail of six numbered value cards (cream and grey), a CV list, a giant 'MOTION IS THE FUTURE' set piece and a project list with phone mockups."
mode: persuade
traits: ["wide gothic display face", "pinned horizontal card rail", "manifesto fill on scroll", "giant staggered statement", "cream cards on black", "phone mockups in project list"]
palette: ["#0A0A0A", "#393937", "#FFFBF0", "#20201F", "#CBCAC3", "#5F5E5C"]
type: ["Science Gothic", "Inter"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The wide gothic gives a personal folio a strong voice, and the horizontal rail is the one place the page changes direction.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One pinned horizontal rail in a vertical page
- A huge staggered statement as the break before work

## What to leave

- Cookie bar stayed over the capture
- Small body copy on cards

## Signature move

'MOTION IS THE FUTURE' staggered in a wide gothic across black.

## Motion

Intro: 'PABLO.MIGUEZ' then 'DEV' scales up on black (~2 s). Wheel (ScrollSmoother, 1 pin): the marquee slides; the manifesto fills grey to white; the card rail pins and slides left card by card; the CV list fades in; 'MOTION IS THE FUTURE' words slide in from different sides; project rows reveal with phones.

Measured (`motion/probe.json`): GSAP 3.14.2; 1 pinned sections; Lenis; WebGL canvas x2 (three.js); split text; smoothed scroll (median 112 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a developer folio on black in a wide gothic display face: name then 'DEV' scaling up as the loader, a Frontend / Motion / Creative marquee, a manifesto that fills in, a pinned horizontal rail of six numbered value cards (cream and grey), a CV list, a giant 'MOTION IS THE FUTURE' set piece and a project list with phone mockups. Type: Science Gothic, Inter.
Ground and ink from the measured palette (#0A0A0A, #393937, #FFFBF0). Motion carries the page through
'MOTION IS THE FUTURE' staggered in a wide gothic across black. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — phone mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: phone mockups

## Reference lock

Primary reference/direction: Pablo Miguez - Web Designer and Creative Frontend Developer — A developer folio on black in a wide gothic display face: name then 'DEV' scaling up as the loader, a Frontend / Motion / Creative marquee, a manifesto that fills in, a pinned horizontal rail of six numbered value cards (cream and grey), a CV list, a giant 'MOTION IS THE FUTURE' set piece and a project list with phone mockups.
Preserve (3-5 traits): wide gothic display face; pinned horizontal card rail; manifesto fill on scroll; giant staggered statement; cream cards on black.
Borrow only (1-2): One pinned horizontal rail in a vertical page; A huge staggered statement as the break before work
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: phone mockups
Reject: Cookie bar stayed over the capture; Small body copy on cards
Token commitments: palette #0A0A0A, #393937, #FFFBF0, #20201F, #CBCAC3, #5F5E5C; type Science Gothic, Inter; engine GSAP + Lenis linked (never vendored).
