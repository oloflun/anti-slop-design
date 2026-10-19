---
title: "I-Creativ"
url: https://i-creativ.net/
source_url: https://i-creativ.net/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: torn-texture-condensed-studio
dna: "Plovdiv design studio x torn-paper texture and condensed caps"
register: cinematic dark
grammar: chaptered editorial
lane: "A dark studio page under a huge condensed 'DIGITAL ARTISANS', where a torn-poster texture image drifts and rips across sections and case projects sit in small framed panels."
mode: persuade
traits: ["huge condensed caps (Bebas)", "torn street-poster texture as the hero image", "framed case panels", "dark charcoal ground", "Barba + Flip transitions"]
palette: ["#15161A", "#5D534E", "#35383B", "#9A9B9F"]
type: ["peridot-pe-variable", "BebasNeue"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The studio's city (Plovdiv's Kapana district) is present as a texture: torn layers of street posters fill the hero and keep drifting between sections, which gives a plain dark layout a material surface. The giant condensed headline is the only loud type.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: I-Creativ Studio).

## What to borrow (principle)

- Use a local texture (torn posters) as the moving surface behind a simple layout
- One very large condensed word block as the hero, everything else small

## What to leave

- Cookie panel over every frame
- Long empty dark stretches near the end

## Signature move

Torn street-poster layers drifting under 'DIGITAL ARTISANS'.

## Motion

Intro: pale grey with a small loader mark, then a cut to dark with 'DIGITAL ARTISANS' rising (~2 s). Scroll (Lenis, ~100 px glide, Barba, Flip): the torn texture slides and scales between sections; case titles fade in beside framed images; contact block at the end.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; Barba page transitions; WebGL canvas x1; smoothed scroll (median 131 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a dark studio page under a huge condensed 'DIGITAL ARTISANS', where a torn-poster texture image drifts and rips across sections and case projects sit in small framed panels. Type: peridot-pe-variable, BebasNeue.
Ground and ink from the measured palette (#15161A, #5D534E, #35383B). Motion carries the page through
torn street-poster layers drifting under 'DIGITAL ARTISANS'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — close-up textures of torn posters and layered paper, desaturated

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: close-up textures of torn posters and layered paper, desaturated

## Reference lock

Primary reference/direction: I-Creativ — A dark studio page under a huge condensed 'DIGITAL ARTISANS', where a torn-poster texture image drifts and rips across sections and case projects sit in small framed panels.
Preserve (3-5 traits): huge condensed caps (Bebas); torn street-poster texture as the hero image; framed case panels; dark charcoal ground; Barba + Flip transitions.
Borrow only (1-2): Use a local texture (torn posters) as the moving surface behind a simple layout; One very large condensed word block as the hero, everything else small
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: close-up textures of torn posters and layered paper, desaturated
Reject: Cookie panel over every frame; Long empty dark stretches near the end
Token commitments: palette #15161A, #5D534E, #35383B, #9A9B9F; type peridot-pe-variable, BebasNeue; engine GSAP + Lenis linked (never vendored).
