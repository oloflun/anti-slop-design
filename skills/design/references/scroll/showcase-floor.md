# Showcase floor — the level GSAP + Lenis pages are held to

Read with `toolchain.md` (how the tools are wired) and `devices.md` (the device kit).
This file is the **floor**: what a house page must reach before it ships, read from
the GSAP showcase (gsap.com/showcase) and the Lenis showcase (lenis.dev/showcase).
Every listed site was captured headless with real wheel scroll
(`scripts/catalogue/motion_capture.py`) and read by the lead from its contact sheet.
Each one is a catalogue entry: `design-catalogue/entries/<slug>/` (`entry.md` +
`motion/sheet.webp` + `motion/probe.json`), `showcase: gsap|lenis` in the frontmatter,
`motion_floor: 2|1|0`. They reach Inspo through `scripts/inspo_import.py`.

Status: **read in full** (2026-10-03). 646 showcase sites: 564 captured and read by the
lead from their contact sheets, 82 skipped with a logged reason
(`design-catalogue/showcase-skipped.jsonl`: dead domains, bot walls, gates that cannot be
passed headless), 0 queued. Section 6 has the measured stack.

## 1. How to use it

The worked example of the whole floor is [`journeys/era-residence.md`](journeys/era-residence.md)
— rank #1 in `design-catalogue/ranking.txt`, the trip Anton named as the kind every house page
should give its visitor. Read it for the *journey*; take the shape, material and door from
elsewhere (its § 5).

- Before the first line of motion code: pick **two `motion_floor: 2` entries** whose
  grammar matches the brief (`python scripts/catalogue/query.py` or `grep -l
  "motion_floor: 2" design-catalogue/entries/*/entry.md`) and open their
  `motion/sheet.webp`. Name the intro, the transitions and the signature object you
  are borrowing in the decision ledger, the same way a visual reference is locked
  (`reference-lock.md`).
- At review (`design-verify`, leadens pixelgranskning): the page's own contact sheet
  (same capture script, run on the build) goes side by side with those two sheets.
  Below the floor = not shipped.

## 2. The floor, in seven rules

1. **Intro and hero are one shot.** The loader's last frame is the hero's first:
   something persists across the handoff. Seen: the count-up that ends in the
   hero's own mark (ddark's sun, Nick Ho's race number 98, A24's counter handing to
   the first disc), the year counter that becomes the name (Khanh Nguyen), the
   ball in the loader that becomes the hero object (IKEA 30), the copy-only intro
   on black that ends by lighting the scene that was there all along (See What Eye
   See, Forge), a dot that ignites into a plasma sun which the camera then reveals
   as the reactor inside a ship (Maritime Fusion), a CRT boot screen the camera dives
   through into the site (Shader), a glowing wordmark that burns into the sparks of
   the next scene (Lore), wordmark letters assembling while a night ocean fades up
   behind them (Hashgraph). **Not allowed:** a spinner or a percentage that fades
   out and then fades the hero in, with nothing shared.
