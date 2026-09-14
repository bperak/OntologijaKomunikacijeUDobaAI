#!/usr/bin/env python3
"""Provjera mreže knjiga: sidra, upute na druge knjige i registar pojmova.

Provjerava:
  1. svaku lokalnu uputu tipa (rukopis/poglavlje-07.md#sidro) — postoji li datoteka i sidro;
  2. upute na druge knjige (github.com/bperak/...) — popisuje ih, a uz --http provjerava HEAD;
  3. registar pojmova: postoji li datoteka poglavlja navedena u 'kanonski';
  4. upozorenja: više od dvije upute na druge knjige u istom odjeljku (pravilo iz docs/MREZA-KNJIGA.md).

Upotreba:
    python kod/check_links.py            # lokalne provjere (brzo, bez mreže)
    python kod/check_links.py --http     # + HEAD provjera vanjskih uputa
Izlaz: 0 = sve u redu, 1 = ima slomljenih uputa.
"""
import os
import re
import sys
import unicodedata
import urllib.request

try:
    import yaml
except ImportError:
    sys.exit("Nedostaje PyYAML: pip install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$", re.M)
CROSS = re.compile(r"https://github\.com/bperak/[A-Za-z0-9_\-]+")
OWN = {"komunikacija_u_doba_ai": "Komunikacija u doba umjetne inteligencije (2025)",
       "dsk": "Data Science u kulturi (u izradi)",
       "OntologijaKomunikacijeUDobaAI": "Razine i entiteti (ova knjiga)"}


def slug(text: str) -> str:
    t = unicodedata.normalize("NFKD", text.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^\w\s\-]", "", t)
    return re.sub(r"\s+", "-", t.strip())


def anchors(path: str) -> set:
    try:
        txt = open(path, encoding="utf-8").read()
    except OSError:
        return set()
    out = set()
    for _, title in HEADING.findall(txt):
        s = slug(title)
        out.add(s)
        out.add(s.replace("-", ""))
    return out


def md_files():
    for sub in ("rukopis", "docs", "plan", "referencije"):
        d = os.path.join(ROOT, sub)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith(".md"):
                yield os.path.join(d, f)


def main():
    http = "--http" in sys.argv
    problems, cross_hits, warn, info = [], [], [], []

    for path in md_files():
        txt = open(path, encoding="utf-8").read()
        rel = os.path.relpath(path, ROOT)
        for _, target in MD_LINK.findall(txt):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            file_part, _, frag = target.partition("#")
            if not file_part:
                continue
            full = os.path.normpath(os.path.join(os.path.dirname(path), file_part))
            if not os.path.exists(full):
                problems.append(f"{rel}: ne postoji datoteka '{target}'")
                continue
            if frag and frag not in anchors(full):
                problems.append(f"{rel}: sidro '#{frag}' nema u '{os.path.relpath(full, ROOT)}'")
        hits = CROSS.findall(txt)
        if hits:
            cross_hits.append((rel, hits))
        for block in re.split(r"\n(?=#{2,3}\s)", txt):
            if not rel.startswith("rukopis"):
                continue  # pravilo "najviše dvije upute" vrijedi za rukopis, ne za popise/registre
            head = block.splitlines()[0][:60] if block.strip() else ""
            n = len(CROSS.findall(block))
            if n > 2:
                warn.append(f"{rel} · odjeljak '{head}' ima {n} uputa na druge knjige (pravilo: najviše 2)")

    # registar pojmova: postoji li datoteka kanonskog poglavlja
    reg = os.path.join(ROOT, "pojmovnik", "koncepti.yaml")
    if os.path.exists(reg):
        data = yaml.safe_load(open(reg, encoding="utf-8"))
        cekaju = {}
        for k in data.get("koncepti", []):
            kb, ch = (k.get("kanonski") or "").split("/")
            if kb == "razine":
                f = os.path.join(ROOT, "rukopis", f"poglavlje-{int(ch):02d}.md")
                if not os.path.exists(f):
                    cekaju.setdefault(int(ch), []).append(k["id"])
        if cekaju:
            info.append("poglavlja koja tek treba napisati (registar ih već najavljuje): "
                        + ", ".join(f"{c} ({len(v)} pojma)" for c, v in sorted(cekaju.items())))

    if http:
        seen = set()
        for _, urls in cross_hits:
            for u in urls:
                if u in seen:
                    continue
                seen.add(u)
                try:
                    req = urllib.request.Request(u, method="HEAD", headers={"User-Agent": "hermes-link-check"})
                    code = urllib.request.urlopen(req, timeout=20).status
                except Exception as e:
                    code = getattr(e, "code", "ERR")
                tag = "OK" if code == 200 else f"❗{code}"
                print(f"  [http] {tag} {u}")

    print(f"=== Mreža knjiga: provjera ({'lokalno + http' if http else 'lokalno'}) ===")
    print(f"upita na druge knjige: {sum(len(h) for _, h in cross_hits)} u {len(cross_hits)} datoteka")
    for rel, hits in cross_hits:
        knjige = sorted({OWN.get(u.rstrip('/').split('/')[-1], '?') for u in hits})
        print(f"  · {rel}: {len(hits)} → {', '.join(knjige)}")
    if warn:
        print("\n⚠ upozorenja:")
        for w in warn:
            print("   -", w)
    for i in info:
        print("\nℹ", i)
    if problems:
        print("\n❌ slomljene upute:")
        for p in problems:
            print("   -", p)
        return 1
    print("\n✔ nema slomljenih uputa")
    return 0


if __name__ == "__main__":
    sys.exit(main())
