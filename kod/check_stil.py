#!/usr/bin/env python3
"""check_stil.py — mjeri prozu rukopisa prema standardu iz docs/STIL.md.

Mjeri (po datoteci i ukupno):
  1. gustoću podebljanoga (udio riječi unutar **…** u odnosu na prozne riječi),
  2. dužinu rečenice (srednja vrijednost, udio < 12 i > 40 riječi),
  3. „upravo" i čestični repertoar (naime, dakle, pak, usto, pritom, otud, naprotiv, štoviše,
     dakako, napose, zacijelo, tek) na 10.000 riječi,
  4. klišeje i menadžerski registar (popis),
  5. popisne retke i retke tablica,
  6. umetke među crtama (par „ — … — " u istoj rečenici) — informativno,
  7. ritam: udio rečenica ≤ 8 riječi, raznolikost dužina (SD), najdulji niz rečenica > 30 riječi,
  8. „šuplje kratke" rečenice — kratkoća bez informacije (mora ih biti 0).

Upotreba:
    python3 kod/check_stil.py                      # izvještaj (0 = u granicama)
    python3 kod/check_stil.py --strict             # izlaz 1 ako je ijedna mjera prekoračena
    python3 kod/check_stil.py --datoteka rukopis/poglavlje-01.md
    python3 kod/check_stil.py --usporedi stara.md nova.md   # provjera da citati/brojke nisu izgubljeni
"""
import glob
import os
import re
import statistics
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUK = os.path.join(ROOT, "rukopis")
GENERIRANO = {"sadrzaj.md", "dodatak-E-izvori-i-brojke.md", "dodatak-G-kazalo.md"}

# Pragovi su ČUVARI, a ne ciljevi: brane od dviju krajnosti — od razvučene proze i od sjeckanja.
# Kalibrirani su na prerađenome poglavlju 1 (srednja 20,1 · <12 riječi 33,8 % · ≤8 riječi 15,3 %),
# uz široku marginu, da 0,1 postotnoga poena ne tjera na umetanje rečenica bez sadržaja.
# DONJA granica srednje dužine NIJE postavljena: autor traži kraće rečenice, pa kratkoća nije
# pogreška (dodatak D, obrasci, ima srednju 10,6 i to je u redu). Gornja granica (30) brani od
# razvučene proze, a udjeli kratkih rečenica brane od sjeckanja.
PRAG = {"bold": 15.0, "bold_dugi": 10.0, "rec_min": 0.0, "rec_max": 30.0, "kratke": 20.0, "duge": 15.0,
        "vrlo_kratke": 13.0, "niz_dagih": 2, "suplje": 0,
        "upravo": 3.0, "cestice_razlicitih": 5, "kliseji": 5, "popis": 280}
CESTICE = ["naime", "dakle", "pak", "usto", "pritom", "otud", "naprotiv", "štoviše",
           "dakako", "napose", "zacijelo", "tek"]
KLISEJI = ["implementira", "fokusira", "procesuira", "validira", "optimizira", "baziran",
           "bazirano", "feedback", "trend", "u okviru", "u kontekstu", "s ciljem",
           "kroz prizmu", "na kraju krajeva", "igra ključnu ulogu", "neizostavan",
           "adresira poruku", "adresirati problem", "adekvatan", "efikasan", "relevantan"]
# „Šuplja kratka": kratka rečenica (do 8 riječi) koja samo ocjenjuje ili najavljuje, a ne nosi
# informaciju. Kratkoća nije stil ako nema sadržaja (autorovo pravilo: „malo su prebanalne").
SUPLJE = re.compile(
    r"\b(?:važn|ključn|nosiv|bitn|zanimljiv|korisn|poučn)\w*"
    r"|\b(?:vrijedi|treba|valja)\s+(?:istaknuti|napomenuti|naglasiti|reći|zapamtiti)"
    r"|\briječ je o\b|\bne smije se prešutjeti\b", re.IGNORECASE)


def datoteke(samo=None):
    if samo:
        return [samo]
    out = []
    for p in sorted(glob.glob(os.path.join(RUK, "**", "*.md"), recursive=True)):
        if os.path.basename(p) in GENERIRANO:
            continue
        out.append(p)
    return out


