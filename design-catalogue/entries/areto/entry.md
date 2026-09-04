---
title: "Areto (Webflow template, Home Two demo)"
url: https://areto.webflow.io/home-two
source_url: https://areto.webflow.io/home-two
captured: 2026-09-04
origin: raw-url
extract: ok
category: institutional
category2: ""
family: dark-hero-consulting-template
dna: "Dark photographic hero x marketplace-template consulting tropes"
register: modern clean
grammar: split stage
lane: "A dark-toned hero photo of a founder at a laptop carries a two-line headline and a floating vertical service list, then the page runs a stock sequence of icon-plus-percentage stat rows, gradient-fade headlines and a yellow scribble accent"
mode: persuade
traits: ["dark-toned founder-at-work hero photo", "floating vertical keyword list (Strategies/Optimization/Analytics)", "yellow-highlight underline on one word", "icon + percentage stat rows", "two-tone fade-out headline", "hand-drawn scribble accent line", "pill CTA buttons", "yellow badge chip"]
palette: ["#ece7e4", "#000000", "#f8fa8d", "#36503f", "#120a0e", "#e0d8cb", "#4d4d4d"]
type: ["Inter Tight"]
measured: designlang
kind: reference-style
source: claude
status: ready
raw: raw/d8f96afdbf747d3d-try-webflow-com.webp
---

## Why it works

This is a Webflow marketplace template ("Areto"), captured from its "Home Two"
demo — worth naming up front, because the page is built to demonstrate a
component library rather than to sell one specific consulting firm. The hero
does one thing well: a dark, desaturated founder-at-a-laptop photograph anchors
a small two-line headline on the left and a vertical list of four keywords
(Strategies / Optimization / Analytics / Execution) floating on the right, with
one word underlined in a bright yellow accent. The vertical list works as a
lightweight alternative to a nav-style feature summary — it reads at a glance
without needing icons or cards.

Everything below the fold, though, runs through a recognisable set of
consulting-template devices: a trust badge pill ("Join the 850+ companies..."),
a headline that fades from solid black to light grey partway through the
sentence, icon-plus-percentage stat rows (95%, 85%) next to a hand-drawn yellow
scribble, and repeated "Discover more →" links on a four-item services grid.
None of these are wrong individually, but stacked together they read as the
template industry's current default vocabulary for "trustworthy B2B services
site" rather than anything specific to a firm's own voice — useful to study
precisely because it shows what generic competence looks like at this genre.

One typeface (Inter Tight) runs the whole page at every weight, which does keep
the surface calm even where the content patterns are formulaic. The extracted
brand voice confirms the impersonal read: third-person, friendly tone,
verbose sentence-case headings — copy built to describe a category of service
rather than address one specific reader.

## What to borrow (principle)

- **A floating vertical keyword list beside a hero photo** is a lighter way to
  summarise service areas than a horizontal nav strip or icon row.
- **Underline exactly one word in an accent colour** in the hero to create a
  single focal point without a second display typeface.
- **Real workplace photography (not stock-posed) grounds an otherwise generic
  page** — the founder-at-laptop and team-huddle photos read as documentary
  enough to avoid pure stock-photo flatness.

## What to leave

- The gradient-fade headline (solid to light grey mid-sentence) is a template
  tell at this point — it reads as decoration applied to any headline rather
  than a considered emphasis device.
- The hand-drawn yellow scribble beside a stat number is decorative filler with
  no connection to the number's meaning.
- Icon-plus-percentage stat rows ("Strategy development — 95%") state
  confidence with no defined denominator — the pattern reads as trust signal
  regardless of what the percentage actually measures.
- The trust badge pill, stat rows, "Discover more" service cards and gradient
  headline are all stock components of this template genre — none is wrong on
  its own, but together they read as assembled rather than designed for one
  specific brand's voice.

## Signature move

The floating vertical keyword list beside the hero photo, with exactly one word
underlined in the accent colour — a lighter-weight way to state "what we do"
than a nav bar or a row of icon cards.

## Motion

(from designlang extract) The extract labels overall feel "responsive" and
confirms scroll-linked behaviour. Two duration tokens cover nearly everything
in use — a 300ms `md` for hover/state changes and a 500ms `lg` for larger
transforms — both riding the same ease-out family rather than a spring or
overshoot curve, so nothing bounces. Two keyframes are actually in use:
`rtvpulse`, a box-shadow ring pulse (reads as a live-status/badge dot), and
`rtvL`, a horizontal `translateX` slide that drives a marquee-style strip. A
`spin` keyframe is also defined in the stylesheet but doesn't register as
in-use, suggesting a loader state that rarely fires. No choreography or
stagger pattern is reported.

| token | duration | easing |
|---|---|---|
| `md` | 300ms | ease-out `cubic-bezier(0.22, 1, 0.36, 1)` |
| `lg` | 500ms | ease-out `cubic-bezier(0.16, 1, 0.3, 1)` |

## Brief

This entry is best used as a genre reference for "generic-competent B2B
consulting template," not as a direction to imitate wholesale. If borrowing
from it: anchor a hero on one dark, desaturated documentary-style photo of a
real person at work, with a short two-line headline and a floating vertical
list of 3-4 keywords beside it, one word underlined in a single accent colour.
Run the whole page on one grotesque. Avoid the gradient-fade headline, the
decorative scribble, and stat rows without a stated basis — replace percentage
claims with concrete, sourced numbers if using the stat-row pattern at all.

## Image recipe

Documentary workplace photograph of [SUBJECT] — a founder or team working at a
laptop or in a huddle — natural window light, desaturated/cool colour grading,
candid framing rather than posed-for-camera, shallow depth of field, no studio
lighting rig visible.

## Photo search

Unsplash first, Pexels second.
- "founder working laptop office candid"
- "team huddle office glass window"
- "business meeting laptop natural light"

## Reference lock

Primary reference/direction: Areto (Home Two) — dark documentary hero with a
floating vertical keyword list; used here as a genre study of consulting-
template defaults, not a direction to reproduce wholesale.
Preserve (3-5 traits): dark desaturated hero photograph with a short two-line
headline; a floating vertical keyword list beside the hero, one word
underlined in a single accent colour; one grotesque typeface at every weight;
real (not obviously staged) workplace photography throughout.
Borrow only (1-2): the pill-shaped trust badge; the "Discover more →" link
style on service cards.
Role rules: accent colour underlines at most one hero word and nothing else at
that scale; stat numbers, if used, must cite a real basis in the copy next to
them.
Media strategy: photo:unsplash — candid, desaturated workplace photography;
avoid overtly posed corporate stock.
Reject: gradient-fade headlines; decorative hand-drawn scribbles with no
semantic link to the content beside them; unsourced percentage stat claims;
more than one accent colour.
Token commitments: ground `#F6F6F6`, ink `#0D0F0F`, accent-yellow `#F8F9C6`,
forest `#324A3A`, taupe `#967E6C`, stone `#A1A59E`; display/body "Inter
Tight" throughout.
