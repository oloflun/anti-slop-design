---
title: "DirectOut ACE"
url: https://ace.directout.eu/
source_url: https://ace.directout.eu/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: pixel-smear-audio-hardware
dna: "Pro audio interface x pixel-smear colour bands"
register: modern clean
grammar: chaptered editorial
lane: "A product page for an audio interface: the letters A-C-E assemble from blocks, teal pixel bands smear across the hero, and each mode (Playback, PA, Prodigy) is announced by a horizontal band of pixels in its colour (red, violet, teal) sweeping under the device."
mode: persuade
traits: ["logo letters built from blocks", "horizontal pixel-smear bands per mode", "one colour per mode (red, violet, teal)", "product shots on black", "annotated front/back panel diagrams", "tabbed mode labels"]
palette: ["#000000", "#FFFFFF", "#58CAA8", "#48504C", "#ADDECF", "#8CB5A8"]
type: ["Onest"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Each mode of the device gets a colour and a gesture: a band of pixels that streaks horizontally across the screen like a signal, under the hardware. It turns a spec page into a sequence of coloured signals while the product photo stays put.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Fabio Carretti).

## What to borrow (principle)

- Give each product mode a colour and a horizontal pixel-band sweep
- Assemble the product name from blocks in the hero
- Annotated hardware diagrams as the closing spec

## What to leave

- Cookie bar in early frames
- Small body text on black

## Signature move

Horizontal pixel-smear bands streaking under the device in each mode's colour.

## Motion

Intro: white with a spinner arc, grey with a power-icon C, then black 'ACE' letters assembling from blocks while teal pixel bands smear in (~3 s). Scroll (Lenis, ~140 px glide): product shots slide in beside 'My New Audio Platform'; 'ACE MODES' intro; Playback with a red band, PA violet, Prodigy teal, each sweeping across; formats list; features; front/back panel diagrams with numbered callouts; case shot.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; smoothed scroll (median 151 px still travelling after input stops); entry gate: Reject. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a product page for an audio interface: the letters A-C-E assemble from blocks, teal pixel bands smear across the hero, and each mode (Playback, PA, Prodigy) is announced by a horizontal band of pixels in its colour (red, violet, teal) sweeping under the device. Type: Onest.
Ground and ink from the measured palette (#000000, #FFFFFF, #58CAA8). Motion carries the page through
horizontal pixel-smear bands streaking under the device in each mode's colour. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — pro audio hardware on black, laptop screens with DAW software

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: pro audio hardware on black, laptop screens with DAW software

## Reference lock

Primary reference/direction: DirectOut ACE — A product page for an audio interface: the letters A-C-E assemble from blocks, teal pixel bands smear across the hero, and each mode (Playback, PA, Prodigy) is announced by a horizontal band of pixels in its colour (red, violet, teal) sweeping under the device.
Preserve (3-5 traits): logo letters built from blocks; horizontal pixel-smear bands per mode; one colour per mode (red, violet, teal); product shots on black; annotated front/back panel diagrams.
Borrow only (1-2): Give each product mode a colour and a horizontal pixel-band sweep; Assemble the product name from blocks in the hero
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: pro audio hardware on black, laptop screens with DAW software
Reject: Cookie bar in early frames; Small body text on black
Token commitments: palette #000000, #FFFFFF, #58CAA8, #48504C, #ADDECF, #8CB5A8; type Onest; engine GSAP + Lenis linked (never vendored).
