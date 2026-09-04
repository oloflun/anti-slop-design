---
title: "Insign"
url: https://www.insign.se/
source_url: https://www.insign.se/
captured: 2026-09-04
origin: raw-url
raw: ""
extract: ok
category: portfolio
category2: ""
family: colour-blocked-service-bands
dna: "Swedish full-service agency ledger x saturated colour-blocked service chapters"
register: modern clean
grammar: chaptered editorial
lane: "A plain white hero with a serif logotype and a dark abstract photo gives way to a mosaic collage strip, then three fully saturated colour-blocked service bands, a white project archive, and a dark stats-and-team close"
mode: persuade
traits: ["serif logotype on plain white nav", "dark abstract hero photograph", "mosaic photo collage strip", "fully saturated colour-blocked service bands", "device-mockup photography per service", "dark stats band with large numerals", "team headshot grid", "dark footer CTA band"]
palette: ["#FFFFFF", "#1A1818", "#ECF58F", "#D1C8D6", "#F2895C", "#484B48"]
type: ["Neue Haas Grotesk RoundDots"]
measured: designlang (confirmed)
kind: reference-style
source: claude
status: ready
---

## Why it works

The page opens conventionally — white ground, serif logotype, plain sans headline over a
dark abstract photograph — before committing to its real device: three service categories
(Webbdesign, Marknadsföring, Design), each rendered as a full-width band in one fully
saturated flat colour (chartreuse, lavender, orange), with no two adjacent bands sharing a
colour family. Because each band is a completely different hue and each pairs a bold
sans heading with a small device-mockup photograph relevant to that service, a visitor
can identify which service they're looking at from a glance at colour alone, before
reading a word — the palette itself becomes the navigation.

Everything outside those three bands stays deliberately plain: white for the hero and
project archive, near-black for the stats and footer. This means the saturated colour
budget is spent entirely on the service bands, so they read as the loudest, most
memorable part of the page rather than competing with hero or proof sections for
attention.

The proof strategy is literal and cumulative rather than persuasive copy: a dark stats
band states three plain numbers (5.0/5.0, 180+, 2002) with no chart or illustration, a
full team headshot grid follows immediately after ("a long-term partner"), and a news
strip closes with real, dated articles. Each proof element uses a different but equally
unadorned format — numerals, faces, dates — so the credibility argument doesn't repeat
itself. That plain-spoken restraint carries into the copy itself: the extract's brand-voice
read is neutral in tone and written in third person rather than the direct-address "you"
common elsewhere in this set, matching the page's unadorned, ledger-like proof strategy
(from designlang extract).

## What to borrow (principle)

- **Assign one fully saturated, non-repeating colour to each service or product
  category**, so the palette itself functions as a navigation and recognition system.
- **Spend your colour budget entirely on the differentiator (the service list)** and keep
  every surrounding section — hero, proof, footer — plain, so the coloured bands stay the
  memorable part of the page.
- **Pair each coloured service band with one small, specific photograph** (a device
  mockup, a real deliverable) rather than an abstract icon alone — it grounds the claim in
  an actual output.
- **Vary your proof formats** (plain numerals, a face grid, dated news) rather than
  repeating the same testimonial-card pattern three times.

## What to leave

- Three adjacent fully saturated colour bands (chartreuse, lavender, orange) in quick
  succession is a high-intensity sequence; a visitor scrolling quickly experiences three
  hard colour jumps in a row with no neutral pause between them.
- The service band headlines wrap awkwardly at this viewport width ("Webbdesig / n"),
  visible in this capture — worth a tighter line-length rule for the bold display size
  used there.
- The hero's cookie-consent panel and the dark abstract photo compete for the same lower-
  right screen quadrant on load in this capture; sequencing so only one overlay commands
  attention at a time would help.

## Signature move

The colour-per-service system: each of the three core service categories gets one
completely saturated, non-repeating flat colour as its entire band background, so the
page's palette becomes a direct index of what the agency offers — a visitor can navigate
by colour memory alone on a return visit.

## Motion