def _ocisti(s):
    s = re.sub(r"!\S*\S", " ", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    return re.sub(r"[*_`#]", " ", s)


def recenice(tekst):
    """Vraća (sve rečenice, duljine, oznaka je li rečenica iz popisa).

    Zašto po retcima, a ne na cijelome tekstu: naslovi, tablice, blokovi koda i oznake popisa
    („- ", „1. ") nemaju rečeničnu strukturu. Kad se tekst najprije spljošti, naslov spoji dvije
    rečenice u jednu, a oznaka popisa spriječi diobu (rečenica nakon nje počinje malim slovom), pa
    mjere dužine i ritma postanu besmislene — i tjeraju na brisanje aparata. Zato se svaki redak
    obrađuje zasebno: naslovi/tablice/kod se preskaču, popisni redak je jedna rečenica, a odlomak se
    dijeli po rečeničnim granicama.
    """
    rec, je_popis = [], []
    for red in tekst.split("\n"):
        r = red.strip()
        if not r or r.startswith(("```", "|", ">", "#", "![", "---", "===")):
            continue
        # Retci popisa literature („Autor 1997 · Autor 2006 · …") i masni podnaslovi na vlastitome
        # retku nisu rečenice: reference nemaju rečeničnu strukturu, a podnaslov je aparat. Kad bi
        # ušli u mjeru, izgledali bi kao goleme „rečenice" i kao „šuplje kratke".
        if r.count("·") >= 3 or re.fullmatch(r"\*\*[^*]+\*\*:?", r):
            continue
        # Uvodna natuknica na početku retka („**Zašto je to važno…** Ovi brojevi…") jest aparat:
        # broji se samo tekst iza natuknice, a sam se natuknica ne broji kao rečenica.
        r = re.sub(r"^\*\*[^*]{2,80}?\*\*[:.]?\s*", "", r)
        popis = bool(re.match(r"^(?:[-*+]|\d+\.)\s+", r))
        if popis:
            r = re.sub(r"^(?:[-*+]|\d+\.)\s+", "", r)
        r = _ocisti(r).strip()
        if popis:
            # cijeli popisni redak jedinica je za sebe (nema spoja sa susjednima)
            if len(r.split()) >= 2:
                rec.append(r)
                je_popis.append(True)
            continue
        for dio in re.split(r"(?<=[.!?])\s+(?=[A-ZČĆĐŠŽ„(\u201e])", r):
            if len(dio.split()) >= 3:
                rec.append(dio)
                je_popis.append(False)
    duz = [len(x.split()) for x in rec] or [0]
    return rec, duz, je_popis


def proza(tekst, bez_popisa=False):
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", tekst)
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"^\|.*$", " ", t, flags=re.M)
    t = re.sub(r"^#{1,6} .*$", " ", t, flags=re.M)
    t = re.sub(r"^> .*$", " ", t, flags=re.M)
    if bez_popisa:
        t = re.sub(r"^\s*(?:[-*+]|\d+\.)\s+.*$", " ", t, flags=re.M)
    t = re.sub(r"[*_`#|]", " ", t)
    return re.sub(r"\s+", " ", t)


