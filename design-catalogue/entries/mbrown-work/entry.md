---
title: "Michael Brown - Creative and Design Director"
url: https://www.mbrown.work/
source_url: https://www.mbrown.work/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: giant-initials-brown-folio
dna: "Creative director x giant condensed initials and monochrome cases on brown"
register: editorial print
grammar: chaptered editorial
lane: "A creative director's folio on dark brown: a stack of print pieces as the loader, giant condensed 'M' and 'B' at opposite corners with a portrait between, statements in mono caps, a client list where the hovered row turns cream, monochrome full-bleed case images with labels, a scattered archive of small images around 'Past work, lasting pride' and a large condensed closing line."
mode: read
traits: ["giant condensed initials at corners", "dark brown and cream", "monochrome case images", "client list row highlight", "scattered archive thumbnails", "mono caps labels"]
palette: ["#271504", "#979695", "#7D7C7B", "#605C5A", "#4A4541", "#E2D5CB"]
type: ["Saans", "Saans Mono", "Neue Corp Tight"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The giant initials framing the portrait and the restrained brown-and-cream palette give a personal brand gravity.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Put the initials at opposite corners as the hero frame
- A scattered archive around a centred line

## What to leave

- Small mono text

## Signature move

A giant 'M' and 'B' at opposite corners framing a portrait.

## Motion

Intro: print pieces stack in the centre (~2 s), the initials slide in. Wheel (Lenis, 1 pin): the 'B' slides up; statements reveal; list rows highlight; cases scale to full bleed; archive thumbnails pop in around the centre text; the closing line rises.

Measured (`motion/probe.json`): GSAP 3.15.0; 11 ScrollTriggers; 1 pinned sections; Lenis; split text; smoothed scroll (median 145 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a creative director's folio on dark brown: a stack of print pieces as the loader, giant condensed 'M' and 'B' at opposite corners with a portrait between, statements in mono caps, a client list where the hovered row turns cream, monochrome full-bleed case images with labels, a scattered archive of small images around 'Past work, lasting pride' and a large condensed closing line. Type: Saans, Saans Mono, Neue Corp Tight.
Ground and ink from the measured palette (#271504, #979695, #7D7C7B). Motion carries the page through
a giant 'M' and 'B' at opposite corners framing a portrait. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — monochrome case photography, portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: monochrome case photography, portrait

## Reference lock

Primary reference/direction: Michael Brown - Creative and Design Director — A creative director's folio on dark brown: a stack of print pieces as the loader, giant condensed 'M' and 'B' at opposite corners with a portrait between, statements in mono caps, a client list where the hovered row turns cream, monochrome full-bleed case images with labels, a scattered archive of small images around 'Past work, lasting pride' and a large condensed closing line.
Preserve (3-5 traits): giant condensed initials at corners; dark brown and cream; monochrome case images; client list row highlight; scattered archive thumbnails.
Borrow only (1-2): Put the initials at opposite corners as the hero frame; A scattered archive around a centred line
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: monochrome case photography, portrait
Reject: Small mono text
Token commitments: palette #271504, #979695, #7D7C7B, #605C5A, #4A4541, #E2D5CB; type Saans, Saans Mono, Neue Corp Tight; engine GSAP + Lenis linked (never vendored).
