# KNJIGA: Jezik kao emergencija — od sustava i mreža do velikih jezičnih modela
### Prvi lejer — kostur knjige (v0.1, rujan 2026.)

> **Temelj:** predavanje *Elements of Cognition in Complex Language Systems* (IUC Dubrovnik, 11. 9. 2026.) + istraživačka linija autora: OMLCC (2018, 2019), disertacija o leksemu *strah* (2014), EmoCNet (2019–21), CGCN (Perak & Ban Kirigin 2023), Qwen3-Embedding eksperimenti (Syntagent/Spark).
> **Status:** prvi lejer (struktura + prošireni sadržaj). Sljedeći lejer: raspisivanje poglavlja u puni tekst (pilot = DIO I).

## 0. KONCEPT KNJIGE

**Radni naslov (opcije)**
1. **Jezik kao emergencija: od sustava i mreža do velikih jezičnih modela**
2. **Emergentni jezik i umjetna inteligencija: sustavi, značenje, modeli**
3. **Mišljenje kao procesiranje: jezik, vektorski prostor i novi entitet u sustavu**

**Ciljana publika**
- Studenti diplomskih studija lingvistike, kognitivne znanosti, digitalne humanistike i informacijskih znanosti (kolegijski udžbenik, 30–45 sati)
- Istraživači u korpusnoj/kognitivnoj lingvistici i semantici koji ulaze u rad s modelima i ugrađivanjima
- Filosofi jezika i kognitivni znanstvenici koje zanima emergencija i "novi entitet" u sustavu
- Praktičari (nastavnici, AI4LANG-i slični projekti) kojima treba teorijski okvir za ono što već rade s modelima

**Pozicioniranje**
- **Prva hrvatska knjiga** koja jezik i velike jezične modele smješta u **jedan formalni okvir — razine organizacije** — i iz njega izvodi istraživački program koji se može opovrgnuti
- **Komplement knjizi *Komunikacija u doba umjetne inteligencije* (Perak 2025):** ondje je fokus na komunikaciji i razvoju modela i komunikacijskih agenata; ovdje je fokus na **teoriji emergencije, značenju i metodama** — i na vlastitom modelu (OMLCC) kao okosnici
- **Razlika prema praktičnoj knjizi *Data Science u kulturi*:** ona uči *kako* raditi s podacima; ova objašnjava *zašto* značenje možemo čitati iz mreža i vektora, i gdje su granice tog čitanja
- Vlastiti empirijski materijal kao dokazna linija (mreže emocija, statički vs. kontekstualni prostori), a ne kao ilustracija
- Open access + otvoreni kod (GitHub: sve skripte, podaci i figure reproducibilne)

**Format**
- **~300 stranica** (16 poglavlja × 15–18 str. + uvod, zaključak i dodaci)
- Svako poglavlje: **teorijski okvir** (imenovani autori, koncepti, kritička perspektiva) + **metode** + **praktikum** (izvršiv kod, rubrika *"Što ako ne radi?"*) + **vježbe** 🟢🟡🏆 + **sažetak i ključni pojmovi** + **literatura**
- Figure u kvaliteti za tisak (300 dpi), preuzete i prerađene iz predavanja
- Izdanje: FFRI (Biblioteka Filozofskih fakulteta, open access) ili komercijalni izdavač — odluka u lejeru 2

**Ton**
- **Između priručnika i udžbenika** (default autora): udžbenička komponenta nosi pojmove i autore, priručnička nosi kod, postupke i "što ako ne radi"
- *Potvrditi u lejeru 2 (odluka se upisuje ovdje s datumom).*

## 1. STRUKTURA KNJIGE (4 dijela, 16 poglavlja) — okosnica: četiri pitanja
> Knjiga slijedi četiri pitanja iz predavanja: (1) što je emergentizam, (2) kako je jezik emergentan, (3) kako je model nastao iz vektorskog prostora, (4) kako se mišljenje događa kroz procesiranje. Svako poglavlje završava okvirom **"Kako bismo znali da griješimo"**.

**UVOD — Zašto emergencija?**
- Mapa knjige, četiri pitanja, četiri male figure (ljestve, mreža, prostor, petlja)
- Upozorenje: slaba emergencija, bez mistike; sve tvrdnje su opovrgljive

