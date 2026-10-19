---
title: "CATCH THAT SANTA - Tote holiday game"
url: https://santa.tote.co.jp/
source_url: https://santa.tote.co.jp/
captured: 2026-10-03
origin: raw-url
extract: none
category: playful
category2: "consumer-brand"
family: holiday-argyle-game
dna: "Holiday campaign x an argyle field and a spinning Santa hat diamond"
register: other
grammar: live surface
lane: "A holiday mini-game: a dark starry screen with a tiny Santa hat and 'COMING SOMETHING' letters circling it, then a full red and green argyle field with a dark diamond in the middle where the hat sits and letters spin around it, an 'OPEN' badge beside it."
mode: experience
traits: ["red and green argyle field", "dark diamond centre", "letters orbiting the hat", "starry dark intro", "OPEN badge", "one-screen game"]
palette: ["#3BA188", "#080B20", "#59494E", "#562631", "#DD2846", "#AB4F61"]
type: ["Chelsea Market"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A seasonal pattern filling the screen and one object in the middle is all a short holiday game needs.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Fill the screen with a seasonal pattern and put one object in a cut-out shape

## What to leave

- No scroll content

## Signature move

A Santa hat in a dark diamond on a full argyle field.

## Motion

Intro: dark stars, the hat appears and the letters circle it (~8 s). Then: the argyle field fills; letters keep spinning around the hat; the badge wobbles.

Measured (`motion/probe.json`): GSAP 3.12.2; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the live surface grammar: a holiday mini-game: a dark starry screen with a tiny Santa hat and 'COMING SOMETHING' letters circling it, then a full red and green argyle field with a dark diamond in the middle where the hat sits and letters spin around it, an 'OPEN' badge beside it. Type: Chelsea Market.
Ground and ink from the measured palette (#3BA188, #080B20, #59494E). Motion carries the page through
a Santa hat in a dark diamond on a full argyle field. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — illustration, pattern

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: illustration, pattern

## Reference lock

Primary reference/direction: CATCH THAT SANTA - Tote holiday game — A holiday mini-game: a dark starry screen with a tiny Santa hat and 'COMING SOMETHING' letters circling it, then a full red and green argyle field with a dark diamond in the middle where the hat sits and letters spin around it, an 'OPEN' badge beside it.
Preserve (3-5 traits): red and green argyle field; dark diamond centre; letters orbiting the hat; starry dark intro; OPEN badge.
Borrow only (1-2): Fill the screen with a seasonal pattern and put one object in a cut-out shape
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: illustration, pattern
Reject: No scroll content
Token commitments: palette #3BA188, #080B20, #59494E, #562631, #DD2846, #AB4F61; type Chelsea Market; engine GSAP + Lenis linked (never vendored).
