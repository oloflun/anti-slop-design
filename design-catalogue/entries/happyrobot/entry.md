---
title: "HappyRobot"
url: https://www.happyrobot.ai
source_url: https://www.happyrobot.ai
captured: 2026-09-04
origin: raw-url
raw: raw/044ccc73bf151c18-www-happyrobot-ai.webp
extract: ok
category: product-focused
category2: institutional
family: cream-enterprise-serif
dna: "Enterprise SaaS deck x quiet paper ledger"
register: modern clean
grammar: chaptered editorial
lane: "A cream, ledger-quiet enterprise pitch: serif display claims stacked over sans-serif proof — logo walls, paired stat cards, vertical photo grids — closing on a repeated dark-CTA banner"
mode: persuade
traits: ["cream paper ground", "old-style serif display", "small-caps sans kickers", "logo-wall social proof", "paired before/after stat cards", "muted industry photo grid", "tan announcement bar", "black pill CTAs"]
palette: ["#ECE8E3", "#B7B2AA", "#584736", "#1B1814", "#7F7D72"]
type: ["Tobias", "Suisse Intl"]
measured: designlang (confirmed)
kind: reference-style
source: claude
status: ready
---

## Why it works

The page borrows the authority of print finance decks rather than SaaS marketing: an
old-style serif (Tobias) carries every headline at a size and leading that would read
naturally in a shareholder letter, while a functional grotesque (Suisse Intl) carries
every other word — nav, body copy, labels, buttons. The split is total and load-bearing;
because the serif never appears smaller than an H2, the reader always knows when the page
is making a claim versus stating a fact.

Colour is almost entirely absent — a warm, slightly grey cream ground (`#ECE8E3`) and
near-black ink (`#1B1814`) do nearly all the work, so the one tan accent bar at the very
top and the black CTA pills read as genuinely rare, not decorative. Photography is kept
desaturated and cool (turbines, freight yards, ports) and boxed into a strict grid rather
than run full-bleed, which keeps the page reading as a document with illustrations, not a
brand film.

