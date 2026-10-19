---
title: "No Art"
url: https://www.noartmusic.com/
source_url: https://www.noartmusic.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: ""
family: festival-label-grid-poster
dna: "Music label and festival x Swiss grid with doodle wordmark"
register: modern clean
grammar: chaptered editorial
lane: "A festival label page on white with crop marks: a single crowd photo inside crop corners grows into a full-bleed aerial of a festival on a lake, then justified caps statements, colourful event posters, a wireframe globe of locations and a merch shop where only the hovered item is in colour."
mode: persuade
traits: ["crop-mark framed image that grows to full bleed", "hand-drawn doodle wordmark", "justified condensed caps statements", "wireframe globe with event pins", "colourful illustrated event posters", "greyed merch with the active item in colour"]
palette: ["#FFFFFF", "#283317", "#596229", "#BBB9B3", "#877B44", "#12100C"]
type: ["Nue Haas Grotesk Text Pro", "Chivomono", "JetBrains Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The page is a Swiss grid with print crop marks, and the life comes from its content: crowds, a hand-drawn logo and loud illustrated posters. The intro frames one photo with crop corners on white and grows it into the festival aerial, so the page literally opens onto the event.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: BORING).

## What to borrow (principle)

- Open by growing one framed photo (with crop marks) into the full-bleed hero
- A wireframe globe for a 'where we go' section
- Grey out a product row and colour only the active item

## What to leave

- Justified caps with wide gaps are uneven
- Very small mono metadata

## Signature move

A crowd photo inside print crop marks that grows into the full-bleed festival aerial.

## Motion

Intro: black 'broaden your mind', white flash with a square, then a crowd photo appears inside crop corners (~2.5 s) and grows to the full-bleed aerial with the doodle wordmark. Scroll (Lenis, ~120 px glide, SplitText, three.js): statement lines reveal; poster carousel with the active poster in colour; 'DISCOVER THE WORLD OF NO ART' with a rotating wireframe globe and pins; merch row greyed except the active product; footer grid.

Measured (`motion/probe.json`): GSAP 3.15.0; 1 ScrollTriggers; Lenis; WebGL canvas x1 (three.js); 1 video; split text; smoothed scroll (median 120 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a festival label page on white with crop marks: a single crowd photo inside crop corners grows into a full-bleed aerial of a festival on a lake, then justified caps statements, colourful event posters, a wireframe globe of locations and a merch shop where only the hovered item is in colour. Type: Nue Haas Grotesk Text Pro, Chivomono, JetBrains Mono.
Ground and ink from the measured palette (#FFFFFF, #283317, #596229). Motion carries the page through
a crowd photo inside print crop marks that grows into the full-bleed festival aerial. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — festival crowd photography, aerials, colourful illustrated event posters

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: festival crowd photography, aerials, colourful illustrated event posters

## Reference lock

Primary reference/direction: No Art — A festival label page on white with crop marks: a single crowd photo inside crop corners grows into a full-bleed aerial of a festival on a lake, then justified caps statements, colourful event posters, a wireframe globe of locations and a merch shop where only the hovered item is in colour.
Preserve (3-5 traits): crop-mark framed image that grows to full bleed; hand-drawn doodle wordmark; justified condensed caps statements; wireframe globe with event pins; colourful illustrated event posters.
Borrow only (1-2): Open by growing one framed photo (with crop marks) into the full-bleed hero; A wireframe globe for a 'where we go' section
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: festival crowd photography, aerials, colourful illustrated event posters
Reject: Justified caps with wide gaps are uneven; Very small mono metadata
Token commitments: palette #FFFFFF, #283317, #596229, #BBB9B3, #877B44, #12100C; type Nue Haas Grotesk Text Pro, Chivomono, JetBrains Mono; engine GSAP + Lenis linked (never vendored).
