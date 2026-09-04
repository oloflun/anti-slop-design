# K1 "Svart scen, vit sal" — build notes

## Reference lock (verbatim, also in the HTML header comment)

```
Primary reference/direction: squarespace — cinematic monochrome gallery, 0% colourfulness
marketing shell that reserves all chroma for user/product content, whisper-weight 300
display type, real customer-site screenshots peeking up from the fold as the hero device.
Preserve: strictly achromatic shell (pure black + pure white + measured greys, zero chroma
anywhere in nav/type/hairlines/buttons); weight-300 whisper display at 64-96px+ with tight
negative tracking; radius split by role (0px hard edge on the one real button, soft edge
only on demo-frame images); customer screenshots as the page's only source of colour; real
screenshots, never fake browser chrome.
Borrow only: the bottom-anchored demo card peeking up at the fold edge, reinterpreted as
three cards that rise on scroll instead of sitting static; the small corner arrow-link.
Role rules: chroma never enters the K1 shell itself; the only saturated colour on the page
lives inside the vendored demo screenshots; 0px radius is button-only, never on frames;
mono is register-only (labels/nav/numbers), never the declarative voice.
Media strategy: photo:local — one vendored dark-stage ground photo (assets/stage-pool.webp,
licensed as ground only, never a claim) behind the fold; three vendored real product
screenshots (demos/*.webp) as the proof device. No stock photography anywhere.
Reject: any chromatic accent token in the shell; a filled/pill CTA (K1 keeps the sharp-edge
button, not K5's pill or K2's colour block); serif anywhere; K3's blue as a shell accent;
insign's colour bands.
Token commitments: stage bg oklch(0.08 0 0), stage ink oklch(0.97 0 0), hall bg
oklch(0.99 0 0), hall ink oklch(0.09 0 0), mute-stage oklch(0.64 0 0), mute-hall
oklch(0.4 0 0), hairline-stage oklch(0.97 0 0 / .14), hairline-hall oklch(0.09 0 0 / .14);
display Space Grotesk 300-500, clamp(2.6rem,7vw,6.5rem), leading 0.94, tracking -0.02 to
-0.045em; register IBM Plex Mono 10.5-13px, tracking 0.16-0.22em, uppercase; radius 0px
button / 6px demo-frame; max-width 1240px.
Secondary borrow (planhat): negative tracking escalating with size; 1px hairline borders as
the complete substitute for shadow, no shadow anywhere; a rationed single ground photograph
above the demo screenshots, nothing else photographic in the shell.
Secondary borrow (aarke): a second face reserved exclusively for register (mono: labels,
system numbers, prices), kept strictly apart from the display voice, aarke's monospace/
grotesque split, inverted (voice is the grotesk here, not the mono).
```

## Decision ledger

| Decision | Source | Role | Why |
|---|---|---|---|
| Pure black stage to pure white hall, one hard cut | squarespace (primary) + contract world | act-shape / tonal inversion | Direct execution of "Svart scen, vit sal"; matches squarespace's own black/white bands, no gradient blend |
| Weight-300 whisper Space Grotesk display | squarespace (primary) | display voice | Achromatic + whisper weight is squarespace's central preserve trait; forbidden list bars serif |
| Demo screenshots as the only chroma source | squarespace (primary), "0% colourfulness, chroma confined to user content" | media role | Exact parallel to K1's authority: the three demos ARE the product, so letting them carry all colour makes the product the only vivid thing |
| Demo cards rise on scroll (signature move) | squarespace (borrowed: static peeking cards), reinterpreted | hero device / signature move | Squarespace's cards sit static at the fold edge; K1's fingerprint requires the frames to rise, so the borrow is the position only, the motion is new |
| Hairline-only separation, no shadow anywhere | planhat (secondary) | structural | TASTE.md's "depth without shadow"; keeps the achromatic shell free of any soft/gradient cue |
| Mono reserved for labels/system-number texture only | aarke (secondary) | type role | Aarke's monospace/grotesque split, inverted: mono is register here, Space Grotesk carries the declarative voice |
| Ledger, not cards, for "how it works" | TASTE.md §1/§4 + house-physics | structure | Four steps are genuinely a list; a card grid is the reflex the spec bans |
| `[behövs pris]` / `[behövs leveranstid]` as dashed placeholder chips | brief.md binding rule | content | No invented numbers permitted anywhere |
| System numbers as one quiet mono line | brief.md "Riktiga systemsiffror" + contract authority "produkten + skala" | texture | K1's authority names scale explicitly; numbers describe what the system contains, never usage, kept to one subdued line so the product never takes over |
| Demo screenshots kept verbatim, incl. Hōrai's in-frame hand | brief.md mandatory proof asset | content | The three screenshots are fixed proof assets the brief requires by filename; the "no photos of people" rule governs K1's own imagery choices, not the mandated third-party proof crops |
| Lede over the fold photo set to near-white at 86% opacity, not muted grey | contrast_over_media measurement | text/media role | First draft's muted grey lede measured 1.9-2.0:1 against the brightest patch of the stage photo; brightening to stage-ink at 0.86 opacity cleared the 4.5:1 floor with margin |

