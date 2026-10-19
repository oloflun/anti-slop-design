---
title: "Chemtest - AIDES"
url: https://chemtest.fr/
source_url: https://chemtest.fr/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "playful"
family: gradient-bubble-health-test
dna: "Harm-reduction health test x bubbly type on a moving gradient"
register: other
grammar: typographic poster
lane: "A French harm-reduction tool for chemsex: a mint and sky gradient with a rising blue horizon, a bubbly 'CHEM TEST' logo, then a sequence of pinned full-screen statements in fat rounded type ('Tu aimes le sexe, tu prends des chems') with small speech-bubble tags popping around them, explanations on blue, and a closing 'Commencer' over a sunrise gradient."
mode: read
traits: ["bubbly rounded display face", "mint, sky and sunrise gradients", "pinned full-screen statements", "speech-bubble tags popping around words", "emoji-like pill icons", "gradient horizon as the transition"]
palette: ["#C2EECF", "#4DC7E9", "#435E93", "#98E0D9"]
type: ["__ppPangramBold_5bfe9c", "__ppPangramSemiBold_cbc023", "__harry_593e9f"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A sensitive health topic is addressed in a warm, non-judging voice: one sentence per screen, a soft gradient that shifts like daylight, and playful tags that answer the reader as they read.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Affaire à Suivre Studio).

## What to borrow (principle)

- One sentence per pinned screen for a sensitive message
- A gradient horizon that rises and sets as the transition

## What to leave

- Body text small on blue
- Long run of near-empty blue frames

## Signature move

Fat bubbly statements on a mint and sky gradient with tags popping around them.

## Motion

Intro: mint ground, a blue horizon rises and the logo bounces in with its tags (~2 s). Wheel (Lenis ~140 px glide, 7 pins): each statement pins and fills in word by word; speech-bubble tags pop in around it; the gradient shifts from mint to sky blue; explanation lines slide sideways; at the end a yellow-pink sunrise rises behind the logo and the start button.

Measured (`motion/probe.json`): GSAP 3.12.5; 7 pinned sections; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 147 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the typographic poster grammar: a French harm-reduction tool for chemsex: a mint and sky gradient with a rising blue horizon, a bubbly 'CHEM TEST' logo, then a sequence of pinned full-screen statements in fat rounded type ('Tu aimes le sexe, tu prends des chems') with small speech-bubble tags popping around them, explanations on blue, and a closing 'Commencer' over a sunrise gradient. Type: __ppPangramBold_5bfe9c, __ppPangramSemiBold_cbc023, __harry_593e9f.
Ground and ink from the measured palette (#C2EECF, #4DC7E9, #435E93). Motion carries the page through
fat bubbly statements on a mint and sky gradient with tags popping around them. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — none, type and gradient only

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: none, type and gradient only

## Reference lock

Primary reference/direction: Chemtest - AIDES — A French harm-reduction tool for chemsex: a mint and sky gradient with a rising blue horizon, a bubbly 'CHEM TEST' logo, then a sequence of pinned full-screen statements in fat rounded type ('Tu aimes le sexe, tu prends des chems') with small speech-bubble tags popping around them, explanations on blue, and a closing 'Commencer' over a sunrise gradient.
Preserve (3-5 traits): bubbly rounded display face; mint, sky and sunrise gradients; pinned full-screen statements; speech-bubble tags popping around words; emoji-like pill icons.
Borrow only (1-2): One sentence per pinned screen for a sensitive message; A gradient horizon that rises and sets as the transition
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: none, type and gradient only
Reject: Body text small on blue; Long run of near-empty blue frames
Token commitments: palette #C2EECF, #4DC7E9, #435E93, #98E0D9; type __ppPangramBold_5bfe9c, __ppPangramSemiBold_cbc023, __harry_593e9f; engine GSAP + Lenis linked (never vendored).
