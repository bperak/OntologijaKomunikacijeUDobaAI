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

Svako poglavlje ima istu anatomiju (sedam blokova): **teza → teorijski okvir → metode i podaci → praktikum s kodom („Ako ne radi") → vježbe 🟢🟡🏆 → sažetak i ključni pojmovi → „Kako bismo znali da griješimo"**.

---

## Struktura repozitorija

```
plan/           plan knjige i detaljni nacrt (varijanta B)
rukopis/        poglavlja (radne verzije)
referencije/    verificirana baza referenci (jedini dopušteni izvor citata)
kod/            skripte za analize i figure (poglavlja 4, 6, 10)
figure/         figure knjige
data/           podaci (korpusi, leksikoni) — veliki skupovi se ne verzioniraju
```

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
| `figure/` | ✅ 20 autorskih figura iz predavanja + popis s mapiranjem na poglavlja |

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
