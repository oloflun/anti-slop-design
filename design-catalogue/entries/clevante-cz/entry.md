---
title: "Clevante"
url: https://clevante.cz/
source_url: https://clevante.cz/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: bracket-lens-dark-agency
dna: "Czech web agency x thin serif-less type and lens brackets"
register: cinematic dark
grammar: chaptered editorial
lane: "A black agency page where thin light words float apart on scroll (Služby, Vybrané projekty), project cards slide in from the edges, and two white curved brackets close in like a lens around the wordmark CLEVANTE before splitting it into 'clever' and 'ante'."
mode: persuade
traits: ["thin extended sans display", "words that travel apart to reveal lists", "white curved bracket lens", "wordmark split into its etymology", "project cards entering from the edges", "Czech copy"]
palette: ["#080A0B", "#6F6B63"]
type: ["Montserrat Variable"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The signature is a pair of thin curved white brackets that close around the wordmark like a camera iris and then reveal its meaning (clever + ante). It is one graphic gesture, repeated, on an otherwise very quiet black page of thin type.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Clevante).

## What to borrow (principle)

- Frame the wordmark with two curved lines that close like an iris
- Split a name into its roots as an about-section beat
- Let section words drift apart so the list can slide in between

## What to leave

- Very thin type on black is hard to read at small sizes
- Project cards crop awkwardly while entering

## Signature move

Two curved white brackets closing around CLEVANTE like an iris, then splitting it into 'clever' and 'ante'.

## Motion

Intro: a 'C' mark on black with a progress line (~2.5 s). Scroll (Lenis, ~160 px glide, SplitText, WebGL x2): 'Služby' with list items fading; 'Vybrané projekty' words split apart; cards slide in from left and right; reviews as 3D-tilted cards; 'POMÁHÁME VAŠÍ ZNAČCE VYNIKNOUT' words scatter; brackets close in around the wordmark and its etymology appears; contact; FAQ.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x2 (three.js); 4 video; smoothed scroll (median 165 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a black agency page where thin light words float apart on scroll (Služby, Vybrané projekty), project cards slide in from the edges, and two white curved brackets close in like a lens around the wordmark CLEVANTE before splitting it into 'clever' and 'ante'. Type: Montserrat Variable.
Ground and ink from the measured palette (#080A0B, #6F6B63). Motion carries the page through
two curved white brackets closing around CLEVANTE like an iris, then splitting it into 'clever' and 'ante'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project screens and product photography on black

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project screens and product photography on black

## Reference lock

Primary reference/direction: Clevante — A black agency page where thin light words float apart on scroll (Služby, Vybrané projekty), project cards slide in from the edges, and two white curved brackets close in like a lens around the wordmark CLEVANTE before splitting it into 'clever' and 'ante'.
Preserve (3-5 traits): thin extended sans display; words that travel apart to reveal lists; white curved bracket lens; wordmark split into its etymology; project cards entering from the edges.
Borrow only (1-2): Frame the wordmark with two curved lines that close like an iris; Split a name into its roots as an about-section beat
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project screens and product photography on black
Reject: Very thin type on black is hard to read at small sizes; Project cards crop awkwardly while entering
Token commitments: palette #080A0B, #6F6B63; type Montserrat Variable; engine GSAP + Lenis linked (never vendored).
