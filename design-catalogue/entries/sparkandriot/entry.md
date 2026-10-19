---
title: "Spark and Riot - Film production"
url: https://www.sparkandriot.com/
source_url: https://www.sparkandriot.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: production-studio-directors-lime
dna: "Film production studio x lime italic serif and a director grid"
register: cinematic dark
grammar: chaptered editorial
lane: "A production studio on navy-black: 'SPARK / RIOT.' split around a film still, a 'Directors' grid of thumbnails with one portrait enlarged on hover, 'Award winning studio' with a list, 'Film & TV', 'What we're all about' in lime italic serif, 'Impact driven' and 'Let's connect' with a big S-lightning-R logo footer."
mode: persuade
traits: ["lime italic serif headings", "split wordmark around film", "director thumbnail grid", "blurred heading reveals", "impact statement with highlights", "bolt logo footer"]
palette: ["#060E19", "#52524E", "#273031", "#838378"]
type: ["PPEditorialOld", "Switzer-Variable", "icomoon"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The blur-to-sharp headings and lime accents give a production house a stylish voice, but the structure is conventional.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Reveal headings from blur in the accent colour

## What to leave

- Cookie panel over every frame
- Small text

## Signature move

Lime italic serif headings sharpening out of blur on navy-black.

## Motion

Intro: navy with the logo (~2 s), the split wordmark slides apart over a still. Wheel (Lenis ~110-170 px glide, 101 triggers): the director grid fills; hovering enlarges a portrait; headings sharpen from blur; images slide; the footer logo rises.

Measured (`motion/probe.json`): GSAP 3.12.5; 101 ScrollTriggers; Lenis; WebGL canvas x1; 27 video; split text; smoothed scroll (median 157 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a production studio on navy-black: 'SPARK / RIOT.' split around a film still, a 'Directors' grid of thumbnails with one portrait enlarged on hover, 'Award winning studio' with a list, 'Film & TV', 'What we're all about' in lime italic serif, 'Impact driven' and 'Let's connect' with a big S-lightning-R logo footer. Type: PPEditorialOld, Switzer-Variable, icomoon.
Ground and ink from the measured palette (#060E19, #52524E, #273031). Motion carries the page through
lime italic serif headings sharpening out of blur on navy-black. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — film stills, director portraits

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: film stills, director portraits

## Reference lock

Primary reference/direction: Spark and Riot - Film production — A production studio on navy-black: 'SPARK / RIOT.' split around a film still, a 'Directors' grid of thumbnails with one portrait enlarged on hover, 'Award winning studio' with a list, 'Film & TV', 'What we're all about' in lime italic serif, 'Impact driven' and 'Let's connect' with a big S-lightning-R logo footer.
Preserve (3-5 traits): lime italic serif headings; split wordmark around film; director thumbnail grid; blurred heading reveals; impact statement with highlights.
Borrow only (1-2): Reveal headings from blur in the accent colour
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: film stills, director portraits
Reject: Cookie panel over every frame; Small text
Token commitments: palette #060E19, #52524E, #273031, #838378; type PPEditorialOld, Switzer-Variable, icomoon; engine GSAP + Lenis linked (never vendored).
