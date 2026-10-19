---
title: "P-V (Paolo Vendramini) - branding"
url: https://www.paolovendramini.com/
source_url: https://www.paolovendramini.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: ""
family: letterbox-card-over-fullbleed-cases
dna: "Branding studio x full-bleed campaign images cycling behind one small white card that frames each case"
register: other
grammar: rhythmic cutlist
lane: "A studio reel as a page: a black loader where 'P' and 'V' are pushed apart by a white bar, then full-bleed case images (a wellness brand, wine labels, a gin, a cake brand, a drinks campaign, sneakers, a Netflix mural, a coffee illustration, crackers packaging, an olive pattern, a lemonade) cutting one after another behind a small white card in the centre that shows the project's name, a thumbnail and tags."
mode: persuade
traits: ["full-bleed case cutlist", "fixed small card framing each case", "bar loader splitting the initials", "bold colour campaign imagery"]
palette: ["#372723", "#5C4943", "#110C07", "#C29C87", "#E7D1C0", "#FFFFFF"]
type: ["NeueMontreal-Regular", "NeueMontreal-Bold"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Keeping one small card fixed while the full-bleed images cut behind it lets very different clients read as one reel.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: ET Studio).

## What to borrow (principle)

- Fix one small frame while full-bleed cases cut behind it

## What to leave

- Card text very small

## Signature move

A small white card fixed in the centre while full-bleed campaign images cut behind it.

## Motion

Intro: P and V pushed apart by a bar (~2 s). Wheel: hard cuts between case images per step; the card content swaps; the thumbnail slides.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 2 video; smoothed scroll (median 140 px still travelling after input stops); entry gate: Rifiuta tutto. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the rhythmic cutlist grammar: a studio reel as a page: a black loader where 'P' and 'V' are pushed apart by a white bar, then full-bleed case images (a wellness brand, wine labels, a gin, a cake brand, a drinks campaign, sneakers, a Netflix mural, a coffee illustration, crackers packaging, an olive pattern, a lemonade) cutting one after another behind a small white card in the centre that shows the project's name, a thumbnail and tags. Type: NeueMontreal-Regular, NeueMontreal-Bold.
Ground and ink from the measured palette (#372723, #5C4943, #110C07). Motion carries the page through
a small white card fixed in the centre while full-bleed campaign images cut behind it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — campaign photography, packaging

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: campaign photography, packaging

## Reference lock

Primary reference/direction: P-V (Paolo Vendramini) - branding — A studio reel as a page: a black loader where 'P' and 'V' are pushed apart by a white bar, then full-bleed case images (a wellness brand, wine labels, a gin, a cake brand, a drinks campaign, sneakers, a Netflix mural, a coffee illustration, crackers packaging, an olive pattern, a lemonade) cutting one after another behind a small white card in the centre that shows the project's name, a thumbnail and tags.
Preserve (3-5 traits): full-bleed case cutlist; fixed small card framing each case; bar loader splitting the initials; bold colour campaign imagery.
Borrow only (1-2): Fix one small frame while full-bleed cases cut behind it
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: campaign photography, packaging
Reject: Card text very small
Token commitments: palette #372723, #5C4943, #110C07, #C29C87, #E7D1C0, #FFFFFF; type NeueMontreal-Regular, NeueMontreal-Bold; engine GSAP + Lenis linked (never vendored).