## Fingerprint row built

grammar: rhythmic cutlist (adapted to modern-clean: short hard-cut acts, reveal on nearly
every element, no pin/spotlight/magnet/dwell/parallax) · nav: minimal top strip, wordmark +
mailto, inverts ink on the stage/hall cut · hero device: dark stage, three demo frames float
· act shape: black stage → white hall, one hard cut · close: white hall, email at display
scale · signature move: demo frames rise on scroll, continuously scrubbed (translateY +
under-glow, two coordinated layers, both scroll directions).

## Feeling curve

1. Curiosity — the stage sits empty and dark, one pool of light, before anything appears
2. Recognition — the three demo frames rise into the light, each pulling its own colour up out of the black
3. Trust — the ledger states the process plainly, gaps named as gaps, not hidden
4. Resolve — the room turns white, one sentence, the email fills the screen

Peak: act 2, the demo frames rising — largest scroll span, the only saturated colour on the
page, the silence of the empty stage right before it.

## Full Swedish copy (plain text)

**Nav:** ALUNIX · hej@alunix.se

**Fold**
- Kicker: Webbdesign
- H1: Tre sajter. / Du bedömer.
- Lede: En byggare. Tre sajter. Ingen delad mall, ingen delad palett, ingen delad rytm mellan dem.
- CTA: hej@alunix.se (mailto)

**Bevis**
- Kicker: Bevis
- H2: Du öppnar dem själv.
- Calyx — »Kursiv och rak i samma rad« — anti-slop-design.vercel.app/calyx
- Hōrai — »Fotografiet bär hela sidan« — anti-slop-design.vercel.app/horai
- Hyperborea — »Ett ritat solmotiv i åtta varianter« — anti-slop-design.vercel.app/hyperborea
- Texture line: Samma händer bygger också Alunix OS.

**Så här**
- Kicker: Så här
- H2: Så bygger du sajten.
- 01 Material — Du skickar logotyp och text. Designen kommer ur dem, inte ur ett tema.
- 02 Förslag — Du får ett förslag att se. Svaret kan vara nej.
- 03 Bygge — Sajten byggs och testas. [chip: Leveranstid: [behövs leveranstid]]
- 04 Pris — Priset sätts per uppdrag. [chip: Pris: [behövs pris]]

**Kontakt**
- Kicker: Kontakt
- Du mejlar. En person svarar.
- Svaret kan vara nej. Du hör det direkt.
- Inget formulär
- hej@alunix.se (display-scale mailto)
- Footer: Alunix · webbdesign

