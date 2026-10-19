---
title: "nk.studio - Digital platforms and branding"
url: https://www.nk.studio/
source_url: https://www.nk.studio/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: neon-slash-agency-grid
dna: "Argentinian studio x a neon green slash over a dark landscape"
register: cinematic dark
grammar: chaptered editorial
lane: "An agency: 'It all starts with a spark' with a glowing dot, a dark green landscape with a neon slash and 'For crafting bold digital realities, the world is our canvas', then a white work grid mixing small mockups, big case images and blurred video placeholders with stats, a project index list, a testimonial and the neon slash returning on the dark ground for values."
mode: persuade
traits: ["neon green slash mark", "dark green landscape", "white work grid", "case stats on images", "project index list", "slash returning at the end"]
palette: ["#424852", "#010201", "#FEFFFA", "#282839", "#686E73", "#DCE3D6"]
type: ["DM Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The slash opens and closes the page as the brand mark, bracketing a long work grid.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Bracket the page with the same hero object at start and end

## What to leave

- Blurred placeholders in grid
- Generic grid

## Signature move

A neon green slash over a dark misty landscape.

## Motion

Intro: dark with a spark dot and text (~2 s), the slash fades in over the landscape. Wheel (Lenis): the white panel rises; grid items slide; numbers count; the index list fills; the slash returns as the dark panel rises.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 140 px still travelling after input stops); entry gate: close, EXPLORE OUR UNIVERSE. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: an agency: 'It all starts with a spark' with a glowing dot, a dark green landscape with a neon slash and 'For crafting bold digital realities, the world is our canvas', then a white work grid mixing small mockups, big case images and blurred video placeholders with stats, a project index list, a testimonial and the neon slash returning on the dark ground for values. Type: DM Sans.
Ground and ink from the measured palette (#424852, #010201, #FEFFFA). Motion carries the page through
a neon green slash over a dark misty landscape. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D landscape, case mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D landscape, case mockups

## Reference lock

Primary reference/direction: nk.studio - Digital platforms and branding — An agency: 'It all starts with a spark' with a glowing dot, a dark green landscape with a neon slash and 'For crafting bold digital realities, the world is our canvas', then a white work grid mixing small mockups, big case images and blurred video placeholders with stats, a project index list, a testimonial and the neon slash returning on the dark ground for values.
Preserve (3-5 traits): neon green slash mark; dark green landscape; white work grid; case stats on images; project index list.
Borrow only (1-2): Bracket the page with the same hero object at start and end
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D landscape, case mockups
Reject: Blurred placeholders in grid; Generic grid
Token commitments: palette #424852, #010201, #FEFFFA, #282839, #686E73, #DCE3D6; type DM Sans; engine GSAP + Lenis linked (never vendored).
