---
title: "Studio Tyrsa"
url: https://www.studiotyrsa.com/
source_url: https://www.studiotyrsa.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "luxury-craft"
family: lettering-wall-grid
dna: "Paris lettering studio x dense logo-and-poster wall"
register: modern clean
grammar: gallery/catalog
lane: "A lettering and identity studio: a Forever King Nike lockup over a portrait opens, then 'All Projects' becomes an endless three-column wall of logos, posters and type pieces that scrolls as one surface."
mode: read
traits: ["hero project as full bleed lockup", "three-up wall of type-led work", "logo rows on white between image rows", "small grey captions under tiles", "floating sticker logo top left", "custom cursor ring"]
palette: ["#FFFFFF", "#E1E2DD", "#1B2A27", "#091016", "#5F6161", "#A6A9AD"]
type: ["Untitled Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

For a lettering studio the work is the typography, so the site gets out of the way: one hero lockup and then wall after wall of logos and posters where every tile is a type specimen.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Studio Tyrsa).

## What to borrow (principle)

- Open on one hero piece, then let the work wall run
- Alternate image rows with white logo rows for rhythm

## What to leave

- Very small captions
- No section breaks in a long wall

## Signature move

An endless wall of lettering, logos and posters under a Forever King hero.

## Motion

Intro: white, the hero lockup fades in over the portrait. Wheel (Lenis, ~110 px glide): the wall scrolls as one surface with slight per-column parallax; tiles fade up as they enter; a sticker logo stays fixed top left.

Measured (`motion/probe.json`): GSAP 3.12.7; Lenis; WebGL canvas x1 (three.js); 7 video; split text; smoothed scroll (median 113 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a lettering and identity studio: a Forever King Nike lockup over a portrait opens, then 'All Projects' becomes an endless three-column wall of logos, posters and type pieces that scrolls as one surface. Type: Untitled Sans.
Ground and ink from the measured palette (#FFFFFF, #E1E2DD, #1B2A27). Motion carries the page through
an endless wall of lettering, logos and posters under a Forever King hero. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — lettering, logos, posters and product photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: lettering, logos, posters and product photography

## Reference lock

Primary reference/direction: Studio Tyrsa — A lettering and identity studio: a Forever King Nike lockup over a portrait opens, then 'All Projects' becomes an endless three-column wall of logos, posters and type pieces that scrolls as one surface.
Preserve (3-5 traits): hero project as full bleed lockup; three-up wall of type-led work; logo rows on white between image rows; small grey captions under tiles; floating sticker logo top left.
Borrow only (1-2): Open on one hero piece, then let the work wall run; Alternate image rows with white logo rows for rhythm
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: lettering, logos, posters and product photography
Reject: Very small captions; No section breaks in a long wall
Token commitments: palette #FFFFFF, #E1E2DD, #1B2A27, #091016, #5F6161, #A6A9AD; type Untitled Sans; engine GSAP + Lenis linked (never vendored).