2. **Every section change has a material cause.** The next section arrives as
   something: a sheet laid over the last (ddark), a film sliding over the previous
   film (Sadu), an image growing from a card behind the heading to full bleed
   (Forge, Filmbot), the ground changing through a full-bleed image that already
   holds both colours (Filmbot), a pixel-block dissolve (Davide Cattaneo), a dot
   field that forms the next object (Manish), a highlighter wiping the slide
   (Nodeck), slats opening over video (Dkton), a photo standing up on a hinge
   (Bulbs), vertical scan bars (Door Dennis), a colour panel growing out of the
   page's axis (Specia1ne), colour bands meeting along the logo's own pixel-cut
   edge (Huehaus), arched windows on paper widening into the room they frame (Capitolium), a diagonal wipe that cuts one layer deeper under the same water
   (Hashgraph), the hero's rings opening into a portal the camera dives through
   (Moblinks), files pouring out of a laptop screen onto the next scene's desk
   (Poly), the light on the page itself turning from day to amber evening (Daylight
   Computer), a swarm of the data's own thumbnails reforming into the next figure
   (Getty Tracing Art). **At least three different transition causes per page,
   never the same twice running** (matches `devices.md`'s ≥4 families). A page
   where every section only fades up 14 px is below the floor.
3. **One signature object recurs and changes.** The best pages give one shape or
   object a job in several sections: Dkton's amber pills are a level meter, then
   bars, then blinds; LxL's orange swash draws through every section; Emotion's
   particle form is a swirl, a cube, a cloud; Run Rob Run's pixel runner is the
   loader and later sprints across the lab; Hungry Tiger's jar tumbles through every
   headline; one leaf is steamed, ground and sealed into a tin across Matcha Cartel's
   production chain; T-Rex Leather's bag turns, goes X-ray, then scatters into
   swatches and the grain itself; Lore's single token carries the manifesto and then
   the founders. Name it in the brief; it is the thread between the transitions in
   rule 2.
4. **Text moves at reading pace, and stands still to be read.** Headings: SplitText
   line masks (`mask:'lines'`), never per-character on long text. At least one
   statement per page is paced by the scroll itself: words filling grey→ink (Forge,
   Filmbot), keywords highlighted in turn (Manish, Nodeck, Nick Ho), the active item
   of a list lit while the rest stay grey (Revelatio's cities, Sadu's services,
   Specia1ne). The house rule from `motion.md` holds over all of these: a heading ≥
   40 vh fully visible, unclipped and still while it is read.
5. **Type and media share a frame at least once.** Video in the gap of a headline
   (Sadu), photos tucked between the words of a statement (a-lign), a title that
   parts so the gallery grows in the gap (Khanh's 'THE WORK', bleibtgleich's
   'Work [cards] 24-26'), the product sitting inside the headline (Don Molinico's
   jar in 'Pimientos del piquillo', Assistantly's mascot in the gap of 'with
   Talent'), photos slotted between the lines of the studio's biggest sentence
   (Ashley Brooke CS), creators placed in the gaps of a split statement (Patreon).
   This is what separates a designed page from a stack of text blocks and image
   blocks.
6. **Smoothing is a choice, measured.** Lenis showcase sites travel 40–220 px after
   the wheel stops. Above ~180 px pages read as floaty (Bulbs, SK Archive); the house
   value (`lerp .075`, `wheelMultiplier .6`) sits in the lower half on purpose and is
   not raised to look "smoother".
7. **Gates are for experiences only.** About one in six showcase sites gates entry
   (ENTER, sound on/off, choose a path). A persuade page never gates. An experience
   page may, but the gate is a designed object (Chasing the Moment's ticket that
   tears into the sound choice), and "without sound" is always offered.

## 3. Intro patterns (pick one per page)

| Pattern | What happens | Seen on | Plugins |
|---|---|---|---|
| Counter → mark | A number counts up; its last frame becomes the hero mark | ddark, nickho-motorsports, a24-raviklaassens, khanhnguyen | core, CustomEase |
| Copy first | 2–3 timed lines on black, then the hero is lit | seewhateyesee, forgeautomotive-co | SplitText |
| Curtain / push | A bar wipes or a character shoves the loader off | filmbot, huyml | core |
| Letters out of blur | Name assembles letter by letter from blur or grey | millemannwines, forgeautomotive-co, mattjinn | SplitText, CustomEase |
| Object in the loader | The loader's moving part is the hero object | family-ikea | core + WebGL |
| Scene fade-up | Logo mark on ground, the scene window rises | illoca-unseen, davidecattaneo | SplitText |

## 4. Transition causes (rule 2 vocabulary)

sheet-over · film-stack · card-to-full-bleed grow · ground change through an image ·
pixel-block dissolve · dot-field forms the next object · tool wipe (highlighter) ·
slats/blinds · hinge stand-up · scan bars · panel grows from the axis · bar-built
display words · horizontal pin pan (Khanh) · camera dolly in a 3D scene (Illoca) ·
wheel-cut between full-bleed films (Forms, Jason Bradley) · pixel-cut edge that is
the logo's unit (Huehaus) · diagonal wipe one layer deeper (Hashgraph) · portal
through the hero's own shape (Moblinks) · contents pouring out of a screen (Poly) ·
light change on the ground itself (Daylight) · data swarm reforming (Getty) · two
statements handing over inside one set of line masks (Alunix R9 tes).

## 5. Below the floor (observed, not to copy)

- Virtual scroll with no progress indicator (Millemann, Illoca): the reader cannot
  tell how far they are.
- Giant words permanently cropped at both edges (Cip Harvin) read as fragments.
- Ghost-grey text before activation, below contrast for long stretches (a-lign,
  Forge before the fill).
- Wheel-only content with no scroll path (A24 discs, Huy Phan, Jesper Landberg).
  Fine for an experiment, wrong for a page that must be read.
- A gate on a page whose job is to persuade.

## 6. Measured stack (from `motion/probe.json`)

Measured over **564 read sites** from `motion/probe.json` (`scripts/catalogue/showcase_stats.py`).

| Measure | Sites |
|---|---|
| GSAP loaded | 515 (91 %) |
| GSAP minor versions | 3.12: 146, 3.15: 139, 3.13: 138, 3.14: 75, 3.11: 20, 3.10: 5 |
| Lenis | 415 (74 %) |
| ScrollSmoother | 25 (4 %) |
| Locomotive | 5 (1 %) |
| Pinned sections | 115 (20 %) |
| WebGL canvas | 273 (48 %) |
| Page transitions (Barba / Swup / Taxi) | 55 / 12 / 34 |
| Smoothed scroll | 352 (62 %); px still travelling after the wheel stops: median 154, p25 134, p75 177 |
| Floor 2 / 1 / 0 (lead's reading) | 65 / 304 / 195 |
| Grammar | chaptered editorial: 335, continuous world: 44, gallery/catalog: 43, live surface: 41, filmic one-shot: 39, rhythmic cutlist: 29, typographic poster: 18, split stage: 13, none: 2 |
| Register | cinematic dark: 195, modern clean: 145, other: 62, warm photographic: 58, editorial print: 55, illustrated dark: 41, historical art: 8 |
| Mode | persuade: 328, experience: 124, read: 107, operate: 5 |

What the numbers say for a house page:

- **Lenis is the norm, ScrollSmoother the exception** (74 % against 4 %): the house
  choice (one Lenis, no ScrollSmoother beside it) is the showcase's own default.
- **Pins are a tool, not a style.** One site in five pins anything. The floor-2 pages
  pin one or two acts and let the rest flow; a page that pins every section is not
  on the list.
- **WebGL is half the showcase, but not half of floor 2.** Many floor-2 pages
  (Huehaus, Bohdan, Ashley Brooke CS, Daylight, Hungry Tiger) carry their journey with
  clip-path, masks, photography and type. The journey is the requirement, the
  renderer is not.
- **The house pace sits low in the measured band.** Smoothed pages travel 134–177 px
  after the wheel stops (median 154); the house Lenis (`lerp .075`, `wheelMultiplier
  .6`) is set for a calm read, and is not raised to look "smoother" (rule 6).
- **Chaptered editorial dominates** (333 of 562). The floor is therefore not "become a
  continuous world": it is that a chaptered page still makes every chapter change a
  material event (rule 2) and carries one object through (rule 3).
