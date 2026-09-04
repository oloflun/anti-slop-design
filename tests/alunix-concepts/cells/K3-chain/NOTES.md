# K3 "Instrument" — Alunix concept notes

## Reference lock + decision ledger

Primary reference/direction: Sanity.io (`design-catalogue/entries/sanity`) —
onyx near-black canvas never pure black, one accent rationed to exactly one
CTA role per view, numbered ledger sections, real content treated as proof.

Preserve: onyx-stack canvas (never pure `#000`, graduated dark steps replacing
shadow); the single accent confined to links/CTA only, never a fill or a
section background; ledger rows (hairline + display numeral) for every list on
the page; one workhorse grotesk running the whole page at every size (borrowed
from Hark Capital's "one grotesque, every size" rule); a single light-source
motif restated once, reinterpreted from Hyperborea's "one light, repeated" as
a monochrome glow on the counted numerals rather than a second colour.

Borrow only: Hark Capital's restrained-headline-against-one-device framing
(the display statement carries all the weight, no photograph behind it);
Hyperborea's "restate the one light source" principle, applied as a static
(non-idle) glow, never as a second hue.

Role rules: `--action` is CTA-and-link only — the hero's second line, the
kicker contact link, the demo links, the close mailto. It never fills a
background, a border, or the counted numerals themselves (bone-toned with a
white glow instead).

Media strategy: product surface (the three demo screenshots, vendored from
`~/alunix/public/demos/` into `./demos/`). No photography, no illustration —
K3's forbidden list bans photos outright.

Reject: any photograph; K1's white/light inversion band; K5's viewport-width
wordmark hero; a second accent hue; rounded pill CTAs; numbered eyebrows or
"No. 01" sub-labels; a scroll cue.

Token commitments: void `#0A0B0D` (close, darkest step); surface-0 `#111214`
(canvas); surface-1 `#17181B` (brief's own instrument-register hex, used for
the data strip and process ledger); surface-2 `#1E2024` (BEVIS panel,
lightest dark step — the page's one tonal inversion, dark-to-lighter-dark
since a true light band is forbidden); bone `#EDEDEE`; bone-dim `#8B9199`;
action `#4B95DC` (see waiver below); Geist (display, 700-800) + Geist Mono
(kicker, ledger labels, numerals).

| Decision | Source | Role | Why |
|---|---|---|---|
| Onyx never-pure-black stack | sanity (primary) | canvas replaces shadow | K3 register = cinematic dark; brief's own `#17181B` becomes one step in the stack, not the whole canvas |
| Accent confined to links/CTA only | brief.md "en blå #1E5E9C bara för handling" + sanity's one-CTA-per-view rule | token-role | Brief is binding on this exact point; sanity supplies the enforcement pattern |
| Numerals glow in bone, not blue | reinterpreting hyperborea's single-light-source principle | decorative-only | Keeps the accent's role pure (gate 91) while delivering the world's "siffror som lyser" trait |
| One grotesque (Geist) at every size | hark capital's "one grotesque, all sizes" + brief's own named/unresolved font spec | display + body | Resolves the brief's own open Instrument Serif / Geist tension; licensed by brand evidence, not an unreasoned default |
| Ledger (`dl`/`dt`/`dd`, hairline rows) for the data strip and the process steps | house-physics "ledger, never card grid" | list structure | K3's authority is "data as texture"; a card grid would compete with the display type |
| No nav, kicker strip only | contract.md K3 fingerprint row | chrome | Locked by the contract; typographic-poster grammar bans marketing chrome beyond the wordmark |
| Value-step ground (surface-1 → surface-2 → void) | house-physics "one tonal inversion per page" | ground | A true light inversion is K1's forbidden white band; a value-inversion within the dark register satisfies the rule without borrowing K1's device |
| Accent lightened to `#4B95DC` (same hue/saturation as brief's `#1E5E9C`, lightness raised) | measured contrast, `a11y_scan.py` | accent value | Brief's literal `#1E5E9C` measures 2.4-2.9:1 against the four page grounds — fails WCAG AA at every size. `#4B95DC` holds the identical hue (209.5°) and saturation, lightness raised until every ground clears 4.5:1 (measured 5.15-6.22:1). Disclosed gate waiver, not silent drift — the brief's literal hex could not ship without failing a11y-audit. |
| Hero rewritten: "Det finns inget vi. Jag svarar själv." replacing "Jag bygger sajten själv. / Mejla mig." | brief.md Röst section, verbatim: "inget 'vi' (det finns inget vi)"; brief.md Erbjudandet: "Den som ritar sidan svarar också i mejlen. Inget formulär, inget team, ingen mellanhand." | headline (sourced statement) + one inline action word (CTA) | Coordinator pixel-pass flagged the original line one as an unsourced slogan and line two as a whole-line CTA dressed as a headline. Rewrite traces line one to the brief's own parenthetical (source rule 1: what the trade actually does — no team exists) and folds the CTA into a single inline word, "svarar," inside a first-person sentence, rather than a separate display line |
| `.hero-action` underlined, not colour-only | `a11y_scan.py` (link-in-text-must-not-rely-on-colour-alone, re-run after the hero rewrite) | link affordance | Moving the action word inline (previously a standalone whole-coloured line) surfaced a genuine 1.4.1 violation; fixed with a thin underline at display scale rather than reverting to a separate CTA line |

## Fingerprint row (contract.md K3)

Grammar: typographic poster · Nav: none, kicker strip only · Hero device:
display-scale statement with one blue word (the inline action verb "svarar",
underlined, mailto-linked) · Act shape: large quiet zone, then ruled data rows
· Close: single statement line · Signature move: numerals count up, paired
with a hairline rule expanding under each row.

## Feeling curve

1. Quiet authority — one dark viewport, a sourced statement of what the firm
   is not (no "we"), one blue action word for what one person does instead.
2. Quiet credibility — four numbers counting up from zero against hairlines.
   **The peak**: largest scroll room, silence before it in the empty hero,
   all of K3's "data as texture" authority spent here.
3. Verification — three real linked sites in hairline frames, not claims.
4. Clarity — five ruled rows, plain process, two placeholders openly marked
   unresolved.
5. Resolve — page quiets to its smallest type, ground drops to its darkest
   value, one address.

## Full Swedish copy (plain text)

```
ALUNIX · hej@alunix.se

Det finns inget vi.
Jag svarar själv.
Jag är en utvecklare. Jag bygger sajter åt små företag, en i taget. Tre
sajter, tre olika byggen. Ingen delad mall mellan dem.

SAMMA HÄNDER
Samma system bygger allt jag levererar.
757 — entiteter
2 847 — kopplingar
346 — skills i 21 buntar
84 — agenter

BEVIS
Tre sajter. Öppna dem.

CALYX
Florist. Cream-papper, Cardo och PT Mono, prissatt index.
anti-slop-design.vercel.app/calyx
Kursiv och rak i samma rad.

HORAI
Restaurang. Tre systrar, lackröd accent, Cinzel-kapitäler.
anti-slop-design.vercel.app/horai
Fotografiet bär hela sidan.

HYPERBOREA
Konferens. Midnattsblå, bärnsten, kodritad SVG.
anti-slop-design.vercel.app/hyperborea
Ett ritat solmotiv i åtta varianter.

HUR DET GÅR TILL
Material — Jag härleder designen ur ditt varumärke: logotyp, produkt, bransch.
Bygge — Jag skriver koden själv. Inget färdigt tema.
Svar — Jag svarar i mejlen. Ibland är svaret nej. Då säger jag det.
Pris — [behövs pris]
Leveranstid — [behövs leveranstid]

Ingen mellanhand. Bara jag som ritar och jag som svarar.
hej@alunix.se
Alunix. En person, tre sajter.
```

All numbers are the brief's own (757 entiteter, 2 847 kopplingar, 346 skills i
21 buntar, 84 agenter) and describe what the system contains, never how many
use it. No customer named, no Klova, no em/en dashes, no questions, no
invented price or timeline — both are `[behövs …]` placeholders styled as
dashed labelled boxes.

## Skills invoked, in order

1. `Skill(design)` — SKILL.md Steps 1b, 2b (bake-off skipped per task
   instruction: K3 is one cell of the six-concept bake-off itself), 3, 4, 5.
2. `Skill(copywriting)` — CONTENT FUNDAMENTALS = the K3 voice rule (first
   person, short, numbers as texture, no adjectives, no questions).
3. `copy-gate.md` read directly (Pass 1b line-sourcing + structure rule
   applied: every line traces to brief.md or the contract).
4. `Skill(humanizer-svenska)` — applied to every Swedish string; removed a
   tricolon ("tre byggen, tre typsnitt, tre paletter") in the lede, added
   "själv" to the hero line for specificity over flat statement.
5. `Skill(humanizer-svenska)` re-run, post-launch — on the rewritten hero
   only ("Det finns inget vi." / "Jag svarar själv."): plain copula ("finns"),
   active first person, no hedging, no forced parallelism, direct sentences
   of deliberately uneven length. Passed clean, no further edits.

## Verification numbers

- `shoot.py` — fold + full-page (5626px) screenshots, read as images, iterated
  twice (blue-accent contrast fix, mobile process-ledger stacking fix), final
  pass clean.
- `scroll_verify.py` — `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
  `contrastUnderMedia: []`, `blankBands: []`. Clean on both the pre-fix and
  post-fix runs.
- `a11y_scan.py` — first run: 1 serious (`color-contrast`, brief's literal
  `#1E5E9C` on six link elements) + 1 moderate (`region`, kicker `div` outside
  a landmark). Both fixed (accent relightened to `#4B95DC`; kicker changed to
  `<header>`). Second run: **0 violations, 31 passes, 1 incomplete** (manual
  best-practice check, not a failure).
- Post-hero-rewrite: `a11y_scan.py` caught a new, real regression — the inline
  action word "svarar" (now mid-sentence text, not a standalone line) failed
  "links must be distinguishable without relying on color" (1.4.1). Fixed with
  a thin display-scale underline. Final run: **0 violations, 32 passes.**
  `scroll_verify.py` re-run clean (all six arrays empty) and the fold
  re-shot and read after both the rewrite and the underline fix.
- Mobile sweep at 320/375/414/768px via a throwaway Playwright script: **zero
  horizontal overflow at every width**. Caught and fixed one bug: the process
  ledger (`Hur det går till`) did not stack on mobile because `.process
  .ledger>div` (specificity 0,3,0) outranked the generic `.ledger>div`
  mobile override (0,2,0) inside the media query; added a matching
  `.process .ledger>div` override. Confirmed stacked and readable after the
  fix.
- `index.html` is 359 lines (budget: ≤400).
- Waived, by name: `overused-font` (Geist) — licensed via Tier 1 brand
  evidence, see decision ledger row 4; not a silent default.
