---
title: "Nicolas Giannantonio - Creative Developer"
url: https://nicolasgiannantonio.com/
source_url: https://nicolasgiannantonio.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: centred-single-image-folio
dna: "Creative developer x one centred project image at a time on white"
register: modern clean
grammar: gallery/catalog
lane: "A minimal folio on white: a name line, then one medium project image centred at a time (a sports site, a car-window photo, a business card, chairs, a portrait, a carpet campaign, a ring render, an app) with its title, role and year small at the left, each image sliding up and replacing the last."
mode: read
traits: ["one centred image at a time", "tiny metadata left", "white ground", "name and nav only", "clip reveal per image", "no headlines"]
palette: ["#FFFFFF", "#2C2725", "#979490", "#ABAAA4", "#494846", "#7C6C62"]
type: ["hv"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Restraint lets the work carry the page; the steady single-image rhythm reads like flipping a portfolio book.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Show one project image at a time with tiny metadata

## What to leave

- Very small type
- No hierarchy beyond the images

## Signature move

One centred project image at a time on an empty white page.

## Motion

Intro: white with the name (~1.5 s). Wheel (Lenis ~60 px glide): each image slides up from below with a clip and the previous one exits upward; metadata swaps at left.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 3 video; smoothed scroll (median 60 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a minimal folio on white: a name line, then one medium project image centred at a time (a sports site, a car-window photo, a business card, chairs, a portrait, a carpet campaign, a ring render, an app) with its title, role and year small at the left, each image sliding up and replacing the last. Type: hv.
Ground and ink from the measured palette (#FFFFFF, #2C2725, #979490). Motion carries the page through
one centred project image at a time on an empty white page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project photography and mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project photography and mockups

## Reference lock

Primary reference/direction: Nicolas Giannantonio - Creative Developer — A minimal folio on white: a name line, then one medium project image centred at a time (a sports site, a car-window photo, a business card, chairs, a portrait, a carpet campaign, a ring render, an app) with its title, role and year small at the left, each image sliding up and replacing the last.
Preserve (3-5 traits): one centred image at a time; tiny metadata left; white ground; name and nav only; clip reveal per image.
Borrow only (1-2): Show one project image at a time with tiny metadata
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project photography and mockups
Reject: Very small type; No hierarchy beyond the images
Token commitments: palette #FFFFFF, #2C2725, #979490, #ABAAA4, #494846, #7C6C62; type hv; engine GSAP + Lenis linked (never vendored).
