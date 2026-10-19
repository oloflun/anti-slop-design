---
title: "/zeroz - Otsuka active inner resource"
url: https://otsuka-air.jp/
source_url: https://otsuka-air.jp/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: ""
family: light-portal-wellness-jp
dna: "Japanese wellness supplement x a glowing white portal and a ring of photos"
register: warm photographic
grammar: chaptered editorial
lane: "A product site: photos changing in a square over a grey '/zeroz' wordmark that turns white, a glowing white circle on green that holds the concept text in Japanese, the circle expanding to fill mint with the logo, photos of active life flying around in a tilted ring, chapter 2 on dark green with dust."
mode: persuade
traits: ["photos inside a square over the wordmark", "glowing white portal", "mint and deep green", "photos in a tilted ring", "Japanese text centred", "chapter labels"]
palette: ["#FEFFFE", "#CCF9E3", "#0B0B09", "#263427", "#A2BDAD", "#606B5E"]
type: ["fpbf_ac93d8111", "TazuganeGothicStdN-Regular", "HelveticaNowDisplay-Regular", "TazuganeGothicStdN-Medium"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The glowing portal that grows into the page is a clear metaphor for inner energy.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: SHIFTBRAIN).

## What to borrow (principle)

- Grow a glowing portal to become the next ground

## What to leave

- Few frames captured

## Signature move

A glowing white circle on green that expands to fill the screen.

## Motion

Intro: photos swap inside a square while the wordmark brightens (~2 s). Wheel (Lenis): the portal glows and grows; text fades inside; the portal fills mint; photos fly into a ring; chapter 2 darkens.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; Barba page transitions; WebGL canvas x1 (three.js); 8 video; smoothed scroll (median 56 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a product site: photos changing in a square over a grey '/zeroz' wordmark that turns white, a glowing white circle on green that holds the concept text in Japanese, the circle expanding to fill mint with the logo, photos of active life flying around in a tilted ring, chapter 2 on dark green with dust. Type: fpbf_ac93d8111, TazuganeGothicStdN-Regular, HelveticaNowDisplay-Regular, TazuganeGothicStdN-Medium.
Ground and ink from the measured palette (#FEFFFE, #CCF9E3, #0B0B09). Motion carries the page through
a glowing white circle on green that expands to fill the screen. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — lifestyle photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: lifestyle photography

## Reference lock

Primary reference/direction: /zeroz - Otsuka active inner resource — A product site: photos changing in a square over a grey '/zeroz' wordmark that turns white, a glowing white circle on green that holds the concept text in Japanese, the circle expanding to fill mint with the logo, photos of active life flying around in a tilted ring, chapter 2 on dark green with dust.
Preserve (3-5 traits): photos inside a square over the wordmark; glowing white portal; mint and deep green; photos in a tilted ring; Japanese text centred.
Borrow only (1-2): Grow a glowing portal to become the next ground
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: lifestyle photography
Reject: Few frames captured
Token commitments: palette #FEFFFE, #CCF9E3, #0B0B09, #263427, #A2BDAD, #606B5E; type fpbf_ac93d8111, TazuganeGothicStdN-Regular, HelveticaNowDisplay-Regular, TazuganeGothicStdN-Medium; engine GSAP + Lenis linked (never vendored).
