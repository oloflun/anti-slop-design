---
title: "AWE Nite Mexico City"
url: https://awexr.mx/
source_url: https://awexr.mx/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: ""
family: xr-meetup-wave-lines
dna: "XR community meetup x purple wave-line field and a warped event card"
register: cinematic dark
grammar: chaptered editorial
lane: "A meetup page: 'AWE NITE MEXICO CITY' loader, a purple field of flowing line waves behind 'Impulsando el computo espacial desde Mexico para el mundo', a 'Proximo evento' card whose photo warps like cloth as it enters, event details and a footer."
mode: persuade
traits: ["flowing line-wave field", "purple and blue", "warped image card", "pill nav", "short page", "Swup transitions"]
palette: ["#27183B", "#080620", "#3A5183", "#3D2467", "#5383AF"]
type: ["Barlow"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The cloth-warp on the event photo is the one spatial-computing gesture that fits the subject; the rest is a simple event page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Nestor Rios).

## What to borrow (principle)

- Warp an image like cloth as it enters to hint at 3D

## What to leave

- Thin content
- Small details text

## Signature move

An event photo warping like cloth over purple line waves.

## Motion

Intro: purple with the logo and 'Cargando' (~2 s). Wheel (Lenis ~130 px glide): the line waves ripple; the headline lifts; the event card enters with a bulge warp that flattens; details slide up.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Swup page transitions; WebGL canvas x1 (three.js); smoothed scroll (median 134 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a meetup page: 'AWE NITE MEXICO CITY' loader, a purple field of flowing line waves behind 'Impulsando el computo espacial desde Mexico para el mundo', a 'Proximo evento' card whose photo warps like cloth as it enters, event details and a footer. Type: Barlow.
Ground and ink from the measured palette (#27183B, #080620, #3A5183). Motion carries the page through
an event photo warping like cloth over purple line waves. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL line waves, venue photo

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL line waves, venue photo

## Reference lock

Primary reference/direction: AWE Nite Mexico City — A meetup page: 'AWE NITE MEXICO CITY' loader, a purple field of flowing line waves behind 'Impulsando el computo espacial desde Mexico para el mundo', a 'Proximo evento' card whose photo warps like cloth as it enters, event details and a footer.
Preserve (3-5 traits): flowing line-wave field; purple and blue; warped image card; pill nav; short page.
Borrow only (1-2): Warp an image like cloth as it enters to hint at 3D
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL line waves, venue photo
Reject: Thin content; Small details text
Token commitments: palette #27183B, #080620, #3A5183, #3D2467, #5383AF; type Barlow; engine GSAP + Lenis linked (never vendored).
