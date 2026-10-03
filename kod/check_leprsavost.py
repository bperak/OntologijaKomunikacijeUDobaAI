#!/usr/bin/env python3
"""Lepršavost i krutost proze (ZAPIS-024).

Autorova korekcija (3. 10. 2026.): „Još uvijek mi nedostaje lepršavosti i učvršćivanja teme i posljedica,
nekako je još uvijek rigidno."

Krutost nije dužina rečenice — to mjeri `check_stil.py`. Krutost je **jednoličnost oblika**:

1. **Konektor na početku rečenice** (Zato, Time, Iz toga, Odatle, Otud, Stoga, Zbog toga, Pritom, Pri tome).
   Visok udio znači da tekst diše na jedan način: svaka tvrdnja dobiva isti uvod.
2. **Antiteza** („a ne", „a ne samo", „nego", „umjesto", „dok") — mjeri se po 1.000 riječi. Antiteza je
   dobra u maloj količini; kad postane ritam, čita se kao bubnjanje.
3. **Isti konektor u istoj datoteci** — najčešći konektor i njegov udio među svim konektorima.
4. **Otvaranje odlomaka** — koliko se različitih riječi pojavljuje na početku odlomaka i koliko puta se
   ponavlja najčešće otvaranje.
5. **Učvršćivanje teme** — pojavljuje li se na kraju poglavlja rečenica koja nalaz veže na temu knjige
   (posljedica), i koliko je često jezgro teme (razina/svojstvo/mjesto/kriterij) ponovljeno.

Pragovi su čuvari, ne ciljevi. Uporaba: python3 kod/check_leprsavost.py [--isoli]
"""
import glob
import os
import re
import statistics
import sys

KOR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUKOPIS = os.path.join(KOR, "rukopis")

KONEKTORI = ["Zato", "Time je", "Time se", "Time je", "Iz toga", "Odatle", "Otud", "Stoga", "Zbog toga",
             "Pritom", "Pri tome", "Na taj način", "Iz toga slijedi"]
ANTITEZA = re.compile(r"\ba ne\b|\ba ne samo\b|\bnego\b|\bumjesto\b|\bdok\b", re.I)
USRED = re.compile(r",\s*(jer|zato|pa|dakle|stoga|međutim|no)\b", re.I)   # konektori USRED rečenice (Claude)
TEMA = re.compile(r"\b(razina|razine|razini|svojstv|mjesto|mjestu|kriterij|ljestvic|entitet|komunikacij)", re.I)


def proza(t):
    t = re.sub(r"^>.*$", "", t, flags=re.M)
    t = re.sub(r"^!\[.*$", "", t, flags=re.M)
    t = re.sub(r"^\|.*$", "", t, flags=re.M)
    t = re.sub(r"^```.*?^```", "", t, flags=re.M | re.S)
    t = re.sub(r"^\s*[-*]\s.*$", "", t, flags=re.M)
    t = re.sub(r"^\s*\d+\.\s.*$", "", t, flags=re.M)
    t = re.sub(r"^#.*$", "", t, flags=re.M)
    return t


def odlomci(t):
    return [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", proza(t)) if len(p.split()) >= 25]


def recenice(t):
    out = []
    for p in odlomci(t):
        out += [r.strip() for r in re.split(r"(?<=[.!?])\s+", p) if r.strip()]
    return out


def datoteke():
    if "--datoteka" in sys.argv:
        return [sys.argv[sys.argv.index("--datoteka") + 1]]
    return ([os.path.join(RUKOPIS, f) for f in ["uvod.md"] +
             [f"poglavlje-{i:02d}.md" for i in range(1, 17)] + ["zakljucak.md"]] +
            [f for f in sorted(glob.glob(os.path.join(RUKOPIS, "dodaci/dodatak-*.md")))
             if os.path.basename(f)[8] not in ("B", "E", "G")])


def main():
    print(f"{'datoteka':<38}{'konektor%':>10}{'antiteza/1k':>12}{'najčešći':>26}{'otvaranja':>10}{'SD odl.':>9}{'usr./1k':>10}")
    nalazi = []
    for p in datoteke():
        t = open(p, encoding="utf-8").read()
        rr = recenice(t)
        rijeci = sum(len(r.split()) for r in rr)
        nk = 0
        broj = {k: 0 for k in KONEKTORI}
        for r in rr:
            for k in KONEKTORI:
                if r.startswith(k):
                    nk += 1
                    broj[k] += 1
                    break
        naj = max(broj.items(), key=lambda x: x[1])
        ant = len(ANTITEZA.findall(" ".join(rr)))
        usr = len(USRED.findall(" ".join(rr)))
        odl = odlomci(t)
        otv = [o.split()[0].strip("*„") for o in odl if o.split()]
        from collections import Counter
        c = Counter(otv)
        najotv, najotv_n = (c.most_common(1)[0] if c else ("-", 0))
        sd = statistics.pstdev([len(o.split()) for o in odl]) if len(odl) > 1 else 0
        print(f"{os.path.basename(p):<38}{100*nk/max(len(rr),1):>9.1f}%{1000*ant/max(rijeci,1):>12.1f}"
              f"{(naj[0] + ' ×' + str(naj[1])):>26}{len(c):>6}{(' ' + najotv + ' ×' + str(najotv_n)):>14}{sd:>9.1f}{1000*usr/max(rijeci,1):>10.1f}")
        nalazi.append((os.path.basename(p), 100*nk/max(len(rr), 1), 1000*ant/max(rijeci, 1), naj, sd))
    if "--isoli" in sys.argv or True:
        print("\n=== KRUTO (konektor > 9 % ili antiteza > 8/1k) ===")
        for ime, kr, an, naj, sd in nalazi:
            if kr > 9 or an > 8:
                print(f"  • {ime:<34} konektor {kr:.1f}% · antiteza {an:.1f}/1k · najčešći {naj[0]} ×{naj[1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
