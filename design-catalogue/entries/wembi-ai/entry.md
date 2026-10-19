---
title: "Wembi - instant digital twin"
url: https://www.wembi.ai/
source_url: https://www.wembi.ai/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "institutional"
family: pastel-glass-discs-tech
dna: "Industrial AI x lime and seafoam, frosted glass discs and a pixel wordmark across the top"
register: modern clean
grammar: chaptered editorial
lane: "An Italian industrial-AI product: a lime panel 'Instant digital twin of everything' opening onto a seafoam field of frosted glass discs under a huge lime pixel wordmark, a lede set over the gradient, a long statement word by word, glass discs stacked into a ribbon with 'Functioning', then a sticky two-part index (01 Digital twin: data, device, application; 02 Functioning: acquisition, control, prediction) where each step swaps a rendered object on the left, highlighted words in lime and lilac pills, sector names in a scrolling list (Aerospace, Medical, Industrial, Energy) and an FAQ."
mode: persuade
traits: ["pixel display wordmark", "frosted glass disc renders", "lime and lilac highlighter pills", "sticky numbered index with swapping render", "word-by-word statement", "sector word list"]
palette: ["#ECE8E7", "#A2B9C0", "#C9DAD8", "#8A9DA5"]
type: ["HaasUnicaSH-Medium", "HaasUnicaSH-Regular", "ductile"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The sticky index swapping one render per step turns an abstract service into a sequence of objects you can point at.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: ET Studio).

## What to borrow (principle)

- Swap one rendered object per step of a sticky index

## What to leave

- Pills overused as highlights
- Cookie banner over the hero

## Signature move

A field of frosted glass discs under a lime pixel wordmark.

## Motion

Intro: lime panel wipes up (~1.5 s). Wheel (Lenis, pins 3): discs drift in depth; the statement lights word by word; the index pins while steps swap with a cross-fade and the render changes; pills pop in; the sector list scrolls as a column.

Measured (`motion/probe.json`): GSAP 3.14.2; 3 pinned sections; Lenis; 13 video; split text; smoothed scroll (median 134 px still travelling after input stops); entry gate: Rifiuta. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an Italian industrial-AI product: a lime panel 'Instant digital twin of everything' opening onto a seafoam field of frosted glass discs under a huge lime pixel wordmark, a lede set over the gradient, a long statement word by word, glass discs stacked into a ribbon with 'Functioning', then a sticky two-part index (01 Digital twin: data, device, application; 02 Functioning: acquisition, control, prediction) where each step swaps a rendered object on the left, highlighted words in lime and lilac pills, sector names in a scrolling list (Aerospace, Medical, Industrial, Energy) and an FAQ. Type: HaasUnicaSH-Medium, HaasUnicaSH-Regular, ductile.
Ground and ink from the measured palette (#ECE8E7, #A2B9C0, #C9DAD8). Motion carries the page through
a field of frosted glass discs under a lime pixel wordmark. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D renders of glass discs and abstract devices

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D renders of glass discs and abstract devices

## Reference lock

Primary reference/direction: Wembi - instant digital twin — An Italian industrial-AI product: a lime panel 'Instant digital twin of everything' opening onto a seafoam field of frosted glass discs under a huge lime pixel wordmark, a lede set over the gradient, a long statement word by word, glass discs stacked into a ribbon with 'Functioning', then a sticky two-part index (01 Digital twin: data, device, application; 02 Functioning: acquisition, control, prediction) where each step swaps a rendered object on the left, highlighted words in lime and lilac pills, sector names in a scrolling list (Aerospace, Medical, Industrial, Energy) and an FAQ.
Preserve (3-5 traits): pixel display wordmark; frosted glass disc renders; lime and lilac highlighter pills; sticky numbered index with swapping render; word-by-word statement.
Borrow only (1-2): Swap one rendered object per step of a sticky index
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D renders of glass discs and abstract devices
Reject: Pills overused as highlights; Cookie banner over the hero
Token commitments: palette #ECE8E7, #A2B9C0, #C9DAD8, #8A9DA5; type HaasUnicaSH-Medium, HaasUnicaSH-Regular, ductile; engine GSAP + Lenis linked (never vendored).
