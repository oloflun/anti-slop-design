---
title: "OUWN creative studio"
url: https://ouwn.jp/
source_url: https://ouwn.jp/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: japanese-index-studio
dna: "Tokyo creative studio x a tiny text index with one image at a time"
register: editorial print
grammar: gallery/catalog
lane: "A Tokyo studio: an almost empty white page with a tiny project index in two columns, one small image appearing in the centre at a time with a counter, and a dense all-caps list of every project along the bottom; then full-bleed photos of their exhibitions and installations."
mode: read
traits: ["tiny type index", "one centred image at a time", "counter line under the image", "dense project list footer", "full-bleed installation photos", "extreme whitespace"]
palette: ["#FFFFFF", "#D6D4D3", "#2A241C", "#AEC3C7", "#939495"]
type: ["neue-haas-grotesk-display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Restraint as identity: tiny type and one image at a time make each project feel curated.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Stand Foundation).

## What to borrow (principle)

- One small image at a time in a vast white page

## What to leave

- Type too small to read
- Long wait before large images

## Signature move

One small image at a time in the centre of an almost empty white page.

## Motion

Intro: white index fades in (X clicked). Wheel (Lenis): the centre image swaps per step with the counter advancing and the active index line highlighting; later images scale to full bleed.

Measured (`motion/probe.json`): GSAP 3.5.1; Lenis; 3 video; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: X. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the gallery/catalog grammar: a Tokyo studio: an almost empty white page with a tiny project index in two columns, one small image appearing in the centre at a time with a counter, and a dense all-caps list of every project along the bottom; then full-bleed photos of their exhibitions and installations. Type: neue-haas-grotesk-display.
Ground and ink from the measured palette (#FFFFFF, #D6D4D3, #2A241C). Motion carries the page through
one small image at a time in the centre of an almost empty white page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product, exhibition and installation photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product, exhibition and installation photography

## Reference lock

Primary reference/direction: OUWN creative studio — A Tokyo studio: an almost empty white page with a tiny project index in two columns, one small image appearing in the centre at a time with a counter, and a dense all-caps list of every project along the bottom; then full-bleed photos of their exhibitions and installations.
Preserve (3-5 traits): tiny type index; one centred image at a time; counter line under the image; dense project list footer; full-bleed installation photos.
Borrow only (1-2): One small image at a time in a vast white page
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product, exhibition and installation photography
Reject: Type too small to read; Long wait before large images
Token commitments: palette #FFFFFF, #D6D4D3, #2A241C, #AEC3C7, #939495; type neue-haas-grotesk-display; engine GSAP + Lenis linked (never vendored).
