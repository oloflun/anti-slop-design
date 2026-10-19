---
title: "All Things WTF"
url: https://www.allthingswtf.com/
source_url: https://www.allthingswtf.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: sticker-collage-youth-media
dna: "Youth media brand x cream paper, condensed caps that tumble letter by letter, stickers and portrait cut-outs"
register: illustrated dark
grammar: typographic poster
lane: "A media brand for young India: 'WTF is happening?' in mixed condensed caps on dotted cream, 'Good question.', an Enter gate, portrait photos sliding in with 'engine for young India', then a black board with stickers (flowers, lips, badges) scattered while one long sentence ('India's next chapter will be built by those who refused to wait.') crosses the screen with each letter dropping into place from a tilt."
mode: experience
traits: ["mixed-weight condensed caps", "dotted cream paper", "sticker scatter", "letters tumbling into a sentence", "portrait cut-outs", "coloured tab stack at the edge"]
palette: ["#272523", "#E2D9C9", "#706355"]
type: ["Poppins", "Hakobi", "New Spirit"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Letters landing one by one at odd angles make a slogan feel shouted by a crowd rather than set by a designer.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Visual Identity).

## What to borrow (principle)

- Drop a long sentence letter by letter from tilts across a pinned board

## What to leave

- Enter gate on a manifesto page

## Signature move

'India's next chapter will be built by those who refused to wait' landing letter by letter.

## Motion

Intro: two questions in mixed type (~3 s), Enter gate. Wheel (Lenis, 6 pins): portraits slide; the board pins while letters fall and rotate into place; stickers drift.

Measured (`motion/probe.json`): GSAP 3.14.2; 6 pinned sections; Lenis; Locomotive; smoothed scroll (median 148 px still travelling after input stops); entry gate: Enter. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the typographic poster grammar: a media brand for young India: 'WTF is happening?' in mixed condensed caps on dotted cream, 'Good question.', an Enter gate, portrait photos sliding in with 'engine for young India', then a black board with stickers (flowers, lips, badges) scattered while one long sentence ('India's next chapter will be built by those who refused to wait.') crosses the screen with each letter dropping into place from a tilt. Type: Poppins, Hakobi, New Spirit.
Ground and ink from the measured palette (#272523, #E2D9C9, #706355). Motion carries the page through
'India's next chapter will be built by those who refused to wait' landing letter by letter. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — portrait photography, stickers

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: portrait photography, stickers

## Reference lock

Primary reference/direction: All Things WTF — A media brand for young India: 'WTF is happening?' in mixed condensed caps on dotted cream, 'Good question.', an Enter gate, portrait photos sliding in with 'engine for young India', then a black board with stickers (flowers, lips, badges) scattered while one long sentence ('India's next chapter will be built by those who refused to wait.') crosses the screen with each letter dropping into place from a tilt.
Preserve (3-5 traits): mixed-weight condensed caps; dotted cream paper; sticker scatter; letters tumbling into a sentence; portrait cut-outs.
Borrow only (1-2): Drop a long sentence letter by letter from tilts across a pinned board
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: portrait photography, stickers
Reject: Enter gate on a manifesto page
Token commitments: palette #272523, #E2D9C9, #706355; type Poppins, Hakobi, New Spirit; engine GSAP + Lenis linked (never vendored).
