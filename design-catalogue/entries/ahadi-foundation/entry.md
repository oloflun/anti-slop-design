---
title: "AHADI Foundation - women with disabilities"
url: https://ahadi-foundation.org/
source_url: https://ahadi-foundation.org/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: illustrated-ngo-cards
dna: "Foundation for women with disabilities x bold flat illustrations and playing-card programmes"
register: illustrated dark
grammar: chaptered editorial
lane: "A foundation site in French: a teal 'AHADI' wordmark, 'Unies par le handicap' with a flat illustrated flower blooming, statements in grotesk with script accents, the founder story (Deza) with a portrait and a zigzag edge, illustrated figures inside the wordmark, programmes presented as illustrated playing cards that flip (Dirigeante d'entreprise, Élue politique, Installations artistiques, Design inclusif), stats ('Seulement 2,3%'), 'S'engager' and contact."
mode: read
traits: ["bold flat illustrations", "playing cards for programmes", "zigzag edges", "teal, orange, lilac and pink", "script accents", "illustrated figures in the wordmark"]
palette: ["#0B5752", "#BB98F0", "#C9835B", "#EDE0CE", "#346C6A", "#A24348"]
type: ["Cormorant Garamond", "Poppins", "pp"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Turning programmes into a deck of illustrated cards gives a serious cause a warm, dignified and memorable form.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Present programmes as a deck of illustrated cards that flip

## What to leave

- Cookie banner at start

## Signature move

Programmes as illustrated playing cards flipping on orange.

## Motion

Intro: teal with the wordmark (~1.5 s), cookie panel. Wheel: the flower blooms behind the title; statements reveal; the founder section rises with a zigzag edge; figures slide into the wordmark; cards flip and stack with arrows; stats count; the flower returns.

Measured (`motion/probe.json`): GSAP 3.12.5; 6 pinned sections; Lenis; split text; smoothed scroll (median 158 px still travelling after input stops); entry gate: Tout refuser, X. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the chaptered editorial grammar: a foundation site in French: a teal 'AHADI' wordmark, 'Unies par le handicap' with a flat illustrated flower blooming, statements in grotesk with script accents, the founder story (Deza) with a portrait and a zigzag edge, illustrated figures inside the wordmark, programmes presented as illustrated playing cards that flip (Dirigeante d'entreprise, Élue politique, Installations artistiques, Design inclusif), stats ('Seulement 2,3%'), 'S'engager' and contact. Type: Cormorant Garamond, Poppins, pp.
Ground and ink from the measured palette (#0B5752, #BB98F0, #C9835B). Motion carries the page through
programmes as illustrated playing cards flipping on orange. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — flat illustration, portraits

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: flat illustration, portraits

## Reference lock

Primary reference/direction: AHADI Foundation - women with disabilities — A foundation site in French: a teal 'AHADI' wordmark, 'Unies par le handicap' with a flat illustrated flower blooming, statements in grotesk with script accents, the founder story (Deza) with a portrait and a zigzag edge, illustrated figures inside the wordmark, programmes presented as illustrated playing cards that flip (Dirigeante d'entreprise, Élue politique, Installations artistiques, Design inclusif), stats ('Seulement 2,3%'), 'S'engager' and contact.
Preserve (3-5 traits): bold flat illustrations; playing cards for programmes; zigzag edges; teal, orange, lilac and pink; script accents.
Borrow only (1-2): Present programmes as a deck of illustrated cards that flip
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: flat illustration, portraits
Reject: Cookie banner at start
Token commitments: palette #0B5752, #BB98F0, #C9835B, #EDE0CE, #346C6A, #A24348; type Cormorant Garamond, Poppins, pp; engine GSAP + Lenis linked (never vendored).
