---
title: "MetaMask"
url: https://metamask.io/
source_url: https://metamask.io/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: blocky-type-fox-wallet
dna: "Crypto wallet x chunky pixel-cut display type, low-poly fox, coins and phone UI on lime, navy and peach"
register: other
grammar: chaptered editorial
lane: "A wallet homepage: a lime loader with the wordmark, a dark green panel 'Where your money lives' in blocky cut type with an orange low-poly fox rising from below, the headline filled with coins, a phone with balances the fox peeks out of, 'Trade anything', feature cards with 3D props (bitcoin, tesla, gift), 'Turn your money on' with coins orbiting on violet, peach 'Maximum security' with a glass card, stats cards and a 'Get started' close."
mode: persuade
traits: ["blocky cut display type", "low-poly fox mascot", "3D coin and prop renders", "colour-blocked feature cards", "phone UI as hero object"]
palette: ["#E5FFC1", "#013430", "#1F1E1A", "#A8B1A4"]
type: ["MMPolyVariable", "MMSansMono", "MMSansVariable", "MMEuclidCircularB"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The fox appears in every chapter (behind the headline, inside the phone, guarding security) and turns a feature list into one character's tour.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Antinomy Studio).

## What to borrow (principle)

- Let one mascot carry the reader from chapter to chapter

## What to leave

- Cookie dialog over the headline
- Huge footer

## Signature move

An orange low-poly fox rising behind 'Where your money lives'.

## Motion

Intro: lime panel, wordmark (~1.5 s). Wheel (Lenis, smoothed): the headline mask fills with coins; the fox slides up and into the phone; cards stagger; coins orbit; grounds switch colour.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x2 (three.js); 1 video; smoothed scroll (median 127 px still travelling after input stops); entry gate: Avvisa Ej väsentligt. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a wallet homepage: a lime loader with the wordmark, a dark green panel 'Where your money lives' in blocky cut type with an orange low-poly fox rising from below, the headline filled with coins, a phone with balances the fox peeks out of, 'Trade anything', feature cards with 3D props (bitcoin, tesla, gift), 'Turn your money on' with coins orbiting on violet, peach 'Maximum security' with a glass card, stats cards and a 'Get started' close. Type: MMPolyVariable, MMSansMono, MMSansVariable, MMEuclidCircularB.
Ground and ink from the measured palette (#E5FFC1, #013430, #1F1E1A). Motion carries the page through
an orange low-poly fox rising behind 'Where your money lives'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D renders, UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D renders, UI

## Reference lock

Primary reference/direction: MetaMask — A wallet homepage: a lime loader with the wordmark, a dark green panel 'Where your money lives' in blocky cut type with an orange low-poly fox rising from below, the headline filled with coins, a phone with balances the fox peeks out of, 'Trade anything', feature cards with 3D props (bitcoin, tesla, gift), 'Turn your money on' with coins orbiting on violet, peach 'Maximum security' with a glass card, stats cards and a 'Get started' close.
Preserve (3-5 traits): blocky cut display type; low-poly fox mascot; 3D coin and prop renders; colour-blocked feature cards; phone UI as hero object.
Borrow only (1-2): Let one mascot carry the reader from chapter to chapter
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D renders, UI
Reject: Cookie dialog over the headline; Huge footer
Token commitments: palette #E5FFC1, #013430, #1F1E1A, #A8B1A4; type MMPolyVariable, MMSansMono, MMSansVariable, MMEuclidCircularB; engine GSAP + Lenis linked (never vendored).
