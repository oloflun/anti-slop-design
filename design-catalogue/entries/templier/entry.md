---
title: "Templier - Art Deco Jewellery Raymond Templier"
url: https://templier.com/
source_url: https://templier.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: luxury-craft
category2: "consumer-brand"
family: art-deco-jewellery-reveal
dna: "Art deco jewellery house x photo panels sliding apart onto a geometric wordmark"
register: editorial print
grammar: filmic one-shot
lane: "A jewellery house relaunch: black, panels of black and white photos with art deco rings, bracelets and a clutch slide in from the corners and assemble a split hero, then the photos slide away upward to reveal the geometric 'TEMPLIER 1925' wordmark on black with a quiet footer."
mode: experience
traits: ["photo panels sliding in from corners", "black and white jewellery photography", "geometric art deco wordmark", "split hero", "black ground", "very short page"]
palette: ["#000000", "#363331", "#AFA28F", "#807C75", "#D6D1C9", "#6E6359"]
type: ["Raymond", "Spectral"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The photo panels assembling and then lifting away to the wordmark is a classic jewellery-box reveal.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Index Studio, Quentin Hocdé).

## What to borrow (principle)

- Assemble the hero from sliding photo panels, then lift them to reveal the name

## What to leave

- Almost nothing after the wordmark

## Signature move

Photo panels lifting away to reveal 'TEMPLIER 1925'.

## Motion

Intro: black, photo panels slide in from the corners and lock into a split (~2 s), cookie banner. Wheel (Lenis): the photos lift upward and the wordmark rises into the black.

Measured (`motion/probe.json`): GSAP 3.12.7; Lenis; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: REFUSER. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the filmic one-shot grammar: a jewellery house relaunch: black, panels of black and white photos with art deco rings, bracelets and a clutch slide in from the corners and assemble a split hero, then the photos slide away upward to reveal the geometric 'TEMPLIER 1925' wordmark on black with a quiet footer. Type: Raymond, Spectral.
Ground and ink from the measured palette (#000000, #363331, #AFA28F). Motion carries the page through
photo panels lifting away to reveal 'TEMPLIER 1925'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — black and white jewellery photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: black and white jewellery photography

## Reference lock

Primary reference/direction: Templier - Art Deco Jewellery Raymond Templier — A jewellery house relaunch: black, panels of black and white photos with art deco rings, bracelets and a clutch slide in from the corners and assemble a split hero, then the photos slide away upward to reveal the geometric 'TEMPLIER 1925' wordmark on black with a quiet footer.
Preserve (3-5 traits): photo panels sliding in from corners; black and white jewellery photography; geometric art deco wordmark; split hero; black ground.
Borrow only (1-2): Assemble the hero from sliding photo panels, then lift them to reveal the name
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: black and white jewellery photography
Reject: Almost nothing after the wordmark
Token commitments: palette #000000, #363331, #AFA28F, #807C75, #D6D1C9, #6E6359; type Raymond, Spectral; engine GSAP + Lenis linked (never vendored).