### DIO I — SUSTAVI I EMERGENTNOST (pogl. 1–4) — "Što je emergencija i kako je misliti precizno"
**Poglavlje 1: Sustavi, cjeline, organizacija** — ✅ postojeći materijal (predavanje 3–5)
- 1.1 Sustav nije hrpa: dijelovi, relacije, organizacija (von Bertalanffy, Anderson, Mitchell)
- 1.2 Slaba i jaka emergencija; emergencija u stupnjevima (Bedau, Chalmers, Emmeche)
- 1.3 Kako se emergencija mjeri: kauzalni testovi, intervencije, granice deskripcije
- 1.4 Vježbe 🟢🟡🏆

**Poglavlje 2: OMLCC — 16 razina ontološke složenosti** — ✅ (Perak, OMLCC (izlaganja 2017) + disertacija 2014)
- 2.1 Tri domene (materijalna, psihološka, društvena) — Searleova podjela; *brute / mental / institutional facts*
- 2.2 Šesnaest razina i relacijske sheme (perceiver, experiencer, cogitor) — kako su izvedene iz korpusa
- 2.3 Metodologija izgradnje modela odozdo prema gore (korpus → shema → razina)
- 2.4 Što model može, a što ne: ograde i falsifikabilnost
- 2.5 Vježbe: kodiranje primjera u OMLCC sheme 🟢🟡🏆

**Poglavlje 3: Od dijelova do strukture — tri koraka emergencije** — ✅ (predavanje 9 + Emmeche)
- 3.1 KORAK 1: dijelovi (entitet–relacija–entitet; morfosintaksa kao kodiranje uloga)
- 3.2 KORAK 2: mreža (stabilizacija relacija; svojstvo entiteta = položaj u mreži)
- 3.3 KORAK 3: novi entitet (mreža kao *jedan* entitet; nove relacije, nova imenovanja)
- 3.4 Isti potez, drugi supstrat: kako se ovo prenosi na model (najava DIO-a III)

**Poglavlje 4: Razine modela i razine jezičnoga opisa** — ✅ (predavanje 10)
- 4.1 Tokeni / obilježja / distrikti / sklopovi / planiranje
- 4.2 Morfologija / leksik / pojmovna polja / konstrukcije / diskurs
- 4.3 Mapiranje: što je informativno, a što dekorativno (i kako to testirati)
- 4.4 Kako bismo znali da griješimo (istraživački program)

### DIO II — JEZIK KAO EMERGENTNA POJAVA (pogl. 5–8) — "Značenje u relacijama"
**Poglavlje 5: Od Saussurea do distribucijske hipoteze** — ✅ (predavanje 11–12)
- 5.1 Pet definicija jezika i njihova neslaganja (Sapir, Bloch & Trager, Chomsky, Saussure, Firth)
- 5.2 Distribucijska hipoteza: Harris, Firth; kontekst kao značenje
- 5.3 Uporabna gramatika i konstrukcije (Croft, Goldberg)
- 5.4 Praktikum: prvi korpusni upit i prve ko-okurencije (Colab)

**Poglavlje 6: Konceptualne mreže i konstrukcijska gramatika** — ✅ (Perak & Ban Kirigin 2023 + CGCN)
- 6.1 Konstrukcijska gramatika kao mreža (form–meaning pairings)
- 6.2 Konceptualna mreža konstrukcija: metoda i kod
- 6.3 Mjere centralnosti i distrikti: kako se čita struktura iz mreže
- 6.4 Praktikum: izgradnja i vizualizacija mreže (NetworkX + Gephi)

**Poglavlje 7: Emocije kao mreža — studija slučaja *strah*** — ✅ (disertacija 2014, EmoCNet, predavanje 19)
- 7.1 Zašto emocije: apstraktno, kulturno uvjetovano, svakom govorniku poznato
- 7.2 Izgradnja mreže 125 hrvatskih emocionalnih leksema (hrWac, ko-okurencija, tvorba)
- 7.3 Čitanje rezultata: obitelji, distrikti, mostovi (*strah ↔ strahovati* 0,91)
- 7.4 Praktikum: od korpusa do mreže (korak po korak) + rubrika *"Što ako ne radi?"*
- 7.5 Kako bismo znali da griješimo: artefakti metode vs. struktura jezika

