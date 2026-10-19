---
title: "maikasui - natural beauty from sake treasures"
url: http://maikasui.com/
source_url: http://maikasui.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "luxury-craft"
family: sake-skincare-mono-quiet
dna: "Sake-brewery skincare x mono type, brush logo and a sepia film"
register: editorial print
grammar: none
lane: "A skincare brand from a 130-year-old sake brewery: black with a brush-script logo that fades, a grey veil lifting to a paper-white page of small monospaced text about rice, flowers and water, three tiny icons, and a sepia film of a woman in a traditional interior that rises from below."
mode: read
traits: ["brush-script logo", "monospaced body text", "paper-white ground", "sepia film panel", "tiny line icons", "extreme restraint"]
palette: ["#000000", "#F1EFEE", "#9B9695", "#BAB7B4"]
type: ["NBAkademieProMono400-Regular", "NBAkademieProMono500", "NBAkademieProMono400", "NBAkademieProMono600"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The restraint is the brand: small mono type, one film and a brush mark say craft and calm without any sales layout.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Sublimio Studio).

## What to borrow (principle)

- Monospaced body text for a quiet craft brand
- One sepia film as the only image

## What to leave

- Text very small
- Almost nothing happens on scroll

## Signature move

A brush-script mark fading on black before a paper-white page of mono text and a sepia film.

## Motion

Intro: black, the brush logo draws and fades (~2 s), a grey veil lifts to white. Wheel (virtual, frame diff): the film panel rises and slowly brightens; nav buttons fade in; little else moves.

Measured (`motion/probe.json`): GSAP 3.13.0; 3 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the none grammar: a skincare brand from a 130-year-old sake brewery: black with a brush-script logo that fades, a grey veil lifting to a paper-white page of small monospaced text about rice, flowers and water, three tiny icons, and a sepia film of a woman in a traditional interior that rises from below. Type: NBAkademieProMono400-Regular, NBAkademieProMono500, NBAkademieProMono400, NBAkademieProMono600.
Ground and ink from the measured palette (#000000, #F1EFEE, #9B9695). Motion carries the page through
a brush-script mark fading on black before a paper-white page of mono text and a sepia film. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — sepia lifestyle film

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: sepia lifestyle film

## Reference lock

Primary reference/direction: maikasui - natural beauty from sake treasures — A skincare brand from a 130-year-old sake brewery: black with a brush-script logo that fades, a grey veil lifting to a paper-white page of small monospaced text about rice, flowers and water, three tiny icons, and a sepia film of a woman in a traditional interior that rises from below.
Preserve (3-5 traits): brush-script logo; monospaced body text; paper-white ground; sepia film panel; tiny line icons.
Borrow only (1-2): Monospaced body text for a quiet craft brand; One sepia film as the only image
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: sepia lifestyle film
Reject: Text very small; Almost nothing happens on scroll
Token commitments: palette #000000, #F1EFEE, #9B9695, #BAB7B4; type NBAkademieProMono400-Regular, NBAkademieProMono500, NBAkademieProMono400, NBAkademieProMono600; engine GSAP + Lenis linked (never vendored).
