---
title: "Onward - inclusive culture consultancy"
url: https://www.thisisonward.com/
source_url: https://www.thisisonward.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: serif-collage-culture-consultancy
dna: "Culture consultancy x serif statements over a 3D photo corridor and a collage 'ON' mark"
register: editorial print
grammar: chaptered editorial
lane: "A consultancy: 'ON' and 'RD' splitting apart as the loader, a serif statement 'At Onward, we believe culture is the winning strategy' over a 3D corridor of photos (Brooklyn Bridge, people) that the camera flies through, data cards ('$2 Trillion', '$3 Trillion') on cream, a dark section where a giant N fills with a collage of people and turns orange, 'Turn In and Transform', 'Turn On and Drive', and a giant 'ONWARD' footer."
mode: persuade
traits: ["serif statement with italic accents", "3D corridor of photos", "data cards with bars", "collage of people inside a letter", "orange accent", "giant footer wordmark"]
palette: ["#1F1F1F", "#F0ECE6", "#050607", "#6B5E5A", "#BEBDBB"]
type: ["Poppins", "Ibmplexserif", "Dmserifdisplay"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Flying through a corridor of photos behind the mission gives depth, and the collage N makes the people the brand.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Fill a letter of the mark with a collage of people

## What to leave

- Data cards look generic

## Signature move

A giant N filled with a collage of people turning orange.

## Motion

Intro: 'ON RD' splits (~2 s). Wheel (Lenis, SplitText): photos fly past in a 3D corridor; serif lines reveal; data cards rise with bars filling; the dark section pins while collage pieces assemble into the N and it turns orange; the footer word builds from strips.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; 1 video; split text; smoothed scroll (median 133 px still travelling after input stops); entry gate: Reject All, Close. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a consultancy: 'ON' and 'RD' splitting apart as the loader, a serif statement 'At Onward, we believe culture is the winning strategy' over a 3D corridor of photos (Brooklyn Bridge, people) that the camera flies through, data cards ('$2 Trillion', '$3 Trillion') on cream, a dark section where a giant N fills with a collage of people and turns orange, 'Turn In and Transform', 'Turn On and Drive', and a giant 'ONWARD' footer. Type: Poppins, Ibmplexserif, Dmserifdisplay.
Ground and ink from the measured palette (#1F1F1F, #F0ECE6, #050607). Motion carries the page through
a giant N filled with a collage of people turning orange. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — photography, collage

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: photography, collage

## Reference lock

Primary reference/direction: Onward - inclusive culture consultancy — A consultancy: 'ON' and 'RD' splitting apart as the loader, a serif statement 'At Onward, we believe culture is the winning strategy' over a 3D corridor of photos (Brooklyn Bridge, people) that the camera flies through, data cards ('$2 Trillion', '$3 Trillion') on cream, a dark section where a giant N fills with a collage of people and turns orange, 'Turn In and Transform', 'Turn On and Drive', and a giant 'ONWARD' footer.
Preserve (3-5 traits): serif statement with italic accents; 3D corridor of photos; data cards with bars; collage of people inside a letter; orange accent.
Borrow only (1-2): Fill a letter of the mark with a collage of people
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: photography, collage
Reject: Data cards look generic
Token commitments: palette #1F1F1F, #F0ECE6, #050607, #6B5E5A, #BEBDBB; type Poppins, Ibmplexserif, Dmserifdisplay; engine GSAP + Lenis linked (never vendored).
