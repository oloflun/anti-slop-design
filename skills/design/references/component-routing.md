# Component routing

**Load at Step 3 of every build.**

Skills are **tools invoked for craft**. They do not choose the direction — the gate already did that. A specialist that arrives at a component and repaints it is a gate-order violation, not a contribution.

`design-route.py` parses the JSON block below on every UI file write and emits one line naming the skill for what was just written. This file is the single source of truth for that table; the hook does not carry its own copy.

---

## The table

| Building | Invoke | Because |
|---|---|---|
| Nav, header, menu, animated dropdown | `animated-navigation` | Rollout tabs, flying-arrow motion, expanding underline, glass dropdown reveal, mobile menu — the full interaction model with real timings |
| Button, modal, drawer, popover, tooltip, toast, sheet, accordion; anything with drag, swipe, gesture, or a press feel | `emil-design-eng` | Easing curves, spring config, `transform-origin` correctness, `:active` states, GPU vs JS. Outputs a Before/After/Why table |
| Carousel, slider, gallery | `slideshow` | 3D carousel mechanics. In project-a, the project's carousel rules bind on top |
| Route or state transition | `vercel-react-view-transitions` | `<ViewTransition>`, `addTransitionType`, directional navigation, list reorder |
| shadcn primitive | `shadcn-ui` | Correct primitive usage and theming against the locked tokens |
| Chart, graph, KPI tile, dashboard panel | `dataviz` | Form heuristic, colour formula with a validator, mark specs, legend and axis rules |
| Imagery-led section | `imagegen-frontend-web` | Real imagery, not CSS scenery. One image per section |
| Form, input, select, validation | `impeccable harden` | Errors, i18n, edge cases — plus all 8 states required |
| React component structure | `react-components` | Composition and props patterns |
| Next.js app surface | `next-best-practices` · `vercel-react-best-practices` | Framework-correct data flow and rendering |
| Any user-facing string | **copy gate** → [`copy-gate.md`](copy-gate.md) | `copywriting` then `humanizer`, every language |
| Landing page, portfolio, or marketing surface (page-scope) | `design-taste-frontend` | v2 brief-inference, intensity dials, design-system map, redesign protocol, and the production-test tells. **Craft and structure only — never lets it pick the palette at Tiers 0–2** |
| A surface, card or panel entering on scroll | `spring-arrival` | Antons fjäder `spring(0.66, 0.95)`, en ruta i taget, texten efter landningen; the `.rise`-transition fault behind "vibrerar" (F-030, F-031) |
| Agent text or a headline written live | `live-text-reveal` | Takt per tecken, pauser före betoningen, markör, `sr-only`, no reduced-motion gate (F-033, F-038) |
| A number counting up | `count-up-in-view` | Starts only fully in view above the bottom fifth, after the row's fade, 2.6 s quadratic; how to verify by arriving from below (F-039) |
| Display type on a photograph | `hero-on-photo` | No shadow shape, a measured band in the photo (≥ 4.5:1 vs the brightest 5 %), one accent word last, light accent (F-032, F-034) |
| Entrance motion on a photo | `photo-stands-whole` | No clip reveal on photos — reads as slow loading; parallax only (F-035) |
| A product surface on a marketing page | `showcase-surfaces` | Constructed in JSX with example data, one family, never a screenshot; `.case-zoom` fill on desktop (F-036) |
| Copy a customer reads in a demo, or copy shared across product pages | `showcase-copy-scope` | Short plain-word motivations, a code-side strip of references, one real answer per demo button, per-product variants (F-033, F-037) |
| Declaring scroll- or load-triggered motion done | `motion-verification-preview` | Arrive from below, front the preview tab, read reduced-motion in the preview, zoom the screenshot, 375 + 1600 px, push to development (F-039) |
| **Dashboard, admin, settings, table, editor, any authenticated in-app surface** | **`impeccable operate`** | **Operate mode. Load [`product-surfaces.md`](product-surfaces.md).** Same tokens, different register: density and familiarity over expression, 150–250ms state-only motion, one font family, Restrained colour floor. Marketing references (hero-enrichment, macrostructures, structure, production-tells) do **not** load here |
| Section or layout, no other signal | `impeccable layout` | Spacing, rhythm, hierarchy |
| Accessibility pass | `ui-ux-pro-max` | 99-rule checklist. Craft only — never lets it set visual direction |
| Review against external guidelines | `web-design-guidelines` | Vercel interface guidelines |

