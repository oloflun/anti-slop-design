---
title: "Studio Nuts - All Work"
url: https://studionuts.com.br/
source_url: https://studionuts.com.br/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: cgi-studio-two-up-grid
dna: "Brazilian CGI studio x a two-column grid of colourful campaign renders"
register: modern clean
grammar: gallery/catalog
lane: "A CGI studio work page: a percent loader on black, 'Thinking boldly. Crafting visually.' on white, filter chips, then a two-column grid of bright campaign renders (a man in a car, a wooden face, a framed chair, a squirrel, cereal mascot, Mountain Dew can, beetle, KFC, Hendrick's gin) with small tags."
mode: read
traits: ["percent loader", "two-column grid", "filter chips", "colourful CGI renders", "small tags", "white ground"]
palette: ["#FFFFFF", "#966556", "#4D2341", "#E5DED4", "#AFB3B2", "#101829"]
type: ["Opensauceone", "Acumin Pro Extra Condensed"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The work is so colourful that a plain grid is enough; the filter chips make it browsable.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Let a plain two-up grid carry very loud work

## What to leave

- No hierarchy or story

## Signature move

A two-column grid of bright CGI campaign renders.

## Motion

Intro: black with a percent counter (~2 s), a white panel. Wheel (smoothed ~100 px): the grid scrolls with images fading up; chips stay fixed.

Measured (`motion/probe.json`): GSAP 3.12.2; 10 ScrollTriggers; smoothed scroll (median 116 px still travelling after input stops); entry gate: Explore All Work. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a CGI studio work page: a percent loader on black, 'Thinking boldly. Crafting visually.' on white, filter chips, then a two-column grid of bright campaign renders (a man in a car, a wooden face, a framed chair, a squirrel, cereal mascot, Mountain Dew can, beetle, KFC, Hendrick's gin) with small tags. Type: Opensauceone, Acumin Pro Extra Condensed.
Ground and ink from the measured palette (#FFFFFF, #966556, #4D2341). Motion carries the page through
a two-column grid of bright CGI campaign renders. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — CGI campaign renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: CGI campaign renders

## Reference lock

Primary reference/direction: Studio Nuts - All Work — A CGI studio work page: a percent loader on black, 'Thinking boldly. Crafting visually.' on white, filter chips, then a two-column grid of bright campaign renders (a man in a car, a wooden face, a framed chair, a squirrel, cereal mascot, Mountain Dew can, beetle, KFC, Hendrick's gin) with small tags.
Preserve (3-5 traits): percent loader; two-column grid; filter chips; colourful CGI renders; small tags.
Borrow only (1-2): Let a plain two-up grid carry very loud work
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: CGI campaign renders
Reject: No hierarchy or story
Token commitments: palette #FFFFFF, #966556, #4D2341, #E5DED4, #AFB3B2, #101829; type Opensauceone, Acumin Pro Extra Condensed; engine GSAP + Lenis linked (never vendored).
