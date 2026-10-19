---
title: "Ryan Ringer-Duffy - Creative Developer"
url: https://ryanringer-duffy.com/
source_url: https://ryanringer-duffy.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: 3d-dev-folio-pavilion
dna: "WebAR and 3D developer x a 3D pavilion model on a grid"
register: cinematic dark
grammar: chaptered editorial
lane: "A 3D developer folio: the 'RRD.' initials assemble from strokes, then a 3D pavilion turns on a green grid between 'Creative' and 'Developer', stats under it, a featured-projects carousel, logo strip, testimonials and a 'What I Do' block with 3D asset previews."
mode: persuade
traits: ["initials drawn from strokes", "3D pavilion on a wireframe grid", "green accent on near-black", "project carousel with dots", "logo marquee", "3D asset previews"]
palette: ["#0F0F0F", "#4F504D", "#839896", "#DBE7E0"]
type: ["Montserrat"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The rotating pavilion proves the skill in the hero; after that the page settles into a conventional folio.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Show the craft as a live 3D object in the hero
- Initials assembled from strokes as the loader

## What to leave

- Generic carousel and testimonials
- Static lower half

## Signature move

A 3D pavilion rotating on a green grid between 'Creative' and 'Developer'.

## Motion

Intro: 'RRD.' assembles from line strokes and slides together (~2 s). Wheel (Lenis, 3 pins): the pavilion rotates and the camera pulls back to show stats; the project carousel slides in and steps; the logo strip scrolls; testimonials fade in as cards; 3D previews rise in the services block.

Measured (`motion/probe.json`): GSAP 3.12.5/3.13.0; 8 ScrollTriggers; 3 pinned sections; Lenis; WebGL canvas x1 (three.js); 8 video; smoothed scroll (median 152 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a 3D developer folio: the 'RRD.' initials assemble from strokes, then a 3D pavilion turns on a green grid between 'Creative' and 'Developer', stats under it, a featured-projects carousel, logo strip, testimonials and a 'What I Do' block with 3D asset previews. Type: Montserrat.
Ground and ink from the measured palette (#0F0F0F, #4F504D, #839896). Motion carries the page through
a 3D pavilion rotating on a green grid between 'Creative' and 'Developer'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D models, project imagery

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D models, project imagery

## Reference lock

Primary reference/direction: Ryan Ringer-Duffy - Creative Developer — A 3D developer folio: the 'RRD.' initials assemble from strokes, then a 3D pavilion turns on a green grid between 'Creative' and 'Developer', stats under it, a featured-projects carousel, logo strip, testimonials and a 'What I Do' block with 3D asset previews.
Preserve (3-5 traits): initials drawn from strokes; 3D pavilion on a wireframe grid; green accent on near-black; project carousel with dots; logo marquee.
Borrow only (1-2): Show the craft as a live 3D object in the hero; Initials assembled from strokes as the loader
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D models, project imagery
Reject: Generic carousel and testimonials; Static lower half
Token commitments: palette #0F0F0F, #4F504D, #839896, #DBE7E0; type Montserrat; engine GSAP + Lenis linked (never vendored).
