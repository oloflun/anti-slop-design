---
title: "Thibault Guignand"
url: https://www.thibaultguignand.com/
source_url: https://www.thibaultguignand.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: flame-mono-dev-folio
dna: "Creative frontend developer x single flame on black"
register: cinematic dark
grammar: filmic one-shot
lane: "A black folio where tiny mono text scrambles in at the centre, then a single flame burns in the frame behind 'Discover my projects' with corner marks, and a project ('STRATUS') bursts in through a glitch of colour bars."
mode: experience
traits: ["single flame video on black", "scrambled mono micro text", "corner diamond marks", "glitch colour-bar transition into projects", "wide logo type for project titles"]
palette: ["#0E100F", "#573F23"]
type: ["ABC Monument Grotesk Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Almost nothing on screen: a flame and one line of text. The restraint makes the glitch burst into the first project feel like a cut in a film.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Thibault Guignand).

## What to borrow (principle)

- One elemental video (flame) as the whole hero
- A colour-bar glitch as the cut into the work

## What to leave

- Long stretch of the same flame frame
- Text very small

## Signature move

A single flame burning behind 'Discover my projects'.

## Motion

Intro: mono text scrambles into 'I explore the web between design and code…' (~2 s). Scroll (Lenis, WebGL): the flame rises and flickers behind the prompt for many beats; a glitch of colour bars cuts to 'STRATUS' over a Paris street.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x2; 7 video; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: DISCOVER MY PROJECNP. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a black folio where tiny mono text scrambles in at the centre, then a single flame burns in the frame behind 'Discover my projects' with corner marks, and a project ('STRATUS') bursts in through a glitch of colour bars. Type: ABC Monument Grotesk Mono.
Ground and ink from the measured palette (#0E100F, #573F23). Motion carries the page through
a single flame burning behind 'Discover my projects'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — single flame on black; city photography for projects

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: single flame on black; city photography for projects

## Reference lock

Primary reference/direction: Thibault Guignand — A black folio where tiny mono text scrambles in at the centre, then a single flame burns in the frame behind 'Discover my projects' with corner marks, and a project ('STRATUS') bursts in through a glitch of colour bars.
Preserve (3-5 traits): single flame video on black; scrambled mono micro text; corner diamond marks; glitch colour-bar transition into projects; wide logo type for project titles.
Borrow only (1-2): One elemental video (flame) as the whole hero; A colour-bar glitch as the cut into the work
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: single flame on black; city photography for projects
Reject: Long stretch of the same flame frame; Text very small
Token commitments: palette #0E100F, #573F23; type ABC Monument Grotesk Mono; engine GSAP + Lenis linked (never vendored).
