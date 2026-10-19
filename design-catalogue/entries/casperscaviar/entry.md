---
title: "Casper's Caviar"
url: https://casperscaviar.com/
source_url: https://casperscaviar.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: luxury-craft
category2: "consumer-brand"
family: caviar-tin-dark-luxury
dna: "Caviar brand x dark macro and script logo"
register: cinematic dark
grammar: chaptered editorial
lane: "A caviar shop that opens on a slow macro of pearls in a dark tin under a script-and-caps logo, then a shop grid of tins and plated dishes on white, a smoking metal case 'WHERE TASTE Meets Culture' with a postmark stamp, and 'NOT JUST CAVIAR, A MODERN RITUAL.' over a dark table spread."
mode: persuade
traits: ["macro caviar video hero", "script + condensed caps logo", "shop grid alternating tins and plated food", "smoking metal case image", "postmark stamp detail", "dark table close"]
palette: ["#1F1F1F", "#3A3A36", "#E8E6E4", "#9D9482", "#5F5347"]
type: ["sloop-script-one", "interstate", "interstate-condensed", "Lexend Giga"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The product's texture does the luxury: a slow, dark macro of the pearls, then plated dishes and the tin as a jewel. The page alternates dark mood and white shop panels, so the selling is clear without breaking the atmosphere.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Kyrylo Orlov).

## What to borrow (principle)

- Open on a slow macro of the product's texture
- A postmark/stamp detail as a small ownership mark
- Alternate dark mood sections with clean white shop panels

## What to leave

- Condensed caps headlines are cut by transitions
- Small product text

## Signature move

A slow macro of caviar pearls in a dark tin under a script logo.

## Motion

Intro: macro video of pearls resolving from blur (~2 s), logo fades in. Scroll (Lenis, ~130 px glide, 25 ScrollTriggers, SplitText): 'SHOP CAVIAR' with a grid where tins and dishes slide at different rates; smoking case with stamp; 'WHERE TASTE Meets Culture'; dark section 'NOT JUST CAVIAR, A MODERN RITUAL.' with a table spread that zooms; footer over the spread.

Measured (`motion/probe.json`): GSAP 3.14.1; 25 ScrollTriggers; Lenis; 2 video; split text; smoothed scroll (median 128 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a caviar shop that opens on a slow macro of pearls in a dark tin under a script-and-caps logo, then a shop grid of tins and plated dishes on white, a smoking metal case 'WHERE TASTE Meets Culture' with a postmark stamp, and 'NOT JUST CAVIAR, A MODERN RITUAL.' over a dark table spread. Type: sloop-script-one, interstate, interstate-condensed, Lexend Giga.
Ground and ink from the measured palette (#1F1F1F, #3A3A36, #E8E6E4). Motion carries the page through
a slow macro of caviar pearls in a dark tin under a script logo. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — dark food and product photography, macro texture, metal tins

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: dark food and product photography, macro texture, metal tins

## Reference lock

Primary reference/direction: Casper's Caviar — A caviar shop that opens on a slow macro of pearls in a dark tin under a script-and-caps logo, then a shop grid of tins and plated dishes on white, a smoking metal case 'WHERE TASTE Meets Culture' with a postmark stamp, and 'NOT JUST CAVIAR, A MODERN RITUAL.' over a dark table spread.
Preserve (3-5 traits): macro caviar video hero; script + condensed caps logo; shop grid alternating tins and plated food; smoking metal case image; postmark stamp detail.
Borrow only (1-2): Open on a slow macro of the product's texture; A postmark/stamp detail as a small ownership mark
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: dark food and product photography, macro texture, metal tins
Reject: Condensed caps headlines are cut by transitions; Small product text
Token commitments: palette #1F1F1F, #3A3A36, #E8E6E4, #9D9482, #5F5347; type sloop-script-one, interstate, interstate-condensed, Lexend Giga; engine GSAP + Lenis linked (never vendored).
