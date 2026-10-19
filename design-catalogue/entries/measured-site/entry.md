---
title: "Measured Analytics - Simple web analytics"
url: https://www.measured.site/
source_url: https://www.measured.site/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: tape-measure-mascot-saas
dna: "Simple web analytics x a blue 3D tape measure that follows you down the page"
register: modern clean
grammar: chaptered editorial
lane: "A small analytics product: the 'Measured' wordmark dissolves into a pixel field, a blue 3D tape measure parks in the top-left corner and stays there, a leaderboard of sites rolls past like a drum, then copy about the script, a black-and-blue feature block, pricing, testimonials and a closing 'Get Measured' with the tape measure centred between the words."
mode: persuade
traits: ["3D tape measure as recurring object", "pixel dissolve from the hero", "leaderboard rolling on a drum", "electric blue on white", "big plain sans", "the object returns for the CTA"]
palette: ["#FFFFFF", "#153BC9", "#5269D1", "#7387CE", "#B1B6C5", "#01014D"]
type: ["untitled"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The tape measure is the product's name made physical: it waits in the corner the whole way down and comes back to sit between 'Get' and 'Measured', so the page starts and ends on the same object.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Josh Chant).

## What to borrow (principle)

- A literal object for the product name that stays on screen and returns at the CTA
- A ranked list rolling on a drum

## What to leave

- Very small body text
- Feature cards look generic

## Signature move

A blue 3D tape measure that waits in the corner and lands between 'Get' and 'Measured'.

## Motion

Intro: white, then the wordmark and tape measure appear as a blue pixel field breaks up below (~2 s). Wheel (Lenis ~130 px glide): the pixels dissolve to white; the tape measure shrinks to the corner and turns as you scroll; leaderboard rows rotate in on a 3D drum; blocks slide up; at the end the tape measure grows back to the centre between the words.

Measured (`motion/probe.json`): GSAP 3.13.0/3.13.0; Lenis; WebGL canvas x3 (three.js); smoothed scroll (median 123 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a small analytics product: the 'Measured' wordmark dissolves into a pixel field, a blue 3D tape measure parks in the top-left corner and stays there, a leaderboard of sites rolls past like a drum, then copy about the script, a black-and-blue feature block, pricing, testimonials and a closing 'Get Measured' with the tape measure centred between the words. Type: untitled.
Ground and ink from the measured palette (#FFFFFF, #153BC9, #5269D1). Motion carries the page through
a blue 3D tape measure that waits in the corner and lands between 'Get' and 'Measured'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D render of one object, product UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D render of one object, product UI

## Reference lock

Primary reference/direction: Measured Analytics - Simple web analytics — A small analytics product: the 'Measured' wordmark dissolves into a pixel field, a blue 3D tape measure parks in the top-left corner and stays there, a leaderboard of sites rolls past like a drum, then copy about the script, a black-and-blue feature block, pricing, testimonials and a closing 'Get Measured' with the tape measure centred between the words.
Preserve (3-5 traits): 3D tape measure as recurring object; pixel dissolve from the hero; leaderboard rolling on a drum; electric blue on white; big plain sans.
Borrow only (1-2): A literal object for the product name that stays on screen and returns at the CTA; A ranked list rolling on a drum
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D render of one object, product UI
Reject: Very small body text; Feature cards look generic
Token commitments: palette #FFFFFF, #153BC9, #5269D1, #7387CE, #B1B6C5, #01014D; type untitled; engine GSAP + Lenis linked (never vendored).
