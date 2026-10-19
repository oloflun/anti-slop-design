---
title: "FAME Real Estate"
url: https://fame-estate.com/
source_url: https://fame-estate.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "luxury-craft"
family: red-black-dubai-realestate
dna: "Dubai real estate agency x deep red panels and condensed caps"
register: cinematic dark
grammar: chaptered editorial
lane: "A Dubai agency that opens on a black 'FAME' wordmark, cuts to a woman on a terrace above a jungle at sunset, then a small yacht image grows inside a deep red panel, big numbers ride over towers, and a red 'READY TO FIND YOUR DREAM HEAVEN?' closes."
mode: persuade
traits: ["deep oxblood red panels", "condensed caps statements", "image that grows inside a coloured panel", "big stat numbers over tower photography", "3D-like logo mark", "marble textures"]
palette: ["#FFFFFF", "#C2BAB3", "#261913", "#E5DEDA", "#B1A59B", "#454135"]
type: ["HelveticaNeueLTW", "HelveticaNeue", "TimesNewRoman"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Every chapter is a hard switch between black, white and a deep red, and images enter as small cards inside the colour panel before growing, so the colour carries the brand while the photos stay aspirational.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: The First The Last, The First The Last Agency).

## What to borrow (principle)

- Grow a small image inside a solid colour panel until it fills it
- Big numbers set over the architecture they describe

## What to leave

- Tiny captions throughout
- Many sections of similar weight

## Signature move

A small yacht image growing inside a deep oxblood panel.

## Motion

Intro: black with 'FAME' (~1 s), cut to the terrace film. Scroll (Lenis, ~145 px glide): red panel with a small image that grows; red statement; white 'Exclusive real estate agency…'; 35+ / 160M / 6 over a tower; 71% / 3 / 6; interior render; 'OUR CASES' grid; market insights; 'ZERO COMMISSIONS…' over sea; partners; founder; red close; office tower; logo footer.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; 2 video; smoothed scroll (median 147 px still travelling after input stops); entry gate: CLOSE. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a Dubai agency that opens on a black 'FAME' wordmark, cuts to a woman on a terrace above a jungle at sunset, then a small yacht image grows inside a deep red panel, big numbers ride over towers, and a red 'READY TO FIND YOUR DREAM HEAVEN?' closes. Type: HelveticaNeueLTW, HelveticaNeue, TimesNewRoman.
Ground and ink from the measured palette (#FFFFFF, #C2BAB3, #261913). Motion carries the page through
a small yacht image growing inside a deep oxblood panel. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — luxury architecture renders, sunset terraces, Dubai skyline

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: luxury architecture renders, sunset terraces, Dubai skyline

## Reference lock

Primary reference/direction: FAME Real Estate — A Dubai agency that opens on a black 'FAME' wordmark, cuts to a woman on a terrace above a jungle at sunset, then a small yacht image grows inside a deep red panel, big numbers ride over towers, and a red 'READY TO FIND YOUR DREAM HEAVEN?' closes.
Preserve (3-5 traits): deep oxblood red panels; condensed caps statements; image that grows inside a coloured panel; big stat numbers over tower photography; 3D-like logo mark.
Borrow only (1-2): Grow a small image inside a solid colour panel until it fills it; Big numbers set over the architecture they describe
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: luxury architecture renders, sunset terraces, Dubai skyline
Reject: Tiny captions throughout; Many sections of similar weight
Token commitments: palette #FFFFFF, #C2BAB3, #261913, #E5DEDA, #B1A59B, #454135; type HelveticaNeueLTW, HelveticaNeue, TimesNewRoman; engine GSAP + Lenis linked (never vendored).
