#!/usr/bin/env python3
"""check_stil.py — mjeri prozu rukopisa prema standardu iz docs/STIL.md.

Mjeri (po datoteci i ukupno):
  1. gustoću podebljanoga (udio riječi unutar **…** u odnosu na prozne riječi),
  2. dužinu rečenice (srednja vrijednost, udio < 12 i > 40 riječi),
  3. „upravo" i čestični repertoar (naime, dakle, pak, usto, pritom, otud, naprotiv, štoviše,
     dakako, napose, zacijelo, tek) na 10.000 riječi,
  4. klišeje i menadžerski registar (popis),
  5. popisne retke i retke tablica,
  6. umetke među crtama (par „ — … — " u istoj rečenici) — informativno.

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

PRAG = {"bold": 15.0, "bold_dugi": 10.0, "rec_min": 20.0, "rec_max": 30.0, "kratke": 18.0, "duge": 14.0,
        "upravo": 3.0, "cestice_razlicitih": 5, "kliseji": 5, "popis": 280}
CESTICE = ["naime", "dakle", "pak", "usto", "pritom", "otud", "naprotiv", "štoviše",
           "dakako", "napose", "zacijelo", "tek"]
KLISEJI = ["implementira", "fokusira", "procesuira", "validira", "optimizira", "baziran",
           "bazirano", "feedback", "trend", "u okviru", "u kontekstu", "s ciljem",
           "kroz prizmu", "na kraju krajeva", "igra ključnu ulogu", "neizostavan",
           "adresira poruku", "adresirati problem", "adekvatan", "efikasan", "relevantan"]


def datoteke(samo=None):
    if samo:
        return [samo]
    out = []
    for p in sorted(glob.glob(os.path.join(RUK, "**", "*.md"), recursive=True)):
        if os.path.basename(p) in GENERIRANO:
            continue
        out.append(p)
    return out


def proza(tekst):
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", tekst)
    t = re.sub(r"^\|.*$", " ", t, flags=re.M)
    t = re.sub(r"^#{1,6} .*$", " ", t, flags=re.M)
    t = re.sub(r"^> .*$", " ", t, flags=re.M)
    t = re.sub(r"[*_`#|]", " ", t)
    return re.sub(r"\s+", " ", t)


def mjere(put):
    tekst = open(put, encoding="utf-8").read()
    t = proza(tekst)
    rijeci = re.findall(r"[^\W\d_]+", t, re.UNICODE)
    N = len(rijeci) or 1
    odlomci = re.findall(r"\*\*(.+?)\*\*", tekst, re.S)
    podebljano = " ".join(odlomci)
    bold_n = len(re.findall(r"[^\W\d_]+", podebljano, re.UNICODE))
    dugi = [o for o in odlomci if len(o.split()) > 6]
    rec = [r for r in re.split(r"(?<=[.!?])\s+(?=[A-ZČĆĐŠŽ„(])", t) if len(r.split()) >= 3]
    duz = [len(r.split()) for r in rec] or [0]
    broj = lambda uzorak: len(re.findall(uzorak, t, re.I))
    c = {k: broj(r"\b" + k) for k in CESTICE}
    return {
        "rijeci": N, "bold": 100.0 * bold_n / N,
        "bold_dugi": (100.0 * len(dugi) / len(odlomci)) if odlomci else 0.0,
        "bold_odlomaka": len(odlomci),
        "rec": statistics.mean(duz), "kratke": 100.0 * sum(1 for d in duz if d < 12) / len(duz),
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
          f"| <12 {m['kratke']:>4.1f}% | >40 {m['duge']:>4.1f}% | „upravo“ {m['upravo']:>4.1f}/10k "
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
    if zbroj["kratke"] < PRAG["kratke"]:
        nal.append(f"kratkih rečenica {zbroj['kratke']:.1f}% < {PRAG['kratke']}%")
    if zbroj["duge"] > PRAG["duge"]:
        nal.append(f"dugih rečenica {zbroj['duge']:.1f}% > {PRAG['duge']}%")
    if zbroj["upravo"] > PRAG["upravo"]:
        nal.append(f"„upravo“ {zbroj['upravo']:.1f}/10k > {PRAG['upravo']}")
    if zbroj["cestice_raz"] < PRAG["cestice_razlicitih"]:
        nal.append(f"čestični repertoar {zbroj['cestice_raz']} < {PRAG['cestice_razlicitih']}")
    if zbroj["kliseji"] > PRAG["kliseji"]:
        nal.append(f"klišeji {zbroj['kliseji']} > {PRAG['kliseji']}")
    if zbroj["popis"] > PRAG["popis"]:
        nal.append(f"popisnih redaka {zbroj['popis']} > {PRAG['popis']}")
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
    upute = set(re.findall(r"(→[ ]*[^ .,;)]+)", t))
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

    zbroj = {"rijeci": 0, "bold": 0.0, "bold_dugi": 0.0, "rec": [], "kratke": [], "duge": [], "upravo": 0.0,
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
    zbroj["duge"] = statistics.mean([m["duge"] for _, m in svi])
    zbroj["upravo"] = statistics.mean([m["upravo"] for _, m in svi])
    zbroj["crte"] = statistics.mean([m["crte"] for _, m in svi])
    zbroj["cestice_raz"] = sum(1 for v in zbroj["cestice"].values() if 10000.0 * v / N >= 0.5)

    if samo:
        for p, m in svi:
            ispis(p, m)
    print("\n=== UKUPNO ===")
    print(f"riječi {zbroj['rijeci']} | podebljano {zbroj['bold']:.1f}% (dugi odlomci {zbroj['bold_dugi']:.1f}%) | rečenica (prosjek poglavlja) "
          f"{zbroj['rec']:.1f} | <12 {zbroj['kratke']:.1f}% | >40 {zbroj['duge']:.1f}% | "
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
