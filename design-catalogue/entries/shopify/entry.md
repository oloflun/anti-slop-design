---
title: "Shopify Editions - release site"
url: https://www.shopify.com/editions/spring2026
source_url: https://www.shopify.com/editions/spring2026
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: aurora-chapter-release-notes
dna: "Platform release x chapters of auroral WebGL colour with product UI"
register: cinematic dark
grammar: chaptered editorial
lane: "A release site on black: 'Everywhere' in white letters flying in a particle forest, chapters (Agentic commerce, Sidekick, Online, Retail, Marketing, Operations, Shop app, Finance) each with an aurora or particle field in a different colour and product UI cards, feature lists in small type, a chapter tab at the bottom."
mode: read
traits: ["particle and aurora fields per chapter", "chapter word large on the field", "UI cards", "chapter tab navigation", "black ground", "fine feature lists"]
palette: ["#090909", "#A88D7F", "#424953", "#776B80", "#23273C", "#D0B6AB"]
type: ["Inter-Variable", "National2", "ShopifyInter", "Inter"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Each chapter gets a different colour field, so a long list of features reads as rooms.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Shopify).

## What to borrow (principle)

- Give each chapter its own colour field behind a single word

## What to leave

- Dense feature lists

## Signature move

'Everywhere' flying through a particle forest.

## Motion

Intro: black particles (~2 s), letters fly in. Wheel: the field shifts colour per chapter; the chapter word fades; UI cards slide; the bottom tab follows.

Measured (`motion/probe.json`): Lenis; 13 video; smoothed scroll (median 69 px still travelling after input stops); entry gate: Reject all. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a release site on black: 'Everywhere' in white letters flying in a particle forest, chapters (Agentic commerce, Sidekick, Online, Retail, Marketing, Operations, Shop app, Finance) each with an aurora or particle field in a different colour and product UI cards, feature lists in small type, a chapter tab at the bottom. Type: Inter-Variable, National2, ShopifyInter, Inter.
Ground and ink from the measured palette (#090909, #A88D7F, #424953). Motion carries the page through
'Everywhere' flying through a particle forest. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL particles, UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL particles, UI

## Reference lock

Primary reference/direction: Shopify Editions - release site — A release site on black: 'Everywhere' in white letters flying in a particle forest, chapters (Agentic commerce, Sidekick, Online, Retail, Marketing, Operations, Shop app, Finance) each with an aurora or particle field in a different colour and product UI cards, feature lists in small type, a chapter tab at the bottom.
Preserve (3-5 traits): particle and aurora fields per chapter; chapter word large on the field; UI cards; chapter tab navigation; black ground.
Borrow only (1-2): Give each chapter its own colour field behind a single word
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL particles, UI
Reject: Dense feature lists
Token commitments: palette #090909, #A88D7F, #424953, #776B80, #23273C, #D0B6AB; type Inter-Variable, National2, ShopifyInter, Inter; engine GSAP + Lenis linked (never vendored).
