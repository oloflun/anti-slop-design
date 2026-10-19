---
title: "Jay Chauhan - Portfolio"
url: https://jaychauhan.framer.website/
source_url: https://jaychauhan.framer.website/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: dark-framer-dev-folio-sanskrit
dna: "Software engineer folio x heavy sans on black with Sanskrit verse and 3D trident"
register: cinematic dark
grammar: chaptered editorial
lane: "A developer folio on black: bracket-percent loader, 'I'M JAY CHAUHAN BASED IN GUJARAT, IND.' under a stone sculpture, a three-step process row, project tiles, a green swirl behind an illustrated self-portrait, numbered services over a script word, an experience list, a Sanskrit verse with 3D tech logos floating around it and a red 3D trident, stack icons and a blue/green 'Let's work together'."
mode: persuade
traits: ["bracket percent loader", "heavy condensed sans on black", "green swirl texture", "numbered services with outline numerals", "Sanskrit verse as a section", "3D trident and floating tech logos"]
palette: ["#000000", "#A5A5A5", "#444344", "#FFFFFF", "#E0E0E0", "#6B6B6B"]
type: ["Kalam Bold", "Kalam Light", "Inter", "Inter Display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The Sanskrit verse and trident give a generic dev folio a personal identity, and the 3D logos orbiting the verse make the stack section feel like a devotion rather than a list.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A cultural artefact as the turning point of a personal page
- Tech logos as floating 3D objects around one centrepiece

## What to leave

- Loader takes long and shows nothing
- Many unrelated sections

## Signature move

3D tech logos and a red trident floating around a Sanskrit verse on black.

## Motion

Intro: black with a bracketed percent counter for several seconds, then the headline and sculpture fade in. Wheel (Lenis ~130 px glide): sections slide up with split-line reveals; the green swirl drifts behind the portrait; service numerals roll from 01 to 04; around the verse JS, triangle, leaf and Next logos float in from the edges and the trident rises; the closing words fill blue and green.

Measured (`motion/probe.json`): GSAP 3.11.3; Lenis; WebGL canvas x1; smoothed scroll (median 137 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a developer folio on black: bracket-percent loader, 'I'M JAY CHAUHAN BASED IN GUJARAT, IND.' under a stone sculpture, a three-step process row, project tiles, a green swirl behind an illustrated self-portrait, numbered services over a script word, an experience list, a Sanskrit verse with 3D tech logos floating around it and a red 3D trident, stack icons and a blue/green 'Let's work together'. Type: Kalam Bold, Kalam Light, Inter, Inter Display.
Ground and ink from the measured palette (#000000, #A5A5A5, #444344). Motion carries the page through
3D tech logos and a red trident floating around a Sanskrit verse on black. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D renders, illustrated portrait, project screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D renders, illustrated portrait, project screenshots

## Reference lock

Primary reference/direction: Jay Chauhan - Portfolio — A developer folio on black: bracket-percent loader, 'I'M JAY CHAUHAN BASED IN GUJARAT, IND.' under a stone sculpture, a three-step process row, project tiles, a green swirl behind an illustrated self-portrait, numbered services over a script word, an experience list, a Sanskrit verse with 3D tech logos floating around it and a red 3D trident, stack icons and a blue/green 'Let's work together'.
Preserve (3-5 traits): bracket percent loader; heavy condensed sans on black; green swirl texture; numbered services with outline numerals; Sanskrit verse as a section.
Borrow only (1-2): A cultural artefact as the turning point of a personal page; Tech logos as floating 3D objects around one centrepiece
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D renders, illustrated portrait, project screenshots
Reject: Loader takes long and shows nothing; Many unrelated sections
Token commitments: palette #000000, #A5A5A5, #444344, #FFFFFF, #E0E0E0, #6B6B6B; type Kalam Bold, Kalam Light, Inter, Inter Display; engine GSAP + Lenis linked (never vendored).