Motion feel reads as springy, and the page is scroll-linked. The duration scale runs six
steps from 100ms to 750ms, plus an outlier `xxl` token at 4.001s that is almost certainly
timing a slow background loop — a hero crossfade or an auto-advancing carousel — rather
than a UI transition. Easing is the most varied of this batch: a plain `ease-in-out`
("ease") covers the large majority of uses, a custom decelerate curve
(`cubic-bezier(0.2, 0, 0.3, 1)`) covers a third family, and single uses each of `linear`,
`ease-in`, and `ease-out` round it out — alongside one explicit spring/overshoot curve,
`cubic-bezier(0.68, -0.55, 0.265, 1.55)`, flagged by the extract itself for its negative
control point. That one spring curve, despite firing only once, is the likely source of
the page's overall "springy" rating. Keyframe use is the busiest in this set and reads as
stock UI-library chrome rather than an authored system: `fadeIn` recurs across several
elements, `ball-scale-multiple` (a scale-plus-opacity "reveal") matches a typical
loading-spinner pattern, `dipi_fade` names the Divi WordPress builder as its source, and
`mc_slideOut` (animating the `bottom` property) is consistent with a slide-up/out panel —
plausibly the same cookie-consent overlay flagged in "What to leave" above as competing
with the hero photo for attention. No stagger choreography is recorded (from designlang
extract).

| kind | name/family | value |
|---|---|---|
| duration | `xs` | 100ms |
| duration | `sm` | 200ms |
| duration | `md` | 275ms |
| duration | `lg` | 500ms |
| duration | `xl` | 750ms |
| duration | `xxl` | 4.001s (likely a background loop, not a UI transition) |
| easing | ease-in-out | `ease` |
| easing | custom | `cubic-bezier(0.2, 0, 0.3, 1)` |
| easing | spring/overshoot | `cubic-bezier(0.68, -0.55, 0.265, 1.55)` |
| easing | ease-in | `cubic-bezier(0.44, 0, 1, 1)` |
| easing | ease-out | `cubic-bezier(0.23, 1, 0.32, 1)` |
| easing | linear | `linear` |

## Brief

Build a full-service agency landing page opening on a plain white hero with a serif
logotype, a plain sans headline, and one dark abstract photograph. Immediately below,
include a mosaic collage strip previewing client work in small mixed-aspect tiles. Then
dedicate one full-width, fully saturated flat-colour band to each core service category —
no two adjacent bands sharing a colour family — pairing a bold sans service name with a
short description, a link list of sub-services, and one small photograph of a real
relevant deliverable (a device mockup, a printed piece). Return to plain white for a
project archive grid. Close with a dark section stating plain, unadorned proof numerals,
a full team headshot grid, and a short dated news strip, ending on a dark footer CTA band.

## Image recipe

Documentary or product photograph of [SUBJECT] relevant to a specific service — a device
displaying a real website mockup, a printed marketing piece, a branded vehicle or
packaging — shot with clean, neutral studio or on-location lighting, true-to-life colour
that will sit inside a saturated flat-colour band without clashing, cropped tightly to the
object itself rather than run full-bleed.

## Photo search

Unsplash first, Pexels second.
- "tablet mockup website design display"
- "phone mockup app interface hand"
- "branded delivery van signage"
- "printed marketing material flatlay"

## Reference lock

Primary reference/direction: Insign — colour-per-service band system for a full-service
agency, plain white/black framing every saturated section.
Preserve (3-5 traits): one non-repeating fully saturated flat colour assigned to each core
service category, functioning as navigation by colour; every other section (hero, project
archive, proof, footer) kept plain white or near-black so the service bands stay the
loudest element; each coloured band paired with one small, specific photograph of a real
deliverable, not an abstract icon; proof presented in varied unadorned formats (plain
numerals, a face grid, dated news) rather than repeated testimonial cards.
Borrow only (1-2): the mosaic collage strip directly beneath the hero; the small
accessibility-icon affordance persistently visible in the corner.
Role rules: no two adjacent full-width bands share a colour family; saturated colour never
appears in the hero, proof, or footer sections; each service band carries exactly one
supporting photograph, never more.
Media strategy: photo:unsplash — clean, true-colour product/device-mockup photography
cropped to the object; never full-bleed atmospheric photography inside a colour band.
Reject: a single-hue palette across all service listings; illustrated icons replacing real
deliverable photography; testimonial-card carousels in place of varied proof formats;
saturated colour bleeding into the hero or footer sections.
Token commitments: bg `#FFFFFF`, ink `#1A1818`, ink-soft `#484B48`, band-1 (chartreuse)
`#ECF58F`, band-2 (lavender) `#D1C8D6`, band-3 (orange) `#F2895C`; `Neue Haas Grotesk
RoundDots` for logotype, headlines and body throughout; each service band uses exactly
one flat background colour, no gradients or tints within a band.
