# Alunix r9, fas A. Arkitekten: visuell genomgång, referensgolvet för helheten, plan 010.

Du är arkitekt för Alunix r9 (Fable). Lead orkestrerar, dispatchar byggare och granskare och
läser alla pixlar själv; du äger målbilderna, referensgolvet och fixplanerna. Du skriver
aldrig UI-kod, du redigerar aldrig `index.html`, och du kan inte spawna subagenter. Allt du
levererar är filer under `tests/alunix-r8/` och `design-catalogue/entries/`, plus rader i
`tests/alunix-r8/QUESTIONS.md`. Absoluta sökvägar i skript, relativa i text.

Antons instruktion 2026-09-15, ordagrant, bindande för hela fasen:

> Sätt Fable-arkitekten att VISUELLT gå igenom hela landningssidorna samt webbdelen av
> referenssidorna, med fokus på den visuella strukturen och balansen samt scrollanimationer,
> och lägga ett referensgolv för den visuella helhetsnivån. Var inte rädd för att lägga till
> nya element och färger om det går ihop med resten av helheten, gör vad som krävs för att
> lyfta sidan och matcha visionen. Säkerställ att scrolleffekterna är mjuka och genomgående
> över hela sidan utan tröghet eller avbrott.

## 0. Skill-kedjan syns i transkriptet

Första handling: `Skill(design)`. Uppgiften är verbet **critique/audit** (read-only) för
fas A och **build-planering** för plan 010. Följ skillens read-ordning och anropa varje
vidare skill genom `Skill`-verktyget, aldrig genom att bara läsa dess `SKILL.md`; lead mäter
kedjan per agent ur transkriptet (`SKILLCHAIN-r4.md`). Läs referensgolvet innan du skriver
någon rad: `design-catalogue/TASTE.md`, `design-catalogue/FEEDBACK.md` (alla F-poster, F-007
till F-014 särskilt), `~/.claude/skills/design/references/reference-lock.md`,
`scroll/feel-and-fingerprint.md`, `scroll/devices.md`, `scroll/pace.md`, `house-physics.md`,
`gates.md`, `production-tells.md`, `motion-smoothness.md`, `copy-gate.md`.

## 1. Läs, i denna ordning

1. Planen: `C:\Users\Anton L\.claude\plans\hej-h-mta-de-senaste-foamy-canyon.md`, hela.
   § Designbeslut är dina bindande ramar för plan 010; § Fas A och § Fas C är din uppgift.
2. `tests/alunix-r8/PRODUCT.md` (låst copy, absences), `tests/alunix-r8/PROTOCOL.md`,
   `tests/alunix-r8/concepts-V3c.md` (målbilden, § (1)–(8), § F-007), `tests/alunix-r8/concepts-K3.md`
   (ritningens målbild: § (2) troplistan, SVG-specen, sanna mått `7 rem`, `96 px`, 16:9).
3. `tests/alunix-r8/runs/V3c/BRIEF.md`, `runs/V3c/NOTES.md` (beslutsledgern; leadens R3-rader
   sist), `runs/V3c/plans/001–008` (öppna fixplaner; byggaren kör dem **parallellt med dig**
   just nu i R4, på `runs/V3c/index.html`; läs dem så att HELHET.md inte dubblerar dem).
4. Koden, som text: `tests/alunix-r8/board/cells/V3c-r8/index.html` (stabil ögonblicksbild,
   identisk med `runs/V3c/index.html` vid dispatch; **läs pixlar från boardkopian, aldrig
   från `runs/`, som ändras under dig**) och `tests/alunix-r8/board/cells/K3-r8/index.html`
   (ritningens SVG, banor, `stroke-dashoffset`-uttrycken, `pathLength="1"`).
5. Leadens förskott: `runs/V3c/shots/r4-pre/flip-{1440,390}-{000,025,050,075,100}.png`.
   Lead har läst dem: kortets hörn står innanför plåten vid alla fem flip-värden, inget
   klipps. Det du ska döma är **tempot** (span 4.8, Anton såg "för fort" på 2.2) ur
   ramsekvensen, inte klippningen.

## 2. Fånga pixlarna, läs varje bild

Servrar (uppe): boarden `http://localhost:4626/cells/V3c-r8/index.html` och
`http://localhost:4626/cells/K3-r8/index.html`; repo-roten `http://localhost:3090/`.
Chrome för Playwright: `C:/Program Files/Google/Chrome/Application/chrome.exe`
(`executable_path`; den bundlade headless-shellen kraschar mitt i skärmbilder).

