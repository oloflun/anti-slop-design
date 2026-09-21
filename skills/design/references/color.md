# Colour

> **Diverges from upstream Hallmark: T6 port (2026-09-09).** This file has been
> extended with material ported from the upstream packages named in the design
> chain's v4 plan, sections 2.1 to 2.5. Every addition is traceable to a source
> file; where a port collided with a rule already in this file, the conflict is
> resolved in the text and the winner is named. Upstream is no longer the bar
> here, and `verify-design-system.py` records the divergence rather than
> treating it as drift.

Most AI-generated UI fails on colour. It picks blue. It uses pure black. It draws a gradient from purple to cyan. It leaves accents on 30% of the page. Fix all of this.

## Principles

- **OKLCH only.** Perceptually uniform; predictable lightness; consistent hue across tints. `hsl()` and `rgb()` lie about brightness.
- **One accent.** Maximum two. Everything else is neutral. The accent should occupy **3% or less** of any given viewport.
- **No pure extremes.** No `#000`, no `#fff`. Always tint with a trace of chroma toward the palette's anchor hue.
- **Tint the greys.** If your anchor hue is orange, your neutrals lean warm. If it's blue, they lean cool. A page with a warm accent and cool grey body copy looks wrong and most people can't name why.
- **The hue is a brand decision and must not come from a default.** Do not reach for blue (hue ~250) or warm orange (hue ~60) by reflex; those are the two dominant AI-design defaults, not the right answer for any specific brand. The tint on the neutrals follows *this* project's brand hue — teal brand, teal-leaning neutrals; amber brand, amber-leaning neutrals. **Avoid the trap of always tinting warm or always tinting cool**: those two are the laziest defaults and they build their own monoculture across projects. (impeccable `reference/color-and-contrast.md` §§ Color Spaces, Tinted Neutrals.)

## Palette construction

A complete Hallmark palette has four layers.

1. **Paper** — the base surface. `oklch(96–98% 0.005–0.015 <anchor hue>)` for light mode, `oklch(12–16% 0.008–0.015 <anchor hue>)` for dark.
2. **Ink** — the primary text. `oklch(16–22% 0.005–0.015 <anchor hue>)` for light mode, `oklch(92–96% 0.005–0.01 <anchor hue>)` for dark.
3. **Neutrals** — 5 to 9 steps between Paper and Ink, each with the anchor's chroma tint at low values (0.005–0.015).
4. **Accent** — one saturated colour with meaningful chroma (0.12–0.22). Used for links, active states, highlights, focus rings. Never as a background fill that covers more than a few percent of the surface.

Example (warm-oat anchor, hue 80):

```css
:root {
  --color-paper:    oklch(96%  0.012 80);
  --color-paper-2:  oklch(93%  0.014 80);
  --color-rule:     oklch(82%  0.010 80);
  --color-neutral:  oklch(56%  0.008 80);
  --color-muted:    oklch(40%  0.008 70);
  --color-ink:      oklch(18%  0.010 60);
  --color-accent:   #FC4C02;                   /* signal orange */
  --color-focus:    oklch(55%  0.19  55);
}
```

Example (midnight anchor, hue 40):

```css
:root {
  --color-paper:    oklch(14%  0.008 40);
  --color-paper-2:  oklch(18%  0.010 40);
  --color-rule:     oklch(30%  0.008 40);
  --color-neutral:  oklch(58%  0.008 40);
  --color-muted:    oklch(72%  0.006 40);
  --color-ink:      oklch(94%  0.006 80);
  --color-accent:   #FC4C02;
  --color-focus:    oklch(70%  0.19  55);
}
```

## Roles, not swatches

The four layers above are the concrete recipe. This is the discipline behind it: **before any value is picked, name the roles the palette has to fill.** A bag of swatches is not a palette; roles are what make a colour decision checkable later. From impeccable `colorize.md` § Choose a strategy:

- canvas and elevated surfaces;
- primary and secondary text;
- action, focus, and selection;
- borders and separators;
- success, warning, error, and information;
- data categories or scales, when there is data.

Name the intended emotional temperature, dominant relationship, contrast range, and colour dosage **before** editing values. **Decoration with no relationship to hierarchy, state, content, or the visual world is not a colour strategy.**

Two more rules from the same source that survive into every register:

