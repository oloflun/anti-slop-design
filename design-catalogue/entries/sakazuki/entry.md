---
title: "SAKAZUKI - Japanese membership collective"
url: https://sakazuki.io/
source_url: https://sakazuki.io/
captured: 2026-10-03
origin: raw-url
extract: none
category: luxury-craft
category2: "editorial"
family: red-cream-triangle-membership
dna: "Japanese craft membership x red and cream, a triangle emblem and numbered philosophy pages"
register: editorial print
grammar: chaptered editorial
lane: "A membership site: cream, then red with a small triangle, 'THE HEART OF SAKAZUKI' over a dark craft film, a philosophy paragraph over a close-up of fruit on a branch, numbered pages ('( people ) 01 SAKAZUKI brings people closer', '( grow ) 02', '( life ) 03') with a tall photo and a big number, 'SAKA / ZUKI / COLLE / CTIVE' in huge grotesk on black with a kaleidoscope triangle, an artist page, 'BENEFITS' with the triangle cutting the word, and benefit cards in red and black with photos."
mode: persuade
traits: ["red, cream and black", "triangle emblem that cuts words", "numbered philosophy pages", "huge split wordmark", "kaleidoscope pattern in the triangle", "Japanese editorial restraint"]
palette: ["#E1D7CC", "#140B09", "#826640", "#3A1C14", "#6E311B", "#B1A389"]
type: ["hagrid", "hagrid-text"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The triangle is the thread: loader mark, pattern window, the notch that cuts BEN FITS.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: SHUN KUDO, Yuta Aoki).

## What to borrow (principle)

- Let the emblem physically cut into the headline
- Number the philosophy pages like a printed booklet

## What to leave

- Small body text

## Signature move

'BEN▼FITS' with the triangle emblem cutting the word.

## Motion

Intro: cream, a red flash, the triangle (~2 s). Wheel (Lenis): the film reveals under the title; paragraphs reveal by line; pages step with the number counting; the giant words slide in halves; the kaleidoscope triangle rotates; cards slide up.

Measured (`motion/probe.json`): Lenis; WebGL canvas x1; smoothed scroll (median 113 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a membership site: cream, then red with a small triangle, 'THE HEART OF SAKAZUKI' over a dark craft film, a philosophy paragraph over a close-up of fruit on a branch, numbered pages ('( people ) 01 SAKAZUKI brings people closer', '( grow ) 02', '( life ) 03') with a tall photo and a big number, 'SAKA / ZUKI / COLLE / CTIVE' in huge grotesk on black with a kaleidoscope triangle, an artist page, 'BENEFITS' with the triangle cutting the word, and benefit cards in red and black with photos. Type: hagrid, hagrid-text.
Ground and ink from the measured palette (#E1D7CC, #140B09, #826640). Motion carries the page through
'BEN▼FITS' with the triangle emblem cutting the word. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — craft photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: craft photography

## Reference lock

Primary reference/direction: SAKAZUKI - Japanese membership collective — A membership site: cream, then red with a small triangle, 'THE HEART OF SAKAZUKI' over a dark craft film, a philosophy paragraph over a close-up of fruit on a branch, numbered pages ('( people ) 01 SAKAZUKI brings people closer', '( grow ) 02', '( life ) 03') with a tall photo and a big number, 'SAKA / ZUKI / COLLE / CTIVE' in huge grotesk on black with a kaleidoscope triangle, an artist page, 'BENEFITS' with the triangle cutting the word, and benefit cards in red and black with photos.
Preserve (3-5 traits): red, cream and black; triangle emblem that cuts words; numbered philosophy pages; huge split wordmark; kaleidoscope pattern in the triangle.
Borrow only (1-2): Let the emblem physically cut into the headline; Number the philosophy pages like a printed booklet
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: craft photography
Reject: Small body text
Token commitments: palette #E1D7CC, #140B09, #826640, #3A1C14, #6E311B, #B1A389; type hagrid, hagrid-text; engine GSAP + Lenis linked (never vendored).