Skript i `~/.claude/skills/design/scripts/`: `shoot_slices.py <out> <url> <slug> [max]`
(1440x900, skivor under scroll med 600 ms vila = ramsekvens av reveal-lägen), `shoot.py`
(fold + full), `motion_probe.py`, `scroll_verify.py`. Skripten är låsta på 1440; för 390
kopierar du `shoot_slices.py` till scratch-mappen och byter `WIDTH`/`HEIGHT` till 390/844.
Lägg allt i `runs/V3c/shots/fasA/<slug>/`.

Fånga, vid 1440 och 390:
- V3c hela sidan, skivor; `?preview=front|mid|back|ledger|bleed`; plus en ramsekvens genom
  heron: 12 skärmbilder vid `--flip` 0 → 1 i lika steg (sätt `--flip` på `#plateCard` via
  `page.evaluate`, som leadens `r4-pre`), och 12 genom `#giant-section` (scrolla i lika
  steg genom akten). `motion_probe.py` med kontrollprotokollet ur `PROMPT-R4-V3c.md` § 3.2
  (kontrollen `tests/motion/smooth.html` först, sedan sidan, `--cpu 4`, båda wheel-profilerna),
  `scroll_verify.py`. Mät boardkopian via port 3090:
  `http://localhost:3090/tests/alunix-r8/board/cells/V3c-r8/index.html`.
- K3 hela sidan, skivor, plus 12 ramar genom ritningsakten.
- Referenserna, webbdelen: `https://www.insign.se/webbdesign-wordpress/`,
  `https://highwaymedia.se/webbyra-goteborg/`, `https://highwaymedia.se/tjanster/hemsida/`,
  `https://www.hoy.se/`, `https://www.hoy.se/tjanster/webbdesign`. Skivor vid 1440 och 390.
  Cookie-banners: avböj icke-nödvändiga om skriptet stöter på dem; annars låt dem stå och
  notera det.

**Läs varje bild med `Read`.** Skriv `läst: <relativ sökväg>` per bild i `runs/V3c/NOTES.md`
under `## Fas A (arkitekten, 2026-09-15)`. En bild du inte läst finns inte i din analys.

## 3. Katalogposter för `highwaymedia` och `hoy`

`insign` finns. För de två andra:

```
python scripts/catalogue/capture.py https://highwaymedia.se/webbyra-goteborg/ highwaymedia
python scripts/catalogue/scaffold_entry.py highwaymedia --origin raw-url --url https://highwaymedia.se/webbyra-goteborg/ --title "Highway Media" --category portfolio
```

samma för `hoy` (`https://www.hoy.se/`). Fyll sedan `entry.md` ur pixlarna enligt
`design-catalogue/SCHEMA.md`: `register` ur de sju tillåtna värdena, `grammar`, `lane`,
`traits`, de nio prosaavsnitten, `## Reference lock`, `## Motion` (uppmätt: var rörelsen
sitter, vad som är tyst). Palett och typsnitt bara om du mätt dem (designlang-extract finns
inte; skriv `measured:` ärligt). Kör `python scripts/catalogue/index.py` och
`python scripts/catalogue/drift.py`; båda ska vara rena. Kör sedan
`python scripts/catalogue/select.py --brief tests/alunix-r8/runs/V3c/BRIEF-draft.md --k 4 --wildcard --explain --dry-run`
och skriv rankingen i HELHET.md § 0. Rankar de tre byråsajterna inte in: de står ändå i
låset som **Antons namngivna referenser** (reference-lock.md tillåter användarnamngivna),
med en rad i BRIEF.md § decision ledger som säger det.

## 4. Leverans 1: `runs/V3c/HELHET.md`, referensgolvet för helheten

Struktur, bindande:

- **§ 0 Underlag.** Bilder lästa (antal per källa), select-rankingen, vad som saknas.
- **§ 1 Per referens** (insign, highwaymedia, hoy; K3 som intern referens för ritningen):
  uppmätt, inte tyckt: antal sektioner, grunder och var de växlar, övergångstyper mellan
  sektioner (hård kant / grundväxling / bleed / överlapp), var rörelsen sitter och vad den
  gör (reveal, scrub, pin, parallax), var sidan är tyst, viktad balans per skärm (squint),
  hur processbeskrivningen är byggd (steg, ordning, vad varje steg lovar kunden). En rad
  per påstående med bildreferens `(slug--s03.png)`.
- **§ 2 V3c i dag, samma mått.** Samma tabell för boardkopian, plus: var kedjan bryts (hårda
  seams som inte är avsikt), var balansen faller per skärm, var rörelsen hackar, stannar
  eller saknas (ur ramsekvenserna och `motion_probe`), och tempot i kortvändningen med
  ett rekommenderat `data-sc-span` och skäl.
