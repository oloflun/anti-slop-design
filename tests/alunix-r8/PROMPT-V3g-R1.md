Du är byggaren för Alunix {{KONCEPT}}, runda 1. Designkedjan är PÅSLAGEN i den här sessionen
(hookarna, referensgolvet, ruttledgern). Det är själva provet: kedjan ska ge minst V3f:s nivå
med de nya verktygen inbyggda. Följ varje nekning från hookarna, arbeta dig förbi den genom att
göra det den kräver, och notera den i rapporten. Kringgå ingenting.

Arbetsmapp: `{{UT_MAPP}}` (en kopia av V3f). Uppdraget står i `{{UT_MAPP}}/SHOWCASE-SPEC.md`.
Läs den först, hela. Bara `#exempelcase` → `#showcase` ändras; allt annat på sidan är orört.

## Kedjan, i den här ordningen, före första kodraden

1. `Skill(design)` (plugin: `anti-slop-design:design`). Gör det referensgolvet kräver:
   - läs `design-catalogue/TASTE.md` och `FEEDBACK.md`;
   - kör `python scripts/catalogue/select.py --brief {{UT_MAPP}}/SHOWCASE-SPEC.md --k 4`, läs de
     valda posternas `entry.md` och deras `fold.webp` som bild;
   - läs `references/reference-lock.md`, `references/scroll/devices.md` (§ The engine: GSAP +
     Lenis) och `references/scroll/feel-and-fingerprint.md`, samt `references/motion.md`
     § Choreography per section.
2. Inspo, enligt `references/inspo-mcp.md`, men med litet budget eftersom formen redan är
   bestämd:
   - en `search_screens` på formproblemet: "sticky text column that crossfades step by step
     beside a scrolling product view";
   - en `get_screen` på den bästa träffen, där fullsidan hämtas och läses som bild.
   - Notera vad du lånar, eller att du inte lånar något och varför.
3. Motorns skills, i ordning: `lenis` → `gsap-core` → `gsap-scrolltrigger` → `gsap-timeline` →
   `gsap-performance`.
4. UI-skills (`mcp__ui-skills__get_skill`): `ibelick/fixing-motion-performance` och
   `zeke/swiss-design`.

## Bygget

Implementera SHOWCASE-SPEC.md punkt A, B och C.
- Behåll vendor-filerna i `{{UT_MAPP}}/assets/vendor/`, som redan är identiska med
  `~/.agents/skills/design/scripts/motion/vendor/`.
- Ingen ny synlig copy. Allt som inte är copy ska vara `aria-hidden`.

## Verifiering: SHOWCASE-SPEC.md § D, hela

Server: `python "C:/Users/Anton L/.agents/skills/design/scripts/serve.py" --port {{PORT}} --root .`
från repots rot, i bakgrunden. Stoppa den när du är klar. URL:
`http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html`.

- `showcase_probe.py` finns i `tests/alunix-r8/`. Kör den headed på 1440 och på 390 till
  `{{UT_MAPP}}/shots/probe-r1-1440` och `-390`.
- Baslinjen ligger i `tests/alunix-r8/runs/V3f/shots/probe-baseline-*/result.json`:
  - 1440 klick: p95 33,4 ms, största scrollY-hopp 358 px;
  - 1440 genom: p95 50,3 ms, max iframe-delta 949 px, 1 stall-then-lurch;
  - 390 klick: p95 50 ms, genom: p95 66,6 ms.
- `verify_motion.py` och `verify.py` i `{{UT_MAPP}}` är redan pekade på V3g. Ändra
  `verify_motion.py` där dess showcase-kontroll förutsätter dragspelets rader.
- Läs dina egna skärmbilder (proben ger `sheet.png` och `click-*.png`) innan du rapporterar.

## Rapport

Skriv `{{UT_MAPP}}/RAPPORT.md`:
- varje kedjesteg ovan med vad det gav, eller att det inte gav något;
- varje hooknekning och hur den löstes;
- siffrorna före och efter i en tabell;
- vad i specen du avvek från och varför;
- vad som återstår.

Ingen commit.
