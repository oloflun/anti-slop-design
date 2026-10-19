---
title: "Ravi Klaassens (R—K)"
url: https://www.raviklaassens.com/
source_url: https://www.raviklaassens.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: red-ink-knight-studio
dna: "Independent design-and-code studio x red ink and knight emblem"
register: editorial print
grammar: chaptered editorial
lane: "A studio site that opens with an R—K monogram where a knight on horseback gallops between the letters, a portrait dissolving in red ink, centred short statements framed by dot markers, a red-and-photograph case grid, a red referral ticket, and 'House of Klaassens' on a red band."
mode: persuade
traits: ["R—K monogram with a riding knight emblem", "red ink dissolve over photography", "centred short lines with corner dots", "case grid of rich photography", "red referral ticket object", "huge red band wordmark footer"]
palette: ["#E0DEDC", "#060605", "#453B36", "#8C5F56", "#A89588", "#C9BEB6"]
type: ["ReplicaLL", "Reckless Neue", "Suisse Intl Book"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

A single red and a single emblem (a knight) give a personal studio a heraldic identity. The red behaves like ink: it bleeds over a portrait at the open and returns on objects (the referral ticket, the footer band), so the colour has a material feel.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Animate an emblem between the letters of a monogram as the loader
- Let the brand colour behave like ink bleeding into photos
- Turn an offer (agency referral) into a printed ticket object

## What to leave

- Very small grey body text
- Statement lines are short and scattered

## Signature move

A knight on horseback galloping between the letters R and K.

## Motion

Intro: 'R—K' letters slide apart on black while a knight emblem rides between them, a red ink image flashes (~2.5 s). Scroll (Lenis, ~120 px glide, 11 ScrollTriggers, Barba, SplitText): portrait with red ink dissolve and tagline; centred statement lines; case grid with photos sliding in; 'For Agencies' with a red ticket tilting in; insights cards; black contact with the red 'House of Klaassens' band.

Measured (`motion/probe.json`): GSAP 3.15.0; 11 ScrollTriggers; Lenis; Barba page transitions; WebGL canvas x1; split text; smoothed scroll (median 134 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a studio site that opens with an R—K monogram where a knight on horseback gallops between the letters, a portrait dissolving in red ink, centred short statements framed by dot markers, a red-and-photograph case grid, a red referral ticket, and 'House of Klaassens' on a red band. Type: ReplicaLL, Reckless Neue, Suisse Intl Book.
Ground and ink from the measured palette (#E0DEDC, #060605, #453B36). Motion carries the page through
a knight on horseback galloping between the letters R and K. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — rich editorial still life and portraits with deep reds

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: rich editorial still life and portraits with deep reds

## Reference lock

Primary reference/direction: Ravi Klaassens (R—K) — A studio site that opens with an R—K monogram where a knight on horseback gallops between the letters, a portrait dissolving in red ink, centred short statements framed by dot markers, a red-and-photograph case grid, a red referral ticket, and 'House of Klaassens' on a red band.
Preserve (3-5 traits): R—K monogram with a riding knight emblem; red ink dissolve over photography; centred short lines with corner dots; case grid of rich photography; red referral ticket object.
Borrow only (1-2): Animate an emblem between the letters of a monogram as the loader; Let the brand colour behave like ink bleeding into photos
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: rich editorial still life and portraits with deep reds
Reject: Very small grey body text; Statement lines are short and scattered
Token commitments: palette #E0DEDC, #060605, #453B36, #8C5F56, #A89588, #C9BEB6; type ReplicaLL, Reckless Neue, Suisse Intl Book; engine GSAP + Lenis linked (never vendored).
