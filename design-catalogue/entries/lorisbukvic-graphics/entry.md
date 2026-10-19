---
title: "Loris Bukvic Portfolio"
url: http://lorisbukvic.graphics/
source_url: http://lorisbukvic.graphics/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "portfolio"
family: dark-3d-folio-scroll
dna: "Multimedia designer folio x electric-blue WebGL creature"
register: cinematic dark
grammar: continuous world
lane: "A short dark one-pager: an electric-blue WebGL creature crawls over black, a pixel-display intro line types in, then a project strip, awards list, education/stack/experience rows and a large tinted portrait behind the contact CTA."
mode: experience
traits: ["electric blue lightning-edged 3D form", "pixel display face for the statement", "horizontal project thumbnail strip", "dock-style icon footer", "floating 3D props between sections", "tinted portrait as contact backdrop"]
palette: ["#000000", "#19242B", "#E2E2E3", "#46535A"]
type: ["__intranet_88ffcb", "__ppSemiBold_e86be0"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The blue creature sets a voice in one frame and the pixel face carries it into the copy; the rest stays quiet black lists so the two loud elements own the page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One loud 3D element plus quiet black lists
- Dock-style social icons as the footer

## What to leave

- Small grey list text on black
- Contact frame repeats across the last third

## Signature move

An electric-blue lightning creature crawling over black above a pixel-type statement.

## Motion

Intro: black with a spinner, the WebGL creature fades up and the statement types in line by line (~2 s). Wheel (Lenis, ~80 px glide): project strip slides up, a 3D phone prop floats in beside the awards list, a book prop drops in at education; the portrait card rises and holds as the page ends.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x2 (three.js); smoothed scroll (median 101 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a short dark one-pager: an electric-blue WebGL creature crawls over black, a pixel-display intro line types in, then a project strip, awards list, education/stack/experience rows and a large tinted portrait behind the contact CTA. Type: __intranet_88ffcb, __ppSemiBold_e86be0.
Ground and ink from the measured palette (#000000, #19242B, #E2E2E3). Motion carries the page through
an electric-blue lightning creature crawling over black above a pixel-type statement. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL creature, product renders, tinted portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL creature, product renders, tinted portrait

## Reference lock

Primary reference/direction: Loris Bukvic Portfolio — A short dark one-pager: an electric-blue WebGL creature crawls over black, a pixel-display intro line types in, then a project strip, awards list, education/stack/experience rows and a large tinted portrait behind the contact CTA.
Preserve (3-5 traits): electric blue lightning-edged 3D form; pixel display face for the statement; horizontal project thumbnail strip; dock-style icon footer; floating 3D props between sections.
Borrow only (1-2): One loud 3D element plus quiet black lists; Dock-style social icons as the footer
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL creature, product renders, tinted portrait
Reject: Small grey list text on black; Contact frame repeats across the last third
Token commitments: palette #000000, #19242B, #E2E2E3, #46535A; type __intranet_88ffcb, __ppSemiBold_e86be0; engine GSAP + Lenis linked (never vendored).
