---
title: "André Cândido"
url: https://www.andre-candido.com/
source_url: https://www.andre-candido.com/
captured: 2026-09-04
origin: refero
extract: ok
category: portfolio
category2: playful
family: highlighter-editorial
dna: "Near-monochrome editorial studio x one highlighter-yellow footer"
register: editorial print
grammar: gallery/catalog
lane: "A cream-and-ink portfolio that opens on a huge whisper-thin didone headline over capsule-shaped project tiles in full client colour, then closes on one dramatic ink-black panel where the yellow accent finally appears"
mode: portfolio
traits: ["160px whisper-thin didone display", "97% achromatic UI, client colour in work only", "800px capsule image radius", "tracked-out 0.107em small type", "single dark footer inversion", "circular rotating text badge"]
palette: ["#111118", "#ffffff", "#dddddd", "#bdbdbd", "#7c7c7c", "#fef199"]
type: ["Editorial New", "PP Mori"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Andre Candido.md
---

## Why it works

Palette and type are read from Refero's extracted tokens. The studio's own UI stays
97% achromatic — ink black `#111118` and paper white carry almost everything — which
means the one place colour is allowed to exist, the work itself, reads as maximally
vivid by contrast. Capsule-shaped project tiles (800px radius, practically a
lozenge) bleed whatever client palette they carry straight onto the cream page, so
the portfolio grid becomes a controlled burst of colour inside an otherwise
disciplined frame.

Type does the same restraint-then-release move as the page's colour: PP Mori
carries every functional voice (nav, labels, body) at weights 200-600 with an
unusually wide 0.107em tracking on small sizes, while Editorial New — a didone
serif at weight 200 only — is reserved exclusively for display headlines from 48px
up to 160px. Because the thin serif never appears below 48px and the sans never
carries a display headline, the pairing reads as two distinct instruments rather
than a font stack.

The single dramatic gesture is saved for the end: the entire page is light until
the footer, which inverts to `#111118` and is the only place the highlighter-yellow
`#fef199` accent appears — outlining a massive pill CTA. Holding one colour and one
inversion in reserve for the close makes the last screen feel like a different room,
not a louder button.

## What to borrow (principle)

- **Let client/project colour be the only colour.** A near-achromatic studio UI
  makes a portfolio grid read as more vivid, not less, because nothing competes
  with it.
- **Reserve an accent for exactly one section.** Saving a colour for the footer
  alone turns the close into an event instead of diluting the accent everywhere.
- **Pair one ultra-thin display face with one workhorse sans, never at the same
  size.** A 200-weight serif above 48px against a 200-600 weight sans below it
  keeps the tension legible instead of muddy.
- **Use one dramatic shape as a signature, sparingly.** An 800px "capsule" image
  radius reads as a device precisely because nothing else on the page shares it.
- **Track out small type generously.** 0.107em letter-spacing at 12-15px is what
  makes nav and labels read as fashion-editorial rather than default UI.

## What to leave

- The "Don't" list is empty in the source export — the system's constraints are
  implicit in its Do's, which makes fidelity harder to check without the live site.
- An 800px capsule radius depends on generous card width; at narrow/mobile
  breakpoints it will collapse toward a pill or a circle, losing the lozenge shape.
- A single reserved accent colour for one section only works if that section is
  genuinely the page's close — used mid-page it would read as an unexplained
  one-off.

## Signature move

The circular rotating text badge — "AVAILABLE NOW" set on an invisible circle,
used once as a floating decorative element beside the hero headline rather than as
a repeatable component. It is deliberately not part of the design system; it is a
single ornament.

## Motion

(from designlang extract) Feel reads as smooth, and the page is scroll-linked.
Interactive transitions run on a plain `ease` curve at three short durations —
100ms, 200ms and 300ms — the fastest tier for hover/colour changes, the slowest for
larger reveals; the broader transition log adds a 400ms opacity fade for section
entrances. The one keyframe confirmed in use is `slide`, a slide-x transform (3
uses) driving translateX motion — most likely the capsule-tile image slider/marquee
behaviour rather than the rotating text badge, since no rotate keyframe registers
as in-use (a `spin` keyframe exists in the stylesheet but isn't confirmed firing).
(observed in capture) the capsule-shaped image containers and the circular rotating
badge suggest the badge text itself may continuously rotate, and hover states on
ghost/filled pill buttons likely invert fill and text colour rather than adding
movement — consistent with the flat, shadow-free, editorial register of the rest of
the system.

| Token | Value | Easing |
|---|---|---|
| xs | 100ms | `ease` |
| sm | 200ms | `ease` |
| md | 300ms | `ease` |
| slide keyframe | — | translateX, 3 uses |

## Brief

Build a visual-design-studio portfolio. Canvas is paper white, ink is near-black
`#111118`, with soft-ash and stone-gray for muted borders and dividers — the whole
UI stays achromatic except for the highlighter-yellow `#fef199` reserved for the
footer only. Open on a full-width Editorial New weight-200 headline (48-160px,
line-height 1.0, no uppercase) stating the studio's promise in one or two lines.
Below, lay out a portfolio grid of capsule-shaped project tiles (800px radius,
8px on the outer card) bleeding full client-project colour and imagery. Use PP Mori
at 0.107em tracking for all nav, labels and body copy; reserve 24px pill radius for
buttons and 8px for cards and links. Add one floating circular rotating text badge
near the hero as a one-off ornament. Close on a full-width `#111118` inverted
footer panel with a giant 150px-radius CTA pill outlined in highlighter yellow.

## Image recipe

Not applicable as a primary photographic recipe — the site's imagery is client
project work (screenshots, illustration, branded colour blocks) rather than
photography. Where a portrait or process shot is needed: a plain, evenly lit studio
headshot or workspace detail of [SUBJECT], neutral background, no heavy retouching,
consistent with an achromatic UI that lets the subject's own colour read clean.

## Photo search

Unsplash first, Pexels second.
- "designer workspace desk minimal flat lay"
- "portrait studio lighting neutral background"
- "laptop screen mockup UI design work"
- "colour palette swatches paper minimal"

## Reference lock

Primary reference/direction: André Cândido — near-monochrome editorial portfolio,
whisper-thin didone display, colour reserved for client work and one footer accent.
Preserve (3-5 traits): 97% achromatic UI (`#111118` ink on white); Editorial New
weight 200 exclusively for display headlines 48px and above, never smaller, never
heavier; PP Mori at 0.107em tracking for all functional text; 800px capsule radius
on portfolio images vs. 8px on cards and 24px on buttons; a single dark `#111118`
footer inversion where highlighter yellow `#fef199` appears for the first and only
time.
Borrow only (1-2): the circular rotating "AVAILABLE NOW" text badge; the 150px-
radius oversized footer CTA pill.
Role rules: yellow never appears outside the footer panel; serif never carries body
copy or UI labels; sans never sets a display headline; client-project colour is the
only large colour field permitted pre-footer.
Media strategy: none (no external photography) — client-work screenshots and
colour blocks carry all chromatic content; any supplementary photography stays
neutral and desaturated to match the UI.
Reject: a second accent colour anywhere outside the footer; rounded corners below
8px or above 24px except the 800px image capsule; shadows or elevation; a bolded
Editorial New headline.
Token commitments: bg `#ffffff`, ink `#111118`, border `#dddddd`/`#bdbdbd`, muted
text `#7c7c7c`, footer accent `#fef199`; display weight 200 at 48-160px/leading 1.0;
body PP Mori 200-600 at 12-24px, 0.107em tracking on 12-15px sizes; radius 8px
cards, 24px buttons, 800px images, 150px footer CTA; base spacing unit 8px, section
gap 80-120px.
