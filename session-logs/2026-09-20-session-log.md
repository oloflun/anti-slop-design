# Session Log — 2026-09-20

## Session Summary

Alunix-landningssidans V3d-variant drevs från runda 21 till runda 23. Rundorna 22 och 23
byggdes och granskades; runda 23 levererade alla nio punkter i Antons beställning (processtexten
till vänster om ritningen, ny övergång med stämpelruta, Exempelcase nedskalat, prissektionen utan
Young Serif, egen kontaktsektion med formulär) men nådde inte nivån, och Anton lämnade ny feedback
som är dokumenterad i en handoff till nästa agent. Tre verktygsfel som tyst förstört mätningar och
granskningar i flera rundor hittades och åtgärdades: boardserverns saknade cache-rubriker,
oregistrerade custom properties som ger `NaN`, och förhandsvisningslägen som siktar på ett utgånget
scrollfönster.

## What Changed

### Files Created
- `tests/alunix-r8/runs/V3d/HANDOFF-2026-09-20.md` — handoff till nästa agent: transkriptets sökväg, Antons feedback bild för bild, de tre mätfällorna, och sex metodinsikter som ska porteras till designsystemet.
- `tests/alunix-r8/astra.py` — skickar bilder plus prompt rakt till `codex exec` och skriver svaret till fil. Ersätter wrapper-agenten som kostade 305 000 tokens per granskning för ett enda Codex-anrop.
- `tests/alunix-r8/PROMPT-V3d-R22.md`, `PROMPT-V3d-R23.md`, `PROMPT-V3d-R24.md` — byggprompter. R24 är oskriven i bygget och väntar på att utökas med Antons senaste feedback.
- `tests/alunix-r8/runs/V3d/plans/067-vanstertext-case-pris-kontakt.md` — arkitektens plan, åtta steg med mätbara mål per bredd. Skriven till disk av lead sedan planeringsagenten visat sig sakna skrivrättigheter.
- `tests/alunix-r8/runs/V3d/PARITET-067.md` — omskrivna och nya paritetsrader (P01, P04, P07–P13, P14, P15, P16, P17, P19, P21 omskrivna; P24 och P25 nya).
- `tests/alunix-r8/runs/V3d/COPY-V3d-r23.md` — sju processteg om 35–44 ord, ny case-ingress, kontaktsektionens strängar. Copy-kedjan körd i full ordning med humanizer-svenska sist.
- `tests/alunix-r8/runs/V3d/reviews/r22-astra.md`, `r23-astra-estetik.md` — granskningar. Den senare är den första estetiska i projektet och den mest värdefulla.
- `tests/alunix-r8/runs/V3d/shots/lead-r22/`, `lead-r23/` — egna mätskript (`col.py`, `wheel.py`, `wheelink.py`, `cap.py`) och bevisbilder.

### Files Modified
- `tests/alunix-r8/runs/V3d/index.html` — rundorna 22 och 23. R22: konturen sluter sig om arkets fyra sidor, slutrektangeln landar rätt. R23: alla nio beställda punkter.
- `~/.agents/skills/design/scripts/board.py` och `skills/design/scripts/board.py` — `Cache-Control: no-store, must-revalidate`. Servern skickade tidigare bara `Last-Modified`, vilket gjorde att webbläsare visade en tidigare runda utan att revalidera.
- `design-catalogue/FEEDBACK.md` — F-018 tillagd: sidan får aldrig berätta vad den strax ska göra.
- `skills/design/references/anti-patterns.md` — ny underrubrik § The page narrating itself.
- `skills/design/references/production-tells.md`, `gates.md`, `copy-gate.md` — gate 99 utvidgad till brödtextstorlek, som skannern inte kan se.
- `tests/alunix-r8/PRODUCT.md` — två lås hävda för V3d på Antons beslut: `.hero-sub`-strängen och förbudet mot formulär. Låst copy räknar nu 11 rader i V3d.
- `tests/alunix-r8/runs/V3d/NOTES.md`, `COPY-GATE.md` — rundornas anteckningar.

### Files Moved/Deleted
- Skärmbilder från rundorna 1–20 i `runs/V3d/shots/` och `runs/V3c/shots/` raderade efter Antons uttryckliga godkännande (alternativ 2). **Alla 128 mätskript och referensbaslinjen `runs/V3c/shots/fasA/` behölls.** Frigjorde 2,7 GB.
- `AppData/Local/Temp` (äldre än ett dygn, utom sessionens egen mapp) och npm-cachen rensade. Totalt 5,1 GB fritt på en disk som låg på 185 MB.

## Decisions Made

- **Astra/Codex används som estetisk kritiker, inte bara funktionsgranskare** — Anton bad uttryckligen om det. Granskaren fick ramen "kunden har rätt per definition, ta reda på vad du missade" och levererade projektets bästa granskning, inklusive ett erkännande i klartext: den hade mätt formens area och tagit den för närvaro. Ska porteras som ett `mode: aesthetic` i `agents/codex-review.md`.
- **Codex körs direkt, inte via wrapper-agent** — wrappern kostade 305 000 Opus-tokens per runda för ett Codex-anrop på 6,3 kB. `astra.py` ger samma dom till nästan ingen kostnad på veckokvoten.
- **Young Serif tas bort helt** — användes på ett ord efter att prissektionen bytt snitt, och kostade sidans enda tredjepartsanrop plus en fjärde typsnittsfil mot budget tre. Öppen post stängd.
- **Prisrubriken sätts i Geist 700, inte fet Public Sans** — Anton bad om brödtextens snitt med fetstil på rubriken, men Public Sans finns i en vikt (300) i repot, så fet blir syntetisk, vilket är en renderingsdefekt. Avvikelsen från hans ordalydelse flaggades och godtogs.
- **Arkets 1440-regression accepterad** — tvåspaltsakten ger 68,8 % vw vid 1920 (upp från 63,4) men 67,8 % vid 1440 (ned från 81,1). Aritmetiken tillåter inte mer med en textspalt bredvid, och tvåspalten är Antons order.
- **Formuläret ljuger inte om sin backend** — submit öppnar ett förberett mejl i besökarens egen klient. Alternativen var ett formulär som tyst inte skickar eller en falsk kvittens.
- **Runda 23 kallas inte klar** — bygget gick igenom men § Verification kördes aldrig (full disk). Ett bygge vars bilder ingen sett rapporteras inte som färdigt.