- **Let the strongest colour own a deliberate region or role** instead of scattering tiny accents. Confetti is not emphasis.
- **Don't spend the primary action's colour on decoration.** If the accent is also the divider and the icon tint and the section background, the primary action is no longer findable.

The chain's own accent ceiling (§ Use of the accent) still binds: "owns a region or a role" means the role, not a third of the viewport.

## Building the ramp

Vary lightness; **reduce chroma as you approach white and black.** High chroma at extreme lightness looks garish, and keeping it there "so the math stays uniform" is the mistake that makes a generated ramp read as generated.

```css
/* One hue, one chroma envelope, lightness doing the work.
   Note the chroma falling off at both ends, not held flat. */
--accent-100: oklch(95% 0.030 55);
--accent-300: oklch(84% 0.090 55);
--accent-500: oklch(63% 0.170 55);   /* the accent proper */
--accent-700: oklch(46% 0.130 55);
--accent-900: oklch(28% 0.070 55);
```

Prefer explicit colours over chains of translucent overlays: alpha makes contrast context-dependent, so a ramp built out of overlays cannot be verified once and trusted.

## Token layers

Two layers, not three: **primitive** values (`--accent-500`) and **semantic** roles (`--color-action: var(--accent-500)`). A theme change remaps the semantic layer; primitives stay put. Components read semantic tokens only — a raw hex in a component is a value that will drift the first time the theme moves.

(impeccable `color-and-contrast.md` § Token Hierarchy, `colorize.md` § Apply at system scale. The chain holds 8–10 named tokens per page, so this is a two-layer discipline over a small set, not an enterprise token architecture.)

## Contrast

Use the APCA contrast check when you can; otherwise WCAG 2.1 ratios.

| Content | Minimum | Target |
| --- | --- | --- |
| Body text | 4.5:1 | 7:1 |
| Large text (≥ 18.66px bold or 24px) | 3:1 | 4.5:1 |
| UI component boundaries | 3:1 | 4.5:1 |
| Placeholder / helper text | 4.5:1 | 4.5:1 |

Verify with the browser devtools vision-deficiency emulator before shipping.

### APCA — the numbers the table above doesn't give you

APCA (Accessible Perceptual Contrast Algorithm) models *perceived* contrast more accurately than WCAG 2 and is the better default for design decisions. **Lc** is the measure. These levels collapse APCA's full size-and-weight lookup:

| Content type | Minimum | Preferred |
| --- | --- | --- |
| Body text (columns or blocks) | Lc 75 | Lc 90 |
| Non-body text (labels, headlines) | Lc 60 | Lc 75 |
| Large text (≥ 36 px) | Lc 45 | Lc 60 |
| UI components | Lc 30 | n/a |

Lc 30 is also the minimum for disabled and placeholder text; Lc 15 is the floor for a non-text element to be discernible at all. **Lc is signed** — positive is dark-on-light, negative is light-on-dark — so compare the absolute value.

**When a project must claim WCAG conformance, WCAG is the gate and APCA is the tiebreaker for anything above it.** The two tables coexist; APCA never lowers a WCAG pass.

**The light/dark crossover is around 73 % perceived lightness.** Above it, dark text scores higher; at or below it, light text does. That is higher than intuition suggests: **between roughly 60 % and 73 % the background already looks light, yet white text still measures meaningfully better than black.** Picking the ink by eye in that band is how a section ends up with the worse of the two options and no one can say why.

**Mid-lightness grounds cap what is reachable.** On a background near 75 % perceived lightness, *even pure black text* reaches only about Lc 60 — below the Lc 75 body-text minimum. So a mid-range surface is not a text surface: **when body text fails on it, the thing that has to change is the background, not the ink.** Body text needs a ground near one extreme.

Quick approximations for body text at |Lc| ≥ 75, to be verified by measuring:

- **Light ground** (above ~90 % perceived lightness) → foreground below ~35 %.
- **Dark ground** (below ~25 % perceived lightness) → foreground above ~90 %.

The gap is asymmetric because APCA is polarity-aware: **mirrored pairs do not score identically**, which is exactly why a pair that passes in light mode fails when the section inverts.

**Fixing a failing pair: change lightness first.** It is the channel contrast responds to; hue and saturation move the measured value far less, so fixing contrast by changing hue is wasted effort and turns a contrast fix into a palette change. Move the foreground away from the background in perceived lightness, hold hue and saturation, remeasure. Pushing lightness can push the colour out of gamut — drop saturation as needed to keep it renderable.

