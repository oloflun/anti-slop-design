---
title: "Bohdan Skrypka - product designer"
url: https://bohdan.design/
source_url: https://bohdan.design/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: ""
family: orange-grotesk-pixel-dissolve-portfolio
dna: "Product designer x giant grey words drifting apart, a pixel-block dissolve to black and orange 'Selected work' running off the edges"
register: cinematic dark
grammar: chaptered editorial
lane: "A product designer's portfolio: name on black, then on pale grey a sentence in giant grotesk ('making tech more human by tying digital products and people with foolproof interfaces') whose words drift apart in rows as you scroll, a pixel-block dissolve into black, 'Selected work' in huge orange running off both edges, case rows with phone screens in a column beside a large mock-up, and a rust-red 'Good design starts with a conversation' close."
mode: persuade
traits: ["giant drifting sentence", "pixel-block dissolve", "orange display words off the edges", "case rows with screen columns", "rust close"]
palette: ["#D3D9D9", "#606B6C", "#312E2D", "#EFF1F1", "#B5B6B4"]
type: ["Geist Mono", "Inter Display", "Inter Display Placeholder"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The sentence breaking apart and the pixel dissolve make the transition from statement to work feel like a cut in a film.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Bogdan Skripka).

## What to borrow (principle)

- Dissolve from the statement to the work through pixel blocks

## What to leave

- Tiny labels on cases

## Signature move

'Selected work' in orange running off both edges after a pixel dissolve.

## Motion

Intro: name on black (~2 s). Wheel (Lenis): rows of words translate in opposite directions; pixel blocks flip from grey to black; the orange title scrolls sideways; case rows slide.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; split text; smoothed scroll (median 115 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a product designer's portfolio: name on black, then on pale grey a sentence in giant grotesk ('making tech more human by tying digital products and people with foolproof interfaces') whose words drift apart in rows as you scroll, a pixel-block dissolve into black, 'Selected work' in huge orange running off both edges, case rows with phone screens in a column beside a large mock-up, and a rust-red 'Good design starts with a conversation' close. Type: Geist Mono, Inter Display, Inter Display Placeholder.
Ground and ink from the measured palette (#D3D9D9, #606B6C, #312E2D). Motion carries the page through
'Selected work' in orange running off both edges after a pixel dissolve. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — UI mock-ups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: UI mock-ups

## Reference lock

Primary reference/direction: Bohdan Skrypka - product designer — A product designer's portfolio: name on black, then on pale grey a sentence in giant grotesk ('making tech more human by tying digital products and people with foolproof interfaces') whose words drift apart in rows as you scroll, a pixel-block dissolve into black, 'Selected work' in huge orange running off both edges, case rows with phone screens in a column beside a large mock-up, and a rust-red 'Good design starts with a conversation' close.
Preserve (3-5 traits): giant drifting sentence; pixel-block dissolve; orange display words off the edges; case rows with screen columns; rust close.
Borrow only (1-2): Dissolve from the statement to the work through pixel blocks
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: UI mock-ups
Reject: Tiny labels on cases
Token commitments: palette #D3D9D9, #606B6C, #312E2D, #EFF1F1, #B5B6B4; type Geist Mono, Inter Display, Inter Display Placeholder; engine GSAP + Lenis linked (never vendored).
