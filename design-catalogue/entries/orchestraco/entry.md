---
title: "Orchestra - Communications for the new media landscape"
url: https://www.orchestraco.com/
source_url: https://www.orchestraco.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: institutional
category2: "product-focused"
family: cube-logo-consultancy
dna: "Communications consultancy x a cube logo that bursts into floating cubes"
register: modern clean
grammar: chaptered editorial
lane: "A consultancy on dark green: an aerial photo of an orchestra that shrinks to a card, the cube logo forming, the mission paragraph, the logo cubes bursting apart and floating around the text, 'We flipped the model', a light grey section with 'Advisory. Strategy. Execution. In concert.' pinned left and cards with small cube icons on the right, a blue stats section (01, 12, 20, 700+) on vertical lines, 'Ready to shape what's next?' and a peach footer where blocks fall."
mode: persuade
traits: ["aerial orchestra photo", "logo cubes bursting and floating", "pinned left heading with cards", "stats on vertical lines", "dark green, grey, blue and peach", "falling blocks in footer"]
palette: ["#223306", "#E7FFD9", "#46582E", "#AEC29A"]
type: ["degular", "degular-display", "proxima-sera", "Bricolage Grotesque"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The logo literally breaking into its parts to frame the mission is a strong link between name, mark and message.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Burst the logo into its parts to frame the mission text
- Pin the heading left while cards scroll right

## What to leave

- Small body text

## Signature move

Cube logo pieces floating around 'We flipped the model.'

## Motion

Intro: the orchestra photo shrinks to a card on green (~2 s), the logo builds from cubes. Wheel (Lenis, Taxi, SplitText): text blurs in; cubes burst and drift into a ring; the grey section pins its heading; stats rise on lines; blocks tumble into the footer.

Measured (`motion/probe.json`): GSAP 3.15.0/3.12.4; 10 ScrollTriggers; 1 pinned sections; Lenis; Taxi page transitions; smoothed scroll (median 133 px still travelling after input stops); entry gate: Reject All, Close. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a consultancy on dark green: an aerial photo of an orchestra that shrinks to a card, the cube logo forming, the mission paragraph, the logo cubes bursting apart and floating around the text, 'We flipped the model', a light grey section with 'Advisory. Strategy. Execution. In concert.' pinned left and cards with small cube icons on the right, a blue stats section (01, 12, 20, 700+) on vertical lines, 'Ready to shape what's next?' and a peach footer where blocks fall. Type: degular, degular-display, proxima-sera, Bricolage Grotesque.
Ground and ink from the measured palette (#223306, #E7FFD9, #46582E). Motion carries the page through
cube logo pieces floating around 'We flipped the model.' Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — aerial photography, 3D cubes

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: aerial photography, 3D cubes

## Reference lock

Primary reference/direction: Orchestra - Communications for the new media landscape — A consultancy on dark green: an aerial photo of an orchestra that shrinks to a card, the cube logo forming, the mission paragraph, the logo cubes bursting apart and floating around the text, 'We flipped the model', a light grey section with 'Advisory. Strategy. Execution. In concert.' pinned left and cards with small cube icons on the right, a blue stats section (01, 12, 20, 700+) on vertical lines, 'Ready to shape what's next?' and a peach footer where blocks fall.
Preserve (3-5 traits): aerial orchestra photo; logo cubes bursting and floating; pinned left heading with cards; stats on vertical lines; dark green, grey, blue and peach.
Borrow only (1-2): Burst the logo into its parts to frame the mission text; Pin the heading left while cards scroll right
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: aerial photography, 3D cubes
Reject: Small body text
Token commitments: palette #223306, #E7FFD9, #46582E, #AEC29A; type degular, degular-display, proxima-sera, Bricolage Grotesque; engine GSAP + Lenis linked (never vendored).
