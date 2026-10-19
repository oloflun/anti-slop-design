---
title: "PX PUSH"
url: https://pxpush.com/
source_url: https://pxpush.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: chrome-y2k-design-subscription
dna: "Design subscription x Y2K chrome and floppy disks"
register: modern clean
grammar: chaptered editorial
lane: "A design-subscription page in Y2K mode: a chrome 3D 'px' badge spins over a sky photo under a marquee, the pitch fills grey to white, a cobalt section stacks its benefits as an accordion with photos, and pricing packages sit beside a slowly turning 3D floppy disk."
mode: persuade
traits: ["chrome 3D logo badge spinning", "sky photograph ground", "large marquee headlines", "grey-to-white statement fill", "cobalt accordion of benefits with photos", "3D floppy disk beside pricing"]
palette: ["#152021", "#6C6D78", "#8197AF", "#2A445B", "#595660", "#A1ACBB"]
type: ["Graphik", "SemiSqueezed", "Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A plain offer (design on subscription) gets a nostalgic object language: a chrome badge like a 2000s sticker, floppy disks as the price packages. Each object turns slowly in 3D, so a pricing page has something physical in it. Marquees and grey-to-white fills keep the copy moving at reading pace.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Lewis Webber, PX PUSH, Stud, Stud Creative House).

## What to borrow (principle)

- Give a service an object that stands for it (floppy disk = package) and turn it slowly beside the price
- Marquee section titles that bleed off both edges as chapter markers
- Accordion list where each opened row brings its own photo

## What to leave

- Several grounds (sky, grey, dark, cobalt) in quick succession
- Small mono body text

## Signature move

A chrome 'px' badge spinning in 3D over a sky photograph.

## Motion

Intro: the chrome badge flips and spins over the clouds while the 'On-Demand Design Department' marquee runs (~2 s); project thumbnails swap bottom-left. Scroll (Lenis, ~70 px glide, Observer, WebGL x3): 'PX PUSH' marquee; statement fills grey→white per line; dark project strip; cobalt section where benefit rows open in turn with photos; 'Packages' marquee with a 3D floppy disk rotating beside Standard/Pro prices; 'Brand Sprint' marquee.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x3 (three.js); 1 video; smoothed scroll (median 78 px still travelling after input stops); entry gate: x. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a design-subscription page in Y2K mode: a chrome 3D 'px' badge spins over a sky photo under a marquee, the pitch fills grey to white, a cobalt section stacks its benefits as an accordion with photos, and pricing packages sit beside a slowly turning 3D floppy disk. Type: Graphik, SemiSqueezed, Mono.
Ground and ink from the measured palette (#152021, #6C6D78, #8197AF). Motion carries the page through
a chrome 'px' badge spinning in 3D over a sky photograph. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — Y2K chrome objects and retro hardware renders, sky photography, candid portraits

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: Y2K chrome objects and retro hardware renders, sky photography, candid portraits

## Reference lock

Primary reference/direction: PX PUSH — A design-subscription page in Y2K mode: a chrome 3D 'px' badge spins over a sky photo under a marquee, the pitch fills grey to white, a cobalt section stacks its benefits as an accordion with photos, and pricing packages sit beside a slowly turning 3D floppy disk.
Preserve (3-5 traits): chrome 3D logo badge spinning; sky photograph ground; large marquee headlines; grey-to-white statement fill; cobalt accordion of benefits with photos.
Borrow only (1-2): Give a service an object that stands for it (floppy disk = package) and turn it slowly beside the price; Marquee section titles that bleed off both edges as chapter markers
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: Y2K chrome objects and retro hardware renders, sky photography, candid portraits
Reject: Several grounds (sky, grey, dark, cobalt) in quick succession; Small mono body text
Token commitments: palette #152021, #6C6D78, #8197AF, #2A445B, #595660, #A1ACBB; type Graphik, SemiSqueezed, Mono; engine GSAP + Lenis linked (never vendored).