**Report, don't repaint.** When a check fails, report the pair, its measured value, and the threshold it misses. The colours are a design decision; change them when asked, not as a reflex during a review.

What must be checked, not assumed:

- **Every pair, in every appearance.** The light and dark palettes are not mirror images.
- **Translucent surfaces.** A colour over a `backdrop-filter` header shifts with whatever scrolls behind it. Test against the lightest and darkest content it can sit over, or make the surface opaque enough that the shift cannot break the pair.
- **Computed colours.** `color-mix()`, relative colour syntax and opacity modifiers resolve at render time. Measure the rendered result, not the declaration.
- **Text over images.** There is no single background colour. Measure the worst region, or guarantee one with a scrim.

Measure against the *nearest ancestor that actually paints a background*. Measuring text on a card against the page background gives the wrong answer.

### Dangerous pairs

These fail contrast or readability often enough to be worth naming (impeccable `color-and-contrast.md` § Dangerous Color Combinations):

| Pair | Why it fails |
| --- | --- |
| Light grey text on white | The single most common accessibility failure |
| Grey text on any coloured ground | Grey looks washed out and dead on colour — derive the tone from the ground's own hue instead |
| Red on green, green on red | ~8 % of men cannot separate them; needs a second channel |
| Blue text on red | Vibrates |
| Yellow text on white | Almost always fails |
| Thin light text over an image | Contrast is unpredictable per region; measure the worst one |
| Placeholder / helper text | Still needs the full body threshold. The pale placeholder everyone ships usually fails |

## Dark mode recipe

- Paper: lightness 12–18% (not `#000`).
- Ink: lightness 92–96% (not `#fff`).
- Body font-weight: reduce by 50 units (400 → 350) to compensate for the optical weight of light text on dark.
- Accent: reduce chroma by 0.02–0.04; increase lightness by 5–10%.
- Elevation: higher surfaces are *lighter*, not darker. Add ~3% lightness per level.
- Never switch the hue between modes. Keep the anchor. Only lightness and chroma move.

**Dark mode is composed, not inverted.** You cannot swap the colours; the two modes are separate design decisions that share a hue. In dark mode depth comes from surface lightness rather than shadow, so build the elevation as a 3-step surface scale (roughly 15 % / 20 % / 25 % lightness) at the *same* hue and chroma, and only vary lightness. Mechanically inverting the light theme is the amateur tell, and it is what produces eye-burning contrast on a page whose light mode was fine. (impeccable `color-and-contrast.md` § Dark Mode Is Not Inverted Light Mode; `colorize.md` § Apply at system scale.)

### Declare the scheme, or the browser draws the rest of the page for you

Without these, a cinematic or illustrated dark page ships with a light scrollbar and light form controls — the parts you did not draw contradicting the parts you did:

```html
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#0f0f0f" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
```

```css
:root              { color-scheme: light; }
[data-theme="dark"]{ color-scheme: dark;  }
```

`color-scheme` on the root fixes scrollbars, `<input>` / `<select>` / `<textarea>` defaults, system dialogs and autofill. `theme-color` sets the browser chrome and the mobile address bar, and it should match the page's actual ground. On Windows the native `<select>` needs its colours restated explicitly even with `color-scheme` set.

**This is a production tell, numbered as one:** a dark page with no `color-scheme` is identifiable from the scrollbar alone. (refero `color.md` § 5 Dark Mode: Technical Implementation.)

## On-colour: every fill behind text declares its ink

Generalised from the `--on-primary` / `--on-success` pairs in refero `color.md` §§ 2.3 and 6, and from the chain's own `--color-accent-ink` contract:

**Every fill that can sit behind text ships with the ink that goes on it, defined in the same place, verified as a pair.** A `--color-accent` without a `--color-accent-ink` is half a token; the missing half gets filled in at build time by whatever `color` happened to be inherited, which is how an accent button ends up with body ink on it at 2:1.

**Maximum two colours per component.** A button carrying a brand gradient *and* a coloured border *and* a coloured shadow *and* coloured text is almost always garbage. State changes are structure, not circus: hover and active shift lightness slightly, add a little contrast, maybe deepen a shadow. They do not repaint the component in a new hue.

## Re-inking an inverted subtree

