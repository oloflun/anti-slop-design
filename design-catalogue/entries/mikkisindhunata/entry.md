---
title: "Mikki Sindhunata"
url: https://mikkisindhunata.com/
source_url: https://mikkisindhunata.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: director-film-full-bleed
dna: "Director x a single full-bleed commercial film as the home page"
register: cinematic dark
grammar: filmic one-shot
lane: "A director's site: a small monogram loader, then one full-bleed film (ECCO Leather - EL3 Motion) playing: macro shots of skin and leather, a tannery, hands working hide, a man under fluorescent tubes; the title and a project list button at the corners."
mode: experience
traits: ["one full-bleed film", "macro texture shots", "small monogram", "project title top left", "project list button", "no scroll content"]
palette: ["#0B0806", "#4C3623", "#261E15", "#7B6648"]
type: ["Anton SC", "B612 Mono", "Poppins", "icomoon"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The work is the page; one strong film says more than a grid.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Open on one full-bleed film with only the title

## What to leave

- Cookie panel at start
- Nothing to read

## Signature move

Macro leather and skin shots in a dark tannery film.

## Motion

Intro: grey with a monogram (~2 s), consent declined. Scroll: none; the film plays full bleed.

Measured (`motion/probe.json`): GSAP 3.12.5; 4 ScrollTriggers; Lenis; 5 video; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Decline, PLAY. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a director's site: a small monogram loader, then one full-bleed film (ECCO Leather - EL3 Motion) playing: macro shots of skin and leather, a tannery, hands working hide, a man under fluorescent tubes; the title and a project list button at the corners. Type: Anton SC, B612 Mono, Poppins, icomoon.
Ground and ink from the measured palette (#0B0806, #4C3623, #261E15). Motion carries the page through
macro leather and skin shots in a dark tannery film. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — commercial film

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: commercial film

## Reference lock

Primary reference/direction: Mikki Sindhunata — A director's site: a small monogram loader, then one full-bleed film (ECCO Leather - EL3 Motion) playing: macro shots of skin and leather, a tannery, hands working hide, a man under fluorescent tubes; the title and a project list button at the corners.
Preserve (3-5 traits): one full-bleed film; macro texture shots; small monogram; project title top left; project list button.
Borrow only (1-2): Open on one full-bleed film with only the title
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: commercial film
Reject: Cookie panel at start; Nothing to read
Token commitments: palette #0B0806, #4C3623, #261E15, #7B6648; type Anton SC, B612 Mono, Poppins, icomoon; engine GSAP + Lenis linked (never vendored).
