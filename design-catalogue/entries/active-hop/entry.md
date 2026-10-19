---
title: "ActiveHop - sparkling hop water"
url: https://www.active-hop.com/
source_url: https://www.active-hop.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "product-focused"
family: floating-can-flavour-orbit
dna: "Hop water x one 3D bottle floating centre stage on a misty white, flavour words in giant type and an orbiting ingredient ring"
register: modern clean
grammar: filmic one-shot
lane: "A drinks brand around one bottle: a misty loader, the aluminium bottle floating in fog, then flavours as the bottle turns and its label changes while giant words (DROP, TRAIL, RAD) slide behind it in the label's colour, a ring of ingredients orbiting the bottle with callouts (zero sugar, zero alcohol, vitamins), then a rock-and-trail landscape where the bottle lies on stone with framed trail photos, and back to the mist."
mode: persuade
traits: ["single 3D bottle centre stage", "label swaps per flavour", "giant flavour words behind", "orbit ring of ingredients", "landscape photo frames"]
palette: ["#FFFFFF", "#D3CFC9", "#EAE8E5", "#7F7574"]
type: ["Lekton", "Sora"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The bottle never leaves the centre, so flavours, ingredients and occasions arrive as changes to the same object.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Six Socks Studio).

## What to borrow (principle)

- Swap the product's label per variant while it stays in place

## What to leave

- Tiny mono callouts

## Signature move

An aluminium bottle turning while DROP, TRAIL and RAD slide behind it in its label colour.

## Motion

Intro: mist clears (~3 s). Wheel (Lenis, smoothed, WebGL x3): the bottle rotates and its texture swaps; words translate in rows; the ring orbits with callouts lighting; the bottle drops onto rock with photos sliding in.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x3 (three.js); smoothed scroll (median 108 px still travelling after input stops); entry gate: DECLINE. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the filmic one-shot grammar: a drinks brand around one bottle: a misty loader, the aluminium bottle floating in fog, then flavours as the bottle turns and its label changes while giant words (DROP, TRAIL, RAD) slide behind it in the label's colour, a ring of ingredients orbiting the bottle with callouts (zero sugar, zero alcohol, vitamins), then a rock-and-trail landscape where the bottle lies on stone with framed trail photos, and back to the mist. Type: Lekton, Sora.
Ground and ink from the measured palette (#FFFFFF, #D3CFC9, #EAE8E5). Motion carries the page through
an aluminium bottle turning while DROP, TRAIL and RAD slide behind it in its label colour. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL product model, landscape photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL product model, landscape photography

## Reference lock

Primary reference/direction: ActiveHop - sparkling hop water — A drinks brand around one bottle: a misty loader, the aluminium bottle floating in fog, then flavours as the bottle turns and its label changes while giant words (DROP, TRAIL, RAD) slide behind it in the label's colour, a ring of ingredients orbiting the bottle with callouts (zero sugar, zero alcohol, vitamins), then a rock-and-trail landscape where the bottle lies on stone with framed trail photos, and back to the mist.
Preserve (3-5 traits): single 3D bottle centre stage; label swaps per flavour; giant flavour words behind; orbit ring of ingredients; landscape photo frames.
Borrow only (1-2): Swap the product's label per variant while it stays in place
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL product model, landscape photography
Reject: Tiny mono callouts
Token commitments: palette #FFFFFF, #D3CFC9, #EAE8E5, #7F7574; type Lekton, Sora; engine GSAP + Lenis linked (never vendored).
