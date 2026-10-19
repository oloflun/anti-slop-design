---
title: "Linearity - on-brand design generation"
url: https://www.linearity.io/
source_url: https://www.linearity.io/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: prompt-sentence-swap-saas
dna: "Design generation tool x a sentence whose chips swap name, team and asset"
register: cinematic dark
grammar: chaptered editorial
lane: "A product home on black: 'Let [Samir] from [Engineering] create [Demo Day Invite]. On brand. Every time.' where the chips swap people, teams and assets, a prompt box, then 'Prompted in seconds. On-brand and editable.' with generated assets (posters, ads) floating around in depth under a glow."
mode: persuade
traits: ["sentence with swapping chips", "prompt box", "generated assets floating in depth", "glow edges", "black ground"]
palette: ["#050505", "#1F1F1F", "#5C534E"]
type: ["AcidGroteskSubset", "AcidGrotesk", "Inter"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The swapping chips show the range of users and outputs in one sentence.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Konpo).

## What to borrow (principle)

- Swap the who, team and what chips inside one headline sentence

## What to leave

- Short capture

## Signature move

'Let [Samir] from [Engineering] create [Demo Day Invite]' with chips swapping.

## Motion

Intro: the sentence with chips cycling. Wheel: the glow frame appears; assets fly in from depth around the centred line; words underline.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x1; entry gate: Start designing in Linearity. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a product home on black: 'Let [Samir] from [Engineering] create [Demo Day Invite]. On brand. Every time.' where the chips swap people, teams and assets, a prompt box, then 'Prompted in seconds. On-brand and editable.' with generated assets (posters, ads) floating around in depth under a glow. Type: AcidGroteskSubset, AcidGrotesk, Inter.
Ground and ink from the measured palette (#050505, #1F1F1F, #5C534E). Motion carries the page through
'Let [Samir] from [Engineering] create [Demo Day Invite]' with chips swapping. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — generated design assets

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: generated design assets

## Reference lock

Primary reference/direction: Linearity - on-brand design generation — A product home on black: 'Let [Samir] from [Engineering] create [Demo Day Invite]. On brand. Every time.' where the chips swap people, teams and assets, a prompt box, then 'Prompted in seconds. On-brand and editable.' with generated assets (posters, ads) floating around in depth under a glow.
Preserve (3-5 traits): sentence with swapping chips; prompt box; generated assets floating in depth; glow edges; black ground.
Borrow only (1-2): Swap the who, team and what chips inside one headline sentence
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: generated design assets
Reject: Short capture
Token commitments: palette #050505, #1F1F1F, #5C534E; type AcidGroteskSubset, AcidGrotesk, Inter; engine GSAP + Lenis linked (never vendored).
