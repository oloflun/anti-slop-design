---
title: "Angel Nin - Video and Photography"
url: https://angelnin.com/
source_url: https://angelnin.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "luxury-craft"
family: product-photographer-wall-to-hero
dna: "Product and food photographer x a wall of shots that dives into single hero images"
register: warm photographic
grammar: chaptered editorial
lane: "A commercial photographer: a tilted wall of product and food shots under a yellow 'ANGEL NIN' name, which blurs away into single dark hero images per specialty (a leather belt, a poke bowl, a blue Ferrari) with a side index, a portrait with bio, a 'Food, framed perfectly' section and a horizontal strip of selected work."
mode: read
traits: ["tilted wall of every shot as the hero", "yellow display name", "dark studio product photography", "side index switching specialty", "horizontal selected-work strip", "blur as the section transition"]
palette: ["#0D0C08", "#282019", "#545142", "#898050"]
type: ["General Sans", "Clash Display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Opening on the whole wall and then isolating one product per specialty mirrors the photographer's job: from the archive to the single perfect frame.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Tikendev).

## What to borrow (principle)

- Start on the wall of work, then isolate one hero frame
- Blur the wall away to change scale

## What to leave

- Small side index text
- Dark-on-dark bio section

## Signature move

A tilted wall of product shots blurring away into one dark hero photograph.

## Motion

Intro: the photo wall pans slowly, the yellow name rises (~1.5 s). Wheel (Lenis ~130 px glide, 3 pins): the wall blurs and darkens; the belt shot pins and scales while the side index highlights 'Commercial product'; the food and car shots replace it in turn; the portrait slides in; the selected-work strip scrolls sideways.

Measured (`motion/probe.json`): GSAP 3.14.2; 3 pinned sections; Lenis; 4 video; smoothed scroll (median 132 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a commercial photographer: a tilted wall of product and food shots under a yellow 'ANGEL NIN' name, which blurs away into single dark hero images per specialty (a leather belt, a poke bowl, a blue Ferrari) with a side index, a portrait with bio, a 'Food, framed perfectly' section and a horizontal strip of selected work. Type: General Sans, Clash Display.
Ground and ink from the measured palette (#0D0C08, #282019, #545142). Motion carries the page through
a tilted wall of product shots blurring away into one dark hero photograph. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — studio product, food and car photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: studio product, food and car photography

## Reference lock

Primary reference/direction: Angel Nin - Video and Photography — A commercial photographer: a tilted wall of product and food shots under a yellow 'ANGEL NIN' name, which blurs away into single dark hero images per specialty (a leather belt, a poke bowl, a blue Ferrari) with a side index, a portrait with bio, a 'Food, framed perfectly' section and a horizontal strip of selected work.
Preserve (3-5 traits): tilted wall of every shot as the hero; yellow display name; dark studio product photography; side index switching specialty; horizontal selected-work strip.
Borrow only (1-2): Start on the wall of work, then isolate one hero frame; Blur the wall away to change scale
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: studio product, food and car photography
Reject: Small side index text; Dark-on-dark bio section
Token commitments: palette #0D0C08, #282019, #545142, #898050; type General Sans, Clash Display; engine GSAP + Lenis linked (never vendored).
