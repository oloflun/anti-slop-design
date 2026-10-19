---
title: "Eduard Bodak - Webdesigner Cologne"
url: https://www.eduardbodak.com/
source_url: https://www.eduardbodak.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: pastel-cards-webdesigner
dna: "German webdesigner x pastel cards that fan out into service lists"
register: modern clean
grammar: chaptered editorial
lane: "A webdesigner's site on cream: 'EINFACHE WEBSITES' huge with three pastel cards (lilac, pink, peach) with pixel icons, a black interlude where four yellow dots bounce, then the three cards fan apart and flip into service lists (strategy, design, build), and 'Mein Prozess' with an inline image."
mode: persuade
traits: ["pastel cards with pixel icons", "cards fanning and flipping into lists", "black interlude with bouncing dots", "giant condensed headings", "inline image in heading", "cream ground"]
palette: ["#F9F4EA", "#000000", "#615D5B"]
type: ["font-mono-medium", "font-normal-medium", "font-narrow-semibold"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The same three cards carry the page: hero decoration, then the service menus, which keeps a simple site coherent.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Turn decorative hero cards into the service lists later

## What to leave

- Small list text

## Signature move

Three pastel cards fanning out and flipping into service lists.

## Motion

Intro: cream with the headline and cards (~1 s). Wheel (Lenis): cards drift; a black panel rises with four dots bouncing in sequence; cards stack, then fan and flip to show lists; the process heading rises.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; smoothed scroll (median 94 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a webdesigner's site on cream: 'EINFACHE WEBSITES' huge with three pastel cards (lilac, pink, peach) with pixel icons, a black interlude where four yellow dots bounce, then the three cards fan apart and flip into service lists (strategy, design, build), and 'Mein Prozess' with an inline image. Type: font-mono-medium, font-normal-medium, font-narrow-semibold.
Ground and ink from the measured palette (#F9F4EA, #000000, #615D5B). Motion carries the page through
three pastel cards fanning out and flipping into service lists. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — pastel card illustrations

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: pastel card illustrations

## Reference lock

Primary reference/direction: Eduard Bodak - Webdesigner Cologne — A webdesigner's site on cream: 'EINFACHE WEBSITES' huge with three pastel cards (lilac, pink, peach) with pixel icons, a black interlude where four yellow dots bounce, then the three cards fan apart and flip into service lists (strategy, design, build), and 'Mein Prozess' with an inline image.
Preserve (3-5 traits): pastel cards with pixel icons; cards fanning and flipping into lists; black interlude with bouncing dots; giant condensed headings; inline image in heading.
Borrow only (1-2): Turn decorative hero cards into the service lists later
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: pastel card illustrations
Reject: Small list text
Token commitments: palette #F9F4EA, #000000, #615D5B; type font-mono-medium, font-normal-medium, font-narrow-semibold; engine GSAP + Lenis linked (never vendored).