**Redefining an ink token on a subtree does not re-ink the text under it.** `color` is inherited as a *computed value*, so text whose `color` already resolved on `<body>` keeps the body's ink no matter what the section redefines the token to.

Every page that inverts a ground mid-page hits this, and **it fails silently**: the inverted section renders bone type on concrete at 1.15:1 while an automated check correctly classifies the line as light-on-dark and grades it in the wrong direction. The fix is one extra declaration on the same subtree:

```css
.section--light { --ink: #14110C; --ink-soft: #4A443A; color: var(--ink); }
```

**Restate `color` wherever you restate the token.** The same applies to any other inherited property driven from a token on a subtree. (scroll-craft `taste.md` § Colour.)

Pair this with the chain's existing rule that every muted tone needs a value *per ground*: a caption grey at 16.4:1 on a dark section carries into a cream one at 1.83:1 and disappears. Pick the tone per ground and measure both.

## Browser surfaces

The parts you did not draw still carry the design, and this is the cheapest signal that a page was built rather than assembled. It is also the step that gets skipped most reliably. Theme all of them:

**selection colour · caret colour · focus ring · scrollbar** — plus, on the typographic side, underline offset and thickness and tabular numerals in anything that counts or tabulates ([`typography.md`](typography.md) § Required features).

(scroll-craft `taste.md` § Browser surfaces.)

## Bans

- **Pure `#000000`** anywhere. Use `oklch(16% 0.01 <hue>)` or similar.
- **Pure `#ffffff`** as a base surface. Use a tinted paper.
- **Flat grey** (`oklch(L 0 H)` with zero chroma). Add at least 0.005.
- **Purple-to-cyan gradients, purple-to-blue gradients, orange-to-pink gradients.** Every LLM picks these. Don't.
- **Accent as background fill** covering more than ~5% of any view.
- **Grey text on coloured background.** Always reads washed out. The positive form of the rule: **secondary text is tinted, never flat grey** — derive it from the foreground or the surface hue. `#888` on a warm dark ground looks dirty. (impeccable `colorize.md`; scroll-craft `taste.md`.)
- **Indigo and violet as a flat accent** — `#6366f1`, `#8b5cf6`, `#7c3aed` and their neighbours. This file already banned the purple *gradients*; the flat fill is the same tell without the gradient. It is the universal fingerprint of AI-generated design, and it now needs an explicit yes to one of: the brand requires purple; a locked reference used purple and you can say why; there is a semantic reason that is not "looks modern". No yes, no purple. (refero `anti-ai-slop.md`; `design-taste-frontend` § 4.2 "the LILA rule" — no automatic purple button glows, no neon gradients; neutral bases with one high-contrast accent instead.)
- **A second accent hue appearing mid-page.** One accent, locked for the whole page: a warm-grey site does not grow a blue CTA in section seven, and a rose-accented site does not get a teal status badge in the footer. Pick one, lock it, audit every component before shipping. The one licensed exception is the two-step accent in § Use of the accent. (`design-taste-frontend` § 4.2 Color Consistency Lock; scroll-craft `taste.md`.)
- **Red–green pairing as the only signal.** Add an icon or pattern.
- **Alpha transparency as the definition of a colour.** If it's a named token, it's opaque. Transparency is a *modifier* for overlays and shadows, not a palette. Heavy use of alpha usually means an incomplete palette: it creates unpredictable contrast, costs compositing work, and makes every measurement context-dependent. Define an explicit overlay colour per context instead. **Exception:** focus rings and interactive states, where see-through is the point.
- **Three-colour gradients.** Two-stop gradients only. The third stop is vanity.

### The premium-consumer palette ban

The second-most-recurring colour tell after purple, and the harder one to see because each individual value looks tasteful. For **premium-consumer briefs** — cookware, wellness, artisan, luxury, heritage craft, DTC home goods — the model default is *warm beige/cream ground + brass/clay/oxblood/ochre accent + espresso near-black text*. Every premium-consumer page ever shipped uses this exact palette, and the brand becomes invisible inside it.

Banned as **default** backgrounds, accents and inks — these are hex *families*, so neighbouring values count:

| Role | Banned family |
| --- | --- |
| Backgrounds — warm paper / cream / chalk / bone | `#f5f1ea` `#f7f5f1` `#fbf8f1` `#efeae0` `#ece6db` `#faf7f1` `#e8dfcb` |
| Accents — brass / clay / oxblood / ochre | `#b08947` `#b6553a` `#9a2436` `#9c6e2a` `#bc7c3a` `#7d5621` |
| Text — espresso / warm near-black | `#1a1714` `#1a1814` `#1b1814` |

