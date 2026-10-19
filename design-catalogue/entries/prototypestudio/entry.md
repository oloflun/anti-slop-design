---
title: "Prototype - Creative house for daring brands"
url: http://prototypestudio.fr/
source_url: http://prototypestudio.fr/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "luxury-craft"
family: numbered-index-creative-house
dna: "Paris creative house x condensed type and a numbered project index"
register: editorial print
grammar: gallery/catalog
lane: "A creative house on white: a loader cycling project images with a big '77/100' counter, a full-bleed video 'Creative house for daring brands', an italic serif manifesto, then a numbered index (01/11 to 11/11) where a big number at left counts up while client names list at right and images slide through the middle, condensed 'Our services' and 'Let's craft your project together'."
mode: read
traits: ["counter loader cycling images", "huge condensed numerals", "client list at right highlights", "italic serif manifesto", "condensed uppercase display", "Taxi page transitions"]
palette: ["#FFFFFF", "#B2B0AE", "#2E2B26", "#64574C", "#5B3A2F", "#9B9495"]
type: ["DeanGothicCMP", "SilvanaDisplay"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The big running number turns a client list into a countdown: you always know where you are in the eleven projects.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Beaucoup).

## What to borrow (principle)

- A huge running index number beside the project list
- Loader that previews the work

## What to leave

- Empty white frames between images
- Very small captions

## Signature move

A big '01/11' counting up beside a client list as images slide past.

## Motion

Intro: images cycle while the counter climbs to 100/100 (~2 s), then the video hero. Wheel (virtual feel, Taxi): the hero shrinks away; the manifesto fades in; the index number rolls 01 to 11 while images slide up through the centre and the active client name darkens; services words slide in from the right.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; Taxi page transitions; 14 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the gallery/catalog grammar: a creative house on white: a loader cycling project images with a big '77/100' counter, a full-bleed video 'Creative house for daring brands', an italic serif manifesto, then a numbered index (01/11 to 11/11) where a big number at left counts up while client names list at right and images slide through the middle, condensed 'Our services' and 'Let's craft your project together'. Type: DeanGothicCMP, SilvanaDisplay.
Ground and ink from the measured palette (#FFFFFF, #B2B0AE, #2E2B26). Motion carries the page through
a big '01/11' counting up beside a client list as images slide past. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — fashion, beauty and lifestyle photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: fashion, beauty and lifestyle photography

## Reference lock

Primary reference/direction: Prototype - Creative house for daring brands — A creative house on white: a loader cycling project images with a big '77/100' counter, a full-bleed video 'Creative house for daring brands', an italic serif manifesto, then a numbered index (01/11 to 11/11) where a big number at left counts up while client names list at right and images slide through the middle, condensed 'Our services' and 'Let's craft your project together'.
Preserve (3-5 traits): counter loader cycling images; huge condensed numerals; client list at right highlights; italic serif manifesto; condensed uppercase display.
Borrow only (1-2): A huge running index number beside the project list; Loader that previews the work
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: fashion, beauty and lifestyle photography
Reject: Empty white frames between images; Very small captions
Token commitments: palette #FFFFFF, #B2B0AE, #2E2B26, #64574C, #5B3A2F, #9B9495; type DeanGothicCMP, SilvanaDisplay; engine GSAP + Lenis linked (never vendored).
