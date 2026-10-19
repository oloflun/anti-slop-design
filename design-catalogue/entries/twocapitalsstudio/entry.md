---
title: "Two Capitals Studio - Creative Web Studio"
url: https://www.twocapitalsstudio.com/
source_url: https://www.twocapitalsstudio.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: astronaut-moon-studio
dna: "Web studio x an astronaut floating above the moon"
register: cinematic dark
grammar: chaptered editorial
lane: "A studio site: a loading percent and 'Visit website', then 'We create digital solutions for your business' curving over the lunar surface, the camera rising into space where a 3D astronaut floats up, a white curved horizon wiping to a light page, an about statement with scrambling letters, service cards stacked like moon photos, and a project list."
mode: persuade
traits: ["3D astronaut", "moon surface and curved text", "white curved horizon wipe", "scrambling letters", "stacked service cards with moon images", "black to off-white flip"]
palette: ["#000000", "#202122", "#464647"]
type: ["Manrope-ExtraBold", "Manrope-Regular", "GothamPro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The astronaut and the curved horizon give the studio one cinematic transition from space to the light page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A curved horizon edge as the wipe from dark to light

## What to leave

- Long empty space frames
- Generic services

## Signature move

An astronaut floating up from the moon before a white horizon wipes the page.

## Motion

Intro: black loader with percent (~4 s), Visit website clicked. Wheel (Lenis): text curves along the moon; the camera rises into stars; the astronaut floats into frame and turns; a white curved edge rises to fill the screen; letters scramble into the statement; service cards stack and shuffle; the project list fades in.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; WebGL canvas x8 (three.js); smoothed scroll (median 120 px still travelling after input stops); entry gate: VISIT WEBSITE. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a studio site: a loading percent and 'Visit website', then 'We create digital solutions for your business' curving over the lunar surface, the camera rising into space where a 3D astronaut floats up, a white curved horizon wiping to a light page, an about statement with scrambling letters, service cards stacked like moon photos, and a project list. Type: Manrope-ExtraBold, Manrope-Regular, GothamPro.
Ground and ink from the measured palette (#000000, #202122, #464647). Motion carries the page through
an astronaut floating up from the moon before a white horizon wipes the page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D astronaut, moon renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D astronaut, moon renders

## Reference lock

Primary reference/direction: Two Capitals Studio - Creative Web Studio — A studio site: a loading percent and 'Visit website', then 'We create digital solutions for your business' curving over the lunar surface, the camera rising into space where a 3D astronaut floats up, a white curved horizon wiping to a light page, an about statement with scrambling letters, service cards stacked like moon photos, and a project list.
Preserve (3-5 traits): 3D astronaut; moon surface and curved text; white curved horizon wipe; scrambling letters; stacked service cards with moon images.
Borrow only (1-2): A curved horizon edge as the wipe from dark to light
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D astronaut, moon renders
Reject: Long empty space frames; Generic services
Token commitments: palette #000000, #202122, #464647; type Manrope-ExtraBold, Manrope-Regular, GothamPro; engine GSAP + Lenis linked (never vendored).
