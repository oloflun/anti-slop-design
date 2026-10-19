---
title: "Lando Norris - McLaren F1 Driver"
url: https://landonorris.com/
source_url: https://landonorris.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "editorial"
family: athlete-signature-scroll
dna: "F1 driver site x neon-lime signature and helmet hall"
register: other
grammar: chaptered editorial
lane: "A driver's personal site: lime loader with the L4 mark, a 3D helmet portrait, then a scroll where the signature is drawn across a marquee, a manifesto lights up word by word, photos drift across a topographic ground, an on/off-track split, a helmet hall of fame grid, champion merch and a social card fan."
mode: experience
traits: ["neon lime on olive and cream", "drawn signature as the transition", "manifesto with word-by-word colour fill", "scattered photo drift over contour lines", "helmet grid on black", "fanned social cards"]
palette: ["#272D20", "#9C9D96", "#FCFCF9", "#4D4637", "#918776"]
type: ["Brier", "Mona Sans Variable"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The signature is the signature object: it is drawn over the hero marquee, reappears as the partners scrawl, and the lime of the helmet runs through every section so a long scroll stays one personality.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: OFF+BRAND).

## What to borrow (principle)

- A handwritten signature drawn on scroll as the link between sections
- Word-by-word colour fill on a manifesto

## What to leave

- Very long page with many modes
- Small serif captions on photos

## Signature move

A neon lime signature drawn across the marquee of a driver's site.

## Motion

Intro: lime screen, the L4 mark morphs into a blurred helmet, then the 3D helmet portrait (~2.5 s). Wheel (Lenis, light ~30 px glide): marquee lines slide in opposite directions while the signature draws over a portrait; the manifesto fills lime word by word; photos drift at different speeds over a contour ground; on/off track split pins briefly; helmet hall grid steps up; social cards fan in. Taxi page transitions.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Taxi page transitions; WebGL canvas x2 (three.js); smoothed scroll (median 58 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a driver's personal site: lime loader with the L4 mark, a 3D helmet portrait, then a scroll where the signature is drawn across a marquee, a manifesto lights up word by word, photos drift across a topographic ground, an on/off-track split, a helmet hall of fame grid, champion merch and a social card fan. Type: Brier, Mona Sans Variable.
Ground and ink from the measured palette (#272D20, #9C9D96, #FCFCF9). Motion carries the page through
a neon lime signature drawn across the marquee of a driver's site. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — driver photography, helmet renders, merch

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: driver photography, helmet renders, merch

## Reference lock

Primary reference/direction: Lando Norris - McLaren F1 Driver — A driver's personal site: lime loader with the L4 mark, a 3D helmet portrait, then a scroll where the signature is drawn across a marquee, a manifesto lights up word by word, photos drift across a topographic ground, an on/off-track split, a helmet hall of fame grid, champion merch and a social card fan.
Preserve (3-5 traits): neon lime on olive and cream; drawn signature as the transition; manifesto with word-by-word colour fill; scattered photo drift over contour lines; helmet grid on black.
Borrow only (1-2): A handwritten signature drawn on scroll as the link between sections; Word-by-word colour fill on a manifesto
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: driver photography, helmet renders, merch
Reject: Very long page with many modes; Small serif captions on photos
Token commitments: palette #272D20, #9C9D96, #FCFCF9, #4D4637, #918776; type Brier, Mona Sans Variable; engine GSAP + Lenis linked (never vendored).
