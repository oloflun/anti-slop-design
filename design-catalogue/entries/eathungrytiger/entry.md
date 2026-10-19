---
title: "Hungry Tiger - bold Indian sauces"
url: https://www.eathungrytiger.com/
source_url: https://www.eathungrytiger.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "hospitality"
family: tumbling-jar-sauce-brand
dna: "Sauce brand x rust ground with paint texture, one jar tumbling through every frame, hot pink and saffron sections"
register: warm photographic
grammar: filmic one-shot
lane: "A sauce brand: 'Bold flavor' in huge saffron caps with the tikka masala jar below, the jar tumbling and turning as the camera follows it through 'A new angle of flavor', 'Unwrap the adventure' (the jar spinning through the words), 'A new perspective on taste', a hand catching it on a hot pink brushstroke ground ('What's inside', 'No fillers, no shortcuts'), a saffron 'Tradition & creation' with food photos and 'Why the jar matters'."
mode: persuade
traits: ["one jar tumbling across sections", "huge saffron condensed caps", "paint-textured rust ground", "hand catching the jar on pink", "food photography on saffron"]
palette: ["#883813", "#DF8D2B", "#52220F"]
type: ["Salmond", "Graphikx"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The tumbling jar is the thread: it falls through every headline, so the product is in every frame without repeating a packshot.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Artemii Lebedev).

## What to borrow (principle)

- Let the product tumble through the headlines as the page's thread

## What to leave

- Tiny body copy

## Signature move

A tikka masala jar tumbling through 'Unwrap the adventure'.

## Motion

Wheel (Lenis, 11 triggers): the jar rotates and translates along a path; headlines reveal by line; the jar lands in a hand; sections wipe colour; photos parallax.

Measured (`motion/probe.json`): GSAP 3.11.3; 11 ScrollTriggers; Lenis; split text; smoothed scroll (median 93 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the filmic one-shot grammar: a sauce brand: 'Bold flavor' in huge saffron caps with the tikka masala jar below, the jar tumbling and turning as the camera follows it through 'A new angle of flavor', 'Unwrap the adventure' (the jar spinning through the words), 'A new perspective on taste', a hand catching it on a hot pink brushstroke ground ('What's inside', 'No fillers, no shortcuts'), a saffron 'Tradition & creation' with food photos and 'Why the jar matters'. Type: Salmond, Graphikx.
Ground and ink from the measured palette (#883813, #DF8D2B, #52220F). Motion carries the page through
a tikka masala jar tumbling through 'Unwrap the adventure'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product cut-out, food photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product cut-out, food photography

## Reference lock

Primary reference/direction: Hungry Tiger - bold Indian sauces — A sauce brand: 'Bold flavor' in huge saffron caps with the tikka masala jar below, the jar tumbling and turning as the camera follows it through 'A new angle of flavor', 'Unwrap the adventure' (the jar spinning through the words), 'A new perspective on taste', a hand catching it on a hot pink brushstroke ground ('What's inside', 'No fillers, no shortcuts'), a saffron 'Tradition & creation' with food photos and 'Why the jar matters'.
Preserve (3-5 traits): one jar tumbling across sections; huge saffron condensed caps; paint-textured rust ground; hand catching the jar on pink; food photography on saffron.
Borrow only (1-2): Let the product tumble through the headlines as the page's thread
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product cut-out, food photography
Reject: Tiny body copy
Token commitments: palette #883813, #DF8D2B, #52220F; type Salmond, Graphikx; engine GSAP + Lenis linked (never vendored).
