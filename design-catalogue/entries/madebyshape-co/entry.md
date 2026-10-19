---
title: "MadeByShape - Web design agency Manchester"
url: https://madebyshape.co.uk/
source_url: https://madebyshape.co.uk/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: agency-hero-collage-lime
dna: "Manchester web agency x a hero collage that swaps and lime accent stickers"
register: modern clean
grammar: chaptered editorial
lane: "An agency: 'A web design and branding agency in Manchester' with a collage panel that swaps between work, a statement, client logos, case pairs, a black services list where the active service lights up with an image, video testimonials, an about statement and a 'Let's work together' marquee."
mode: persuade
traits: ["swapping hero collage", "lime accent badges", "services list highlight", "video testimonials", "marquee CTA", "dark services panel"]
palette: ["#FFFFFF", "#362B21", "#E0C2C7", "#161511", "#ACAAA7", "#4E4A46"]
type: ["Oldschool Grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Competent agency site; the hero collage swapping work is its main motion idea.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Swap work inside the hero collage on a timer

## What to leave

- Generic agency structure

## Signature move

A hero collage swapping between client work.

## Motion

Intro: the hero with the collage swapping (~3 s). Wheel: statements fill; cases slide; the black panel rises; service rows highlight; the marquee runs.

Measured (`motion/probe.json`): GSAP 3.13.0; 3 video; entry gate: Mute/Unmute video. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an agency: 'A web design and branding agency in Manchester' with a collage panel that swaps between work, a statement, client logos, case pairs, a black services list where the active service lights up with an image, video testimonials, an about statement and a 'Let's work together' marquee. Type: Oldschool Grotesk.
Ground and ink from the measured palette (#FFFFFF, #362B21, #E0C2C7). Motion carries the page through
a hero collage swapping between client work. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — case photography and video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: case photography and video

## Reference lock

Primary reference/direction: MadeByShape - Web design agency Manchester — An agency: 'A web design and branding agency in Manchester' with a collage panel that swaps between work, a statement, client logos, case pairs, a black services list where the active service lights up with an image, video testimonials, an about statement and a 'Let's work together' marquee.
Preserve (3-5 traits): swapping hero collage; lime accent badges; services list highlight; video testimonials; marquee CTA.
Borrow only (1-2): Swap work inside the hero collage on a timer
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: case photography and video
Reject: Generic agency structure
Token commitments: palette #FFFFFF, #362B21, #E0C2C7, #161511, #ACAAA7, #4E4A46; type Oldschool Grotesk; engine GSAP + Lenis linked (never vendored).
