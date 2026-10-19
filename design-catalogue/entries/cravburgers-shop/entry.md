---
title: "CRAV"
url: https://www.cravburgers.shop/
source_url: https://www.cravburgers.shop/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: smash-burger-sticker-brand
dna: "Smash burger chain x cartoon stickers and wavy colour bands"
register: other
grammar: chaptered editorial
lane: "A burger brand on red and cream where a cartoon burger stacks itself in the loader, condensed red caps headlines are interrupted by cut-out ingredients, wavy red and yellow bands carry the sections, and a gloved cartoon burger character grabs the page."
mode: persuade
traits: ["loader that stacks a burger layer by layer", "ultra-condensed red caps", "wavy section edges in red and yellow", "cut-out ingredients flying across headlines", "cartoon burger character with gloves", "dashed travel route with photo stops"]
palette: ["#F5E4CE", "#F91814", "#AC6235", "#E9CA90", "#C6100F"]
type: ["Modak", "Mouse Memoirs"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The product assembles itself as the loader (bun, lettuce, patty), so the first thing the visitor sees is the brand's object being built. Sections are separated by soft waves rather than straight edges, and real ingredient cut-outs fly through the headlines, keeping a food site fun without losing appetite appeal.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Anyflow).

## What to borrow (principle)

- Assemble the product layer by layer as the loader
- Wavy section edges that roll in as the next colour band
- Real cut-out ingredients flying through big type

## What to leave

- Very busy: stickers, cut-outs and type together
- Headlines often cropped mid-word

## Signature move

A burger that stacks itself layer by layer in the loader.

## Motion

Intro: red ground, burger layers drop in one by one with 'preparing artisan kitchen…' and a progress bar (~2.5 s). Scroll (Lenis, ~145 px glide): 'THE BURGER' with the hero burger and stickers; 'JUICY CHEESY FULLY LOADED' with photo cards; red wave rises; 'FOOD THAT FEELS GOOD' with the gloved character; close-up burger photo grows; 'EVERY LAYER PACKED WITH SIGNATURE FLAVOR' with flying lettuce and tomato; yellow wave with a dashed travel route between city photos; 'FEEL THE CHANGE'; huge CRAV footer.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; smoothed scroll (median 143 px still travelling after input stops); entry gate: LATER. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a burger brand on red and cream where a cartoon burger stacks itself in the loader, condensed red caps headlines are interrupted by cut-out ingredients, wavy red and yellow bands carry the sections, and a gloved cartoon burger character grabs the page. Type: Modak, Mouse Memoirs.
Ground and ink from the measured palette (#F5E4CE, #F91814, #AC6235). Motion carries the page through
a burger that stacks itself layer by layer in the loader. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — glossy burger close-ups, people eating, cartoon stickers

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: glossy burger close-ups, people eating, cartoon stickers

## Reference lock

Primary reference/direction: CRAV — A burger brand on red and cream where a cartoon burger stacks itself in the loader, condensed red caps headlines are interrupted by cut-out ingredients, wavy red and yellow bands carry the sections, and a gloved cartoon burger character grabs the page.
Preserve (3-5 traits): loader that stacks a burger layer by layer; ultra-condensed red caps; wavy section edges in red and yellow; cut-out ingredients flying across headlines; cartoon burger character with gloves.
Borrow only (1-2): Assemble the product layer by layer as the loader; Wavy section edges that roll in as the next colour band
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: glossy burger close-ups, people eating, cartoon stickers
Reject: Very busy: stickers, cut-outs and type together; Headlines often cropped mid-word
Token commitments: palette #F5E4CE, #F91814, #AC6235, #E9CA90, #C6100F; type Modak, Mouse Memoirs; engine GSAP + Lenis linked (never vendored).
