---
title: "Mees Verberne - Creative Developer"
url: https://meesverberne.com/
source_url: https://meesverberne.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: pixel-dissolve-split-titles
dna: "Creative developer x pixel-block dissolves and section words split by the work"
register: other
grammar: chaptered editorial
lane: "A developer folio on beige: 'MEES VERBERNE' in heavy navy grotesk with a barcode, a red flash, a bird photo, 'W O RK' split wide with project media between the letters, projects (Mikki Sindhunata, iglo, Lucky Done Gone, Milka x Bloomon) whose images dissolve in and out through pixel blocks, 'CLI ( ) ENTS' split on navy with orange type, client names in a list, and a 'C ON NECT' footer with a blurred bird."
mode: read
traits: ["section words split wide around content", "pixel-block dissolve on images", "beige, navy and orange", "barcode detail", "client name list", "script signature in footer"]
palette: ["#7D6C9D", "#24253A", "#D2C1AA", "#695366", "#A18E86"]
type: ["Doner Text", "Doner Display", "icomoon"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Splitting each section word (W O RK, CLI ENTS, C ON NECT) leaves room for the content inside the word, and the pixel dissolve ties every image transition together.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Split the section word wide and put the content in the gap
- Dissolve images through pixel blocks

## What to leave

- Tiny project labels

## Signature move

'W O RK' split wide with project images dissolving through pixel blocks between the letters.

## Motion

Intro: beige (~1.5 s), the name, a red flash. Wheel (Lenis, SplitText, DrawSVG): the bird drifts; the section word splits apart; images pixel-dissolve in and out as projects pass; the navy panel rises; 'CLIENTS' splits; the footer word splits around the bird.

Measured (`motion/probe.json`): GSAP 3.12.5; 85 ScrollTriggers; Lenis; WebGL canvas x3 (three.js); 1 video; smoothed scroll (median 191 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a developer folio on beige: 'MEES VERBERNE' in heavy navy grotesk with a barcode, a red flash, a bird photo, 'W O RK' split wide with project media between the letters, projects (Mikki Sindhunata, iglo, Lucky Done Gone, Milka x Bloomon) whose images dissolve in and out through pixel blocks, 'CLI ( ) ENTS' split on navy with orange type, client names in a list, and a 'C ON NECT' footer with a blurred bird. Type: Doner Text, Doner Display, icomoon.
Ground and ink from the measured palette (#7D6C9D, #24253A, #D2C1AA). Motion carries the page through
'W O RK' split wide with project images dissolving through pixel blocks between the letters. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project photography, bird photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project photography, bird photography

## Reference lock

Primary reference/direction: Mees Verberne - Creative Developer — A developer folio on beige: 'MEES VERBERNE' in heavy navy grotesk with a barcode, a red flash, a bird photo, 'W O RK' split wide with project media between the letters, projects (Mikki Sindhunata, iglo, Lucky Done Gone, Milka x Bloomon) whose images dissolve in and out through pixel blocks, 'CLI ( ) ENTS' split on navy with orange type, client names in a list, and a 'C ON NECT' footer with a blurred bird.
Preserve (3-5 traits): section words split wide around content; pixel-block dissolve on images; beige, navy and orange; barcode detail; client name list.
Borrow only (1-2): Split the section word wide and put the content in the gap; Dissolve images through pixel blocks
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project photography, bird photography
Reject: Tiny project labels
Token commitments: palette #7D6C9D, #24253A, #D2C1AA, #695366, #A18E86; type Doner Text, Doner Display, icomoon; engine GSAP + Lenis linked (never vendored).
