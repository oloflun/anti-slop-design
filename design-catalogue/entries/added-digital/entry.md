---
title: "ADDED - Digital Studio and Webflow Agency Stockholm"
url: https://www.added.digital/
source_url: https://www.added.digital/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: stacking-case-cards-agency
dna: "Stockholm Webflow agency x stacked case cards sliding over each other"
register: cinematic dark
grammar: rhythmic cutlist
lane: "An agency on black: a stacked 'AD / DE / D' wordmark, then a sequence of case cards (Greenely, Supernormal Greens, Kungliga Tennisklubben, Sylvera, Neumeister) where each new card slides up over the previous one in the centre of the screen, a numbered services list and a pill-pattern footer."
mode: persuade
traits: ["stacked three-line wordmark", "case cards sliding over each other", "each card its own brand colour", "numbered service list", "pill pattern footer", "Swedish/English toggle"]
palette: ["#0A0A0A", "#FCFBEE", "#282D74", "#636A6D"]
type: ["Nhaasgrotesktxpro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

One move, used well: each case card rises over the last, so the work reads as a deck of brand colours.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Slide case cards up over each other in a fixed frame

## What to leave

- Little beyond the card stack
- Small service text

## Signature move

Brand-coloured case cards sliding up over each other on black.

## Motion

Intro: black, the stacked wordmark types in (~1.5 s). Wheel (Lenis plus ScrollSmoother, 40 triggers): the first card rises from below; each following card slides up and covers the previous one while its logo scales slightly; the services numbers roll; the pill pattern fades in.

Measured (`motion/probe.json`): GSAP 3.15.0; 40 ScrollTriggers; Lenis; ScrollSmoother; split text; smoothed scroll (median 96 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: an agency on black: a stacked 'AD / DE / D' wordmark, then a sequence of case cards (Greenely, Supernormal Greens, Kungliga Tennisklubben, Sylvera, Neumeister) where each new card slides up over the previous one in the centre of the screen, a numbered services list and a pill-pattern footer. Type: Nhaasgrotesktxpro.
Ground and ink from the measured palette (#0A0A0A, #FCFBEE, #282D74). Motion carries the page through
brand-coloured case cards sliding up over each other on black. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — brand case imagery

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: brand case imagery

## Reference lock

Primary reference/direction: ADDED - Digital Studio and Webflow Agency Stockholm — An agency on black: a stacked 'AD / DE / D' wordmark, then a sequence of case cards (Greenely, Supernormal Greens, Kungliga Tennisklubben, Sylvera, Neumeister) where each new card slides up over the previous one in the centre of the screen, a numbered services list and a pill-pattern footer.
Preserve (3-5 traits): stacked three-line wordmark; case cards sliding over each other; each card its own brand colour; numbered service list; pill pattern footer.
Borrow only (1-2): Slide case cards up over each other in a fixed frame
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: brand case imagery
Reject: Little beyond the card stack; Small service text
Token commitments: palette #0A0A0A, #FCFBEE, #282D74, #636A6D; type Nhaasgrotesktxpro; engine GSAP + Lenis linked (never vendored).
