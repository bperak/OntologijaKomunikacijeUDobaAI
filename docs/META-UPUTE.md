*GENERIRANO skriptom `kod/check_meta.py` iz `docs/meta-upute.yaml` — ne uređivati ručno.*

# META-UPUTE — sve upute, provjerljive

*Svaka uputa ima provjeru: `provjera` se pokreće, a `ocekivano` mora se pojaviti u izlazu. Ako uputa nema provjeru, nije meta-uputa nego želja.*

**Stanje provjere:** 26/26 prolazi.

| id | vrsta | pravilo | status |
|---|---|---|---|
| `MU-01` | stil | Podebljano samo na POJMOVIMA, nikad na tvrdnjama; ukupno masno ≤ 15 %, dugi masni odlomci (>6 riječi) ≤ 10 %. | provjereno automatski |
| `MU-02` | stil | Ritam: ≥20 % rečenica kraćih od 12 riječi, ≥13 % do 8 riječi, ≤15 % duljih od 40, nijedan niz dulji od dvije rečenice preko 30 riječi. | provjereno automatski |
| `MU-03` | stil | Kratka rečenica mora nositi razliku, posljedicu ili uvjet, ime pojma ili mjeru — „šupljih kratkih" (koje samo ocjenjuju ili najavljuju) mora biti 0. | provjereno automatski |
| `MU-04` | stil | Repertoar čestica ≥ 5 različitih (naime, dakle, pak, usto, pritom, otud, naprotiv, štoviše, dakako, napose, zacijelo, tek); „upravo" ≤ 3 na 10.000 riječi. | provjereno automatski |
| `MU-05` | sadržaj | Nijedan element aparata (popis, naslov, tablica, slika, blok koda, ključni pojmovi, literatura) ne smije biti izgubljen u zahvatu. | provjereno automatski |
| `MU-06` | sadržaj | Nijedan citat, godina, brojka, naslov ni uputa ne smije se izgubiti u zahvatu. | provjereno automatski |
| `MU-07` | sadržaj | Tvrdnja + citat + izvor u istoj rečenici; nijedan citat ne ulazi u rukopis ako nije u bazi referenci (provjera u oba smjera). | provjereno automatski |
| `MU-08` | sadržaj | Svaka brojka ima vrstu (mjereno / procjena / izvedeno), izvor i datum; procjena se nikad ne prikazuje kao mjerenje. | provjereno automatski |
| `MU-09` | sadržaj | Nema homoglifa, skrivenih markera ni miješanoga nazivlja („Slika", ne „Figure"). | provjereno automatski |
| `MU-10` | sadržaj | Svaka unutarnja uputa (→ pogl. X, Slika, Tablica) ima postojeći cilj. | provjereno automatski |
| `MU-11` | sadržaj | Nema slomljenih uputa ni sidara. | provjereno automatski |
| `MU-12` | sadržaj | Figura nikad ne tvrdi više od teksta; tekst se ne prelijeva iz slike. | provjereno automatski |
| `MU-13` | čitatelj | Svako poglavlje ima tezu prevedenu na običan jezik i odlomak „Što vam ovo poglavlje daje." u DRUGOM LICU (čitatelj vidi svoju situaciju, a ne rječnik knjige). | provjereno automatski |
| `MU-14` | čitatelj | Nema više trećega lica za čitatelja („što čitatelj odatle dobiva") u otvaranjima. | provjereno automatski |
| `MU-15` | čitatelj | Uvod ima odjeljak „Što ćete odatle ponijeti" s ishodima u drugom licu. | provjereno automatski |
| `MU-16` | pojmovi | Pojam se ne rabi prije nego je objašnjen; prva uporaba nosi glos ili uputu na mjesto uvođenja. | ručni pregled — mjera je sito: prijavljuje kandidate, presudu daje pregled |
| `MU-17` | pojmovi | Registar pojmova (pojmovnik/koncepti.yaml) rabi iste nazive kao knjiga; rječnik se generira iz registra. | provjereno automatski |
| `MU-18` | povezanost | Na spoju sekcija: referencijalna veza (što se preuzima), paradigmatska (prema čemu tvrdnja stoji) i sintagmatska (što slijedi) — bez ijedne praznine osim zaštićenih odjeljaka. | ručni pregled — 14 paradigmatskih praznina su namjerne: 13 u dodatku I (alternativna formalizacija stoji u falsifikatorima, a to je aparat koji se ne dira) i 1 u uvodu („Što ćete odatle ponijeti") |
| `MU-19` | povezanost | Otvaranje uvlači: konkretna situacija → problem → preslika rješenja → veza na knjigu; otvaranja ne smiju postati formula. | ručni pregled — alat ispisuje zastavice (situacija / preslika / uputa) za pregled |
| `MU-20` | tvrdnje | Tvrdnja ne visi: ako odlučno tvrdi ili izvodi zaključak, u odlomku stoji na čemu stoji (razlog, uvjet, mjera, dokaz, izvor, uputa). | ručni pregled — mjera je sito; preostale tvrdnje pregledane i ocijenjene oslonjenima u kontekstu |
| `MU-21` | proces | Pogreška se ne briše — bilježi se (ISPRAVKE) i zapisuje (ZAPISI); broj zapisa samo raste. | provjereno automatski |
| `MU-22` | proces | Prije i poslije svakoga zahvata pokreće se mjera; namjerna promjena (preimenovan naslov, ispravljena uputa) bilježi se u ZAPIS i osvježava snimku. | provjereno posredno |
| `MU-23` | proces | U zahvatu se ne dodaje nijedna nova tvrdnja, izvor, brojka ni citat — sve što zahvat tvrdi stoji na građi koja je već u tekstu. | provjereno automatski |
| `MU-24` | proces | Stil dodataka (prozne dodatke A, C, D, F, H, I) drži iste pragove kao glavni tekst; aparatni dodaci (B rječnik, E izvori, G kazalo) izuzeti su. | provjereno automatski |
| `MU-25` | stil | Nijedna rečenica nije fraza: izrazi koji zvuče odlučno, a ne tvrde ništa (uzeti ozbiljno, igra ključnu ulogu, na pragu, nije slučajno, u suštini) zamjenjuju se tvrdnjom. | ručni pregled — 2 preostale iznimke su namjerne: „na pragu nečega većega" stoji u tuđem stavu koji knjiga citira, a „Emergentno nije slučajno." je tvrdnja, ne fraza |
| `MU-26` | stil | Pokazna zamjenica u tvrdnji („to", „ovo", „time") ima imenicu na koju se veže u istoj ili prethodnoj rečenici. | ručni pregled — mjera je gruba (76 kandidata); presudu daje čitanje |

## Kako se pokreće

```bash
python3 kod/check_meta.py            # sve upute
python3 kod/check_meta.py --samo MU-18
```
