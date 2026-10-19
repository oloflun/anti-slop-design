---
title: "Cheese & Pixels"
url: https://cheeseandpixels.com/
source_url: https://cheeseandpixels.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: pixel-block-yellow-agency
dna: "Creative technology agency x pixel blocks and isometric room"
register: modern clean
grammar: chaptered editorial
lane: "A creative-tech agency where an isometric 3D office assembles behind a yellow-highlighted name, black pixel blocks scatter as transitions, and services, about and team sit in bright colour-blocked panels (yellow, lilac, sky)."
mode: persuade
traits: ["isometric 3D room hero", "black pixel-block scatter", "yellow highlight band under the name", "colour-blocked panels (yellow, lilac, sky)", "service list beside an image mosaic", "Unica One + Space Grotesk"]
palette: ["#FFFFF6", "#FEF100", "#010808", "#5C5842", "#CACD81", "#F9F575"]
type: ["Unica One", "Space Grotesk", "Mona Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The name contains the idea (pixels): black square pixels burst out of the hero and dissolve sections into the next. Panels are flat blocks of strong colour, so the page reads like a playful game UI while staying a plain agency structure.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Scatter square pixel blocks as the transition for a digital-craft brand
- Colour-block whole panels (yellow, lilac, sky) to separate chapters
- An isometric 3D model of the studio as the hero

## What to leave

- Generic team-photo grid
- Form-heavy close

## Signature move

Black pixel blocks bursting out of the isometric office into the yellow page.

## Motion

Intro: spinner, then the isometric office builds above 'CHEESE & PIXELS' on its yellow band (~2 s) and pixel blocks scatter. Scroll (window, WebGL x2, SplitText): yellow ground rises; 'Who We Are' types in with a 3D blob; black panel with services list beside an image mosaic, each service lighting in turn; lilac 'About'; sky 'Meet the Team'; black 'Get In Touch' with pixel blocks.

Measured (`motion/probe.json`): GSAP 3.14.2; WebGL canvas x2 (three.js); split text. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a creative-tech agency where an isometric 3D office assembles behind a yellow-highlighted name, black pixel blocks scatter as transitions, and services, about and team sit in bright colour-blocked panels (yellow, lilac, sky). Type: Unica One, Space Grotesk, Mona Sans.
Ground and ink from the measured palette (#FFFFF6, #FEF100, #010808). Motion carries the page through
black pixel blocks bursting out of the isometric office into the yellow page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — isometric 3D renders, team portraits, project mosaics

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: isometric 3D renders, team portraits, project mosaics

## Reference lock

Primary reference/direction: Cheese & Pixels — A creative-tech agency where an isometric 3D office assembles behind a yellow-highlighted name, black pixel blocks scatter as transitions, and services, about and team sit in bright colour-blocked panels (yellow, lilac, sky).
Preserve (3-5 traits): isometric 3D room hero; black pixel-block scatter; yellow highlight band under the name; colour-blocked panels (yellow, lilac, sky); service list beside an image mosaic.
Borrow only (1-2): Scatter square pixel blocks as the transition for a digital-craft brand; Colour-block whole panels (yellow, lilac, sky) to separate chapters
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: isometric 3D renders, team portraits, project mosaics
Reject: Generic team-photo grid; Form-heavy close
Token commitments: palette #FFFFF6, #FEF100, #010808, #5C5842, #CACD81, #F9F575; type Unica One, Space Grotesk, Mona Sans; engine GSAP + Lenis linked (never vendored).