Voice rule applied throughout: declarative, second person ("du"), max five words per
heading clause with a period after each, no adjectives (numerals and the brief's own
required phrases — "delad mall/palett/rytm" — are structural, not promotional, and are
kept as the source's own defining claim, not decoration).

## Skill(...) calls made, in order

1. `Skill(design)` — front door, Steps 1b/2b/3/4/5 followed as directed (bake-off skipped per instructions, this is a bake-off cell)
2. `Skill(copywriting)` — CONTENT FUNDAMENTALS voice rule applied (declarative, 2nd person, ≤5 words/heading, period after each, no adjectives)
3. `Skill(humanizer-svenska)` — applied to every Swedish string; no AI-tell patterns present (no nominalizations, no vague attributions, no tricolons-with-och, no filler, no em/en dashes)

References read directly (not via Skill tool): `design-catalogue/TASTE.md` §1/§4/§6; catalog entries `squarespace`, `planhat`, `aarke` (`entry.md` + `fold.webp` + 2 slices each, read as images); `references/reference-lock.md`, `references/scroll/grammars.md`, `references/scroll/feel-and-fingerprint.md`, `references/house-physics.md`, `references/copy-gate.md` (also explicitly required by the task).

## Verification numbers

- `shoot.py` fold + full (1440×900, full page 2773px) — read both PNGs, iterated twice on real bugs found (see below), final pass clean.
- `scroll_verify.py` desktop (1440×900, 8 stops): deadScroll 0 · cuesNeverFull 0 · unrevealed 0 · contrastUnderMedia 0 · blankBands 0.
- `scroll_verify.py` mobile (375×812, 12 stops): deadScroll 0 · cuesNeverFull 0 · unrevealed 0 · contrastUnderMedia 0 (1 finding fixed, see below) · blankBands 0.
- `scroll_verify.py` `--reduced-motion` (1440×900): deadScroll 0 · cuesNeverFull 0 · unrevealed 0 · contrastUnderMedia 0 · blankBands 0.
- `a11y_scan.py`: violations 0, passes 24, incomplete 1 (axe's own manual-review bucket, no HIGH/serious/critical finding) — verdict **Approve**.
- Manual overflow sweep at 320/375/414/768px (Playwright, scrollWidth vs clientWidth + element-bounds check): 0 overflow elements at every breakpoint.

## Bugs found and fixed during verification (both were real, not test artifacts)

1. **Demo frames invisible in the full-page capture.** The signature-move rise effect tied
   the whole `.frame` card's opacity to a scroll-computed `--p` custom property that only
   updates on a real `scroll`/`resize` event; a full-page screenshot taken without ever
   scrolling left `--p` at its initial 0, so all three demo cards (image, name, tagline,
   link) were fully transparent. Fixed by moving `.frame` onto the same fail-toward-visible
   `.reveal` system as the rest of the page (visible by default, IntersectionObserver +
   above-fold-at-mount + 1.5s failsafe) and demoting the scroll-scrub to a small additive
   embellishment (a 14px image lift + an under-glow layer) that degrades gracefully to "at
   rest, fully visible" rather than "invisible" when no scroll ever fires.
2. **Contrast under the fold photo.** `scroll_verify.py --width 375` flagged the fold lede
   ("En byggare. Tre sajter...") at 1.9:1 against a 4.5 floor. Strengthened the photo's
   overlay gradient and, more decisively, swapped the lede from muted grey to near-white at
   86% opacity — re-measured clean at both 375px and 1440px.

Both fixes are reflected in the decision ledger above and in the shipped file.

## Coordinator pixel-pass fixes (round 2, 2026-09-04)

1. **Frame misalignment + not-dominant-enough.** The Bevis act's stagger
   (`nth-child(2){margin-top:-34px}`) made the settled state read as misaligned rather
   than mid-rise. Removed the stagger entirely — all three frames now share one top
   edge, one height, one caption baseline. The frame row was also pulled out of `.wrap`
   into a new full-bleed `.bleed` container (edge-to-edge minus a small gutter, no
   1240px cap), and the image `aspect-ratio` changed from 16:10 to 1:1, making the row
   both the widest object on the page (wider than the 1240px-capped headline column
   above it) and tall enough that the frame block alone (image + meta) is ~520-540px at
   1440px width, with the full Bevis act (kicker + heading + frames + texture) well over
   a full viewport height. This also satisfies the house-physics "one grid-break where
   something meets the viewport edge" requirement, which the first draft lacked.
2. **Data-as-texture belongs to K3.** Dropped "757 entiteter · 2 847 kopplingar · 346
   skills i 21 buntar · 84 agenter" entirely — the contract assigns numbers-as-texture
   to K3's fingerprint, not K1's. The "samma händer" mention stays as a single mono
   line with zero digits: "Samma händer bygger också Alunix OS."

Re-verified after both fixes: `scroll_verify.py` desktop and 375px mobile both clean
(0 deadScroll/unrevealed/cuesNeverFull/blankBands/contrastUnderMedia); `a11y_scan.py`
0 violations, 24 passes; fold + full screenshots re-shot and read, no defects found.
