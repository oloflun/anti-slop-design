---
title: "Quentin Hocdé"
url: https://quentinhocde.com/
source_url: https://quentinhocde.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: liquid-chrome-blur-dev
dna: "Creative technologist folio x blurred liquid chrome"
register: cinematic dark
grammar: typographic poster
lane: "A folio where a grey card on black expands into a field of soft, blurred liquid chrome that keeps flowing behind four lines of huge wide caps 'QUENTIN HOCDÉ CREATIVE TECHNOLOGIST & DEVELOPER'."
mode: experience
traits: ["blurred liquid chrome WebGL ground", "huge extended caps in four lines", "card that expands to full screen", "small info columns at top", "monochrome"]
palette: ["#111111", "#888888", "#272727", "#6E6E6E", "#414141", "#FAFAFA"]
type: ["Kinetica", "PP Neue Montreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Type and texture only: a soft, blurred chrome flow behind enormous extended caps. The intro grows a small card into the whole frame, so the texture is revealed as something opening.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Quentin Hocdé).

## What to borrow (principle)

- Grow a small card into the full-screen texture as the intro
- Soft blurred fluid behind huge type for a monochrome hero

## What to leave

- Nothing changes but the flow under the wheel in captures
- Small info text

## Signature move

A grey card that expands into flowing, blurred liquid chrome.

## Motion

Intro: black, a small grey card appears and expands to fill the screen with blurred liquid (~2.5 s). Then: four lines of caps set in; the chrome flows continuously (WebGL); wheel did not advance the page in capture.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x1; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the typographic poster grammar: a folio where a grey card on black expands into a field of soft, blurred liquid chrome that keeps flowing behind four lines of huge wide caps 'QUENTIN HOCDÉ CREATIVE TECHNOLOGIST & DEVELOPER'. Type: Kinetica, PP Neue Montreal.
Ground and ink from the measured palette (#111111, #888888, #272727). Motion carries the page through
a grey card that expands into flowing, blurred liquid chrome. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — monochrome fluid/chrome simulation, heavy blur

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: monochrome fluid/chrome simulation, heavy blur

## Reference lock

Primary reference/direction: Quentin Hocdé — A folio where a grey card on black expands into a field of soft, blurred liquid chrome that keeps flowing behind four lines of huge wide caps 'QUENTIN HOCDÉ CREATIVE TECHNOLOGIST & DEVELOPER'.
Preserve (3-5 traits): blurred liquid chrome WebGL ground; huge extended caps in four lines; card that expands to full screen; small info columns at top; monochrome.
Borrow only (1-2): Grow a small card into the full-screen texture as the intro; Soft blurred fluid behind huge type for a monochrome hero
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: monochrome fluid/chrome simulation, heavy blur
Reject: Nothing changes but the flow under the wheel in captures; Small info text
Token commitments: palette #111111, #888888, #272727, #6E6E6E, #414141, #FAFAFA; type Kinetica, PP Neue Montreal; engine GSAP + Lenis linked (never vendored).