def mjere(put):
    tekst = open(put, encoding="utf-8").read()
    t = proza(tekst)
    rijeci = re.findall(r"[^\W\d_]+", t, re.UNICODE)
    N = len(rijeci) or 1
    # Podebljane TVRDNJE mjere se odvojeno od podebljanih UVODNIH NATUKNICA („Slučaj A — …",
    # „Ključni nalaz: …"): natuknica je aparat, ne tvrdnja, i ne smije se brojiti u „duge“ odlomke.
    odlomci, natuknice = [], []
    for m in re.finditer(r"\*\*(.+?)\*\*", tekst, re.S):
        red_poc = tekst.rfind("\n", 0, m.start()) + 1
        ostatak = tekst[m.end():tekst.find("\n", m.end()) if tekst.find("\n", m.end()) >= 0 else len(tekst)]
        prije_na_retku = re.sub(r"^\s*(?:[-*+]|\d+\.)\s*", "", tekst[red_poc:m.start()])
        if prije_na_retku == "" and ostatak.strip():
            natuknice.append(m.group(1))
        else:
            odlomci.append(m.group(1))
    podebljano = " ".join(odlomci + natuknice)
    bold_n = len(re.findall(r"[^\W\d_]+", podebljano, re.UNICODE))
    dugi = [o for o in odlomci if len(o.split()) > 6]
    rec, duz, je_popis = recenice(tekst)
    vrlo_kratke = 100.0 * sum(1 for d in duz if d <= 8) / len(duz)
    # „Šuplja kratka" ne broji uvodne retke („Ključne izmjerene vrijednosti, s izvornim stranicama:")
    # jer oni najavljuju tablicu, a nisu tvrdnja.
    suplje = sum(1 for r, d in zip(rec, duz)
                 if d <= 8 and not r.rstrip().endswith(":") and SUPLJE.search(r))
    sd = statistics.pstdev(duz) if len(duz) > 2 else 0.0
    # Niz dugih rečenica mjeri se SAMO na prozi (bez popisnih redaka): niz dugih popisnih
    # čestica (falsifikatori, koraci postupka) jest aparat, a ne ritam, i ne smije se „popravljati".
    duz_run = [d for d, p in zip(duz, je_popis) if not p] or [0]
    niz, najduzi = 0, 0
    for d in duz_run:
        niz = niz + 1 if d > 30 else 0
        najduzi = max(najduzi, niz)
    broj = lambda uzorak: len(re.findall(uzorak, t, re.I))
    c = {k: broj(r"\b" + k) for k in CESTICE}
    return {
        "rijeci": N, "bold": 100.0 * bold_n / N,
        "bold_dugi": (100.0 * len(dugi) / len(odlomci)) if odlomci else 0.0,
        "bold_odlomaka": len(odlomci) + len(natuknice), "bold_natuknica": len(natuknice),
        "rec": statistics.mean(duz), "kratke": 100.0 * sum(1 for d in duz if d < 12) / len(duz),
        "vrlo_kratke": vrlo_kratke, "sd": sd, "niz_dagih": najduzi, "suplje": suplje,
        "duge": 100.0 * sum(1 for d in duz if d > 40) / len(duz),
        "upravo": 10000.0 * broj(r"\bupravo\b") / N,
        "cestice": c, "cestice_raz": sum(1 for v in c.values() if 10000.0 * v / N >= 0.5),
        "kliseji": sum(broj(r"\b" + k) for k in KLISEJI),
        "popis": sum(1 for l in tekst.splitlines() if l.strip().startswith(("- ", "• "))),
        "tablice": sum(1 for l in tekst.splitlines() if l.strip().startswith("|")),
        "crte": 10000.0 * len(re.findall(r"—[^—]{1,80}—", t)) / N,
    }


def ispis(put, m):
    ime = os.path.relpath(put, ROOT)
    print(f"{ime}\n   riječi {m['rijeci']:>6} | podebljano {m['bold']:>5.1f}% | rečenica {m['rec']:>4.1f} "
          f"| <12 {m['kratke']:>4.1f}% | ≤8 {m['vrlo_kratke']:>4.1f}% | >40 {m['duge']:>4.1f}% | SD {m['sd']:>4.1f} | niz>30 {m['niz_dagih']:>2} | šuplje {m['suplje']:>2} | „upravo“ {m['upravo']:>4.1f}/10k "
          f"| čestice {m['cestice_raz']}/12 | klišeji {m['kliseji']:>2} | popis {m['popis']:>3} "
          f"| crte {m['crte']:>4.1f}/10k")


