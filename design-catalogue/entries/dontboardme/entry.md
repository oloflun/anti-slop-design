---
title: "Don't Board Me"
url: https://dontboardme.com/
source_url: https://dontboardme.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "consumer-brand"
family: bounce-gate-dog-brand
dna: "Dog-care brand x bounce-a-ball game gate"
register: other
grammar: live surface
lane: "A pink page that tells you to 'BOUNCE A BALL TO GET TO THE SITE' in huge red condensed caps, with a yellow tennis ball you have to bounce to enter."
mode: experience
traits: ["huge condensed caps instruction", "yellow ball as the only object", "pink ground, red type", "game gate"]
palette: ["#F2C2CC", "#E13429", "#EB8F90", "#E55C56"]
type: ["Bayon", "Neue Montreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The gate is the brand's personality: a dog brand makes you play fetch before you get in. It is a joke executed with one object and one sentence.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: The First The Last).

## What to borrow (principle)

- A one-object playful gate that matches the brand's world (fetch for a dog brand)

## What to leave

- Captured only the gate: the bounce interaction was not performed
- Gate blocks all content

## Signature move

A tennis ball you must bounce to enter the site.

## Motion

Intro: the instruction slides in and the ball drops and rolls (~1 s). Gate: the ball rests until clicked/bounced (not captured); wheel does nothing.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the live surface grammar: a pink page that tells you to 'BOUNCE A BALL TO GET TO THE SITE' in huge red condensed caps, with a yellow tennis ball you have to bounce to enter. Type: Bayon, Neue Montreal.
Ground and ink from the measured palette (#F2C2CC, #E13429, #EB8F90). Motion carries the page through
a tennis ball you must bounce to enter the site. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — single bright prop on a flat colour ground

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: single bright prop on a flat colour ground

## Reference lock

Primary reference/direction: Don't Board Me — A pink page that tells you to 'BOUNCE A BALL TO GET TO THE SITE' in huge red condensed caps, with a yellow tennis ball you have to bounce to enter.
Preserve (3-5 traits): huge condensed caps instruction; yellow ball as the only object; pink ground, red type; game gate.
Borrow only (1-2): A one-object playful gate that matches the brand's world (fetch for a dog brand)
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: single bright prop on a flat colour ground
Reject: Captured only the gate: the bounce interaction was not performed; Gate blocks all content
Token commitments: palette #F2C2CC, #E13429, #EB8F90, #E55C56; type Bayon, Neue Montreal; engine GSAP + Lenis linked (never vendored).
