# The motion toolchain — the machine's real GSAP + Lenis, not copies

Read before the first line of motion code, together with `devices.md` § The engine
(the init and its house values) and `showcase-floor.md` (what the result must reach).
Everything below was measured on this machine 2026-10-02 unless marked *unverified*.

## 1. What is installed, and where

One global install, set up by Anton (`anti-slop-design/Global GSAP + Lenis – Architecture.txt`):

| Package | Path | Version |
|---|---|---|
| `gsap` (every plugin, free since 3.13) | `%APPDATA%\npm\node_modules\gsap` | 3.15.0 |
| `lenis` (+ `lenis/snap`, `lenis/react`, `lenis/vue`, `lenis.css`) | `%APPDATA%\npm\node_modules\lenis` | 1.3.26 |

**Never `npm install gsap`/`lenis`, never a CDN, never a vendored copy in a new build.**
A project reaches the install through two npm links. The old house route (copy
`scripts/motion/vendor/` into `assets/vendor/`) reached 4 files — gsap, ScrollTrigger,
SplitText, Lenis — out of 25 modules. CustomEase, which most GSAP showcase sites use,
was not among them. Vendoring stays only for pages already built that way (V3f, V3g).

## 2. Linking a project — `scripts/motion/link_motion.py`

The `design-intent` hook runs it automatically at the start of every larger design job
and every animation fix (prompt mentions animation/rörelse/övergång/hover/GSAP/Lenis/…
and the project has UI files). By hand:

```bash
python ~/.agents/skills/design/scripts/motion/link_motion.py <project>        # link + scaffold
python ~/.agents/skills/design/scripts/motion/link_motion.py <project> --check
```

What it does, and why each step exists:

1. Creates `package.json` (`"private": true`) when missing.
2. Adds `"gsap": "^3.15.0", "lenis": "^1.3.26"` to `dependencies` when absent.
   **Measured:** a bare `npm link gsap lenis` leaves both links *extraneous*, and the very
   next `npm install <anything>` prunes them silently. With semver deps the links survive
   every later install (`@gsap/react`, `react`, `vite` tested), and a deploy installs the
   same version from the registry. `npm link --save` is the wrong fix: it writes
   `file:../../AppData/Roaming/...`, a machine path that breaks every other machine and Vercel.
3. `npm link gsap lenis` — one command, both names (older npm pruned the first link when
   the second was linked separately). Windowless (`CREATE_NO_WINDOW`).
4. Copies `templates/gsap.js` and `templates/smooth-scroll.js` to the root when no
   central file exists in `.`, `src`, `src/lib`, `lib`, `app/lib`, `assets/js`, `js`.
   Never overwrites.

Check: `npm list gsap lenis` shows `gsap@3.15.0 -> ...\Roaming\npm\node_modules\gsap`.

## 3. The two central files

- **`gsap.js`** imports from `"gsap/all"`, registers every plugin **once**, re-exports them.
  The template registers 19 plugins, more than the architecture file's 14: it adds
  `CustomEase`, `CustomBounce`, `CustomWiggle`, `EasePack` and `Physics2DPlugin`.
  Everything else imports from it: `import { gsap, ScrollTrigger, SplitText } from "./gsap.js"`.
- **`smooth-scroll.js`** holds the one Lenis instance with the house values (`devices.md`
  § The engine). Import it once, early: `import lenis from "./smooth-scroll.js"`.

Two deliberate deviations from the architecture file (house measurements win):
`gsap.ticker.lagSmoothing(500, 33)` instead of `0` (a stalled frame made `scrollTo` jump
490–724 px in V3g), and the Lenis options `autoRaf:false, anchors:true,
respectReducedMotion:false, lerp:.075, wheelMultiplier:.6`.

**Trim before shipping.** `gsap/all` cannot be tree-shaken once registered. Measured with
esbuild, minified + gzip:

| Entry | gzip |
|---|---|
| template `gsap.js` (all 19 plugins) + Lenis | 115 kB |
| gsap + ScrollTrigger + SplitText + Lenis | 53 kB |

Develop against the full file. Before delivery, cut `gsap.js` down to the plugins the
page calls. It is the only file to edit, since nothing else imports gsap directly.
`performance.md` § 1 owns the budget.

## 4. Per project type

**Static HTML (the house prototypes, `tests/*/runs/*`).** Serve the project root over
http and give the page an import map. Verified headless (Chromium, 0 console errors,
0 4xx): SplitText with mask, pinned scrubbed ScrollTrigger, Lenis smoothing at house pace
(10 wheel notches = 720 px).

```html
<link rel="stylesheet" href="/node_modules/lenis/dist/lenis.css">
<script type="importmap">
{ "imports": {
  "gsap": "/node_modules/gsap/index.js",
  "gsap/all": "/node_modules/gsap/all.js",
  "gsap/": "/node_modules/gsap/",
  "lenis": "/node_modules/lenis/dist/lenis.mjs"
} }
</script>
<script type="module" src="/main.js"></script>
```

`"gsap/all"` needs its own line: the `"gsap/"` prefix would map `gsap/all` to a path
without `.js`. Paths are server-root-relative, so serve the folder that holds
`node_modules`. A page nested deeper (a board cell) uses `../../node_modules/...`.
**Deploying static HTML:** Vercel and most hosts do not upload `node_modules`. Bundle
first (`npx esbuild main.js --bundle --minify --format=esm --outfile=assets/app.js`).
Do not vendor; vendoring needs Anton's explicit go-ahead (architecture file).

**Vite.** Works unchanged with the links. Verified with Vite 8.3: dev pre-bundles gsap
into `.vite/deps`, serves `lenis.css` through `/@fs/` (200), and `vite build` bundles
3.15.0 from the link. In the entry: `import "lenis/dist/lenis.css"`.

**React / Next.** `npm i @gsap/react` is the one extra package. Measured: it dedupes onto
the linked gsap (`gsap@3.15.0 deduped -> ...Roaming\npm\node_modules\gsap`). Use `useGSAP`
(`gsap-react` skill). Put `gsap.js`/`smooth-scroll.js` in `src/lib/`; Lenis in a client
component, or `lenis/react` (`<ReactLenis root options={{autoRaf:false, ...}}>` driven by
`gsap.ticker`). *Unverified:* Turbopack resolves symlinks outside the project root only when
`turbopack.root` (or `outputFileTracingRoot`) covers the target. Test `next build` once in a
real Next project before trusting the link there.

## 5. Agent rules (from the architecture file, plus what measurement added)

Do: link, never install · import only through `gsap.js` · one Lenis instance in
`smooth-scroll.js` · `lenis.on('scroll', ScrollTrigger.update)` · `gsap.ticker` drives Lenis ·
trim `gsap.js` before shipping · `npm list gsap lenis` as the check.

Never: `npm install gsap|lenis` · plugins installed separately · `registerPlugin` outside
`gsap.js` · a Lenis instance per component · `ScrollSmoother.create()` on a Lenis page (two
scroll owners) · JavaScript imports typed into PowerShell · `npm link --save`.

## 6. Full potential — what the tools are for

The API lives in the official skills (`gsap-core`, `gsap-scrolltrigger`, `gsap-timeline`,
`gsap-plugins`, `gsap-utils`, `gsap-performance`, `gsap-react`, `lenis`). What a
showcase-level page does with the API, and which plugin carries each move, is in
`showcase-floor.md`, read from 646 GSAP and Lenis showcase sites.
