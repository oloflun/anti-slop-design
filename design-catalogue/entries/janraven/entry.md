---
title: "Jan Raven Studio - Freelance UI/UX Designer"
url: https://janraven.studio/
source_url: https://janraven.studio/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: glass-orb-freelancer-folio
dna: "Freelance UX designer x a giant wordmark and a golden glass orb shattering"
register: modern clean
grammar: chaptered editorial
lane: "A freelance designer: scrambling characters on black, a giant 'JANRAVEN.STUDIO' wordmark over a small laptop mockup that grows, project mockups (laptops and phones in warm photographed scenes), then a dark section where a glowing golden glass orb sheds fragments as statements appear over it, and a light contact block with a pixel icon."
mode: persuade
traits: ["giant wordmark full width", "mockup growing from small to large", "photographed device scenes", "golden glass orb with fragments", "scramble loader", "pixel icon in the email"]
palette: ["#E0E0E0", "#171413", "#8A796C", "#574940", "#ADA9A5"]
type: ["Neue Montreal", "DM Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The orb shedding fragments gives the philosophy section its own object and moment between the work and the contact.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One glowing object that breaks apart as the statement plays

## What to leave

- Statements overlap the orb
- Small meta text

## Signature move

A golden glass orb shedding fragments behind a statement.

## Motion

Intro: black scramble text, a white panel with the wordmark (~2 s). Wheel (Lenis ~110 px glide, 1 pin): the laptop mockup scales up and swaps projects; phone scenes slide; the dark section pins with the orb glowing and fragments breaking off as lines fade in; the orb drops away into the contact panel.

Measured (`motion/probe.json`): GSAP 3.13.0; 1 pinned sections; Lenis; 2 video; smoothed scroll (median 116 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a freelance designer: scrambling characters on black, a giant 'JANRAVEN.STUDIO' wordmark over a small laptop mockup that grows, project mockups (laptops and phones in warm photographed scenes), then a dark section where a glowing golden glass orb sheds fragments as statements appear over it, and a light contact block with a pixel icon. Type: Neue Montreal, DM Mono.
Ground and ink from the measured palette (#E0E0E0, #171413, #8A796C). Motion carries the page through
a golden glass orb shedding fragments behind a statement. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — device mockups, 3D orb

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: device mockups, 3D orb

## Reference lock

Primary reference/direction: Jan Raven Studio - Freelance UI/UX Designer — A freelance designer: scrambling characters on black, a giant 'JANRAVEN.STUDIO' wordmark over a small laptop mockup that grows, project mockups (laptops and phones in warm photographed scenes), then a dark section where a glowing golden glass orb sheds fragments as statements appear over it, and a light contact block with a pixel icon.
Preserve (3-5 traits): giant wordmark full width; mockup growing from small to large; photographed device scenes; golden glass orb with fragments; scramble loader.
Borrow only (1-2): One glowing object that breaks apart as the statement plays
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: device mockups, 3D orb
Reject: Statements overlap the orb; Small meta text
Token commitments: palette #E0E0E0, #171413, #8A796C, #574940, #ADA9A5; type Neue Montreal, DM Mono; engine GSAP + Lenis linked (never vendored).