**Poglavlje 8: Semantički distrikti i kulturni modeli** — 🟡 djelomično (predavanje 13, 29)
- 8.1 Pojmovna polja i njihove granice; polisemija i gdje ona ne stanuje
- 8.2 Kulturno uvjetovane strukture: što se replicira preko jezika, a što ne
- 8.3 Mreža emocija kao kulturni artefakt (usporedba s drugim jezicima)
- 8.4 Vježbe: vlastita mini-mreža na odabranom leksičkom polju 🟡🏆

### DIO III — OD VEKTORSKOG PROSTORA DO MODELA (pogl. 9–12) — "Kako je model nastao i što je u njemu"
**Poglavlje 9: Ugrađivanje — od riječi do vektora** — ✅ (predavanje 14–15)
- 9.1 Ugrađivanje, pažnja, model, mišljenje: četiri definicije bez jednadžbi
- 9.2 Distribucijsko podrijetlo: word2vec, GloVe; jedna riječ — jedan vektor
- 9.3 Vektorska aritmetika: *king − man + woman ≈ queen* i što ona (ne) dokazuje
- 9.4 Praktikum: statički prostor na vlastitom leksiku (fastText cc.hr)

**Poglavlje 10: Kontekstualni obrat — pažnja, slojevi, predikcija** — ✅ (predavanje 16 + Qwen3 eksperimenti)
- 10.1 Transformer: reprezentacija se računa iz cijelog konteksta (Vaswani 2017)
- 10.2 Slojevi i mjesta: gdje u modelu živе koje informacije
- 10.3 Praktikum: Qwen3-Embedding-8B (4096-dim, vlastita infrastruktura) — poziv, evaluacija, zamke

**Poglavlje 11: Geometrija značenja na djelu — što se vidi, a što ne** — ✅ (predavanje 19–20)
- 11.1 Isti leksik u dva prostora: statički vs. kontekstualni (vlastiti rezultati)
- 11.2 Distrikti preživljavaju promjenu tehnologije — a što se gubi izvan konteksta
- 11.3 Metode: t-SNE, konveksne ljuske, prototipni labeli; što je artefakt metode
- 11.4 Iskrena granica: deskripcija vs. kauzalna intervencija

**Poglavlje 12: Skala, rezultati, kontekst — što se zapravo mijenjalo** — ✅ (predavanje 17–18, 21 + FlyWire)
- 12.1 Parametri, compute i kontekstni prozor: tri osi rasta (Kaplan, Chinchilla, 2026. praksa)
- 12.2 Rezultatske ljestvice i njihovi stropovi (GPQA, HLE) — i zašto "veličina" više nije ljestvica
- 12.3 Organizacija, ne veličina: ista lekcija iz drugog supstrata (139.255 neurona, 734 parametra — FlyWire/Lappalainen 2024)
- 12.4 Praktikum: kako provjeriti brojku o modelu prije nego je citiraš (Epoch, Thompson, primarni radovi)

### DIO IV — MIŠLJENJE, AGENTI, POSLJEDICE (pogl. 13–16) — "Kamo to vodi"
**Poglavlje 13: Mišljenje kao procesiranje** — ✅ (predavanje 23–24)
- 13.1 Petlja: kontekst → predikcija → kontekst (stanje se prepisuje, ne dohvaća)
- 13.2 Emergentna radna memorija: lanci mišljenja, samokorekcija, eksternalizacija
- 13.3 Vrijeme kao varijabla: koliko dugo model radi samostalno (METR horizonti)
- 13.4 Ljudska nagrada i rekurzivno samo-poboljšanje: što je unutarnja, a što vanjska petlja

**Poglavlje 14: Od modela do agenta — alati, memorija, djelovanje** — ✅ (predavanje 27–28)
- 14.1 Pet dodataka koji model pretvaraju u agenta (akcija, memorija, pretraga, orkestracija, interoperabilnost)
- 14.2 Protokoli kao društvena instalacija (MCP, A2A, AP2/x402)
- 14.3 Novi entitet u sustavu: kolaborator i potencijalni kompetitor za resurse (računanje, energija, podaci, pažnja, jurisdikcija)
- 14.4 Rad, autorstvo, odgovornost: pravna i etička pitanja bez patetike

