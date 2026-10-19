---
title: "HOMERUN Creative Things"
url: https://homerun.today/
source_url: https://homerun.today/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: sports-agency-helmet
dna: "Sports creative agency x a giant name over a reel and a 3D helmet CTA"
register: modern clean
grammar: chaptered editorial
lane: "A sports marketing agency: lilac loader, 'HOMERUN Creative Things' huge over a reel, 'Play beyond the limits. Score big.' over clips, a statement with underlined words and round photos popping in, an orange highlight phrase, a news card strip and an orange 3D baseball helmet for 'Ready to push beyond limits?'."
mode: persuade
traits: ["giant name over reel", "round photos popping into a statement", "orange highlight phrase", "news card strip", "3D baseball helmet CTA", "lilac and cream"]
palette: ["#171815", "#F7F7EC", "#7F2F22", "#B5A49A"]
type: ["Figtree Variable", "Space Grotesk Variable"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Round photos popping inside the statement make the claims concrete; the helmet gives the CTA an object.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Pop round photos into a statement at the words they illustrate

## What to leave

- Thin news section

## Signature move

An orange 3D baseball helmet next to 'Ready to push beyond limits?'.

## Motion

Intro: lilac (~2 s), then the name over the reel. Wheel (Lenis, 20 triggers): clips swap under the slogan; the statement fills while round photos pop beside key words; the orange highlight sweeps; news cards slide; the helmet rotates in.

Measured (`motion/probe.json`): GSAP 3.12.7; 20 ScrollTriggers; Lenis; 1 video; smoothed scroll (median 77 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a sports marketing agency: lilac loader, 'HOMERUN Creative Things' huge over a reel, 'Play beyond the limits. Score big.' over clips, a statement with underlined words and round photos popping in, an orange highlight phrase, a news card strip and an orange 3D baseball helmet for 'Ready to push beyond limits?'. Type: Figtree Variable, Space Grotesk Variable.
Ground and ink from the measured palette (#171815, #F7F7EC, #7F2F22). Motion carries the page through
an orange 3D baseball helmet next to 'Ready to push beyond limits?'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — sports and campaign footage, 3D helmet

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: sports and campaign footage, 3D helmet

## Reference lock

Primary reference/direction: HOMERUN Creative Things — A sports marketing agency: lilac loader, 'HOMERUN Creative Things' huge over a reel, 'Play beyond the limits. Score big.' over clips, a statement with underlined words and round photos popping in, an orange highlight phrase, a news card strip and an orange 3D baseball helmet for 'Ready to push beyond limits?'.
Preserve (3-5 traits): giant name over reel; round photos popping into a statement; orange highlight phrase; news card strip; 3D baseball helmet CTA.
Borrow only (1-2): Pop round photos into a statement at the words they illustrate
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: sports and campaign footage, 3D helmet
Reject: Thin news section
Token commitments: palette #171815, #F7F7EC, #7F2F22, #B5A49A; type Figtree Variable, Space Grotesk Variable; engine GSAP + Lenis linked (never vendored).
