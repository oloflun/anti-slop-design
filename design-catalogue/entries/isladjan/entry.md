---
title: "isladjan - Frontend Developer"
url: https://isladjan.com/
source_url: https://isladjan.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: ballerina-scrollytelling-dev
dna: "Frontend developer x a ballerina that turns from silhouette to particles to iridescent 3D"
register: cinematic dark
grammar: continuous world
lane: "A developer folio told in five chapters (Hello, Animation, Design, Frontend, Backend): a ballerina silhouette in a spotlight, then the same pose as a particle cloud with 'Portfolio' text ringing her waist, then an iridescent 3D figure on yellow, then a stone statue among clouds on blue, while mono text explains each skill."
mode: experience
traits: ["one ballerina pose through every chapter", "material changes per chapter", "text ring around the waist", "colour split panels", "mono typewriter text", "chapter counter"]
palette: ["#000000", "#222222", "#393746", "#91917A"]
type: ["vcr-osd-mono", "7pixelsofperfection", "Aldrich", "departure-mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The ballerina is the signature object, and each chapter re-renders her in a new material that matches the skill, so the CV becomes a transformation.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Re-render one figure in a new material per chapter

## What to leave

- Mono text small

## Signature move

A ballerina turning from particles to iridescent 3D to stone among clouds.

## Motion

Intro: white ballerina silhouette (~1 s), then a spotlight. Wheel (Lenis, 1 pin): the silhouette dissolves into particles; a text ring spins at her waist; a yellow panel slides across and she becomes iridescent; a blue panel slides and she turns to stone with clouds drifting.

Measured (`motion/probe.json`): GSAP 3.12.7; 1 pinned sections; Lenis; WebGL canvas x2 (three.js). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a developer folio told in five chapters (Hello, Animation, Design, Frontend, Backend): a ballerina silhouette in a spotlight, then the same pose as a particle cloud with 'Portfolio' text ringing her waist, then an iridescent 3D figure on yellow, then a stone statue among clouds on blue, while mono text explains each skill. Type: vcr-osd-mono, 7pixelsofperfection, Aldrich, departure-mono.
Ground and ink from the measured palette (#000000, #222222, #393746). Motion carries the page through
a ballerina turning from particles to iridescent 3D to stone among clouds. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL figure

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL figure

## Reference lock

Primary reference/direction: isladjan - Frontend Developer — A developer folio told in five chapters (Hello, Animation, Design, Frontend, Backend): a ballerina silhouette in a spotlight, then the same pose as a particle cloud with 'Portfolio' text ringing her waist, then an iridescent 3D figure on yellow, then a stone statue among clouds on blue, while mono text explains each skill.
Preserve (3-5 traits): one ballerina pose through every chapter; material changes per chapter; text ring around the waist; colour split panels; mono typewriter text.
Borrow only (1-2): Re-render one figure in a new material per chapter
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL figure
Reject: Mono text small
Token commitments: palette #000000, #222222, #393746, #91917A; type vcr-osd-mono, 7pixelsofperfection, Aldrich, departure-mono; engine GSAP + Lenis linked (never vendored).
