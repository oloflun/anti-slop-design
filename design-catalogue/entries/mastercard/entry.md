---
title: "Mastercard - customer stories"
url: https://www.mastercard.com/businessoutcomes
source_url: https://www.mastercard.com/businessoutcomes
captured: 2026-10-03
origin: raw-url
extract: none
category: institutional
category2: "consumer-brand"
family: orange-gradient-pill-corporate
dna: "Corporate stories x orange-to-red gradients, sculptural ribbon forms and white pill counters"
register: modern clean
grammar: chaptered editorial
lane: "A corporate impact page: the circles logo on white, rounded orange panels with sculptural folded forms ('Get to know today's Mastercard', 'Let's talk about your goals'), a photo of a woman paying, a small photo card, then impact numbers in a white pill that rolls between figures (25, 500, 250, 50) on orange, 'Unlocking potential' with a ribbon form, 'Together, the possibilities are priceless', goals as rows that light in turn with a portrait in the black bar, and a dark footer."
mode: persuade
traits: ["orange-red gradient panels", "sculptural ribbon forms", "rolling numbers in a white pill", "rows lit in turn", "rounded panels"]
palette: ["#FFFFFF", "#F26718", "#C94F17", "#D97B2C", "#9A1905", "#D9A870"]
type: ["Mark Offc for MC"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One pill that rolls from figure to figure keeps four impact numbers in one place, so they read as a sequence, not a grid.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Alper Dostal, Christophe Massolin, Clément Pavageau, Florent BIFFI, KKPK, Little Red Robot).

## What to borrow (principle)

- Roll successive figures through one fixed counter

## What to leave

- Corporate stock imagery

## Signature move

A white pill on orange rolling from 25 to 500 to 250 to 50.

## Motion

Intro: logo (~2 s). Wheel (Lenis, smoothed): panels round their corners as they arrive; the pill counter rolls digits vertically per step; ribbon forms rotate; rows highlight in sequence.

Measured (`motion/probe.json`): GSAP 3.12.5/3.6.0; Lenis; 9 video; smoothed scroll (median 108 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a corporate impact page: the circles logo on white, rounded orange panels with sculptural folded forms ('Get to know today's Mastercard', 'Let's talk about your goals'), a photo of a woman paying, a small photo card, then impact numbers in a white pill that rolls between figures (25, 500, 250, 50) on orange, 'Unlocking potential' with a ribbon form, 'Together, the possibilities are priceless', goals as rows that light in turn with a portrait in the black bar, and a dark footer. Type: Mark Offc for MC.
Ground and ink from the measured palette (#FFFFFF, #F26718, #C94F17). Motion carries the page through
a white pill on orange rolling from 25 to 500 to 250 to 50. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D abstract forms, corporate photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D abstract forms, corporate photography

## Reference lock

Primary reference/direction: Mastercard - customer stories — A corporate impact page: the circles logo on white, rounded orange panels with sculptural folded forms ('Get to know today's Mastercard', 'Let's talk about your goals'), a photo of a woman paying, a small photo card, then impact numbers in a white pill that rolls between figures (25, 500, 250, 50) on orange, 'Unlocking potential' with a ribbon form, 'Together, the possibilities are priceless', goals as rows that light in turn with a portrait in the black bar, and a dark footer.
Preserve (3-5 traits): orange-red gradient panels; sculptural ribbon forms; rolling numbers in a white pill; rows lit in turn; rounded panels.
Borrow only (1-2): Roll successive figures through one fixed counter
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D abstract forms, corporate photography
Reject: Corporate stock imagery
Token commitments: palette #FFFFFF, #F26718, #C94F17, #D97B2C, #9A1905, #D9A870; type Mark Offc for MC; engine GSAP + Lenis linked (never vendored).
