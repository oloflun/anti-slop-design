---
title: "Studio375"
url: https://375.studio/
source_url: https://375.studio/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: neon-blur-italian-agency
dna: "Vicenza agency x neon gradient blur and floating type"
register: cinematic dark
grammar: chaptered editorial
lane: "A dark agency page that loads with a huge percentage, opens on a neon blue-magenta blur under a serif-italic line, then shows cases as large photographs with a coloured circle cursor and floating title, a scrambled 'Featured' word, and a neon closing image."
mode: persuade
traits: ["huge percentage loader", "neon blue/magenta gradient blur", "serif with italic words", "big case photos with coloured circle marker", "letter-jumbling section titles", "Italian copy"]
palette: ["#000000", "#9D655E", "#282A2B", "#D8D5BE", "#693947"]
type: ["hatton", "neue"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Two signatures: neon gradient light at the open and close, and section titles whose letters jumble up and down as they settle ('Feaᵗᵘred', 'Awardˢ'). The cases between are big quiet photographs, so the neon frames the work rather than competing.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Studio375).

## What to borrow (principle)

- Bookend a page with the same neon light (open and close)
- Let section titles' letters jump and settle into place

## What to leave

- Cookie banner across every frame
- Coloured circle cursor overlaps the photos

## Signature move

Section titles whose letters jumble vertically before settling.

## Motion

Intro: black with 'Loading' and a percentage 0 → 59 → 100 (~2.5 s). Scroll (Lenis, ~140 px glide, SplitText, three.js): neon blur hero with 'The creative studio you've been eager to meet'; serif intro; 'Featured' letters jump; case photos (Cantina Bartolomeo, Tamashii, Palladiana, Mioni, Intrapan) with floating titles and a coloured circle; services grid; 'Awards' table; neon close with contact.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x1 (three.js); split text; smoothed scroll (median 138 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a dark agency page that loads with a huge percentage, opens on a neon blue-magenta blur under a serif-italic line, then shows cases as large photographs with a coloured circle cursor and floating title, a scrambled 'Featured' word, and a neon closing image. Type: hatton, neue.
Ground and ink from the measured palette (#000000, #9D655E, #282A2B). Motion carries the page through
section titles whose letters jumble vertically before settling. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product and food photography with warm light, neon gradients

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product and food photography with warm light, neon gradients

## Reference lock

Primary reference/direction: Studio375 — A dark agency page that loads with a huge percentage, opens on a neon blue-magenta blur under a serif-italic line, then shows cases as large photographs with a coloured circle cursor and floating title, a scrambled 'Featured' word, and a neon closing image.
Preserve (3-5 traits): huge percentage loader; neon blue/magenta gradient blur; serif with italic words; big case photos with coloured circle marker; letter-jumbling section titles.
Borrow only (1-2): Bookend a page with the same neon light (open and close); Let section titles' letters jump and settle into place
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product and food photography with warm light, neon gradients
Reject: Cookie banner across every frame; Coloured circle cursor overlaps the photos
Token commitments: palette #000000, #9D655E, #282A2B, #D8D5BE, #693947; type hatton, neue; engine GSAP + Lenis linked (never vendored).