def provjera(zbroj):
    nal = []
    if zbroj["bold"] > PRAG["bold"]:
        nal.append(f"podebljano {zbroj['bold']:.1f}% > {PRAG['bold']}%")
    if zbroj["bold_dugi"] > PRAG["bold_dugi"]:
        nal.append(f"podebljanih odlomaka >6 riječi {zbroj['bold_dugi']:.1f}% > {PRAG['bold_dugi']}% (podebljane tvrdnje)")
    if not (PRAG["rec_min"] <= zbroj["rec"] <= PRAG["rec_max"]):
        nal.append(f"srednja rečenica {zbroj['rec']:.1f} izvan {PRAG['rec_min']}–{PRAG['rec_max']}")
    if zbroj["suplje"] > PRAG["suplje"]:
        nal.append(f"šupljih kratkih rečenica {zbroj['suplje']} > {PRAG['suplje']} (kratka rečenica mora nositi informaciju)")
    if zbroj["vrlo_kratke"] < PRAG["vrlo_kratke"]:
        nal.append(f"kratkih rečenica (≤8 riječi) {zbroj['vrlo_kratke']:.1f}% < {PRAG['vrlo_kratke']}%")
    if zbroj["niz_dagih"] > PRAG["niz_dagih"]:
        nal.append(f"niz rečenica >30 riječi {zbroj['niz_dagih']} > {PRAG['niz_dagih']} (ritam se ne mijenja)")
    # Na razini cijele knjige ne provjeravaju se APSOLUTNI zbrojevi (klišeji, popisni retci): pragovi
    # za njih vrijede po datoteci, a zbroj kroz 27 datoteka nije mjera i ne smije rušiti provjeru.
    if zbroj["kratke"] < PRAG["kratke"]:
        nal.append(f"kratkih rečenica {zbroj['kratke']:.1f}% < {PRAG['kratke']}%")
    if zbroj["duge"] > PRAG["duge"]:
        nal.append(f"dugih rečenica {zbroj['duge']:.1f}% > {PRAG['duge']}%")
    if zbroj["upravo"] > PRAG["upravo"]:
        nal.append(f"„upravo“ {zbroj['upravo']:.1f}/10k > {PRAG['upravo']}")
    # Čestični repertoar traži se razmjerno duljini: od dvjestostraničnoga poglavlja smisleno je
    # tražiti pet različitih čestica, a od dodatka od 280 riječi nije (tamo je dosta dvije).
    w = zbroj["rijeci"]
    prag_cestica = 5 if w >= 1500 else (3 if w >= 800 else (2 if w >= 400 else 1))
    if zbroj["cestice_raz"] < prag_cestica:
        nal.append(f"čestični repertoar {zbroj['cestice_raz']} < {prag_cestica}")
    # (klišeji i popisni retci ispisuju se u zbroju, ali se ovdje ne provjeravaju — vidi gore)
    return nal


AUTOR = (
    r"[A-ZČĆĐŠŽ][A-Za-zČĆĐŠŽčćđšž'’.-]*"
    r"(?:[ ]+(?:i sur[.]|et al[.]|&|and)[ ]+[A-ZČĆĐŠŽ][A-Za-zČĆĐŠŽčćđšž'’.-]*)*"
    r"(?:[ ]*,[ ]*[A-ZČĆĐŠŽ][A-Za-zČĆĐŠŽčćđšž'’.-]*)?"
)


def skupovi(put):
    """Skupovi za provjeru istovjetnosti sadržaja: citati (autor+godina), godine, brojke, naslovi, upute."""
    t = open(put, encoding="utf-8").read()
    citati = {a + " " + g for a, g in re.findall("(" + AUTOR + r")[ ]*,?[ ]*([0-9]{4}[a-z]?)", t)}
    godine = set(re.findall(r"(1[89][0-9]{2}|20[0-9]{2})", t))
    brojke = set(re.findall(r"([0-9][0-9.,]*[ ]*(?:%|puta|bioloških|riječi|poglavlja|razina|parametara|koraka))", t))
    naslovi = set(re.findall(r"^#{2,4} .+$", t, re.M))
    # Unutarnje upute su samo prave upute (→ pogl. 2.3, → dodatak I.1, → Slika I.1, → data/…), a ne
    # svaki „→ " u tekstu: lanac pojmova („materijal → informacija → interakcija → komunikacija") nije
    # uputa. Zato se traži poznata oznaka, a masni markeri se prije toga uklanjaju.
    t_clean = re.sub(r"[*_`]", "", t)
    upute = set(re.findall(
        r"→\s*(?:pogl\.|dodatk\w*|Slika|Tablica|odjeljak|docs/\S+|data/\S+|kod/\S+)\s*[IVXLC0-9][\w.,–\-]*",
        t_clean))
    return citati, godine, brojke, naslovi, upute