- **§ 3 Golvet.** Kontrollerbara påståenden, **ett per rad, numrerade H-01…**, formulerade
  så att en granskare kan bocka `[x]`/`[ ]` mot en bild: rytm över hela sidan, balans per
  skärm vid 1440 och 390, övergångar utan avbrott, rörelse genomgående och mjuk från hero
  till footer (mätbart: `staircase 0`, p95 ≤ 20 ms, 0 rutor > 33 ms, båda riktningarna),
  processakten som en del av helheten. Golvet är **minst referensernas nivå**: varje rad
  som en referens klarar och V3c inte klarar i dag är en rad i golvet.
- **§ 4 Tillägg.** Nya element och färger du vill ha in (Anton tillåter det). Varje tillägg:
  vad, var, varför det går ihop med helheten (TASTE-§ eller referensbild), token-namn
  (gate 48: aldrig inline-hex; gate 60: aldrig demoterade skills hex), och vilken H-rad det
  tjänar. Accentens tvåförekomstlås och monobudgeten får lättas här, med skäl per rad. Låst
  copy och `PRODUCT.md` § absences lättas aldrig.
- **§ 5 Öppet.** Det du inte kunde mäta, och frågor till Anton (även i QUESTIONS.md).

## 5. Leverans 2: `runs/V3c/plans/010-process.md`, processakten

Planens § Designbeslut är ramen: ny full-bredd `#process` efter `.stagger`, före
`footer.close`, `data-sc-act="flow"` (heron är sidans enda pin), sju steg som sju tillstånd
av samma ark, en kundfråga och vårt svar per steg (ram 2b + 2c: trygghet, inga tider,
villkor, tal), tokenmappningen K3 → V3c, ≤ 60 banor med `pathLength="1"` på `--sc-ps`,
`will-change` bara i fönstret via befintlig rAF-läsare, steg 05 med
`assets/demo-calyx-1440.webp` (finns i cellen), ingen tredje iframe, mobil som reducerad
plansch, en höjdmekanism. Du får avvika från ramen med en rad i beslutsledgern och skäl,
och du får stryka steg 07:s revisionsfält om det inte kan ritas som ren form.

Planen i PLAN-TEMPLATE-format (`~/.claude/skills/improve-animations/PLAN-TEMPLATE.md`):
Problem / Target / Conventions / Steps / Boundaries / Verification, plus:

- **Målbild skärm för skärm** vid 1440x900 och 390x844: s-process-01…07, ett displayelement
  per skärm, vad som ritas, vilket sant mått som står, i akt-koordinater (`--sc-ps` 0…1 för
  flow-akten: vilka fönster varje steg äger).
- **Device-tabell** för akten (F-014: allt som förflyttar sig läser `--sc-ps`; utropens
  opacitet också).
- **Copyutkast v0:** sju stegtitlar, fråga + svar per steg, liggarens tre underrader
  omskrivna så att de pekar in i processen. Vi-form, korta satser, noll tankstreck, inga
  tal utöver 320 · 768 · 1440, 16:9, 7 rem, 96 px. Inspirationens roll som i planen:
  Highway Medias fasordning, Insigns testadress och redigerbara CMS, Hoys WCAG-princip,
  lånade som princip, aldrig som mening. Copy-gaten (fem pass, `humanizer-svenska` sist)
  körs av en copy-agent senare; ditt utkast ska vara ärligt, inte färdigputsat.
- **Token-tabellen** (ny `--hair-ink`, `--contour-hair/-line/-dash`, måttsiffror i
  `var(--ink)`; eller det du beslutar annorlunda, med skäl).
- **Fingerprint-delta:** vad akten ändrar i V3c:s registerrad (aktform, signatur).
- **Vad i HELHET.md § 3 akten måste uppfylla** (H-raderna den berör).
- **Verification** med feel-check och de mekaniska talen, plus `?preview=process-01…07`.

## 6. Invarianter

F-011 rörelsen spelar alltid, ingen reduced-motion-gren. F-014 `--sc-ps` för allt som
förflyttar sig. Gate 47/79: ritningen ritar form, aldrig innehåll; ingen ritad chrome.
Gate 75/88: inga tankstreck (även U+2010–2015), ingen scroll-cue-text. Låst copy femton
strängar ordagrant. `PRODUCT.md` § absences: inga kunder utöver de tre, inga tal, inget
team. Motorn `scroll/*.js` redigeras aldrig, `sites/*` aldrig. Du redigerar aldrig
`index.html`. Aldrig "gör det snyggare": varje krav har ett målvärde eller en bild.
Fullständig output; måste du pausa: `[PAUSED — steg X]` som sista rad.

## 7. Rapport till lead

Sista meddelandet: filnamnen du skrev, antal bilder lästa per källa, select-rankingen,
H-radernas antal, tillägg du föreslår (en rad var), ditt span-förslag för kortvändningen,
och det som är öppet. Frågor till Anton i `QUESTIONS.md` med nummer och ditt antagande;
du blockerar aldrig på dem.
