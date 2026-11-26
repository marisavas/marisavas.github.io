#!/usr/bin/env python3
"""Build _data/publications.json from the .bib files in this folder.

Run from the _bibliography folder:  python3 build_data.py
No extra packages needed. Each .bib file becomes one section on the Publications page.
"""
import json
import re
import unicodedata

SECTIONS = [
    ("journals", "Journal articles", "journals.bib"),
    ("conferences", "Conference papers", "conferences.bib"),
    ("workshops", "Workshop and short papers", "workshops.bib"),
    ("abstracts", "Extended abstracts and posters", "abstracts.bib"),
]
OUTPUT = "../_data/publications.json"
ME = "Vasconcelos"

ACCENTS = {"'": "\u0301", "`": "\u0300", "^": "\u0302", "~": "\u0303", '"': "\u0308", "c": "\u0327"}


def latex_to_text(s):
    s = re.sub(r"\\i\b", "i", s)

    def repl(m):
        mark, letter = m.group(1), m.group(2)
        return unicodedata.normalize("NFC", letter + ACCENTS[mark])
    s = re.sub(r"\\([\'`^~\"c])\s*\{?\s*([A-Za-z])\s*\}?", repl, s)
    s = s.replace("\\&", "&").replace("--", "\u2013")
    s = s.replace("{", "").replace("}", "")
    return " ".join(s.split())


def field(body, name):
    m = re.search(r"\b" + name + r"\s*=\s*", body, re.I)
    if not m:
        return ""
    i = m.end()
    if body[i] == "{":
        depth, j = 0, i
        while j < len(body):
            if body[j] == "{":
                depth += 1
            elif body[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        return body[i + 1:j].strip()
    if body[i] == '"':
        return body[i + 1:body.index('"', i + 1)].strip()
    return re.match(r"[^,\n}]+", body[i:]).group(0).strip()


def short_name(a):
    a = " ".join(a.split())
    if "," in a:
        last, first = [x.strip() for x in a.split(",", 1)]
    else:
        toks = a.split(" ")
        k = len(toks) - 1
        if toks[-1] in ("Jr", "Jr.") and len(toks) > 2:
            k -= 1
        while k > 1 and toks[k - 1].lower() in ("de", "da", "do", "dos", "das"):
            k -= 1
        last, first = " ".join(toks[k:]), " ".join(toks[:k])
    if ME in last:
        return "M. Vasconcelos", True
    initials = " ".join(p[0] + "." for p in first.replace("-", " ").split() if p)
    return (initials + " " + last).strip(), False


def parse(path):
    items = []
    text = open(path, encoding="utf-8").read()
    for chunk in re.split(r"\n(?=@)", text):
        if not chunk.strip().startswith("@"):
            continue
        authors = []
        for a in re.split(r"\s+and\s+", latex_to_text(field(chunk, "author"))):
            if a.strip():
                name, is_me = short_name(a)
                authors.append({"name": name, "me": is_me})
        doi = field(chunk, "doi")
        url = field(chunk, "url") or ("https://doi.org/" + doi if doi else "")
        year = field(chunk, "year")
        items.append({
            "title": latex_to_text(field(chunk, "title")).rstrip("."),
            "authors": authors,
            "venue": latex_to_text(field(chunk, "booktitle") or field(chunk, "journal")),
            "year": int(re.sub(r"\D", "", year) or 0),
            "award": latex_to_text(field(chunk, "award")),
            "url": url,
        })
    items.sort(key=lambda x: -x["year"])
    return items


data = []
for key, label, path in SECTIONS:
    try:
        entries = parse(path)
    except FileNotFoundError:
        print("Skipping " + path + " (not found)")
        continue
    data.append({"key": key, "label": label, "entries": entries})
    print(label + ": " + str(len(entries)))

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("Wrote " + OUTPUT)