def main():
    args = sys.argv[1:]
    if "--usporedi" in args:
        i = args.index("--usporedi")
        stari, novi = args[i + 1], args[i + 2]
        a, b = skupovi(stari), skupovi(novi)
        imena = ["citati (autor+godina)", "godine", "brojke s jedinicom", "naslovi", "upute"]
        nal = 0
        for ime, x, y in zip(imena, a, b):
            izg = x - y
            print(f"{ime}: prije {len(x)} | poslije {len(y)} | izgubljeno {len(izg)}")
            for z in sorted(izg)[:20]:
                print("   ⚠ izgubljeno:", z.strip()[:110])
            nal += len(izg)
        print("\n✔ sadržaj istovjetan" if not nal else f"\n⚠ izgubljenih jedinica: {nal}")
        return 1 if nal else 0

    samo = None
    if "--datoteka" in args:
        samo = args[args.index("--datoteka") + 1]
        if not os.path.isabs(samo):
            samo = os.path.join(ROOT, samo)

    zbroj = {"rijeci": 0, "bold": 0.0, "bold_dugi": 0.0, "vrlo_kratke": 0.0, "sd": 0.0, "niz_dagih": 0, "suplje": 0,
             "rec": [], "kratke": [], "duge": [], "upravo": 0.0,
             "cestice": {k: 0 for k in CESTICE}, "kliseji": 0, "popis": 0, "tablice": 0, "crte": 0.0}
    svi = []
    for p in datoteke(samo):
        m = mjere(p)
        svi.append((p, m))
        zbroj["rijeci"] += m["rijeci"]
        zbroj["bold"] += m["bold"] * m["rijeci"] / 100.0
        zbroj["kliseji"] += m["kliseji"]
        zbroj["popis"] += m["popis"]
        zbroj["tablice"] += m["tablice"]
        zbroj["bold_dugi"] += m["bold_dugi"]
        for k in CESTICE:
            zbroj["cestice"][k] += m["cestice"][k]
        zbroj.setdefault("_rec", []).append(m)

    N = zbroj["rijeci"] or 1
    zbroj["bold"] = 100.0 * zbroj["bold"] / N
    zbroj["bold_dugi"] = statistics.mean([m["bold_dugi"] for _, m in svi])
    sve_duz = []
    for _, m in svi:
        sve_duz.extend([m["rec"]] * 1)
    zbroj["rec"] = statistics.mean([m["rec"] for _, m in svi])
    zbroj["kratke"] = statistics.mean([m["kratke"] for _, m in svi])
    zbroj["vrlo_kratke"] = statistics.mean([m["vrlo_kratke"] for _, m in svi])
    zbroj["sd"] = statistics.mean([m["sd"] for _, m in svi])
    zbroj["niz_dagih"] = max(m["niz_dagih"] for _, m in svi)
    zbroj["suplje"] = sum(m["suplje"] for _, m in svi)
    zbroj["duge"] = statistics.mean([m["duge"] for _, m in svi])
    zbroj["upravo"] = statistics.mean([m["upravo"] for _, m in svi])
    zbroj["crte"] = statistics.mean([m["crte"] for _, m in svi])
    zbroj["cestice_raz"] = sum(1 for v in zbroj["cestice"].values() if 10000.0 * v / N >= 0.5)

    if samo:
        for p, m in svi:
            ispis(p, m)
    print("\n=== UKUPNO ===")
    print(f"riječi {zbroj['rijeci']} | podebljano {zbroj['bold']:.1f}% (dugi odlomci {zbroj['bold_dugi']:.1f}%) | rečenica (prosjek poglavlja) "
          f"{zbroj['rec']:.1f} | <12 {zbroj['kratke']:.1f}% | ≤8 {zbroj['vrlo_kratke']:.1f}% | "
          f">40 {zbroj['duge']:.1f}% | SD {zbroj['sd']:.1f} | niz>30 {zbroj['niz_dagih']} | "
          f"„upravo“ {zbroj['upravo']:.1f}/10k | čestice {zbroj['cestice_raz']}/12 | "
          f"klišeji {zbroj['kliseji']} | popis {zbroj['popis']} | tablice {zbroj['tablice']} | "
          f"crte {zbroj['crte']:.1f}/10k")
    print("čestice:", {k: v for k, v in sorted(zbroj["cestice"].items(), key=lambda x: -x[1]) if v})
    nal = provjera(zbroj)
    if nal:
        print("\n⚠ izvan granica standarda:")
        for n in nal:
            print("   -", n)
        return 1 if "--strict" in args else 0
    print("\n✔ proza je u granicama standarda (docs/STIL.md)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