**Never routed to at Tiers 0–2:** `minimalist-ui`, `industrial-brutalist-ui`, `high-end-visual-design`. See [`gates.md`](gates.md) gate 60.

---

## Detection

```json
{
  "version": 1,
  "rules": [
    { "id": "nav",        "skill": "animated-navigation",             "why": "nav/header/menu",
      "path": ["nav", "header", "navbar", "menu", "topbar", "sidebar"],
      "code": ["<nav", "role=\"navigation\"", "NavigationMenu", "DropdownMenu", "MobileMenu"] },

    { "id": "interaction", "skill": "emil-design-eng",                "why": "interactive component or gesture",
      "path": ["button", "modal", "drawer", "popover", "tooltip", "toast", "sheet", "accordion", "dialog", "snackbar"],
      "code": ["onDrag", "onSwipe", "draggable", "useGesture", "framer-motion", ":active", "data-state=\"open\"",
               "transition:", "animate=", "@keyframes", "cubic-bezier", "transform-origin"] },

    { "id": "carousel",   "skill": "slideshow",                       "why": "carousel/slider/gallery",
      "path": ["carousel", "slider", "gallery", "swiper"],
      "code": ["embla", "keen-slider", "swiper", "scrollSnapType", "scroll-snap-type"] },

    { "id": "transition", "skill": "vercel-react-view-transitions",   "why": "route or state transition",
      "path": [],
      "code": ["startViewTransition", "<ViewTransition", "addTransitionType", "view-transition-name"] },

    { "id": "shadcn",     "skill": "shadcn-ui",                       "why": "shadcn primitive",
      "path": ["components/ui/"],
      "code": ["@/components/ui/", "cva(", "cn(", "@radix-ui/"] },

    { "id": "dataviz",    "skill": "dataviz",                         "why": "chart or KPI",
      "path": ["chart", "graph", "metric", "kpi", "dashboard", "stat"],
      "code": ["recharts", "d3", "victory", "visx", "<ResponsiveContainer", "chartjs", "plotly"] },

    { "id": "imagery",    "skill": "imagegen-frontend-web",           "why": "imagery-led section where the image does not exist yet — never for material already vendored under assets/",
      "path": ["hero", "gallery", "showcase"],
      "not_path": ["assets/", "credits.json"],
      "code": ["src=\"\"", "src={undefined}", "TODO: image", "placeholder-image"] },

    { "id": "form",       "skill": "impeccable harden",               "why": "form — 8 states required",
      "path": ["form", "input", "field", "checkout", "signup", "login", "contact"],
      "code": ["<form", "<input", "<select", "<textarea", "react-hook-form", "zodResolver", "onSubmit"] },

    { "id": "react",      "skill": "react-components",                "why": "React component structure",
      "path": ["components/"],
      "code": ["export function", "export default function", "useState", "useReducer"] },

    { "id": "next",       "skill": "next-best-practices",             "why": "Next.js surface",
      "path": ["app/", "pages/"],
      "code": ["\"use client\"", "'use client'", "generateMetadata", "async function Page"] },

    { "id": "copy",       "skill": "copy-gate",                       "why": "user-facing string",
      "path": [],
      "code": [">[A-ZÅÄÖ][a-zåäö]{3,}", "title=\"", "placeholder=\"", "aria-label=\"", "alt=\""],
      "regex": true },

    { "id": "landing",    "skill": "design-taste-frontend",            "why": "landing/marketing/portfolio page",
      "path": ["landing", "marketing", "portfolio"],
      "code": ["<Hero", "<Pricing", "<Testimonial", "<FAQ", "<CTA", "<LogoWall", "<FeatureGrid"] },

    { "id": "product",    "skill": "impeccable operate",               "why": "product surface — Operate mode, not marketing taste",
      "path": ["dashboard", "admin", "settings", "console", "portal", "workspace",
               "(app)", "app/(", "account", "billing", "onboarding", "table", "datagrid",
               "editor", "inbox", "analytics"],
      "code": ["<Sidebar", "<DataTable", "<TableHead", "useReactTable", "AgGrid",
               "<CommandDialog", "<Skeleton", "role=\"grid\"", "aria-sort",
               "<Tabs", "<Breadcrumb", "getServerSession", "<Toolbar"] },

    { "id": "scroll",     "skill": "design",                          "why": "scroll choreography — Step 2b: scroll/devices.md + feel-and-fingerprint.md",
      "path": [],
      "code": ["data-sc-", "animation-timeline", "scroll-timeline", "scrollY", "IntersectionObserver",
               "position: sticky", "position:sticky", "requestAnimationFrame"] },

    { "id": "generation", "skill": "design",                          "why": "generated material — references/generation.md owns the model route, the credit gate and the provenance stamp",
      "path": ["assets/", "credits.json", "frames/", "higgsfield"],
      "code": ["<video", "data-sc-clip", ".mp4", "poster=", "generated:"] },

    { "id": "perf",       "skill": "design",                          "why": "performance surface — references/performance.md (budget, gate 93)",
      "path": [],
      "code": ["will-change", "backdrop-filter", "filter:", "@font-face", "<iframe", "loading=\"lazy\"", "fetchpriority"] },

    { "id": "gsap-core",  "skill": "gsap-core",                        "why": "GSAP animation API written",
      "path": [],
      "code": ["gsap\\.|ScrollTrigger|new Lenis|SplitText"],
      "regex": true },

    { "id": "gsap-scrolltrigger", "skill": "gsap-scrolltrigger",       "why": "GSAP/ScrollTrigger/Lenis scroll-driven motion",
      "path": [],
      "code": ["gsap\\.|ScrollTrigger|new Lenis|SplitText"],
      "regex": true },

    { "id": "gsap-lenis", "skill": "lenis",                            "why": "GSAP/ScrollTrigger/Lenis scroll-driven motion",
      "path": [],
      "code": ["gsap\\.|ScrollTrigger|new Lenis|SplitText"],
      "regex": true },

    { "id": "spring-arrival", "skill": "spring-arrival",              "why": "a surface entering on scroll — Antons fjäder 0.66/0.95, en ruta i taget, texten efter landningen (F-030, F-031)",
      "path": [],
      "code": ["spring(", "data-case-box", "data-case", "caseEntry", "case:landed"] },

    { "id": "live-text",  "skill": "live-text-reveal",                "why": "agent text or a headline written live — takt, markör, sr-only, ingen reduced-motion-spärr (F-033, F-038)",
      "path": ["LiveText", "skrivs"],
      "code": ["skrivFram(", "live-caret", "hero-caret", "typewriter", "typed-text", "HeroText"] },

    { "id": "count-up",   "skill": "count-up-in-view",                "why": "a number counting up — startar först helt i bild, 2,6 s, kvadratisk (F-039)",
      "path": [],
      "code": ["RaknaUpp", "data-sc-count", "countUp", "CountUp", "count-up", "odometer", "toFixed(decimaler)"] },

    { "id": "hero-photo", "skill": "hero-on-photo",                   "why": "display type on a photograph — ingen skugga, bandet mätt 4,5:1, ett betonat ord i ljus accent (F-032, F-034)",
      "path": [],
      "code": ["hero-scrim", "hero-band", "hero-lede", "data-mo=\"hero"] },

    { "id": "photo-whole", "skill": "photo-stands-whole",             "why": "a clip reveal or parallax near a photo — foton står hela, bara drift i ramen (F-035)",
      "path": [],
      "code": ["data-parallax", "clipPath:", "clip-path: inset", "clipPath: \"inset"] },

    { "id": "showcase-surface", "skill": "showcase-surfaces",         "why": "a constructed product surface — aldrig skärmdump, fyller rutan på desktop (F-036)",
      "path": ["ProduktBilder", "showcase", "Showcase"],
      "code": ["case-zoom", "exempeldata", "data-hole"] },

    { "id": "showcase-copy", "skill": "showcase-copy-scope",          "why": "copy a customer reads in a demo or shared per product — korta motiveringar, inga referenser, varianter per produkt (F-033, F-037)",
      "path": ["marketing/copy", "copy-sections", "lib/data/emails", "email-studio", "textkvalitet"],
      "code": ["utanReferenser", "motivering", "varforSnajp", "varforSupport"] },

    { "id": "motion-review", "skill": "review-animations",            "why": "motion written — emil-design-eng builds it, review-animations grades it (both must be invoked by name)",
      "path": [],
      "code": ["rotateY", "rotateX", "clip-path", "--sc-p", "--sc-ps", "transform-origin", "@keyframes", "transition:"] },

    { "id": "a11y",       "skill": "a11y-audit",                      "why": "interactive or media surface — the audit is invoked by name, never approximated",
      "path": [],
      "code": ["<iframe", "<video", "<button", "<a ", "aria-", "tabindex", "role=\""] },

    { "id": "catalogue",  "skill": "design-catalog",                  "why": "brief or lock being written — the catalogue owns selection (Step 0)",
      "path": ["BRIEF.md", "reference-lock", "concepts.md"],
      "code": [] },

    { "id": "layout",     "skill": "impeccable",                      "why": "layout, no other signal",
      "path": [],
      "code": [],
      "fallback": true }
  ],
  "ui_extensions": [".tsx", ".jsx", ".ts", ".js", ".vue", ".svelte", ".astro", ".html", ".css", ".scss", ".sass", ".less"],
  "trap_hexes": {
    "minimalist-ui": ["#F7F6F3","#FBFBFA","#F9F9F8","#EAEAEA","#111111","#2F3437","#787774","#333333","#FDEBEC","#E1F3FE","#EDF3EC","#FBF3DB","#9F2F2D","#1F6C9F","#346538","#956400"],
    "industrial-brutalist-ui": ["#F4F4F0","#EAE8E3","#050505","#0A0A0A","#121212","#E61919","#FF2A2A","#4AF626"],
    "high-end-visual-design": ["#050505","#FDFBF7"]
  }
}
```

