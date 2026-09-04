---
title: "wild (Craft, Engineered.)"
url: https://craft.wild.as/
source_url: https://craft.wild.as/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/347257dc674d5529-screenshot.webp
category: portfolio
category2: ""
family: vienna-pixel-atelier
dna: "Studio manifesto x pixel-art skyline banner"
register: modern clean
grammar: chaptered editorial
lane: "White ground opens on a stacked all-caps headline, drops into a full-width pixel-art skyline banner, then alternates a case-study thumbnail row with two long-form essay chapters on craft history and AI"
mode: persuade
traits: ["white ground, black ink", "stacked all-caps display headline", "pixel-art skyline banner in brand blue/gold", "case-study thumbnail row with captions", "long-form essay copy", "colour reserved to one banner element", "small grid-icon mark", "Vienna/Wiener Werkstätte origin story"]
palette: ["#FFFFFF", "#111111", "#3D5AFE", "#F5B400", "#C0392B"]
type: ["Sneak"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
---

## Why it works

The page opens with almost no colour at all — black type on white, a small
grid-icon mark, a plain all-caps headline ("CRAFT, ENGINEERED.") — and then spends
its one splash of colour on a single full-width pixel-art skyline banner in the
studio's blue and gold. Because everything else on the page is monochrome, that
banner becomes the entire brand-colour system in one image; it doesn't need to
repeat anywhere else to be remembered.

The case-study row is understated on purpose: three small thumbnails (a laptop
mockup, a robot product shot, an illustrated character) each captioned in plain
sentence case, no hover flourish implied. The studio is trusting recognisable
client names (Replit, Serve Robotics) to do the selling rather than dressing the
thumbnails up.

The real weight of the page is in its two essay chapters, set as plain justified
or left-aligned reading columns — one on the studio's Vienna/Wiener Werkstätte
lineage, one a point of view on AI and craft. For a design studio, choosing to
argue a position in prose, rather than show a portfolio grid first, is itself a
credibility move: it says the thinking came before the deliverables.

The restraint reads static in a screenshot but isn't: the headline and its
underline rules genuinely animate in on scroll, and a couple of stepped,
stop-motion-style easter eggs (a spinning mark, a jumping/heart-burst icon)
sit under the surface — the monochrome discipline is a choice about where to
spend colour, not motion.

## What to borrow (principle)

- **Spend your entire brand-colour budget on one image.** A single pixel-art or
  illustrated banner in your two brand colours does more identity work than
  scattering the colours across UI chrome.
- **Let recognisable client names caption small thumbnails plainly** instead of
  building an elaborate case-study grid — the names carry the proof.
- **Open a studio site with a point of view, not a portfolio grid.** An essay on
  how you think earns more trust than a wall of thumbnails before it.
- **Keep 90% of the page monochrome** so the one colour moment reads as deliberate,
  not decorative.

## What to leave

- Essay-length copy this early risks losing visitors who came to see work, not
  read a manifesto — it needs a visible portfolio link within the first screen.
- The pixel-art banner, while distinctive, doesn't repeat or echo anywhere else on
  the page, so it risks reading as a one-off flourish rather than a system.

## Signature move

The pixel-art skyline banner: a full-width mosaic cityscape rendered in large
coloured blocks (blue night sky fading to gold dawn, a black skyline silhouette),
used exactly once, directly under the hero headline, as the studio's entire
colour statement.

## Motion

(from designlang extract) Despite reading as static in the screenshot, the
extract shows a genuinely animated page: feel is "mixed" with scroll-linked
motion confirmed. The hero headline rises in on a soft `heroIn` fade-and-lift
while individual lines draw in with `heroLine` (a 115%→0% translateY reveal);
underlines and rules grow open with `lineGrowX`/`lineGrowY` scale transforms.
A handful of micro-interactions carry the studio's playful side — `wSpin`
rotates a mark a full 360°, `smJump` and `smHeart` are a bouncing/heart-burst
easter egg — animated on stepped easing (`steps(4)`–`steps(6)`) rather than
smooth curves, which reads mechanical/print-like next to the one continuous
`cubic-bezier(0.16,1,0.3,1)` ease-out used elsewhere.

| token | value | role |
|---|---|---|
| `xs`–`sm` | 100–200ms | micro state changes |
| `md` | 300ms | default reveal |
| `lg`/`xl` | 450/800ms | headline & line-draw reveals |
| ease-out | `cubic-bezier(0.16,1,0.3,1)` | continuous motion (3 uses) |
| steps | `steps(4)`–`steps(6)` | mechanical/stop-motion accents (53 uses) |

## Brief

Build a monochrome studio-manifesto page: white ground, black ink, one small
mark, a stacked all-caps headline stating the studio's position in four words or
fewer. Immediately below, run one full-width illustrated or pixel-art banner in
exactly two brand colours — this is the only colour on the page. Follow with a
plain three-thumbnail case-study row, each captioned with a real client name and
one line of description, no elaborate hover treatment. Below that, run two
long-form essay sections in a single reading column — one origin/history
chapter, one point-of-view chapter — set in the same sans throughout, no serif,
no pull quotes.

## Image recipe

A pixel-art or large-block mosaic skyline of [SUBJECT], rendered in exactly two
brand colours plus black, gradient from cool to warm across the width, silhouette
buildings only — no photographic detail, no gradients beyond the two-colour
transition.

## Photo search

Unsplash first, Pexels second.
- "city skyline silhouette dusk to dawn"
- "pixel art cityscape illustration"
- "minimal skyline gradient blue gold"

## Reference lock

Primary reference/direction: wild — monochrome studio manifesto with a single two-colour pixel-art banner as its entire colour system.
Preserve (3-5 traits): white-ground, black-ink monochrome base for all type and UI; exactly one full-width illustrated banner carrying both brand colours; plain-captioned case-study thumbnails naming real clients; long-form essay chapters set in a single reading column.
Borrow only (1-2): the Vienna/craft-history origin chapter as a trust device; the small grid-icon mark in place of a wordmark logo.
Role rules: brand colour appears only inside the one banner image, never in UI chrome or text; case-study thumbnails never exceed one caption line; essay columns never exceed ~65 characters per line.
Media strategy: illustration/pixel-art only for the banner — no photography anywhere else on the page.
Reject: scattering the brand colours into buttons or links; hover-heavy case-study cards; a portfolio grid before the point-of-view copy.
Token commitments: bg `#FFFFFF`, ink `#111111`, banner-blue `#3D5AFE`, banner-gold `#F5B400`, banner-red `#C0392B`; single grotesk sans for all type; headline in stacked all-caps, body in sentence case.
