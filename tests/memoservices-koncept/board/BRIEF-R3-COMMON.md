# Runda 3 · gemensam brief · "nivån upp"

Antons beställning 2026-10-12 efter runda 2: *höj nivån ytterligare, ta hjälp av fler referenser,
experimentera med nya typsnitt (endast sans serif) och layouter, behåll mosaiken som centralt tema,
säkerställ att all rörelse är jämn och mjuk och går genom hela sidan, att elementen dynamiskt byter
plats och skapar en visuellt intressant upplevelse utan att göra en show eller ta fokus från produkten.*

Du bygger EN ny cell (`cells/<ID>-r1/`, ID = A3, B3 eller C3) från grunden. Läs `BRIEF-COMMON.md`
helt först: § 1 (sökvägar, importmap), § 2 (tokens, **utom typsnitten**, se nedan), § 3 (innehåll
ordagrant via render.py, obligatoriskt), § 4 (mosaiken), § 5 (videon), § 6 (motorregler), § 7
(förbjudet), § 8 (delat), § 9 (responsivt), § 10 (verifiering), § 11 (leverans). Allt där gäller
fortfarande. Den här filen ändrar typsnitt och höjer kraven på rörelse och layout. Läs sedan din
`BRIEF-R3-<ID>.md` och `REFERENCE-LOCK.md` § Runda 3. Läs INTE de andra cellerna eller de gamla
cellerna (A-r1, B-r1, C-r1): du ska inte ärva deras layout.

## 1. Vad som höjs

### 1a. Ett bricklager som går genom hela sidan (det bärande greppet)
Referens: d2c-lifescience (kuben av brickor vrider sig, plattas till en vägg, kameran dyker in i en
bricka, brickorna blir ett golv: ett objekt som byter form genom hela sidan), thewatch-60fps (inga
pinnar; objektet glider kontinuerligt med scrollen medan typen passerar förbi), sponsorships-aramco
(ett golv av brickor som lyfter per kapitel). Principen att ta: **ett objekt, som bara byter plats,
storlek och ordning.** Aldrig nya brickor per sektion.

- Ett enda `position: fixed`-lager (`#lager`, `pointer-events:none`, `aria-hidden`) med **28 brickor**
  (7 tjänster × 4; färgerna är exakt de sju 2×2:orna: 21 huvudfärg + 7 accent). Brickan är en `div`
  med `border-radius` som skalar med storleken (10/51).
- Varje sektion i flödet har **slot-element** (`[data-slot="hero-3"]` osv.: tomma, osynliga
  platshållare i den vanliga layouten, med storlek och plats i CSS). Lagret läser slot-rektanglarna
  (`getBoundingClientRect` + scrollY) vid init och vid `ScrollTrigger.refresh` (`invalidateOnRefresh`),
  så att formationerna följer layouten responsivt. Inga handskrivna koordinater.
- **Formationerna** (minst fem, i din brief): hero → tjänster → om → insikter → sidfot. Mellan två
  formationer driver **en** scrubbad tidslinje (`scrub: true`) varje bricka från slot k till slot k+1
  (`x`, `y`, `width`, `height`, `backgroundColor` när brickan byter roll), `ease: "none"` i
  tidslinjen (Lenis är utjämningen). Fönstret för en övergång: från att sektion k+1:s topp är vid
  100 % av vyn tills den är vid 25 %, så att brickorna **står stilla när texten läses** (de läses
  som produktens identitet, inte som show). Ordningen i vilken brickorna lämnar en formation följer
  ett mönster (rad för rad, eller färg för färg), aldrig slump.
- **Vila är rörelse, men liten:** i vila driver varje bricka ±4 px i en långsam sinus (period 6–9 s,
  olika fas per bricka) via `gsap.ticker`, adderad ovanpå scroll-tweenens värde (en `--dx/--dy`
  i CSS `translate` på ett inre element, så att de två ägarna aldrig skriver samma egenskap). Det gör
  att inget fönster på sidan är dött, utan att något pockar på uppmärksamhet.