**Matching:** a rule fires when any `path` fragment appears in the file path (case-insensitive) **or** any `code` fragment appears in the written content. Multiple rules may fire — emit all of them, most specific first. `fallback: true` fires only when nothing else does. The `copy` rule always fires alongside whatever else matched; it never suppresses another route.

**Output shape.** One line per route, no prose:

```
→ emil-design-eng (drawer + drag detected)
→ copy-gate (3 new user-facing strings)
```

---

## Scope beats signal

A route names the skill for **craft on that component**. It never re-opens the direction.

- A drawer in a Tier-0 project routes to `emil-design-eng` for its motion. It uses the locked tokens. `emil-design-eng` does not pick its colours.
- A chart routes to `dataviz` for form and legend rules. Its categorical palette derives from the locked accent, not from `dataviz`'s placeholder palette.
- A hero routes to `imagegen-frontend-web` for real imagery. The imagery serves the derived world.

If a routed skill's guidance conflicts with the locked system, **the locked system wins** and you say so in one line rather than splitting the difference.

---

## Telemetry

Every route is logged so the router can be evaluated instead of assumed.

Ledger: `.impeccable/design-session.jsonl`, append-only, one object per line.

```jsonc
{"ts":"…","event":"edit|route|skill|gate-deny|gate-pass|copy-flag|verify|trap",
 "file":"…","component":"…","signal":"…","skill":"…","tier":"…","detail":"…"}
```

- `design-route.py` → `edit` and `route`
- `design-telemetry.py` → `skill`, correlated to the most recent `edit`, so every skill call is attributed to a component
- `design-gate.py` → `gate-deny` / `gate-pass` with the rule id, and `trap` on any `trap_hexes` match
- `design-verify-gate.py` → `verify`

`design-stop.py` renders `.impeccable/design-report-<date>.md`:

1. **Component → skills, in order** — did the right skill fire on the right component
2. **Route-vs-invocation gap** — every `route` with no matching `skill`. The router said load X and nothing loaded. **This number must be zero**; it is the direct measurement of the failure this system was built to fix
3. **Coverage** — UI files edited with no route at all
4. **Gate activity** — denials by rule id, with retry outcome
5. **Trap firings** — which demoted skill's hex, which file, caught pre- or post-write
6. **Timeline** — the full ordered sequence, so drift traces to the edit where it began

A build that looks right but ships an empty or gap-heavy ledger has not passed. It got lucky, and there is no way to tell which.
