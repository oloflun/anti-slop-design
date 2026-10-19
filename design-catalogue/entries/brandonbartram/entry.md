---
title: "Brandon Bartram"
url: https://brandonbartram.dev/
source_url: https://brandonbartram.dev/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: mint-gradient-serif-dev
dna: "Freelance XR developer x mint gradient and italic serif"
register: editorial print
grammar: chaptered editorial
lane: "A mint-and-lilac gradient folio with an italic green serif word inside each headline, a horizontal project rail with a 'scroll to explore' cue, then a forest-green services panel and an FAQ, closing on 'Let's collab'."
mode: persuade
traits: ["mint/lilac soft gradient ground", "green italic serif word per headline", "horizontal project rail (1 pin)", "forest-green services panel", "small flower mark", "hairline-table CV"]
palette: ["#D5F3D4", "#2E3623", "#BFD2E0", "#969B77"]
type: ["Cormorant Garamond", "Geist", "JetBrains Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Soft colour and one recurring typographic gesture (a green italic word inside each serif headline) make a developer page feel editorial. The project rail pins and runs sideways so many small projects pass without a grid.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One italic accent word in a contrasting colour per headline
- Pin a horizontal rail for many small projects

## What to leave

- Very small grey body type
- Generic logo strip

## Signature move

A green italic word set inside each serif headline ('shipping ideas', 'Augmented Reality').

## Motion

Intro: name and flower mark with a 'loading 0% → 100%' hairline (~2 s). Scroll (ScrollSmoother, 1 pin): headline with portrait; logo strip; bio paragraph reveals; stats; 'Projects' pins and its card rail slides left; green 'Services' panel slides over with rows expanding; FAQ accordion; 'Let's collab' form.

Measured (`motion/probe.json`): GSAP 3.13.0; 1 pinned sections; ScrollSmoother. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a mint-and-lilac gradient folio with an italic green serif word inside each headline, a horizontal project rail with a 'scroll to explore' cue, then a forest-green services panel and an FAQ, closing on 'Let's collab'. Type: Cormorant Garamond, Geist, JetBrains Mono.
Ground and ink from the measured palette (#D5F3D4, #2E3623, #BFD2E0). Motion carries the page through
a green italic word set inside each serif headline ('shipping ideas', 'Augmented Reality'). Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project screenshots and XR stills, mixed

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project screenshots and XR stills, mixed

## Reference lock

Primary reference/direction: Brandon Bartram — A mint-and-lilac gradient folio with an italic green serif word inside each headline, a horizontal project rail with a 'scroll to explore' cue, then a forest-green services panel and an FAQ, closing on 'Let's collab'.
Preserve (3-5 traits): mint/lilac soft gradient ground; green italic serif word per headline; horizontal project rail (1 pin); forest-green services panel; small flower mark.
Borrow only (1-2): One italic accent word in a contrasting colour per headline; Pin a horizontal rail for many small projects
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project screenshots and XR stills, mixed
Reject: Very small grey body type; Generic logo strip
Token commitments: palette #D5F3D4, #2E3623, #BFD2E0, #969B77; type Cormorant Garamond, Geist, JetBrains Mono; engine GSAP + Lenis linked (never vendored).
