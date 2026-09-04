---
title: "Diabla"
url: https://www.diablaoutdoor.com/en/
source_url: https://www.diablaoutdoor.com/en/
captured: 2026-09-04
origin: refero
extract: ok
category: luxury-craft
category2: "consumer-brand"
family: blush-courtyard-editorial
dna: "Fashion-magazine cropped headlines x Mediterranean poolside photography"
register: editorial print
grammar: gallery/catalog
lane: "A full-bleed sunlit courtyard photograph carries a centre-distributed red nav and a cropped 110px headline, then the page settles onto a blush-pink canvas of three-up editorial columns where red exists only as outline and ink, never as fill"
mode: persuade
traits: ["80-110px display at 0.88 line-height", "red as outline/ink only, never a fill", "blush canvas, never pure white", "monoweight Helvetica, no bold anywhere", "centre-distributed nav, wordmark at centre", "zero shadow, whitespace as separator"]
palette: ["#ed2e38", "#fcf0f3", "#333333", "#000000"]
type: ["Helvetica Neue Light", "Helvetica Neue Roman"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Diabla.md
---

## Why it works

Palette and type are read from Refero's extracted tokens. The system's whole
identity rides on a single rule: vermillion `#ed2e38` is never a flood fill — it
appears only as the wordmark, link text, heading colour, and 1px button outlines.
Because the brand's one chromatic note is always ink or stroke, never a coloured
surface, the page keeps the restraint of a magazine layout even where a typical
e-commerce site would reach for a filled "Shop now" button.

Type is deliberately monoweight: a single Helvetica Neue family runs Light for
display and Roman for everything else, with no bold or semibold anywhere.
Hierarchy comes entirely from a brutal size jump (14px body to 110px display) and
from colour (vermillion vs. charcoal), plus line-height compressed to 0.88-0.91 at
display sizes — tight enough that ascenders and descenders crop, turning product
names into cropped fashion headlines rather than comfortable web type.

Layout reinforces the editorial register: navigation is distributed
left-centre-right with the wordmark dead centre rather than flush left, three-up
grid columns are separated by whitespace alone with no card chrome, and the entire
system avoids shadows — components read as printed on paper. Full-bleed
photography (sun-bleached courtyards, poolscapes) is never inset or rounded,
letting the Mediterranean setting carry the mood the UI deliberately withholds.

## What to borrow (principle)

- **Restrict a chromatic accent to outline and ink, never fill.** A single colour
  used only as stroke and text keeps a bold hue from reading as loud or
  commercial.
- **Run a single typeface at exactly two weights, no bold.** Forcing hierarchy
  onto size and colour alone, with weight locked, keeps the system honest and
  impossible to over-emphasize.
- **Compress display leading below 1.0 deliberately.** Cropping ascenders and
  descenders at 0.88-0.91 line-height is what turns oversized type into a
  poster statement instead of merely "large text."
- **Centre the wordmark in a distributed nav.** Placing the brand mark at the
  optical centre, flanked symmetrically by nav groups, reads as a magazine
  masthead rather than a standard left-logo header.
- **Separate grid columns with whitespace, not chrome.** No card border, no
  background — three equal columns held apart purely by generous gutters.

## What to leave

- Monoweight type with no bold option removes a common emphasis lever; any content
  team used to bolding key phrases will need a different technique (colour, size,
  case) instead.
- A single, never-filled accent colour depends on the rest of the page staying
  genuinely neutral — introducing a second saturated hue anywhere would break the
  "one sharp edge" reading entirely.
- Extremely compressed display leading (0.88) is unforgiving of long headlines;
  it only works with short, poster-length copy.

## Signature move

The outlined vermillion button: a 1px `#ed2e38` border with transparent or
blush-tinted fill and uppercase vermillion text — the brand's only interactive
control, communicating action entirely through a stroke rather than a filled
surface.

## Motion

(from designlang extract) Feel reads as mixed, and the page is scroll-linked.
Property transitions (filter, opacity, width/height/background) run at 300-800ms
on a single custom ease-in-out-cubic curve, `cubic-bezier(0.645, 0.045, 0.355,
1)` — the 800ms step on `filter` most likely drives an image hover/focus
treatment. The keyframes the extract confirms firing (`bounce`, `mc_slideOut`,
`slideIn`) are a Mailchimp signup-popup's own animations, not bespoke page
choreography — third-party widget chrome, same as the swiper-carousel spinner and
cookie-banner fade also present in the stylesheet. Note: the live site currently
shows a "Coming Soon" placeholder mid-relaunch, so this entry's images are drawn
from the Refero export rather than a fresh capture; the designlang extraction
itself ran against real page markup and is not affected. (observed in capture)
the small red downward arrow beneath the hero headline suggests a simple
scroll-cue nudge rather than an animated affordance, and the full-bleed
photography with no card framing implies plain crossfades between sections
rather than parallax.

| Token | Value | Easing |
|---|---|---|
| md | 300ms | `cubic-bezier(0.645, 0.045, 0.355, 1)` |
| lg | 500ms | `cubic-bezier(0.645, 0.045, 0.355, 1)` |
| xl (filter/hover) | 800ms | `cubic-bezier(0.645, 0.045, 0.355, 1)` |

## Brief

Build an editorial outdoor-furniture landing page. Canvas is blush pink `#fcf0f3`
everywhere — never pure white; body copy is charcoal `#333333`, not black.
Vermillion `#ed2e38` is the single chromatic note, used only for the wordmark,
nav links, heading text, and 1px outlined-button borders — never as a fill. Open
full-bleed on a sun-drenched courtyard or poolscape photograph with a
distributed, transparent nav (nav groups left and right, wordmark centred) and a
centred display headline at 80-110px, Helvetica Neue Light, line-height 0.88-0.91,
white on the photo. Below the hero, settle to a max-width ~1200px three-up
editorial grid: full-bleed image, uppercase vermillion eyebrow, uppercase
headline, charcoal body copy, one outlined vermillion button — columns separated
by whitespace only, no card chrome. Keep 80px section gaps, zero shadows, and
never round or frame photography.

## Image recipe

Sun-drenched Mediterranean lifestyle photograph of [SUBJECT] — a poolside or
courtyard setting in bleached pastel colour, strong midday sun with hard shadows,
outdoor furniture styled in situ (not isolated), palm foliage or stone
architecture in frame, high-key and slightly desaturated except for one or two
saturated accent objects, full-bleed with no vignette or border.

## Photo search

Unsplash first, Pexels second.
- "Mediterranean courtyard pool midday sun"
- "outdoor furniture poolside pastel pink"
- "striped awning courtyard architecture"
- "palm trees rocky coastline bright light"

## Reference lock

Primary reference/direction: Diabla — Mediterranean editorial furniture page,
red as outline/ink only, cropped 80-110px display type.
Preserve (3-5 traits): blush pink `#fcf0f3` canvas, never pure white; vermillion
`#ed2e38` restricted to wordmark, links, headings and outlined-button borders,
never a fill; monoweight Helvetica (Light for display, Roman for everything else),
no bold anywhere; display line-height capped at 0.88-0.91; distributed nav with
the wordmark at dead centre.
Borrow only (1-2): the three-up editorial grid pattern (product / catalogue /
designer profile); the black-and-white monochrome designer-portrait treatment.
Role rules: vermillion never becomes a filled surface; body text never bolds;
photography is always full-bleed, never rounded or framed; nav stays distributed,
never flush-left.
Media strategy: photo:unsplash — full-bleed, sun-drenched Mediterranean lifestyle
photography and monochrome portraiture only; no product-only white-cyc shots.
Reject: filled red CTAs; bold or semibold Helvetica; drop shadows; rounded-corner
photography; a left-aligned logo; a second saturated accent colour.
Token commitments: bg `#fcf0f3`, ink `#333333`, ink-hard `#000000`, accent
`#ed2e38`; display 80-110px/leading 0.88-0.91; body 14-16px/leading 1.5; radius
0px cards/images, 14px buttons/links; page max-width 1200px, section gap 80px.