Proof is structured, not narrated: a dense logo wall, then a grid of industry photo tiles
labelled by vertical, then paired stat cards ("70% reduction" next to "10% margin
increase") set in the same small mono-weight caption style as everything else. Nothing is
oversized or centred for emphasis — the numbers earn attention by being the only bold,
large glyphs against acres of quiet grey type, the same device the serif headlines use one
level up.

The copy voice underneath the type system matches the same restraint: friendly in tone but
we-only in pronoun throughout, so the company stays the actor in every claim rather than
addressing the reader directly (from designlang extract).

## What to borrow (principle)

- **One serif for claims, one sans for everything else, no third voice.** The reader
  learns the grammar in one screen and never has to re-parse a headline as a label.
- **Spend colour on exactly one non-neutral element.** Here it's the top announcement bar
  and the CTA pills; every other surface stays cream, grey, or near-black.
- **Let proof be a grid, not a paragraph.** Logo walls and stat pairs, ruled and evenly
  spaced, persuade an enterprise buyer faster than adjective-heavy copy.
- **Desaturate photography toward the ink, not away from it.** Cool, muted industry
  photos sit inside the same tonal range as the type, so images never fight the grid.
- **Repeat the close, don't escalate it.** The final CTA restates the opening line in the
  same serif/sans pair rather than introducing a new device.

## What to leave

- The thin decorative line diagram behind the hero photo tiles — it reads as filler
  geometry with no informational payload and competes with the headline for attention.
- The cookie banner overlapping the primary CTA on first paint (observed in this capture,
  locale-triggered) — worth designing around explicitly rather than leaving to the consent
  library's default position.
- Card backgrounds that shift from cream to a slightly darker taupe block with no other
  signal for why (the "we handle the work that matters most" band) — the tonal jump reads
  arbitrary rather than structural.

## Signature move

The paired stat card: two numbers in the same weight and size, one framed as a cost/effort
reduction and one as a gain, set side by side with no chart, just ruled whitespace and
mono-caption labels underneath. It turns the page's restraint into the pitch itself — the
numbers don't need decoration because everything around them is already quiet.

## Motion

Feel reads as mixed rather than a single house rhythm, and the page is scroll-linked:
sections trigger their own enter animations as they cross the viewport instead of firing on
load. Short micro-interactions (hover states, icon pops) run at 150-200ms while section and
card reveals stretch to 280-420ms. Three easing curves are in real use, all plain cubic
decelerate/accelerate curves with no spring or overshoot: a standard
`cubic-bezier(0.4,0,0.2,1)` for generic property transitions, a snappier custom
`cubic-bezier(0.33,0,0.15,1)` for transform-heavy moves, and a symmetric
`cubic-bezier(0.65,0,0.35,1)` ease-in-out. The keyframe vocabulary is small and functional:
`hero-enter` and `demoFadeIn` fade content up/down into place on entrance, `hr-blink` pulses
opacity for a blinking-indicator effect, `hr-marquee`/`demoLogoMarquee` loop a horizontal
translate to -50% for the scrolling logo wall, `hr-underline-sweep` wipes a link underline
out then back in across a hover, and the generic Tailwind `enter`/`exit` pair plus two
scale-pop keyframes (one with a fixed 45° rotate, one without) handle small icon/badge
pop-ins. No stagger or choreography pattern is documented beyond scroll-triggered section
entry (from designlang extract).

| token | value | used for |
|---|---|---|
| xs | 150ms | micro/hover transitions |
| sm | 200ms | button, icon state changes |
| md | 280ms | height/opacity reveals |
| lg | 420ms | section/card entrances |
| ease | `cubic-bezier(0.4,0,0.2,1)` | standard property transitions |
| ease | `cubic-bezier(0.33,0,0.15,1)` | transform-heavy moves |
| ease | `cubic-bezier(0.65,0,0.35,1)` | symmetric in-out |

## Brief

Build a cream-paper enterprise pitch page for an AI/software product selling to large
buyers. Ground the whole page in a warm, slightly grey off-white (`#ECE8E3`) with near-
black ink (`#1B1814`); reserve colour for a single top announcement bar and black CTA
pills. Set every headline in an old-style serif at a size that reads like a pull-quote;
set every label, nav item, button and body line in a functional grotesque, never mixing
the two roles. Open on a serif headline over a thin-line diagram or a single muted photo,
with a work-email capture field beside the CTA. Below the fold, alternate: a dense logo
wall; a photo grid of use-case tiles labelled by vertical; paired stat cards with no
chart, just numbers and mono captions; a single embedded product video in a dark frame.
Close on a full-width dark or cream banner that restates the opening headline and repeats
the CTA.

## Image recipe

Documentary industrial photograph of [SUBJECT] — logistics yards, freight, ports, energy
infrastructure — shot in overcast or blue-hour light, desaturated toward cool grey-blue,
no people posed for camera, no gradient overlay, cropped tightly into a grid tile rather
than run full-bleed, contrast kept low so the photo reads as documentation, not a hero.

## Photo search

Unsplash first, Pexels second.
- "freight yard overcast blue hour"
- "wind turbines offshore muted"
- "warehouse logistics workers documentary"
- "shipping port cranes desaturated"

## Reference lock

Primary reference/direction: HappyRobot — cream enterprise pitch, serif claims over sans
proof, stat pairs as the persuasion device.
Preserve (3-5 traits): warm cream ground `#ECE8E3` with near-black ink `#1B1814`; old-style
serif (Tobias-class) reserved for headlines only; small functional-grotesque kickers and
body in one weight; proof delivered as logo walls and paired stat cards, never prose
claims; black pill CTAs as the only saturated shape on the page.
Borrow only (1-2): the single tan/accent announcement bar at the very top; the dark
embedded-video frame as a mid-page break.
Role rules: serif never sets a label or button; sans never sets a headline; colour
appears on at most two elements per screen (announcement bar, CTA); photography stays
desaturated within the page's tonal range, never full-saturation.
Media strategy: photo:unsplash — documentary industrial/logistics stills, muted and cool,
always cropped into a grid tile, never a full-bleed emotional hero.
Reject: full-bleed saturated hero photography; decorative line-art with no informational
role; more than one accent colour; centred marketing copy blocks; animated counters or
gradient CTAs.
Token commitments: bg `#ECE8E3`, bg-alt `#B7B2AA`, ink `#1B1814`, ink-soft `#584736`,
stone `#7F7D72`; display `Tobias` (or nearest old-style serif), body/label `Suisse Intl`
(or Suisse-class grotesque); headline set large with tight leading, body and labels one
consistent small size; grid strictly ruled, generous vertical whitespace between chapters.
