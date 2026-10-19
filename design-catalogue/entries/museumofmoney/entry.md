---
title: "MoMoney - Museum of Money Dallas"
url: https://www.museumofmoney.com/
source_url: https://www.museumofmoney.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "playful"
family: sticker-pop-attraction
dna: "Interactive money museum x yellow sticker labels and tilted photo cards"
register: other
grammar: chaptered editorial
lane: "A visitor-attraction site: full-bleed video of money and kids at exhibits under a tilted yellow sticker headline, then cream sections with tilted photo cards, a location block, review cards, a blue CTA band and a map sticker in the footer."
mode: persuade
traits: ["yellow highlighter sticker headlines", "tilted photo cards with thick outlines", "cream ground", "electric blue CTA band", "press ticker under the hero", "hand-drawn map sticker"]
palette: ["#FFF5DD", "#6D3839", "#2A212D", "#716151", "#B48B63", "#CAC298"]
type: ["Archivo Black", "Manrope", "JetBrains Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The sticker system does the brand work: every headline is a tilted yellow label and every photo a tilted outlined card, so a plain stack of sections reads as a scrapbook for a fun day out.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Jordan Gilroy, Studio Chong).

## What to borrow (principle)

- Headline as a tilted highlighter sticker
- Tilted outlined photo cards for a playful attraction

## What to leave

- Native scroll with little motion past the hero
- Review cards in small type

## Signature move

Tilted yellow sticker headlines over money-themed exhibit photos.

## Motion

Intro: hero video cycles shots of cash and exhibits, the sticker headline stays fixed. Wheel (native, no smoothing): sections enter with simple reveals; photo cards sit tilted; the blue CTA band arrives as a hard colour change. Little scroll-linked motion.

Measured (`motion/probe.json`): 1 video. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a visitor-attraction site: full-bleed video of money and kids at exhibits under a tilted yellow sticker headline, then cream sections with tilted photo cards, a location block, review cards, a blue CTA band and a map sticker in the footer. Type: Archivo Black, Manrope, JetBrains Mono.
Ground and ink from the measured palette (#FFF5DD, #6D3839, #2A212D). Motion carries the page through
tilted yellow sticker headlines over money-themed exhibit photos. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — exhibit photography and video, people at installations

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: exhibit photography and video, people at installations

## Reference lock

Primary reference/direction: MoMoney - Museum of Money Dallas — A visitor-attraction site: full-bleed video of money and kids at exhibits under a tilted yellow sticker headline, then cream sections with tilted photo cards, a location block, review cards, a blue CTA band and a map sticker in the footer.
Preserve (3-5 traits): yellow highlighter sticker headlines; tilted photo cards with thick outlines; cream ground; electric blue CTA band; press ticker under the hero.
Borrow only (1-2): Headline as a tilted highlighter sticker; Tilted outlined photo cards for a playful attraction
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: exhibit photography and video, people at installations
Reject: Native scroll with little motion past the hero; Review cards in small type
Token commitments: palette #FFF5DD, #6D3839, #2A212D, #716151, #B48B63, #CAC298; type Archivo Black, Manrope, JetBrains Mono; engine GSAP + Lenis linked (never vendored).
