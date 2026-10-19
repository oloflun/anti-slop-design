---
title: "Aventura Dental Arts"
url: https://aventuradentalarts.com/
source_url: https://aventuradentalarts.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: "institutional"
family: bw-portrait-dental-luxury
dna: "Cosmetic dentistry practice x black-and-white portraits and italic serif"
register: editorial print
grammar: chaptered editorial
lane: "A dental practice in black-and-white portraits and a condensed serif with italic words: 'Your smile, effortlessly enhanced' over video, a statement that fills grey to ink, service chapters (Esthetic Dentistry, Preventive Care) with B&W photos, equipment items in a numbered list and a team portrait under 'Team of Experts'."
mode: persuade
traits: ["black-and-white portrait photography", "condensed serif with italic words", "statement fill grey to ink", "numbered equipment list with product shots", "circle stats", "clean light and dark alternation"]
palette: ["#EAE8E9", "#17171D", "#928C8C", "#626165", "#C6C5C6"]
type: ["InstrumentSerif", "InterTight"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A medical service is styled like a fashion editorial: monochrome portraits, a tall serif with italic accents, generous white. It makes trust visual through craft rather than stock smiles.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: The First The Last Agency).

## What to borrow (principle)

- Monochrome portraits and a condensed serif to give a clinical service an editorial voice
- Numbered equipment list where each item gets its own product shot

## What to leave

- Heavy smoothing (~150 px glide)
- Many sections of similar weight

## Signature move

A condensed serif with italic accents over black-and-white portraits.

## Motion

Intro: dark with a spinner arc (~2 s). Scroll (Lenis, ~150 px glide, SplitText): 'Your smile, effortlessly enhanced' slides across video; statement fills; service chapters with B&W images swap; 'Technology-Driven' with equipment list highlighting each device; team portrait under a huge 'Team of Experts'; 'We are here to Enhance Your Smile'; circle stats; testimonial; close.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; 1 video; split text; smoothed scroll (median 151 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a dental practice in black-and-white portraits and a condensed serif with italic words: 'Your smile, effortlessly enhanced' over video, a statement that fills grey to ink, service chapters (Esthetic Dentistry, Preventive Care) with B&W photos, equipment items in a numbered list and a team portrait under 'Team of Experts'. Type: InstrumentSerif, InterTight.
Ground and ink from the measured palette (#EAE8E9, #17171D, #928C8C). Motion carries the page through
a condensed serif with italic accents over black-and-white portraits. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — black-and-white portraits and clinical equipment product shots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: black-and-white portraits and clinical equipment product shots

## Reference lock

Primary reference/direction: Aventura Dental Arts — A dental practice in black-and-white portraits and a condensed serif with italic words: 'Your smile, effortlessly enhanced' over video, a statement that fills grey to ink, service chapters (Esthetic Dentistry, Preventive Care) with B&W photos, equipment items in a numbered list and a team portrait under 'Team of Experts'.
Preserve (3-5 traits): black-and-white portrait photography; condensed serif with italic words; statement fill grey to ink; numbered equipment list with product shots; circle stats.
Borrow only (1-2): Monochrome portraits and a condensed serif to give a clinical service an editorial voice; Numbered equipment list where each item gets its own product shot
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: black-and-white portraits and clinical equipment product shots
Reject: Heavy smoothing (~150 px glide); Many sections of similar weight
Token commitments: palette #EAE8E9, #17171D, #928C8C, #626165, #C6C5C6; type InstrumentSerif, InterTight; engine GSAP + Lenis linked (never vendored).