**Poglavlje 15: Hoće li imati kulturu?** — ✅ (predavanje 29)
- 15.1 OMLCC razine 12–16 kod agenata: što se već vidi (imena, persone, protokoli, artefakti memorije)
- 15.2 Što nedostaje: norme reciprociteta, prepoznavanje namjera, statusne funkcije
- 15.3 Searle i kolektivna intencionalnost: gdje je tvrdnja, a gdje želja
- 15.4 Naslijeđeni kulturni model — i što bi značilo da ga naslijede drugačije

**Poglavlje 16: Što to znači za lingvistiku — i kako bismo znali da griješimo** — ✅ (predavanje 31 + AI4LANG)
- 16.1 Interpretabilnost kao novo empirijsko polje (mapiranje razina)
- 16.2 Korpusna interpretabilnost na hrvatskome i morfološki bogatim jezicima
- 16.3 Model nije informant: kauzalni testovi, ne konzultacije
- 16.4 Pet testova koje bi ovu knjigu trebalo oboriti (i gdje se izvode: AI4LANG)

**ZAKLJUČAK — Četiri odgovora i jedna posljedica** — ✅ (predavanje 32)
- 16.5 → zaključno mapiranje na četiri pitanja; što ostaje otvoreno

## 2. DODACI (A–F)
- **Dodatak A: Postavljanje okruženja** — Python/Colab, vlastiti embedding poslužitelj (Qwen3-Embedding-8B), Gephi, reproducibilnost
- **Dodatak B: Rječnik pojmova** — ✅ postoji (*definicije-pojmovi.md*, 28 natuknica s verificiranim citatima) → proširiti na ~60 natuknica
- **Dodatak C: Rješenja vježbi** (🟢🟡)
- **Dodatak D: Predlošci** — korpusni upit, evaluacija ugrađivanja, protokol kauzalnog testa, obrazac za mrežnu analizu
- **Dodatak E: Izvori, podaci i provjera brojki** — Epoch AI, LifeArchitect/Thompson, FlyWire, GPQA/HLE; pravilo: nijedna brojka bez primarnog izvora
- **Dodatak F: Prigovori i odgovori** — kineska soba, symbol grounding (Harnad), stohastički papige (Bender), antropomorfizam, "samo statistika"

## 3. STATUS SADRŽAJA

| Dio | Poglavlje | Status | Opseg |
|-----|-----------|--------|-------|
| — | Uvod | 🟡 iz predavanja 2 | 8–10 str |
| I | 1. Sustavi i emergencija | ✅ predavanje 3–5 | 15–18 str |
| I | 2. OMLCC 16 razina | ✅ Perak, OMLCC (2017) + disertacija 2014 | 18–22 str |
| I | 3. Tri koraka emergencije | ✅ predavanje 9 + Emmeche | 15–18 str |
| I | 4. Razine modela i jezika | ✅ predavanje 10 | 15–18 str |
| II | 5. Od Saussurea do Harrisa | ✅ predavanje 11–12 | 15–18 str |
| II | 6. Konceptualne mreže i KG | ✅ CGCN 2023 | 15–18 str |
| II | 7. Emocije kao mreža (*strah*) | ✅ disertacija + EmoCNet | 18–22 str |
| II | 8. Distrikti i kulturni modeli | 🟡 djelomično | 15–18 str |
| III | 9. Ugrađivanje | ✅ predavanje 14–15 | 15–18 str |
| III | 10. Kontekstualni obrat | ✅ predavanje 16 + Qwen3 | 15–18 str |
| III | 11. Geometrija na djelu | ✅ predavanje 19–20 + vlastiti podaci | 18–22 str |
| III | 12. Skala, rezultati, kontekst | ✅ predavanje 17–18, 21 + FlyWire | 15–18 str |
| IV | 13. Mišljenje kao procesiranje | ✅ predavanje 23–24 | 15–18 str |
| IV | 14. Od modela do agenta | ✅ predavanje 27–28 | 15–18 str |
| IV | 15. Hoće li imati kulturu? | ✅ predavanje 29 | 15–18 str |
| IV | 16. Što to znači za lingvistiku | ✅ predavanje 31 + AI4LANG | 15–18 str |
| — | Zaključak | ✅ predavanje 32 | 6–8 str |
| — | Dodaci A–F | 🟡 (B postoji) | 30–35 str |