## Context & Discussion

- **Antons dom över R23:** alla punkter gjorda, men *"resten av ändringarna motsvarade inte riktigt heller mina förväntningar även om de utfördes på papper."* Avbockade punkter är inte samma sak som nådd nivå.
- **Case-ingressen underkändes för andra gången.** Jag skrev F-018-regeln den här sessionen och bröt den sedan i nästa mening jag levererade: "Vi har ingen husstil… och därför valde vi de två projekt som ligger längst ifrån varandra" förklarar fortfarande sidans eget urval. Ingen frågar varför just de exemplen finns på sidan. Regeln behöver ett mekaniskt prov, inte bara prosa.
- **Anton granskade gammal kod minst två gånger** på grund av boardserverns cachning, och trodde rimligen att ingenting byggts. Jag verifierade först bytes över HTTP och rapporterade att ändringarna fanns — fel kontroll. Rätt kontroll var att rendera sidan och titta.
- **Planeringsagenter (`subagent_type: Plan`) saknar skrivrättigheter.** Arkitekten rapporterade en komplett plan tre gånger utan att kunna spara den, och sa det först när jag uttryckligen bad om filerna.
- **Fable-kvoten tog slut** mitt i sessionen; arkitekten kördes på Opus enligt Antons regel.
- **Disken var full** (185 MB av 237 GB) och stoppade R23:s verifiering. Byggaren upptäckte `ENOSPC`, kontrollerade att filen var oskadad och slutade skriva bilder i stället för att fortsätta — rätt beslut.

## Open Threads

- **Runda 24 ska köras när veckokvoten återställs (onsdag 23/9).** `PROMPT-V3d-R24.md` finns med fyra uppmätta fel men måste utökas med Antons senaste feedback ur handoffen innan den körs.
- **Plan 067 § Verification A/B/C har aldrig körts.** Den skulden måste betalas innan R23 plus R24 kan kallas klara.
- **Sex metodinsikter ligger bara i handoffen och i transkriptet** och ska porteras till designsystemet: estetiskt granskningsläge, direktanrop av Codex, F-018:s mekaniska prov, cachningsregeln för granskningsytor, kontrollen att planer faktiskt ligger på disk, och regeln att rendera i stället för att greppa.
- **Obesvarad fråga till Anton, ställd tre gånger:** skriver och fotograferar Alunix åt kunden, eller bearbetas bara det kunden lämnar? Steg 05 i processen står i den försiktiga formen tills svar.
- **`AppData/Local/hermes` (6 GB) ska arkiveras, inte raderas**, enligt Antons egen avvecklingsplan. Utrymmet frigörs först när det flyttas till annan enhet.
- **Designsystemets ändringar är inte committade** i super-intelligence-paketet.

## Cross-Project Handoffs

None this session. Handoffen `tests/alunix-r8/runs/V3d/HANDOFF-2026-09-20.md` är intern till
Alunix-arbetet och riktar sig till nästa agent i samma projekt.

## Current State After This Session

V3d är byggd med allt Anton beställt och renderar korrekt, men övergången från den blå sektionen
till ritningen, processektionernas täthet, case-övergången och case-ingressen håller inte nivån.
Nästa session läser handoffen och råtranskriptet, utökar R24-prompten med Antons feedback, kör
copy-kedjan för kortare processtexter i hans egen ton, bygger, och kör därefter hela plan 067:s
verifiering som aldrig blev av. Veckokvoten är slut till onsdag; disken har 5,1 GB fritt.

<!-- session-state
date: 2026-09-20
type: design-iteration
files_created:
  - tests/alunix-r8/runs/V3d/HANDOFF-2026-09-20.md
  - tests/alunix-r8/astra.py
  - tests/alunix-r8/PROMPT-V3d-R22.md
  - tests/alunix-r8/PROMPT-V3d-R23.md
  - tests/alunix-r8/PROMPT-V3d-R24.md
  - tests/alunix-r8/runs/V3d/plans/067-vanstertext-case-pris-kontakt.md
  - tests/alunix-r8/runs/V3d/PARITET-067.md
  - tests/alunix-r8/runs/V3d/COPY-V3d-r23.md
  - tests/alunix-r8/runs/V3d/reviews/r22-astra.md
  - tests/alunix-r8/runs/V3d/reviews/r23-astra-estetik.md
files_modified:
  - tests/alunix-r8/runs/V3d/index.html
  - skills/design/scripts/board.py
  - design-catalogue/FEEDBACK.md
  - skills/design/references/anti-patterns.md
  - skills/design/references/production-tells.md
  - skills/design/references/gates.md
  - skills/design/references/copy-gate.md
  - tests/alunix-r8/PRODUCT.md
decisions_made: 7
open_threads: 6
handoffs_pending: []
priority_changes: true
status_updated: true
goals_updated: "skipped -- iteration inom befintligt delmal, malbilden orord"
next_session_focus: "Las HANDOFF-2026-09-20.md och rataranskriptet, utoka PROMPT-V3d-R24.md med Antons feedback, kor rundan och darefter plan 067 § Verification"
session-state -->
