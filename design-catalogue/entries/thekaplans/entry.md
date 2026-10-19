---
title: "The Kaplans - Film and Photo"
url: https://www.thekaplans.studio/
source_url: https://www.thekaplans.studio/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "consumer-brand"
family: product-film-duo-colour-split
dna: "Commercial product film duo x giant name with a split-colour reel"
register: other
grammar: filmic one-shot
lane: "A product filmmaking duo: 'The Kaplans' huge on yellow with 'Film' and 'Photo' at the bottom, a strip of shots that grows into a central reel on a blue ground of sliding thumbnails, the reel cutting between product shots on a split orange/blue set (a peanut butter cup, an Oreo)."
mode: experience
traits: ["giant name on yellow then blue", "split orange/blue product set", "central reel", "thumbnails sliding behind", "Film / Photo labels", "bold grotesk"]
palette: ["#0968D7", "#043597", "#020612", "#F2BE25", "#2C1D18", "#E55203"]
type: ["Youth"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The split-colour set is the brand look and the reel shows it immediately.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A strip of thumbnails that grows into the hero reel

## What to leave

- Nothing beyond the reel captured

## Signature move

Peanut butter cups and Oreos on a split orange and blue set.

## Motion

Intro: white then yellow with the name (~1.5 s); thumbnails slide in under it and the middle one scales up as the ground turns blue. Scroll: the reel plays; thumbnails drift.

Measured (`motion/probe.json`): GSAP 3.12.5; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the filmic one-shot grammar: a product filmmaking duo: 'The Kaplans' huge on yellow with 'Film' and 'Photo' at the bottom, a strip of shots that grows into a central reel on a blue ground of sliding thumbnails, the reel cutting between product shots on a split orange/blue set (a peanut butter cup, an Oreo). Type: Youth.
Ground and ink from the measured palette (#0968D7, #043597, #020612). Motion carries the page through
peanut butter cups and Oreos on a split orange and blue set. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product film

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product film

## Reference lock

Primary reference/direction: The Kaplans - Film and Photo — A product filmmaking duo: 'The Kaplans' huge on yellow with 'Film' and 'Photo' at the bottom, a strip of shots that grows into a central reel on a blue ground of sliding thumbnails, the reel cutting between product shots on a split orange/blue set (a peanut butter cup, an Oreo).
Preserve (3-5 traits): giant name on yellow then blue; split orange/blue product set; central reel; thumbnails sliding behind; Film / Photo labels.
Borrow only (1-2): A strip of thumbnails that grows into the hero reel
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product film
Reject: Nothing beyond the reel captured
Token commitments: palette #0968D7, #043597, #020612, #F2BE25, #2C1D18, #E55203; type Youth; engine GSAP + Lenis linked (never vendored).
