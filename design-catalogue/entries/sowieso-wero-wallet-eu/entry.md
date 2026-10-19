---
title: "Wero - iDEAL is becoming Wero (merchants)"
url: https://sowieso.wero-wallet.eu/nl-en/merchant
source_url: https://sowieso.wero-wallet.eu/nl-en/merchant
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: gradient-3d-sticker-fintech
dna: "Payment brand transition x pink-to-yellow gradient, chunky condensed caps and glossy 3D objects that tumble through"
register: other
grammar: chaptered editorial
lane: "A payment-scheme migration page: two big 3D hands framing 'iDEAL is becoming Wero' on a hot pink to yellow gradient, a paper plane and puzzle pieces flying through the headline as it reflows into 'the new European way to pay', merchant phases as tilted gradient cards with a clock, a stack of FAQs each answered by its own 3D object (a padlock for reliability, a coin for ease, a piggy bank for banks), a video interview, a 3D bank building, and a logo wall of partners."
mode: persuade
traits: ["pink-to-yellow gradient ground", "chunky condensed caps", "3D glossy objects per question", "highlighted word in a pill", "tilted gradient cards", "floating pill navigation"]
palette: ["#FFF590", "#FF998C", "#783D4D", "#A3E9AF", "#FFFDD7"]
type: ["GT Walsheim Wero"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Giving each anxious question its own playful 3D object turns a dull migration notice into something a merchant scrolls through willingly.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: 51north).

## What to borrow (principle)

- Answer each objection with its own object, not just text

## What to leave

- Cookie dialog over the hero
- Many pills

## Signature move

Two 3D hands framing 'iDEAL is becoming Wero' on a pink-yellow gradient.

## Motion

Intro: cookie gate, hands slide in. Wheel (Lenis, 7 pins): the headline reflows while a paper plane crosses it; cards tilt and stack; each question pins while its object spins in; highlighted words get a pill.

Measured (`motion/probe.json`): GSAP 3.15.0; 7 pinned sections; Lenis; 7 video; smoothed scroll (median 146 px still travelling after input stops); entry gate: Deny. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a payment-scheme migration page: two big 3D hands framing 'iDEAL is becoming Wero' on a hot pink to yellow gradient, a paper plane and puzzle pieces flying through the headline as it reflows into 'the new European way to pay', merchant phases as tilted gradient cards with a clock, a stack of FAQs each answered by its own 3D object (a padlock for reliability, a coin for ease, a piggy bank for banks), a video interview, a 3D bank building, and a logo wall of partners. Type: GT Walsheim Wero.
Ground and ink from the measured palette (#FFF590, #FF998C, #783D4D). Motion carries the page through
two 3D hands framing 'iDEAL is becoming Wero' on a pink-yellow gradient. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D glossy objects, video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D glossy objects, video

## Reference lock

Primary reference/direction: Wero - iDEAL is becoming Wero (merchants) — A payment-scheme migration page: two big 3D hands framing 'iDEAL is becoming Wero' on a hot pink to yellow gradient, a paper plane and puzzle pieces flying through the headline as it reflows into 'the new European way to pay', merchant phases as tilted gradient cards with a clock, a stack of FAQs each answered by its own 3D object (a padlock for reliability, a coin for ease, a piggy bank for banks), a video interview, a 3D bank building, and a logo wall of partners.
Preserve (3-5 traits): pink-to-yellow gradient ground; chunky condensed caps; 3D glossy objects per question; highlighted word in a pill; tilted gradient cards.
Borrow only (1-2): Answer each objection with its own object, not just text
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D glossy objects, video
Reject: Cookie dialog over the hero; Many pills
Token commitments: palette #FFF590, #FF998C, #783D4D, #A3E9AF, #FFFDD7; type GT Walsheim Wero; engine GSAP + Lenis linked (never vendored).
