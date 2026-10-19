---
title: "Relats - protection sleeves"
url: https://toptier.relats.com/
source_url: https://toptier.relats.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "institutional"
family: orange-industrial-macro
dna: "Industrial supplier x orange braided sleeves in macro on warm grey, landscapes and vehicle cutaways"
register: warm photographic
grammar: chaptered editorial
lane: "A technical sleeve maker: a percentage loader, 'Protection sleeves for the mobility of tomorrow' over a macro of orange braid, a mosaic of landscapes for 'We cover all sustainable mobility solutions', product macros of orange sleeves on metal busbars with model names (Revitex, Periflex) and spec chips, a glass card listing sectors over each product, an aerial road for '141,000,000 metres of sleeving per year', an orange excavator, an X-ray truck chassis where sleeves light up along the cable route, a battery pack and 'Join the ri(de)'."
mode: persuade
traits: ["orange braid macros", "glass spec cards", "aerial road statistic", "X-ray vehicle cutaway", "model names in large grotesk", "video loops per product"]
palette: ["#552A18", "#9F9F9E", "#B8B5B2", "#D46020", "#A74216", "#8A8582"]
type: ["DM Mono", "Roobert"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Showing the sleeve in macro and then inside an X-ray vehicle connects a commodity part to the machines people know.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: FIRMA).

## What to borrow (principle)

- Locate a small component inside an X-ray of the whole machine

## What to leave

- Many near-identical product chapters

## Signature move

An orange braided sleeve lighting up along the cable route inside an X-ray truck.

## Motion

Intro: percentage loader (~2 s). Wheel (Lenis, taxi): product videos scrub; glass cards slide; the road photo scales into the statistic; the X-ray cutaway reveals the sleeve route; sections cross-fade.

Measured (`motion/probe.json`): GSAP 3.11.5; Lenis; Taxi page transitions; 25 video; split text; smoothed scroll (median 143 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a technical sleeve maker: a percentage loader, 'Protection sleeves for the mobility of tomorrow' over a macro of orange braid, a mosaic of landscapes for 'We cover all sustainable mobility solutions', product macros of orange sleeves on metal busbars with model names (Revitex, Periflex) and spec chips, a glass card listing sectors over each product, an aerial road for '141,000,000 metres of sleeving per year', an orange excavator, an X-ray truck chassis where sleeves light up along the cable route, a battery pack and 'Join the ri(de)'. Type: DM Mono, Roobert.
Ground and ink from the measured palette (#552A18, #9F9F9E, #B8B5B2). Motion carries the page through
an orange braided sleeve lighting up along the cable route inside an X-ray truck. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product macro video, aerial photography, 3D cutaway

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product macro video, aerial photography, 3D cutaway

## Reference lock

Primary reference/direction: Relats - protection sleeves — A technical sleeve maker: a percentage loader, 'Protection sleeves for the mobility of tomorrow' over a macro of orange braid, a mosaic of landscapes for 'We cover all sustainable mobility solutions', product macros of orange sleeves on metal busbars with model names (Revitex, Periflex) and spec chips, a glass card listing sectors over each product, an aerial road for '141,000,000 metres of sleeving per year', an orange excavator, an X-ray truck chassis where sleeves light up along the cable route, a battery pack and 'Join the ri(de)'.
Preserve (3-5 traits): orange braid macros; glass spec cards; aerial road statistic; X-ray vehicle cutaway; model names in large grotesk.
Borrow only (1-2): Locate a small component inside an X-ray of the whole machine
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product macro video, aerial photography, 3D cutaway
Reject: Many near-identical product chapters
Token commitments: palette #552A18, #9F9F9E, #B8B5B2, #D46020, #A74216, #8A8582; type DM Mono, Roobert; engine GSAP + Lenis linked (never vendored).