**Ukupno procijenjeno: ~300 stranica** (≈ 290–330)
**Prednost ovog projekta:** ≈ 80 % sadržaja već postoji u obliku predavanja, radova i kodova — knjiga je uglavnom *proširivanje u prozu + pedagogija*, ne istraživanje od nule.

## 4. SLJEDEĆI KORACI (lejer 2)
1. **Odobriti strukturu** (naslov, dijelovi, poglavlja) i **ton** (priručnik / udžbenik / između)
2. **Pilot: DIO I (pogl. 1–3)** u puni tekst — potvrda tona i dubine prije pisanja ostaloga
3. **Odluka o izdanju:** FFRI Biblioteka (open access) ili komercijalni izdavač
4. **Jezik:** hrvatski (osnovno) + odluka o engleskom izdanju/poglavljima
5. **Repozitorij:** `github.com/bperak/<knjiga>` — kod, podaci, figure, build knjige
6. **Figure u kvaliteti za tisak** (300 dpi) + **dozvole** za tuđe figure (Thompson/LifeArchitect: citat ostaje)
7. **Recenzija:** 2 recenzenta; poglavlja 4, 11 i 16 su najosjetljivija (tvrdnje o mapiranju razina)
8. **Verifikacija koda** — svaki primjer izvršiv (Colab), s podacima u repozitoriju

## 5. POVEZNICE
- **Predavanje (izvor materijala):** IUC Dubrovnik 2026 — 35 slajdova, bilješke govora, audio, nacrt, definicije
- **Teorijska knjiga (prethodna):** *Komunikacija u doba umjetne inteligencije* (Perak 2025) — https://github.com/bperak/komunikacija_u_doba_ai
- **Praktična knjiga (u izradi):** *Data Science u kulturi* — https://github.com/bperak/dsk
- **Vlastiti radovi kao jezgra:** Perak 2014 (disertacija, *strah*) · Perak, OMLCC (izlaganja 2017) · Perak & Ban Kirigin 2023 (CGCN) · EmoCNet 2019–21

---

# 6. VARIJANTA B — "RAZINE + AI" (komunikacija kao nosiva razina)

> **Pitanje autora:** ako je knjiga više o **ontološkim razinama i AI-ju**, kako se u to uklapa **komunikacija**?

## 6.1 Tri odgovora (zašto komunikacija i AI *pripadaju* u knjigu o razinama)

**1) Komunikacija nije tema uz ontologiju — ona je jedan od njezinih nivoa.**
U OMLCC-u je komunikacija **razina 14 (SocCommunication)**, u društvenoj domeni (12–16). Knjiga o ontološkim razinama dakle *već sadrži* komunikaciju — ne kao poglavlje "dodatka", nego kao **poziciju u modelu**. Komunikacija prestaje biti tema i postaje *mjesto* u strukturi.

**2) Komunikacija je ujedno i metoda.**
Razine se ne čitaju iz glave, nego **iz komunikacijskih podataka**: korpusa, ko-okurencije, konstrukcija, mreža značenja. Komunikacija je istovremeno **objekt** (razina 14) i **instrument** (podaci iz kojih izvodimo sve ostale razine). To je razlog zašto knjiga o razinama *mora* imati komunikaciju u središtu, a ne na margini.

**3) AI ulazi kao novi entitet — ne kao nova razina.**
Model ne dodaje 17. razinu: on **zauzima postojeće razine u novom supstratu** (8 → informacijski, 9–11 → obrada, 14 → komunikacija, 15–16 → institucije i kulturni modeli). Zato je pravo pitanje: **što se mijenja na razini 14 kad se pojavi novi tip sudionika?** Iz toga slijedi cijeli DIO IV: prepoznavanje namjera, zajedničke obveze, konvencije, protokoli (MCP/A2A/AP2 kao komunikacijska infrastruktura), kolaborator/kompetitor, kultura.

**Zaključak dizajna:** dvije knjige se nadopunjuju bez ponavljanja:
- *Komunikacija u doba UI* (2025) = **povijest i praksa**: komunikacijske tehnologije → LLM → komunikacijski agenti
- **ova knjiga** = **ontološki smještaj**: razine 1–16, komunikacija kao razina 14, AI kao novi entitet koji u tu razinu ulazi

