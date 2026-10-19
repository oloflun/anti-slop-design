---
title: "Victor Furuya"
url: https://victorfuruya.com/
source_url: https://victorfuruya.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: mono-portrait-pixel-dissolve
dna: "Multidisciplinary designer x black-and-white portrait and pixel dissolve"
register: cinematic dark
grammar: filmic one-shot
lane: "A black folio that counts 44 → 100, opens a small black-and-white portrait that grows to full frame, drops a black card 'Make It Last ’26' over it, then dissolves the card in pixel blocks into a statement that brightens word by word."
mode: experience
traits: ["counter loader", "portrait growing from a small frame to full", "black title card over the portrait", "pixel-block dissolve", "statement brightening word by word", "ScrollSmoother + 7 pins"]
palette: ["#000000", "#3A3A3A", "#5F5F5F", "#1B1B1B", "#7A7A7A", "#9B9B9B"]
type: ["Satoshi"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Three moves in sequence, each a different material: a photo that grows, a card that lands on it, a pixel dissolve that removes the card. The statement then comes up out of the dark word by word. It is a short, well-ordered chain of transitions.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Victor Furuya).

## What to borrow (principle)

- Chain three distinct transitions (grow, overlay card, pixel dissolve) for the intro
- Brighten a statement word by word out of the dark

## What to leave

- Captured virtually; content beyond the statement not reached
- Very little content

## Signature move

A 'Make It Last ’26' card that dissolves in pixel blocks off the portrait.

## Motion

Intro: counter 44 → 100 on black (~1.5 s), a small portrait appears and grows to full frame. Scroll (ScrollSmoother, 7 pins, SplitText): a black card with 'Make It Last ’26' drops over the portrait, expands, then breaks into pixel blocks; 'Unforgettable memories are not defined by details.' brightens word by word from grey.

Measured (`motion/probe.json`): GSAP 3.15.0; 7 pinned sections; Lenis; ScrollSmoother; split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Close, Close. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a black folio that counts 44 → 100, opens a small black-and-white portrait that grows to full frame, drops a black card 'Make It Last ’26' over it, then dissolves the card in pixel blocks into a statement that brightens word by word. Type: Satoshi.
Ground and ink from the measured palette (#000000, #3A3A3A, #5F5F5F). Motion carries the page through
a 'Make It Last ’26' card that dissolves in pixel blocks off the portrait. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — black-and-white studio portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: black-and-white studio portrait

## Reference lock

Primary reference/direction: Victor Furuya — A black folio that counts 44 → 100, opens a small black-and-white portrait that grows to full frame, drops a black card 'Make It Last ’26' over it, then dissolves the card in pixel blocks into a statement that brightens word by word.
Preserve (3-5 traits): counter loader; portrait growing from a small frame to full; black title card over the portrait; pixel-block dissolve; statement brightening word by word.
Borrow only (1-2): Chain three distinct transitions (grow, overlay card, pixel dissolve) for the intro; Brighten a statement word by word out of the dark
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: black-and-white studio portrait
Reject: Captured virtually; content beyond the statement not reached; Very little content
Token commitments: palette #000000, #3A3A3A, #5F5F5F, #1B1B1B, #7A7A7A, #9B9B9B; type Satoshi; engine GSAP + Lenis linked (never vendored).