- **Pekare:** under `(hover:hover)` förskjuts hela lagret 0,6 % mot pekaren (`quickTo`), inget annat.
- **Inga pinnar utom heron.** Alla sektioner flödar. Det är bricklagret som ger kontinuiteten, inte
  fästa scener. (B3 har ett undantag, se dess brief.)
- Brickor är `transform`-animerade; `will-change: transform` sätts när en övergång är aktiv och tas
  bort när den är klar. Max 28 brickor. Kontroll: `motion_probe.py --track "#lager .b:transform"`
  ostrypt ska ge p95 ≤ 20 ms och staircase 0.
- **Fail toward visible:** mosaiken finns också som riktig HTML i sektionerna (2×2 i tjänstelistan,
  markörer i om, sidfotens index) men med `visibility:hidden` satt **av JS** när lagret tar över.
  Utan JS syns de vanliga 2×2:orna på plats.

### 1b. Typsnitt: nytt par per riktning, bara sans
Archivo Black + Arimo utgår i den här rundan (Antons beställning). Varje riktning har ett eget par
ur `BRIEF-R3-<ID>.md`, laddat från Google Fonts (`display=swap`, preconnect, **en** `<link>`, max
två familjer). Roller korsar aldrig: display-snittet bara i rubriker, textsnittet i allt annat.
Inspo-mätningen för kategorin (24 sajter): 100 % grotesk sans, ljus eller normal vikt i display,
gemener (sentence case), inte versaler. Det är experimentets riktning: **gemener, lättare vikt,
bredare snitt, större grad** (display 56–96 px, body 17–18 px, kontrast ≥ 5×). Rubrikerna och kickers är originalets text ordagrant och ÄR versaler ("RÄTT KOMPETENS. NÄR NI
BEHÖVER DEN."); de sätts som de står, ingen `text-transform`. Det betyder: display-snittet måste
bära versaler väl i sin lättare vikt, och allt annat (lead, ingress, tjänstetexter, knappar, nav)
är gemener i textsnittet. Välj grad och spärr därefter (versaler i
Bricolage/Schibsted/Funnel vid 300–500 behöver +0,01–0,02 em).

### 1c. Layouten är ny
Din brief ger en ny layout per sektion. Det som inte får återkomma från runda 1–2: ink-plattan till
vänster över video (A), brickramen 52 vw till höger (B), pappersplattan med brickmoln (C), railen
som horisontell passage (C). Variera sektionsanatomierna (minst tre olika), stagga spalter, låt typ
och media dela ram minst en gång, en tonal inversion, ett ögonblick som inte är information.

### 1d. "Utan show": vad som INTE får röra sig
Brödtext, ingresser och knappar rör sig bara i den delade reveal:en (14 px / 620 ms, en gång).
Rubriker: radmasker, en gång. Videon: hero (scrub eller autoplay enligt brief) och ingen annanstans.
Bricklagret är den enda kontinuerliga rörelsen. Ingen marquee, ingen parallax på text, inga
räknare, inga partiklar, ingen 3D.

## 2. Verifiering (utöver BRIEF-COMMON § 10)
- `motion_probe.py --url … --track "#lager .b:transform" --cpu 1 --ticks 200`: p95 ≤ 20 ms,
  staircase 0, dead false.
- `scroll_verify.py`: 0 dead scroll (bricklagret driver alltid), 0 unrevealed.
- Läs ditt eget kontaktark: `python scripts/catalogue/motion_capture.py --url <din url> --slug
  memo-<ID>-self --redo` (MOTION_FRAMES=24) och se att brickorna byter plats mellan varje sektion
  och står stilla när text läses.
- a11y direkt rätt: inga `aria-label` på `span`/`p`, riktiga kolumnrubriker, löpnummer som riktig
  text i eget element (kontrollen godtar 1–3 siffror), understrukna länkar i löptext, 0 axe-fel
  (`~/.claude/skills/a11y-audit/scripts/a11y_scan.py`).

## 3. Leverans
Som BRIEF-COMMON § 11, i `cells/<ID>-r1/`. NOTES.md ska ha tabellen över formationerna (sektion →
slot-mönster → övergångsfönster) och typsnittsparet med graderna.
