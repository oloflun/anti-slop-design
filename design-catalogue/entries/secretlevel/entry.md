---
title: "Secret Level"
url: https://www.secretlevel.co/
source_url: https://www.secretlevel.co/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: stacked-title-film-cards
dna: "AI entertainment studio x stacked full-width film cards"
register: cinematic dark
grammar: rhythmic cutlist
lane: "An AI entertainment studio whose page is a deck of full-width film cards, each with a huge white condensed title (ASHWICK, THE HEIST 3, EAST LA, STITCHED TOGETHER), sliding up over the previous one while a thumbnail rail at the left marks the current film."
mode: persuade
traits: ["full-width film cards stacking", "huge condensed white titles", "thumbnail rail as index", "dark cinematic grade", "client and original labels"]
palette: ["#070506", "#24221F", "#4E4843", "#6D6B68", "#BFBCB7"]
type: ["aeonikCondensed", "aeonikFono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Like Sadu Media's reel but more uniform: every project is the same full-width card with a title in the same huge face, and the deck slides card over card, so the studio's range reads through a single repeating gesture. The left thumbnail rail tells you where you are.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Make every project the same full-width card so the deck has one rhythm
- A thumbnail rail along the edge as the position indicator

## What to leave

- Cards slide before the title is readable in places
- Repetitive after many cards

## Signature move

Full-width film cards with huge titles stacking one over the next.

## Motion

Intro: black, then the hero film card 'AN ENTERTAINMENT STUDIO POWERED BY AI' (~2.5 s). Scroll (Lenis, ~60–120 px glide): each film card slides up over the previous; title and buttons sit at the card top; the thumbnail rail at the left highlights the active film; the deck loops back to the hero card.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; 8 video; smoothed scroll (median 73 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: an AI entertainment studio whose page is a deck of full-width film cards, each with a huge white condensed title (ASHWICK, THE HEIST 3, EAST LA, STITCHED TOGETHER), sliding up over the previous one while a thumbnail rail at the left marks the current film. Type: aeonikCondensed, aeonikFono.
Ground and ink from the measured palette (#070506, #24221F, #4E4843). Motion carries the page through
full-width film cards with huge titles stacking one over the next. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — cinematic film stills, warm and moody grade

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: cinematic film stills, warm and moody grade

## Reference lock

Primary reference/direction: Secret Level — An AI entertainment studio whose page is a deck of full-width film cards, each with a huge white condensed title (ASHWICK, THE HEIST 3, EAST LA, STITCHED TOGETHER), sliding up over the previous one while a thumbnail rail at the left marks the current film.
Preserve (3-5 traits): full-width film cards stacking; huge condensed white titles; thumbnail rail as index; dark cinematic grade; client and original labels.
Borrow only (1-2): Make every project the same full-width card so the deck has one rhythm; A thumbnail rail along the edge as the position indicator
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: cinematic film stills, warm and moody grade
Reject: Cards slide before the title is readable in places; Repetitive after many cards
Token commitments: palette #070506, #24221F, #4E4843, #6D6B68, #BFBCB7; type aeonikCondensed, aeonikFono; engine GSAP + Lenis linked (never vendored).
