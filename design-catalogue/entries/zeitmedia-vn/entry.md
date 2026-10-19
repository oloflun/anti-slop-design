---
title: "Zeit Media - Art Comes First"
url: http://zeitmedia.vn/
source_url: http://zeitmedia.vn/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "institutional"
family: event-agency-red-stage
dna: "Vietnamese event agency x red stage footage and a client name cloud"
register: cinematic dark
grammar: chaptered editorial
lane: "An events and communications agency: barcode-line loader that becomes the 'zeit' logo, a red stage film with 'Art comes first - creative above all', stats, a cloud of client names that settles into a block, a 'Lead boldly' marquee with images inside the line, a red mouth-like stage that opens around a glass sphere, selected cases and services."
mode: persuade
traits: ["barcode loader into logo", "red stage footage", "client names flying into a block", "images set inside a marquee line", "3D red stage opening", "case grid on black"]
palette: ["#000000", "#742415", "#3F0F07", "#65433A", "#ABA4A3"]
type: ["Interdisplay"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The scattered client names snapping into a block is a strong way to show scale, and the red stage that opens like a mouth gives the CTA a moment.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Scatter the client list and snap it into a block on scroll
- Inline images inside a marquee line

## What to leave

- Many similar case thumbnails
- Small labels

## Signature move

A red 3D stage that opens around a glass sphere for 'Ready to create your brand breakthrough?'.

## Motion

Intro: black with barcode lines that collapse into the logo (~2 s), then the red stage film. Wheel (Lenis, 1 pin, Barba): the film card shrinks; stats count; client names fly in from scattered positions and lock into a justified block; the marquee runs with images inside it; the red stage pins and opens; cases rise in a grid.

Measured (`motion/probe.json`): GSAP 3.15.0/3.13.0; 13 ScrollTriggers; 1 pinned sections; Lenis; Barba page transitions; WebGL canvas x1 (three.js); 4 video; smoothed scroll (median 125 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: an events and communications agency: barcode-line loader that becomes the 'zeit' logo, a red stage film with 'Art comes first - creative above all', stats, a cloud of client names that settles into a block, a 'Lead boldly' marquee with images inside the line, a red mouth-like stage that opens around a glass sphere, selected cases and services. Type: Interdisplay.
Ground and ink from the measured palette (#000000, #742415, #3F0F07). Motion carries the page through
a red 3D stage that opens around a glass sphere for 'Ready to create your brand breakthrough?'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — event and stage photography, 3D stage

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: event and stage photography, 3D stage

## Reference lock

Primary reference/direction: Zeit Media - Art Comes First — An events and communications agency: barcode-line loader that becomes the 'zeit' logo, a red stage film with 'Art comes first - creative above all', stats, a cloud of client names that settles into a block, a 'Lead boldly' marquee with images inside the line, a red mouth-like stage that opens around a glass sphere, selected cases and services.
Preserve (3-5 traits): barcode loader into logo; red stage footage; client names flying into a block; images set inside a marquee line; 3D red stage opening.
Borrow only (1-2): Scatter the client list and snap it into a block on scroll; Inline images inside a marquee line
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: event and stage photography, 3D stage
Reject: Many similar case thumbnails; Small labels
Token commitments: palette #000000, #742415, #3F0F07, #65433A, #ABA4A3; type Interdisplay; engine GSAP + Lenis linked (never vendored).
