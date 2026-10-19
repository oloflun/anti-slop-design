---
title: "Cappen - Web Design and Development Studio"
url: https://cappen.com/
source_url: https://cappen.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: chrome-coil-agency
dna: "Brazilian studio x a black chrome coil and cut-out thumbnails"
register: cinematic dark
grammar: chaptered editorial
lane: "A studio site: white with thumbnails cycling in a small square, 'Human thinkers / Digital makers', then a black page with a 3D chrome coil turning, thumbnails flying out of it, an italic serif statement, featured project pairs, a project list, '(Human) thinkers digital' in huge wobbling type, awards, 'Talk ideas' over the coil, a chatbot and 'Rock'n & rolling since 2006'."
mode: persuade
traits: ["black chrome coil", "thumbnails flying from the object", "italic serif statement", "huge wobbling display type", "awards list", "chatbot CTA"]
palette: ["#000000", "#FDFDFD", "#382C29", "#575656", "#A29A94"]
type: ["Martian Mono", "Taklobo Display", "PP Editorial New", "HelveticaNowDisplay"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The coil is the recurring object: it opens the page, holds 'Talk ideas' and closes the footer, giving a dense agency site a centre.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One sculptural 3D object that opens, interrupts and closes the page

## What to leave

- Grey placeholder frame
- Many small labels

## Signature move

A black chrome coil turning behind 'Talk ideas'.

## Motion

Intro: white, a small square cycles project thumbnails between two labels (~2 s). Wheel (Lenis ~90 px glide): the coil spins and thumbnails fly out and line up; the statement types in; project pairs drift; the list highlights rows; the huge type wobbles and splits; the coil returns behind 'Talk ideas'; the footer title slants in.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x2 (three.js); 9 video; smoothed scroll (median 94 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a studio site: white with thumbnails cycling in a small square, 'Human thinkers / Digital makers', then a black page with a 3D chrome coil turning, thumbnails flying out of it, an italic serif statement, featured project pairs, a project list, '(Human) thinkers digital' in huge wobbling type, awards, 'Talk ideas' over the coil, a chatbot and 'Rock'n & rolling since 2006'. Type: Martian Mono, Taklobo Display, PP Editorial New, HelveticaNowDisplay.
Ground and ink from the measured palette (#000000, #FDFDFD, #382C29). Motion carries the page through
a black chrome coil turning behind 'Talk ideas'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D coil, project photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D coil, project photography

## Reference lock

Primary reference/direction: Cappen - Web Design and Development Studio — A studio site: white with thumbnails cycling in a small square, 'Human thinkers / Digital makers', then a black page with a 3D chrome coil turning, thumbnails flying out of it, an italic serif statement, featured project pairs, a project list, '(Human) thinkers digital' in huge wobbling type, awards, 'Talk ideas' over the coil, a chatbot and 'Rock'n & rolling since 2006'.
Preserve (3-5 traits): black chrome coil; thumbnails flying from the object; italic serif statement; huge wobbling display type; awards list.
Borrow only (1-2): One sculptural 3D object that opens, interrupts and closes the page
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D coil, project photography
Reject: Grey placeholder frame; Many small labels
Token commitments: palette #000000, #FDFDFD, #382C29, #575656, #A29A94; type Martian Mono, Taklobo Display, PP Editorial New, HelveticaNowDisplay; engine GSAP + Lenis linked (never vendored).