## 6.2 Struktura varijante B (4 dijela, 16 poglavlja)

**Radni naslov (opcije)**
1. **Razine ontološke složenosti i umjetna inteligencija: jezik, komunikacija i novi entitet u sustavu**
2. **Šesnaest razina i jedan novi entitet: ontologija komunikacije u doba umjetne inteligencije**
3. **Od materije do kulturnog modela: ontološke razine, jezik i AI kao novi sudionik**

### DIO I — RAZINE: OKVIR (pogl. 1–4)
1. Sustavi, cjeline, organizacija: što je razina, što je emergencija (slaba/jaka, stupnjevi)
2. OMLCC: 16 razina ontološke složenosti — tri domene (Searle), relacijske sheme, izgradnja odozdo
3. Od dijelova do strukture: tri koraka emergencije (dijelovi → mreža → novi entitet)
4. Kako se razine čitaju iz podataka: korpus, mreže, vektori (metodologija + kod)

### DIO II — KOMUNIKACIJA KAO RAZINA (pogl. 5–8)
5. Jezik kao emergentna pojava: značenje u relacijama (Saussure → Harris → konstrukcije)
6. Od ko-okurencije do konceptualnih mreža (CGCN; **emocije/*strah* kao studija slučaja**)
7. **Komunikacija kao razina 14**: što je komunikacijski čin kao društveni entitet (Grice, Harris, Searle — statusne funkcije i kolektivna intencionalnost; zajednički artefakti; konvencije; imena i adresiranje)
8. Institucije (15) i kulturni modeli (16): kako komunikacija nosi kulturu (naslijeđeni vs. vlastiti model)

### DIO III — AI U SUSTAVU (pogl. 9–12)
9. Od vektorskog prostora do modela: ugrađivanje, pažnja, kontekst
10. Geometrija značenja i njezine granice (vlastiti podaci) + skala, rezultati, kontekst ("organizacija, ne veličina")
11. Mišljenje kao procesiranje: kontekst koji se kontinuirano unapređuje
12. **Novi entitet u sustavu**: od modela do agenta; protokoli (MCP, A2A, AP2/x402) kao komunikacijska infrastruktura

### DIO IV — KOMUNIKACIJA S NOVIM ENTITETOM (pogl. 13–16)
13. Human→agent i agent→agent: što se mijenja **na razini 14** (prepoznavanje namjera, zajedničke obveze, konvencije, artefakti memorije)
14. Kolaborator i kompetitor: resursi (računanje, energija, podaci, pažnja, jurisdikcija), odgovornost, autorstvo
15. Hoće li imati kulturu? Razine 12–16 u agentskim sustavima — što vidimo, što nedostaje
16. Što to znači za lingvistiku — i kako bismo znali da griješimo (istraživački program; AI4LANG kao laboratorij)

## 6.3 Što se mijenja u odnosu na varijantu A
| | Varijanta A (trenutni plan) | **Varijanta B (razine + AI)** |
|---|---|---|
| Težište | emergencija + jezik + modeli | **ontološke razine + AI** |
| Komunikacija | raspoređena (pogl. 5–8, 14) | **vlastiti dio DIO II — razina 14 kao nosiva** |
| Vlastiti model (OMLCC) | jedno poglavlje (2) | **okosnica cijele knjige** (pogl. 2, 4, 7, 8, 13–15) |
| AI | DIO III–IV (modeli i agenti) | **novi entitet koji ulazi u razinu 14** — time AI dobiva ontološko mjesto, a ne samo tehnički opis |
| Rizik | sličnost s knjigom 2025. | **jasna razlika**: 2025 = praksa/povijest, ova = ontološki smještaj |
| Snaga | pristupačniji ulaz | **autorski doprinos je u središtu** (najcitiraniji dio) |

**Preporuka:** varijanta B. Razlog: tvoja je posebnost upravo OMLCC (16 razina) i tvrdnja "novi entitet, ne razina"; varijanta A tu posebnost troši na jedno poglavlje, a varijanta B od nje gradi cijelu knjigu. Komunikacija pritom ne ispada — ona postaje **razina na kojoj se sve vidi**.
