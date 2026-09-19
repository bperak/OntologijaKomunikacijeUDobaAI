# Razine i entiteti — ontologija komunikacije u doba umjetne inteligencije

**Radni repozitorij knjige** · autor: **Benedikt Perak** (Filozofski fakultet u Rijeci / Laboratorij za istraživanje kulturne složenosti)
**Verzija:** v0.1 (radna) · **ustanovljeno:** 14. rujna 2026.

---

## O čemu je knjiga

Knjiga postavlja jedno pitanje i brani tri tvrdnje.

**Pitanje:** gdje u ontološkom smislu stoje jezik, komunikacija i veliki jezični modeli?

**Tri tvrdnje:**

1. **Razine su operativan okvir, ne metafora.** Ontološke razine (OMLCC: tri domene, šesnaest razina) definiraju se *relacijskim shemama* i mogu se čitati iz podataka.
2. **Komunikacija je jedna od tih razina (14) — i ujedno metoda.** Ona je istovremeno objekt (društveni čin s namjerom, artefaktom i konvencijom) i instrument (sve ostale razine čitamo iz komunikacijskih podataka).
3. **AI nije sedamnaesta razina, nego novi entitet koji ulazi u postojeće razine** — i time mijenja uvjete komunikacije: novi tip sudionika, novi artefakti, nove konvencije, novi protokoli.

**Razlika prema prethodnim knjigama autora:** *Komunikacija u doba umjetne inteligencije* (2025) daje povijest i praksu; *Data Science u kulturi* daje metode; **ova knjiga daje ontološki smještaj.**

---

## Struktura rukopisa (4 dijela × 4 poglavlja)

| dio | poglavlja | posao dijela |
|---|---|---|
| **I. RAZINE: OKVIR** | 1 sustavi i razine · 2 OMLCC (16 razina) · 3 tri koraka emergencije · 4 kako se razine čitaju iz podataka | postaviti pojmove i metodologiju |
| **II. KOMUNIKACIJA KAO RAZINA** | 5 jezik kao emergentna pojava · 6 mreže značenja · 7 **komunikacija kao razina 14** · 8 institucije i kulturni modeli | dokazati da je komunikacija razina |
| **III. AI U SUSTAVU** | 9 od vektorskog prostora do modela · 10 geometrija i granice · 11 mišljenje kao procesiranje · 12 novi entitet: od modela do agenta | što model jest, a što nije |
| **IV. KOMUNIKACIJA S NOVIM ENTITETOM** | 13 human→agent, agent→agent · 14 razine 12–16 kod agenata · 15 hoće li imati kulturu · 16 posljedice i falsifikacija | što se mijenja i kako to provjeriti |

