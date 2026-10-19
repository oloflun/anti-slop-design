---
title: "Mister Pio - Peruvian rotisserie"
url: https://www.misterpio.com/
source_url: https://www.misterpio.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: "consumer-brand"
family: restaurant-sticker-magenta
dna: "Peruvian chicken restaurant x magenta ground, stickers and ember footage"
register: other
grammar: chaptered editorial
lane: "A restaurant site on magenta: a rotating circular logo, scattered photo stickers (peppers, roast chicken on a plate, a toy, mountains), an ember video, 'Experience the authentic flavors of Peru' with a 'Menu Menu Menu' marquee over a torn-paper menu card, a purple 'About' with tilted photos, a circular badge and 'Contact' marquee with a staff photo footer."
mode: persuade
traits: ["magenta and periwinkle", "photo stickers scattered", "ember video interlude", "repeated word marquees", "torn-paper menu", "circular rotating badge"]
palette: ["#E065E3", "#8C9CF6", "#190204", "#563150", "#E2E2E2", "#A277B0"]
type: ["Caveat", "futuraPT", "futuraPTCond"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The sticker collage and ember footage make a small restaurant feel loud and fun, and the marquee per section keeps navigation obvious.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One repeated word marquee per section as its title

## What to leave

- Very busy collage

## Signature move

Photo stickers scattered on magenta around a rotating rotisserie badge.

## Motion

Intro: magenta with the logo rotating (~2 s). Wheel: stickers scatter and drift; the ember video wipes in; marquees run; the menu card tilts in; photos tilt; the badge rotates; the footer wordmark rises.

Measured (`motion/probe.json`): GSAP 3.12.7; 1 video. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a restaurant site on magenta: a rotating circular logo, scattered photo stickers (peppers, roast chicken on a plate, a toy, mountains), an ember video, 'Experience the authentic flavors of Peru' with a 'Menu Menu Menu' marquee over a torn-paper menu card, a purple 'About' with tilted photos, a circular badge and 'Contact' marquee with a staff photo footer. Type: Caveat, futuraPT, futuraPTCond.
Ground and ink from the measured palette (#E065E3, #8C9CF6, #190204). Motion carries the page through
photo stickers scattered on magenta around a rotating rotisserie badge. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — food photography, stickers, ember video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: food photography, stickers, ember video

## Reference lock

Primary reference/direction: Mister Pio - Peruvian rotisserie — A restaurant site on magenta: a rotating circular logo, scattered photo stickers (peppers, roast chicken on a plate, a toy, mountains), an ember video, 'Experience the authentic flavors of Peru' with a 'Menu Menu Menu' marquee over a torn-paper menu card, a purple 'About' with tilted photos, a circular badge and 'Contact' marquee with a staff photo footer.
Preserve (3-5 traits): magenta and periwinkle; photo stickers scattered; ember video interlude; repeated word marquees; torn-paper menu.
Borrow only (1-2): One repeated word marquee per section as its title
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: food photography, stickers, ember video
Reject: Very busy collage
Token commitments: palette #E065E3, #8C9CF6, #190204, #563150, #E2E2E2, #A277B0; type Caveat, futuraPT, futuraPTCond; engine GSAP + Lenis linked (never vendored).
