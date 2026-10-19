---
title: "Dorian Lods - Creative Developer"
url: https://www.dorianlods.com/
source_url: https://www.dorianlods.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: blackletter-glass-prism-folio
dna: "Creative developer x a blackletter wordmark and iridescent glass prisms"
register: cinematic dark
grammar: chaptered editorial
lane: "A creative developer folio: a small loader on black, a huge stylised blackletter 'DORIAN LODS' with iridescent glass prisms orbiting through it, the prisms forming a star beside a list of selected works and clients, a blackletter 'Gen AI, AI video, real, shader design...' list and a short bio with socials."
mode: read
traits: ["stylised blackletter display", "iridescent glass prisms", "prisms forming a star", "work list with tags", "blackletter skills list", "dark gradient"]
palette: ["#0E0704", "#747579"]
type: ["Dirtyline", "TTNormsPro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The blackletter and glass prisms make an instantly recognisable identity; the prisms turning into a star give the work list a centrepiece.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Pair one exotic display face with one 3D object family

## What to leave

- Short page
- Small bio text

## Signature move

Iridescent glass prisms orbiting through a blackletter name.

## Motion

Intro: black with a spinner (~2 s), the blackletter fades in with prisms swirling through. Wheel (Lenis, short): the name dissolves; prisms rotate into a star beside the work list; the skills list slides up in blackletter.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x1; smoothed scroll (median 49 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a creative developer folio: a small loader on black, a huge stylised blackletter 'DORIAN LODS' with iridescent glass prisms orbiting through it, the prisms forming a star beside a list of selected works and clients, a blackletter 'Gen AI, AI video, real, shader design...' list and a short bio with socials. Type: Dirtyline, TTNormsPro.
Ground and ink from the measured palette (#0E0704, #747579). Motion carries the page through
iridescent glass prisms orbiting through a blackletter name. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D glass prisms

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D glass prisms

## Reference lock

Primary reference/direction: Dorian Lods - Creative Developer — A creative developer folio: a small loader on black, a huge stylised blackletter 'DORIAN LODS' with iridescent glass prisms orbiting through it, the prisms forming a star beside a list of selected works and clients, a blackletter 'Gen AI, AI video, real, shader design...' list and a short bio with socials.
Preserve (3-5 traits): stylised blackletter display; iridescent glass prisms; prisms forming a star; work list with tags; blackletter skills list.
Borrow only (1-2): Pair one exotic display face with one 3D object family
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D glass prisms
Reject: Short page; Small bio text
Token commitments: palette #0E0704, #747579; type Dirtyline, TTNormsPro; engine GSAP + Lenis linked (never vendored).
