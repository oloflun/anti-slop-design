---
title: "Aerleum - Synthetic fuels from CO2"
url: https://aerleum.com/
source_url: https://aerleum.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "institutional"
family: climate-tech-dark-cards
dna: "Climate tech startup x dark rounded cards with line-drawn reactor parts"
register: modern clean
grammar: chaptered editorial
lane: "A climate-tech startup: a 000 counter on white, a statement about methanol, a dark rounded card with a silhouette photo and the founding story, dark cards for the technology (a checkerboard reactive adsorbent, a line-drawn single reactor), sector cards (maritime, aviation, chemicals, trucks), partner logos, team, hiring and an FAQ."
mode: persuade
traits: ["counter loader", "dark rounded cards", "line-drawn reactor", "checkerboard adsorbent graphic", "sector photo cards", "FAQ"]
palette: ["#FFFFFF", "#0C0C0C", "#5E5546", "#A5A7A1", "#4C3E31", "#777269"]
type: ["DM Sans", "Inter"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Clean and credible; the line-drawn reactor parts explain the technology simply.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Line drawings of the technology inside dark cards

## What to leave

- Cookie bar in every frame

## Signature move

A line-drawn reactor cylinder inside a dark card.

## Motion

Intro: white with a 000 counter (~2 s). Wheel (Lenis, 2 pins): statements slide; dark cards rise; the reactor draws; sector cards swap; logos fade in.

Measured (`motion/probe.json`): GSAP 3.12.5; 2 pinned sections; Lenis; Taxi page transitions; WebGL canvas x1 (three.js); 1 video; split text; smoothed scroll (median 203 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a climate-tech startup: a 000 counter on white, a statement about methanol, a dark rounded card with a silhouette photo and the founding story, dark cards for the technology (a checkerboard reactive adsorbent, a line-drawn single reactor), sector cards (maritime, aviation, chemicals, trucks), partner logos, team, hiring and an FAQ. Type: DM Sans, Inter.
Ground and ink from the measured palette (#FFFFFF, #0C0C0C, #5E5546). Motion carries the page through
a line-drawn reactor cylinder inside a dark card. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — photography, line drawings

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: photography, line drawings

## Reference lock

Primary reference/direction: Aerleum - Synthetic fuels from CO2 — A climate-tech startup: a 000 counter on white, a statement about methanol, a dark rounded card with a silhouette photo and the founding story, dark cards for the technology (a checkerboard reactive adsorbent, a line-drawn single reactor), sector cards (maritime, aviation, chemicals, trucks), partner logos, team, hiring and an FAQ.
Preserve (3-5 traits): counter loader; dark rounded cards; line-drawn reactor; checkerboard adsorbent graphic; sector photo cards.
Borrow only (1-2): Line drawings of the technology inside dark cards
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: photography, line drawings
Reject: Cookie bar in every frame
Token commitments: palette #FFFFFF, #0C0C0C, #5E5546, #A5A7A1, #4C3E31, #777269; type DM Sans, Inter; engine GSAP + Lenis linked (never vendored).
