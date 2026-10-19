---
title: "Lucas Aufrère"
url: https://www.lucas-aufrere.com/
source_url: https://www.lucas-aufrere.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: gradient-bar-french-dev
dna: "Freelance front-end developer x teal-to-orange gradient bar"
register: cinematic dark
grammar: chaptered editorial
lane: "A dark French developer folio: a large name in light sans with a teal-to-amber gradient bar underneath, a portrait above, then philosophy, projects, a light services panel that slides up, collaborators and a 'PARLONS-EN.' close with the same bar."
mode: persuade
traits: ["teal-to-amber gradient bar under headlines", "large light sans name", "light services panel sliding over dark", "numbered section labels", "project thumbnails row", "French copy"]
palette: ["#0A0A0A", "#4E4F50", "#B3B2A9", "#2F2620"]
type: ["Manrope", "Inter", "JetBrains Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

One graphic device, a gradient bar under the big headlines, opens and closes the page and gives an otherwise monochrome, typographic site its signature. The services section switches to a light panel to signal 'commercial information' versus the dark editorial parts.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One gradient bar as the recurring signature under key headlines
- Slide a light panel over a dark page for the practical section

## What to leave

- Very small grey body and labels
- Generic structure

## Signature move

A teal-to-amber gradient bar under the giant name and the closing 'PARLONS-EN.'

## Motion

Intro: dark with the portrait fading in, name sliding up over the gradient bar (~1.5 s). Scroll (Lenis, ~150 px glide, SplitText): philosophy paragraph; skills grid; 'Projets sélectionnés' cards; light 'Prestations' panel slides over with its grid; collaborations; 'PARLONS-EN.' with the bar; footer.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; smoothed scroll (median 152 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a dark French developer folio: a large name in light sans with a teal-to-amber gradient bar underneath, a portrait above, then philosophy, projects, a light services panel that slides up, collaborators and a 'PARLONS-EN.' close with the same bar. Type: Manrope, Inter, JetBrains Mono.
Ground and ink from the measured palette (#0A0A0A, #4E4F50, #B3B2A9). Motion carries the page through
a teal-to-amber gradient bar under the giant name and the closing 'PARLONS-EN.' Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — moody portrait, project thumbnails

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: moody portrait, project thumbnails

## Reference lock

Primary reference/direction: Lucas Aufrère — A dark French developer folio: a large name in light sans with a teal-to-amber gradient bar underneath, a portrait above, then philosophy, projects, a light services panel that slides up, collaborators and a 'PARLONS-EN.' close with the same bar.
Preserve (3-5 traits): teal-to-amber gradient bar under headlines; large light sans name; light services panel sliding over dark; numbered section labels; project thumbnails row.
Borrow only (1-2): One gradient bar as the recurring signature under key headlines; Slide a light panel over a dark page for the practical section
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: moody portrait, project thumbnails
Reject: Very small grey body and labels; Generic structure
Token commitments: palette #0A0A0A, #4E4F50, #B3B2A9, #2F2620; type Manrope, Inter, JetBrains Mono; engine GSAP + Lenis linked (never vendored).
