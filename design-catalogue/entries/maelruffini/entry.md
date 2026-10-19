---
title: "Mael Ruffini - Front-end developer"
url: https://www.maelruffini.com/
source_url: https://www.maelruffini.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: heart-mask-stairs-folio
dna: "Front-end developer x serif titles and a heart-shaped mask onto a pastel staircase"
register: editorial print
grammar: chaptered editorial
lane: "A developer folio: a serif name loader, a pastel 3D staircase room, 'Creative developer crafting experiences and freelancing' in thin serif with an italic line, case cards (a red Jonathan Grado card, Rose Island laptop, a hand writing), a 'Clients' list where a pastel puffy 'CLIENTS' word passes over the names, 'With love', and a heart-shaped mask that grows to reveal the staircase room again."
mode: persuade
traits: ["thin serif titles", "pastel 3D staircase room", "puffy pastel word over a list", "heart-shaped mask reveal", "mint label bar", "case cards with laptop photos"]
palette: ["#FFFFFF", "#B6A68B", "#AD1B18", "#B6E5CE", "#91705C", "#562720"]
type: ["Ibm", "ESAllianz", "EditorialOld"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The heart mask growing into the staircase room brings back the opening scene as the ending, with a personal sign-off.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- End by growing a shape mask (heart) back into the opening scene

## What to leave

- Small labels

## Signature move

A heart-shaped mask growing to reveal a pastel staircase room.

## Motion

Intro: white with a serif monogram (~2 s), the staircase scene. Wheel: the headline lines shift; case cards rise; the laptop photo scales; the puffy word slides over the client list; 'With love' appears; a small heart grows to fill the screen with the staircase.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; WebGL canvas x2 (three.js); smoothed scroll (median 86 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a developer folio: a serif name loader, a pastel 3D staircase room, 'Creative developer crafting experiences and freelancing' in thin serif with an italic line, case cards (a red Jonathan Grado card, Rose Island laptop, a hand writing), a 'Clients' list where a pastel puffy 'CLIENTS' word passes over the names, 'With love', and a heart-shaped mask that grows to reveal the staircase room again. Type: Ibm, ESAllianz, EditorialOld.
Ground and ink from the measured palette (#FFFFFF, #B6A68B, #AD1B18). Motion carries the page through
a heart-shaped mask growing to reveal a pastel staircase room. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D interior, project photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D interior, project photography

## Reference lock

Primary reference/direction: Mael Ruffini - Front-end developer — A developer folio: a serif name loader, a pastel 3D staircase room, 'Creative developer crafting experiences and freelancing' in thin serif with an italic line, case cards (a red Jonathan Grado card, Rose Island laptop, a hand writing), a 'Clients' list where a pastel puffy 'CLIENTS' word passes over the names, 'With love', and a heart-shaped mask that grows to reveal the staircase room again.
Preserve (3-5 traits): thin serif titles; pastel 3D staircase room; puffy pastel word over a list; heart-shaped mask reveal; mint label bar.
Borrow only (1-2): End by growing a shape mask (heart) back into the opening scene
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D interior, project photography
Reject: Small labels
Token commitments: palette #FFFFFF, #B6A68B, #AD1B18, #B6E5CE, #91705C, #562720; type Ibm, ESAllianz, EditorialOld; engine GSAP + Lenis linked (never vendored).
