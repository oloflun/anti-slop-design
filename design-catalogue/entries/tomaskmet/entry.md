---
title: "Tomas Kmet - Creative Web Developer"
url: https://www.tomaskmet.com/
source_url: https://www.tomaskmet.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: condensed-dev-folio-falling-cards
dna: "Creative developer x condensed titles and service cards falling with physics"
register: cinematic dark
grammar: chaptered editorial
lane: "A developer folio: 'TOMAS KMET' condensed over a blurred portrait, an about and awards on black, a cream 'SERVICES' where four black service cards drop in with physics and tumble, 'WORK' with numbered project images stepping down the page and 'GET IN TOUCH'."
mode: persuade
traits: ["condensed display caps", "blurred portrait", "service cards dropping with physics", "numbered stepped project images", "cream and black", "grainy muted photography"]
palette: ["#1B1918", "#BFBFB2", "#8B7A6F"]
type: ["PP Formula Black", "PP Neue Montreal Book"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Cards falling and tumbling onto the services section is a playful physical moment in an otherwise restrained page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Drop service cards in with physics

## What to leave

- Small body copy

## Signature move

Black service cards tumbling onto a cream 'SERVICES' title.

## Motion

Intro: black then the name over the portrait (~1.5 s). Wheel: about lines fade; the cream panel rises; cards fall one by one and settle tilted; 'WORK' with numbered images slides in a stepped diagonal; 'GET IN TOUCH' rises.

Measured (`motion/probe.json`): GSAP 3.14.2; WebGL canvas x1 (three.js). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a developer folio: 'TOMAS KMET' condensed over a blurred portrait, an about and awards on black, a cream 'SERVICES' where four black service cards drop in with physics and tumble, 'WORK' with numbered project images stepping down the page and 'GET IN TOUCH'. Type: PP Formula Black, PP Neue Montreal Book.
Ground and ink from the measured palette (#1B1918, #BFBFB2, #8B7A6F). Motion carries the page through
black service cards tumbling onto a cream 'SERVICES' title. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — muted project photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: muted project photography

## Reference lock

Primary reference/direction: Tomas Kmet - Creative Web Developer — A developer folio: 'TOMAS KMET' condensed over a blurred portrait, an about and awards on black, a cream 'SERVICES' where four black service cards drop in with physics and tumble, 'WORK' with numbered project images stepping down the page and 'GET IN TOUCH'.
Preserve (3-5 traits): condensed display caps; blurred portrait; service cards dropping with physics; numbered stepped project images; cream and black.
Borrow only (1-2): Drop service cards in with physics
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: muted project photography
Reject: Small body copy
Token commitments: palette #1B1918, #BFBFB2, #8B7A6F; type PP Formula Black, PP Neue Montreal Book; engine GSAP + Lenis linked (never vendored).
