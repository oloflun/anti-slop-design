---
title: "OVA - Investment Fund"
url: https://ova-investment.com/
source_url: https://ova-investment.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "luxury-craft"
family: horizon-carousel-fund
dna: "Investment fund x a curved carousel of sector images on a sunset horizon"
register: cinematic dark
grammar: split stage
lane: "A fund on a sunset gradient: the 'ova' logo glowing at the horizon, 'Valuable, that is our future / portfolio / collaboration' with the last word swapping, a curved 3D carousel of sector images riding along the horizon, then each sector (technology, real estate, health, tourism, finance, media, energy, entertainment) takes the full screen with a paragraph and a side index."
mode: persuade
traits: ["sunset horizon gradient", "curved 3D image carousel", "word swap in the tagline", "full-screen sector chapters", "side index of sectors", "cinematic AI imagery"]
palette: ["#A4A39F", "#2C2F36", "#C2BEB3", "#676665", "#12151A", "#EEE6C9"]
type: ["Neue Montreal", "Geist Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The carousel on the horizon is the portfolio as one object; then each sector gets its own full-screen scene, which suits a fund that sells a vision.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Department Maison de Création, Jeremy Fagis, Jordan Thiervoz, type8 studio).

## What to borrow (principle)

- A curved carousel along a horizon line
- One-word swap in a recurring tagline

## What to leave

- Paragraphs over busy images
- Generic AI imagery

## Signature move

A curved carousel of sector images riding a sunset horizon.

## Motion

Intro: black, the logo fades in on the horizon (~2 s). Wheel (Lenis ~75 px glide): the tagline word swaps; the carousel rotates along the curve; it recedes into the dark; each sector image fills the screen and crossfades to the next while the index advances.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; WebGL canvas x1; split text; smoothed scroll (median 84 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the split stage grammar: a fund on a sunset gradient: the 'ova' logo glowing at the horizon, 'Valuable, that is our future / portfolio / collaboration' with the last word swapping, a curved 3D carousel of sector images riding along the horizon, then each sector (technology, real estate, health, tourism, finance, media, energy, entertainment) takes the full screen with a paragraph and a side index. Type: Neue Montreal, Geist Mono.
Ground and ink from the measured palette (#A4A39F, #2C2F36, #C2BEB3). Motion carries the page through
a curved carousel of sector images riding a sunset horizon. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — cinematic photography and AI imagery

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: cinematic photography and AI imagery

## Reference lock

Primary reference/direction: OVA - Investment Fund — A fund on a sunset gradient: the 'ova' logo glowing at the horizon, 'Valuable, that is our future / portfolio / collaboration' with the last word swapping, a curved 3D carousel of sector images riding along the horizon, then each sector (technology, real estate, health, tourism, finance, media, energy, entertainment) takes the full screen with a paragraph and a side index.
Preserve (3-5 traits): sunset horizon gradient; curved 3D image carousel; word swap in the tagline; full-screen sector chapters; side index of sectors.
Borrow only (1-2): A curved carousel along a horizon line; One-word swap in a recurring tagline
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: cinematic photography and AI imagery
Reject: Paragraphs over busy images; Generic AI imagery
Token commitments: palette #A4A39F, #2C2F36, #C2BEB3, #676665, #12151A, #EEE6C9; type Neue Montreal, Geist Mono; engine GSAP + Lenis linked (never vendored).
