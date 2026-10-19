---
title: "Yourwave"
url: https://yourwave.nl/
source_url: https://yourwave.nl/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: dutch-freelancer-sunburst
dna: "Dutch freelancer x italic serif accents and a sunburst line icon"
register: editorial print
grammar: chaptered editorial
lane: "A freelancer site on light grey: a big counter with a vertical line, 'YOURWAVE', an intro with italic serif words, cases (a sunburst line drawing, JVE Studio, Leroy Hirschfeld, Hola Hurghada), a 'Creative - Immersive - Branding' marquee, a portrait, story, FAQ and a giant wordmark that waves into place."
mode: persuade
traits: ["big counter loader", "italic serif accent words", "sunburst line drawing", "word marquee", "FAQ accordion", "wordmark with a wave settle"]
palette: ["#F6F6F6", "#9B8F89", "#B6B4B5", "#554B4A", "#DDDCDC"]
type: ["PPHatton", "PPNeueMontreal", "Saans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The wordmark settling with a wave at the end ties the name to the motion; the rest is a tidy freelancer page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Let the footer wordmark settle with a wave motion that matches the name

## What to leave

- Generic case cards
- Long FAQ

## Signature move

'YOURWAVE' rippling into place as the footer.

## Motion

Intro: grey, a big counter 11 to 100 with a line growing (~2 s). Wheel (Lenis + ScrollSmoother ~125 px glide): the intro fills; case cards drift; the sunburst rotates; the marquee runs; the portrait slides; the footer letters rise in a wave.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; ScrollSmoother; split text; smoothed scroll (median 123 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a freelancer site on light grey: a big counter with a vertical line, 'YOURWAVE', an intro with italic serif words, cases (a sunburst line drawing, JVE Studio, Leroy Hirschfeld, Hola Hurghada), a 'Creative - Immersive - Branding' marquee, a portrait, story, FAQ and a giant wordmark that waves into place. Type: PPHatton, PPNeueMontreal, Saans.
Ground and ink from the measured palette (#F6F6F6, #9B8F89, #B6B4B5). Motion carries the page through
'YOURWAVE' rippling into place as the footer. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — portrait, case imagery

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: portrait, case imagery

## Reference lock

Primary reference/direction: Yourwave — A freelancer site on light grey: a big counter with a vertical line, 'YOURWAVE', an intro with italic serif words, cases (a sunburst line drawing, JVE Studio, Leroy Hirschfeld, Hola Hurghada), a 'Creative - Immersive - Branding' marquee, a portrait, story, FAQ and a giant wordmark that waves into place.
Preserve (3-5 traits): big counter loader; italic serif accent words; sunburst line drawing; word marquee; FAQ accordion.
Borrow only (1-2): Let the footer wordmark settle with a wave motion that matches the name
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: portrait, case imagery
Reject: Generic case cards; Long FAQ
Token commitments: palette #F6F6F6, #9B8F89, #B6B4B5, #554B4A, #DDDCDC; type PPHatton, PPNeueMontreal, Saans; engine GSAP + Lenis linked (never vendored).