**Override:** acceptable only when the brand brief explicitly names those colours, or when the identity is genuinely vintage / artisan / warm-craft **and** you can articulate why this palette fits *this* brand. Reaching for it because "this is a cookware brief" is exactly the banned move.

**Rotate instead** — and do not reuse the family you used on the previous premium-consumer project: cold luxury (silver-grey + chrome + smoke) · forest (deep green + bone + amber) · black-and-tan (true off-black + warm tan, no beige) · cobalt + cream · terracotta + slate · olive + brick + paper · pure monochrome + one saturated pop. The rotation list and the "which family did the last project use" bookkeeping belong to `invention.md`; the hex-family detection is mechanical and belongs to the gate, not to a reviewer's eye. This section is the human-readable rule behind both.

(`design-taste-frontend` § 4.2 Premium-Consumer Palette Ban; scroll-craft `taste.md` § Colour states the same trap in prose.)

### Note: tinted near-black is required here and is also a tell

Two rules point in opposite directions and both are correct, so neither gets "fixed" out of existence:

- This file and the slop-test's gate 22 require **tinted neutrals** — zero-chroma greys read as flat, so a near-black carries at least 0.005 chroma toward the anchor hue.
- anthropic `frontend-design` lists **"tinted near-black (`#0B0B0B`, `#111`) standing in for black"** among the *template chrome* traits — the cluster of moves that appears on a generated page whatever its subject.

**They are compatible, and the difference is the anchor.** The tell is the *same* tinted near-black on every project, arriving as a default rather than as a decision. A near-black derived from *this* page's anchor hue satisfies gate 22 and is not the tell; `#0B0B0B` pasted in regardless of the palette is the tell and still fails gate 22, since it is tinted toward nothing in particular. Do not "fix" gate 22 by going back to pure black.

## Use of the accent

The accent is a highlighter, not a colour block. Reach for it to:

- Mark an active nav item.
- Draw a focus ring.
- Underline a link on hover.
- Indicate a primary CTA's border or text.
- Place a small square beside a heading as a visual anchor.

Do not fill giant buttons with it. Do not set whole sections on it. Do not use it for decorative gradients. If you feel the urge to use more, that's the slop defaulting. Use less.

**Accent colours work *because* they are rare.** The common mistake is using the accent everywhere because it is "the brand colour"; overuse kills its power. That is the whole mechanism, and it is why the ceiling below is a ceiling rather than a target.

### 60-30-10 as visual weight — and how it resolves against the 3 % ceiling

60-30-10 is a rule about **visual weight**, not pixel count:

- **60 %** — neutral grounds, white space, base surfaces.
- **30 %** — the secondary tier: text, borders, inactive states.
- **10 %** — accent *and semantics together*: CTAs, highlights, focus states, status.

*Conflict resolved.* This file's § Principles caps the accent at **3 % or less of any viewport**, and § Bans refuses accent-as-background-fill above ~5 %. That is a stricter number than the 10 % band, and **the chain's ceiling wins**: 60-30-10 is imported as the *weight framing* for reading a composition, not as a licence to spend 10 % of a viewport on the accent. Read the 10 % tier as accent plus every semantic and state colour combined, with the accent's own share held under 3 %.

The version of 60-30-10 that ships with 10–12-step neutral ramps and 50–950 accent scales is deliberately **not** ported: it is incompatible with the 8–10 named tokens this chain holds per page. Only impeccable's visual-weight reading is in. (impeccable `color-and-contrast.md` § The 60-30-10 Rule (Applied Correctly).)

### The two-step accent — the one licensed exception to accent lock

**A page that hard-cuts between light and dark grounds physically cannot clear 4.5:1 on both with a single accent stop.** That page carries a two-stop accent: **one hue, two lightnesses**, keyed to the ground family, redefined per section alongside the ink.

Still one accent per ground, still one hue for the page. **Two different hues is not what this licenses**, and neither is a third stop for a third ground — a page needing three is a page with an unresolved theme. This is the same rule as "one tonal inversion per page" seen from the colour side: the inversion is allowed exactly once, deliberately, and the accent follows it.

(scroll-craft `taste.md` § Colour.)