Knjiga ima **uvod** (tri tvrdnje, dvije razlike, falsifikacijski okvir) i **zaključak** (stanje dokaza po tvrdnjama, otvorene stavke, što bi knjigu oborilo). Svako poglavlje ima istu anatomiju (sedam blokova): **teza → teorijski okvir → metode i podaci → praktikum s kodom („Ako ne radi") → vježbe 🟢🟡🏆 → sažetak i ključni pojmovi → „Kako bismo znali da griješimo"**.

---

## Struktura repozitorija

```
plan/           plan knjige i detaljni nacrt (varijanta B)
rukopis/        uvod.md · poglavlja 01–16 · zakljucak.md · predgovor.md · studije-slucaja/
rukopis/dodaci/ dodaci A–G (okruzenje, rjecnik, rjesenja vjezbi, predlosci, evidencija
                brojki, prigovori i odgovori, kazalo); E i G su GENERIRANI skriptama
referencije/    verificirana baza referenci (jedini dopušteni izvor citata)
pojmovnik/      registar pojmova za sve tri knjige + generirani rječnik
docs/           citiranje, mreža knjiga, upute po poglavljima
kod/            skripte za analize, figure i provjere mreže (check_lit, check_fakti,
                check_cisto, check_links, check_figure_overflow, mermaid_render,
                kazalo_build, evidencija_build, pojmovnik_build)
figure/         figure knjige
data/           podaci (korpusi, leksikoni) — veliki skupovi se ne verzioniraju
```

## Provjere (pokreću se prije svakoga commita)

```bash
python3 kod/check_lit.py             # citati ↔ baza referenci (oba smjera)
python3 kod/check_fakti.py --strict  # brojke u tekstu ↔ data/fakti.csv
python3 kod/check_cisto.py           # higijena: homoglifi, markeri, nazivlje slika
python3 kod/check_links.py           # upute, sidra, poveznice
python3 kod/check_figure_overflow.py # prelijevanje teksta u figurama
```

Generatori (izlaz se obnavlja jednom naredbom, pa ne može zastarjeti):

```bash
python3 kod/kazalo_build.py      # → rukopis/dodaci/dodatak-G-kazalo.md
python3 kod/evidencija_build.py  # → rukopis/dodaci/dodatak-E-izvori-i-brojke.md
python3 kod/pojmovnik_build.py   # → pojmovnik/RJECNIK.md
```

## Mreža triju knjiga

Ova knjiga nije samostalan projekt: čini mrežu s *Komunikacija u doba umjetne inteligencije* (2025) i *Data Science u kulturi*. Podjela posla, pravilo vlasništva tema, registar pojmova i automatska provjera uputa opisani su u **[`docs/MREZA-KNJIGA.md`](docs/MREZA-KNJIGA.md)**, a konkretne upute po poglavljima u **[`docs/UPUTE-PO-POGLAVLJIMA.md`](docs/UPUTE-PO-POGLAVLJIMA.md)**.

Provjera mreže (radi lokalno, bez mreže i s mrežom):

```bash
python kod/pojmovnik_build.py        # registar → rječnik + CSV
python kod/check_links.py --http     # sidra, upute na druge knjige, mrežne provjere
python kod/check_fakti.py --strict   # svaka brojka u rukopisu mora biti u data/fakti.csv (s vrstom dokaza)
python kod/check_lit.py              # citiranje u oba smjera: popis ↔ tekst ↔ REFERENCE_BASE.md
python kod/izvuci_doktorat.py        # ponovno izvlačenje podataka iz doktorata 2014.
```

**Automatska provjera u CI-u:** workflow je pripremljen u [`docs/ci-mreza.yml.example`](docs/ci-mreza.yml.example). GitHub ne dopušta stvaranje datoteka u `.github/workflows/` tokenom koji nema `workflow` ovlast — aktiviraj ga tako da datoteku kopiraš u `.github/workflows/mreza.yml` (kroz web sučelje ili tokenom s `workflow` scopeom), pa se provjera pokreće pri svakom commitu.

---

## Pravila rada (obvezujuća)

1. **Nijedna referenca ne ulazi u rukopis ako nije u `referencije/REFERENCE_BASE.md`.** Ako izvor nije ondje, dodaje se tek nakon provjere.
2. **Tvrdnja + citat + izvor u istoj rečenici.** Nema „vidi literaturu".
3. **Brojevi su sveti:** svaka brojka ima izvor, datum i vrstu (**mjereno** ili **procjena**). Procjena se nikad ne prikazuje kao mjerenje.
4. **Tuđe se ne pripisuje sebi:** podjela na tri domene (materijalna / psihološka / društvena) je Searleova (1995; 2010); razrada na šesnaest razina i relacijske sheme su autorski doprinos (Perak 2018; 2019).
5. **Skromnost tvrdnji:** knjiga radi isključivo sa **slabom emergencijom** (Bedau 1997); model je **kandidat** za novi entitet, nikad zaključak.
6. **Terminološka stega:** *entitet* = **gdje** je (pozicija u sustavu) · *agent* = **što radi** (sistemska uloga). Riječ „razina" nikad se ne upotrebljava za model.
7. **Nepotvrđeno se označava** (`❓ nepotvrđeno`) i ne tvrdi.

---

## Stanje rada

| datoteka | status |
|---|---|
| `plan/NACRT_B_DETALJNO.md` | ✅ detaljni nacrt (16 poglavlja do razine sekcija) |
| `plan/KNJIGA_PLAN.md` | ✅ plan v0.2 (varijante A i B) |
| `referencije/REFERENCE_BASE.md` | ✅ v1.0 — provjerene reference (kanonske 1843–1977 + recentne 2024–2026) |
| `rukopis/poglavlje-01.md` | ✅ prva radna verzija (3.786 riječi) |
| `rukopis/poglavlje-02.md` | ✅ prva radna verzija (4.486 riječi, OMLCC) |
| `rukopis/poglavlje-03.md` | ✅ prva radna verzija (4.494 riječi, tri koraka) |
| `rukopis/poglavlje-04.md` | ✅ prva radna verzija (7.000 riječi, kako se razine čitaju iz podataka — metodologija) |
| `rukopis/predgovor.md` | ✅ predgovor + „kako čitati uz druge dvije knjige" (804 riječi) |
| `rukopis/poglavlje-05.md` | ✅ prva radna verzija (4.392 riječi, jezik kao emergentna pojava) |
| `rukopis/poglavlje-06.md` | ✅ prva radna verzija (4.497 riječi, mreže značenja + praktikum s kodom) |
| `rukopis/poglavlje-07.md` | ✅ prva radna verzija (3.205 riječi, komunikacija kao razina 14) |
| `rukopis/poglavlje-08.md` | ✅ prva radna verzija (institucije 15 i kulturni modeli 16) |
| `rukopis/poglavlje-09.md` | ✅ prva radna verzija (4.270 riječi, od vektorskog prostora do modela — DIO III) |
| `rukopis/poglavlje-10.md` | ✅ prva radna verzija (6.420 riječi, geometrija na djelu i njezine granice) |
| `rukopis/poglavlje-11.md` | ✅ prva radna verzija (5.546 riječi, mišljenje kao procesiranje) |
| `rukopis/poglavlje-12.md` | ✅ prva radna verzija (5.782 riječi, od modela do agenta — novi entitet) |
| `rukopis/poglavlje-13.md` | ✅ prva radna verzija (5.667 riječi, human→agent i agent→agent — DIO IV) |
| `rukopis/poglavlje-14.md` | ✅ prva radna verzija (6.470 riječi, razine 12–16 kod agenata: funkcionalno vs. intrinzično) |
| `rukopis/poglavlje-15.md` | ✅ prva radna verzija (6.498 riječi, hoće li imati kulturu — prijenos, ne veličina) |
| `rukopis/poglavlje-16.md` | ✅ prva radna verzija, završno (6.500 riječi, posljedice za lingvistiku + zbirna tablica „kako bismo znali da griješimo") |
| `rukopis/studije-slucaja/incidenti-2026.md` | ✅ studija slučaja: zašto razlučivati razine (AI incidenti 2026) |
| `docs/ISPRAVKE.md` | ✅ evidencija ispravljenih javnih tvrdnji (ISPRAVAK-001/002/003) |
| `doktorat-strah` (zaseban repo) | ✅ doktorski rad 2014. objavljen u otvorenom pristupu: https://github.com/bperak/doktorat-strah |
| `data/fakti.csv` | ✅ evidencija brojki (34 zapisa) + `kod/check_fakti.py` (provjerava i brojke u rukopisu) + `kod/izvuci_doktorat.py` |
| `figure/` | ✅ 19 autorskih figura iz predavanja + popis s mapiranjem na poglavlja (⚠ u tekst je zasad ugrađeno 2 — vidi `figure/README.md`) |

---

## Izvorište

Knjiga se razvija iz izlaganja **„Elements of Cognition in Complex Language"** (Inter-University Centre Dubrovnik, 11. rujna 2026.) — 35 slajdova i ~8.600 riječi govornih bilješki. Predavanje je **kondenzat knjige**, a ne skica.

---

## Licenca i citiranje

**Licenca: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)** — *Attribution-NonCommercial 4.0 International* (puni tekst: [`LICENSE`](LICENSE)).

Ukratko: knjiga se može **slobodno čitati, preuzimati, dijeliti i prerađivati u nekomercijalne svrhe — ali je navođenje autorstva obvezno**, a komercijalna uporaba (prodaja, naplaćena izdanja) zahtijeva pisanu suglasnost autora. Objava pod vlastitim imenom ili bez reference nije dopuštena.

**Citiranje (APA 7):**
> Perak, B. (2026). *Razine i entiteti: ontologija komunikacije u doba umjetne inteligencije* (radni rukopis v0.1). Filozofski fakultet u Rijeci. https://github.com/bperak/OntologijaKomunikacijeUDobaAI

**Svi formati citiranja** — APA 7 · Chicago · MLA · BibTeX · pojedinačno poglavlje · englesko izdanje, te **kako citirati ostale knjige autora** (2025, *Data Science u kulturi*) i figure/podatke/kod: **[`docs/CITIRANJE.md`](docs/CITIRANJE.md)**.
Strojno čitljiv zapis za alate: [`CITATION.cff`](CITATION.cff).

Kontakt: **bperak@uniri.hr**
