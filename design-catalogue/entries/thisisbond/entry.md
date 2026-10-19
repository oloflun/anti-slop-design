---
title: "BOND - brand agency"
url: https://www.thisisbond.com/
source_url: https://www.thisisbond.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: ""
family: blob-wordmark-brand-agency
dna: "Brand agency x a melting blob wordmark and a giant red 'one' behind the studio facts"
register: cinematic dark
grammar: chaptered editorial
lane: "A brand agency: 'Originality pays. Let's find yours.' over a sequence of full-bleed film close-ups (fabric, a face, a blue identity), the 'BOND' wordmark in fat white letters that melt and stretch as it scrolls, serif paragraphs where lines brighten, 'The Originality Dividend.' in red serif, filter pills over a mixed grid of cases and opinion cards (Visa, Norrin, cans), 'Independent since 2009. 40 people, 15 nationalities' over a giant red 'one', an AI toolkit card, testimonials in coloured cards and the melting wordmark again in the footer."
mode: persuade
traits: ["melting blob wordmark", "serif paragraphs brightening", "red serif statement", "filter pills over a mixed grid", "giant red word behind facts", "coloured testimonial cards"]
palette: ["#282828", "#5B75AD", "#33518F", "#83576E", "#DFDBC6", "#02040B"]
type: ["Signifier", "SCTO Groteska Bond"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The wordmark melting under the scroll gives a type-only identity a physical moment, and it returns at the end as a bookend.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Let the wordmark deform with scroll and bring it back in the footer
- Put a giant red word behind the studio facts

## What to leave

- Cookie panel at start

## Signature move

The fat BOND wordmark melting and stretching as you scroll.

## Motion

Intro: full-bleed close-up films cutting under the headline (~4 s). Wheel (Lenis): the wordmark rises and melts; serif lines fade from grey; the grid slides up with pills; 'one' scales behind the facts; cards slide sideways; the footer wordmark melts back.

Measured (`motion/probe.json`): GSAP 3.15.0; 10 ScrollTriggers; Lenis; 27 video; split text; entry gate: Deny all, Skip to main content. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a brand agency: 'Originality pays. Let's find yours.' over a sequence of full-bleed film close-ups (fabric, a face, a blue identity), the 'BOND' wordmark in fat white letters that melt and stretch as it scrolls, serif paragraphs where lines brighten, 'The Originality Dividend.' in red serif, filter pills over a mixed grid of cases and opinion cards (Visa, Norrin, cans), 'Independent since 2009. 40 people, 15 nationalities' over a giant red 'one', an AI toolkit card, testimonials in coloured cards and the melting wordmark again in the footer. Type: Signifier, SCTO Groteska Bond.
Ground and ink from the measured palette (#282828, #5B75AD, #33518F). Motion carries the page through
the fat BOND wordmark melting and stretching as you scroll. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — brand film close-ups, case imagery

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: brand film close-ups, case imagery

## Reference lock

Primary reference/direction: BOND - brand agency — A brand agency: 'Originality pays. Let's find yours.' over a sequence of full-bleed film close-ups (fabric, a face, a blue identity), the 'BOND' wordmark in fat white letters that melt and stretch as it scrolls, serif paragraphs where lines brighten, 'The Originality Dividend.' in red serif, filter pills over a mixed grid of cases and opinion cards (Visa, Norrin, cans), 'Independent since 2009. 40 people, 15 nationalities' over a giant red 'one', an AI toolkit card, testimonials in coloured cards and the melting wordmark again in the footer.
Preserve (3-5 traits): melting blob wordmark; serif paragraphs brightening; red serif statement; filter pills over a mixed grid; giant red word behind facts.
Borrow only (1-2): Let the wordmark deform with scroll and bring it back in the footer; Put a giant red word behind the studio facts
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: brand film close-ups, case imagery
Reject: Cookie panel at start
Token commitments: palette #282828, #5B75AD, #33518F, #83576E, #DFDBC6, #02040B; type Signifier, SCTO Groteska Bond; engine GSAP + Lenis linked (never vendored).
