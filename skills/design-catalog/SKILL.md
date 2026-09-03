---
name: design-catalog
description: Add or look up entries in the design reference catalog (~/design-catalog, a GitHub repo). Use when the user says "lägg till i katalogen", "spara den här designen", "add to the catalog", pastes a URL/screenshot to keep as a reference, or when Step 1b of the design skill needs references.
metadata:
  version: 1.0.0
---

# Design Catalog

Local-first design reference catalog. The repo `oloflun/design-catalog`
(cloned at `C:/Users/Anton L/design-catalog`) IS the database — every entry
is a directory under `catalog/<slug>/` with a `entry.md` (YAML frontmatter +
body) plus captured images. There is no server-side database; `index.json`
and `families.json` are generated from the `entry.md` files by
`scripts/index.py` and must never be hand-edited.

A local app also exists at `npm run dev` -> http://127.0.0.1:4610 (grid,
detail pages, `/add` flow) for browsing visually — this skill covers the
command-line / in-session add-and-lookup path, which is faster inside an
agent session because the agent's own vision replaces the `claude -p`
subprocess call that the app's `/add` flow uses.

## Adding an entry

1. **Sync first.** `bash scripts/sync.sh pull` (run from
   `C:/Users/Anton L/design-catalog`) to make sure the local clone has
   whatever anyone else pushed.

2. **Capture.** `python scripts/capture.py <url|file> <slug>` — Playwright
   navigates the page (use a `file://` URL for a local HTML file), scrolls it
   once to trigger reveals, and writes `catalog/<slug>/shot.webp` (full
   page), `fold.webp` (first 1440x900 viewport), `shot.png` (lossless copy of
   the fold, for vision), and up to 12 `slices/NN.webp` viewport-height
   slices. Pick `<slug>` as a short kebab-case name for the site/brand.

3. **Describe it yourself — do not shell out to `claude -p` inside a
   session.** Read `catalog/<slug>/shot.png` and every image in
   `catalog/<slug>/slices/` with your own vision, then write
   `catalog/<slug>/entry.md` by hand, following the exact schema below. Being
   the same agent that captured it, you already have the page content in
   context — use that instead of guessing from pixels alone where you can
   (e.g. exact font names, real copy).

   **Frontmatter (exact keys):**
   ```yaml
   ---
   title: <string>
   url: <source url, file:// for local>
   captured: <ISO date>
   family: <short kebab-case family name>
   dna: "<A x B lineage, short>"
   register: <editorial print | cinematic dark | illustrated dark | modern clean | warm photographic | historical art | other>
   grammar: <filmic one-shot | chaptered editorial | live surface | continuous world | typographic poster | gallery/catalog | split stage | rhythmic cutlist | none>
   lane: <one concrete phrase for its scroll/interaction lane>
   mode: <persuade | operate | read | experience>
   traits: [<4 to 8 short chips>]
   palette: [<hex colors>]
   type: [<font names>]
   kind: <example | reference-style>
   source: <anton | claude | chat>
   status: ready
   ---
   ```

   **Body, H2 sections in this exact order:** Why it works · What to borrow
   (principle) · What to leave · Signature move · Brief · Image recipe ·
   Photo search · Reference lock.

   - **Brief**: a 4-8 line prompt that would reproduce the style.
   - **Image recipe**: an art-direction prompt with a `[SUBJECT]` placeholder.
   - **Photo search**: 2-4 search phrases + preferred source (Unsplash
     first, Pexels second).
   - **Reference lock**, filled in exactly:
     ```
     Primary reference/direction:
     Preserve (3-5 traits):
     Borrow only (1-2):
     Role rules:
     Media strategy: photo:unsplash|pexels / generated / code-native / placeholder
     Reject:
     Token commitments:
     ```

   If you truly cannot look at the images in this turn, leave `status:
   pending` and note why — do not fabricate palette/type/traits.

4. **Rebuild the index.** `python scripts/index.py` — regenerates
   `catalog/index.json` and `catalog/families.json` from every `entry.md`.
   Always run this after adding or editing an entry.

5. **Push.** `bash scripts/sync.sh push "catalog: <slug>"` — pulls/rebases
   first, commits everything, pushes. If the push fails it prints `queued`
   and leaves the commit local; the next `sync.sh push` run will pick it up.

## Looking up references

`python scripts/query.py --family X --register Y --grammar Z --mode M`
(all filters optional, and combinable) prints matching slugs with their lane
and traits — use this from Step 1b of the `design` skill to pull references
that match a target register/grammar/mode instead of starting from nothing.

## Running the app

`npm run dev` from `C:/Users/Anton L/design-catalog` serves the grid and
detail UI at `http://127.0.0.1:4610`. It pulls the repo once on startup
(instrumentation hook) so the local clone stays current without a manual
`sync.sh pull`. The `/add` page there talks to the same `capture.py` /
`describe.py` / `index.py` / `sync.sh` pipeline via server actions, spawned
in the background and polled through `/api/status/<slug>` — useful when
Anton wants to add something himself outside a session, but inside a
session prefer the manual steps above (skip `describe.py`'s `claude -p`
subprocess call — it is slow and redundant when you can just read the
images directly).
