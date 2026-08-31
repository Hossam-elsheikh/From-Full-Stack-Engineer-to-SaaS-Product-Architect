#!/usr/bin/env python3
"""Build the study artifacts from artifacts/data/.

Usage:  python3 artifacts/build.py            # every phase, every story chapter, the atlas
        python3 artifacts/build.py phase-2    # one phase (the Atlas is not rebuilt)
        python3 artifacts/build.py story      # every story chapter
        python3 artifacts/build.py ch-01      # one story chapter

Phase data lives in data/phase-N.json; story chapters in data/story/ch-NN.json
with their drawings alongside in data/story/ch-NN.art.html. Each data file
produces a self-contained artifacts/<name>.html ready to publish with the
Artifact tool. URLs live in artifacts/artifacts.md — always republish to the
existing URL so the link the user has keeps working.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent
T = ROOT / "template"
STORY = ROOT / "data" / "story"
HEAD = """<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap">
<style>
"""

def css(*names: str) -> str:
    """Concatenate stylesheets. A stray `</style>` inside one silently ends the
    style block and dumps the rest of the CSS onto the page as text — so refuse."""
    out = []
    for n in names:
        t = (T / n).read_text()
        if "</style" in t:
            raise SystemExit(f"{n}: contains a closing </style> tag — it would end "
                             f"the style block early and render the rest as text")
        out.append(t)
    return "".join(out)

def build(path: pathlib.Path) -> pathlib.Path:
    data = json.loads(path.read_text())
    for key in ("phase", "title", "weeks", "lede", "concepts"):
        if key not in data:
            raise SystemExit(f"{path.name}: missing required key '{key}'")
    ids = [c["id"] for c in data["concepts"]]
    if len(ids) != len(set(ids)):
        raise SystemExit(f"{path.name}: duplicate concept ids")
    body = (T / "phase.body.html").read_text().replace(
        "__DATA__", json.dumps(data, ensure_ascii=False))
    html = (HEAD.format(title=data["title"])
            + css("base.css", "phase.css")
            + "</style>\n" + body)
    out = ROOT / (path.stem + ".html")
    out.write_text(html)
    print(f"{path.name:16} -> {out.name:34} {len(data['concepts']):2} concepts, "
          f"{sum(len(c.get('cards', [])) for c in data['concepts']):3} cards, {len(html):,} bytes")
    return out

def build_atlas() -> pathlib.Path:
    """The Atlas is generated from atlas.json plus every phase file, so a concept
    added to a phase appears on the map automatically."""
    a = json.loads((ROOT / "data" / "atlas.json").read_text())
    phases = []
    for p in a["phases"]:
        cs = []
        if p.get("sheet"):
            pd = json.loads((ROOT / "data" / (p["sheet"] + ".json")).read_text())
            for c in pd["concepts"]:
                cs.append({"i": c["id"], "t": c["t"], "cap": 1, "e": c["lede"],
                           "c": c.get("cards", []), "d": c.get("drill", "")})
        cs += p.get("ghosts", [])
        phases.append({"n": p["n"], "t": p["t"], "w": p["w"], "now": p.get("now", 0),
                       "sheet": p.get("url"), "cs": cs})
    data = {"phases": phases, "sims": a["sims"]}
    if a.get("serial"):
        data["serial"] = a["serial"]
    body = (T / "atlas.body.html").read_text().replace(
        "__DATA__", json.dumps(data, ensure_ascii=False))
    html = (HEAD.format(title="The Architect's Atlas")
            + css("base.css", "atlas.css")
            + "</style>\n" + body)
    out = ROOT / "atlas.html"
    out.write_text(html)
    n = sum(len(p["cs"]) for p in phases)
    cap = sum(1 for p in phases for c in p["cs"] if c.get("cap"))
    print(f"{'atlas.json':16} -> {'atlas.html':34} {n:2} concepts, {cap:3} captured, {len(html):,} bytes")
    return out


# ---------------------------------------------------------------- story chapters

def _rgb(h: str):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def accent_css(acc: dict) -> str:
    """One faded spot colour per chapter, emitted for all three theme states so no
    component rule ever needs a raw hex."""
    def block(h):
        r, g, b = _rgb(h)
        return (f"--acc:{h};--accBg:rgba({r},{g},{b},.12);"
                f"--accLine:rgba({r},{g},{b},.42)")
    return (f':root{{{block(acc["l"])}}}\n'
            f'@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{{block(acc["d"])}}}}}\n'
            f':root[data-theme="dark"]{{{block(acc["d"])}}}\n')

ART_KEY = re.compile(r"^<!--@\s*([a-z0-9][a-z0-9-]*)\s*-->\s*$")

def load_art(path: pathlib.Path) -> dict:
    """Drawings live in a sibling .art.html, one inline SVG per `<!--@ key -->` block."""
    if not path.exists():
        raise SystemExit(f"{path.name}: missing — the chapter's drawings go here")
    out, key, buf = {}, None, []
    for line in path.read_text().splitlines():
        m = ART_KEY.match(line)
        if m:
            if key:
                out[key] = "\n".join(buf).strip()
            key, buf = m.group(1), []
            if key in out:
                raise SystemExit(f"{path.name}: duplicate drawing key '{key}'")
        elif key is not None:
            buf.append(line)
    if key:
        out[key] = "\n".join(buf).strip()
    return out

def accent_classes(chapters) -> str:
    """The contents page shows every chapter's spot colour at once, so each gets a
    class rather than a :root block — still emitted for all three theme states."""
    def rules(sel_pre, key):
        return "".join(
            f'{sel_pre}.a{c["ch"]}{{--acc:{c["acc"][key]};'
            f'--accBg:rgba({",".join(map(str,_rgb(c["acc"][key])))},.12)}}'
            for c in chapters)
    return (rules("", "l") + "\n"
            + '@media (prefers-color-scheme:dark){'
            + rules(':root:not([data-theme="light"]) ', "d") + '}\n'
            + rules(':root[data-theme="dark"] ', "d") + "\n")

def build_serial() -> pathlib.Path:
    """The contents page: every book chapter, drawn or not yet."""
    data = json.loads((STORY / "index.json").read_text())
    for c in data["chapters"]:
        f = STORY / ("ch-" + c["ch"] + ".json")
        if f.exists():
            ch = json.loads(f.read_text())
            c["t"], c["acc"] = ch["title"], ch["acc"]
            c["log"], c["read"] = ch["gist"], ch["read"]
            c["figs"] = len({s["art"] for s in ch["sections"] if s.get("art")})
        elif isinstance(c.get("acc"), str):
            raise SystemExit(f"index.json: chapter {c['ch']} needs an acc pair")
    body = (T / "serial.body.html").read_text().replace(
        "__DATA__", json.dumps(data, ensure_ascii=False))
    html = (HEAD.format(title=data["title"])
            + css("base.css") + accent_classes(data["chapters"]) + css("serial.css")
            + "</style>\n" + body)
    out = ROOT / "story.html"
    out.write_text(html)
    drawn = sum(1 for c in data["chapters"] if c.get("url"))
    print(f"{'index.json':16} -> {out.name:34} {len(data['chapters']):2} chapters, "
          f"{drawn:3} drawn,     {len(html):,} bytes")
    return out

def gen_ratings(g: dict) -> str:
    """The star ratings every architecture-style chapter ends on. Same grammar in
    all nine so the styles can be compared by eye across sheets."""
    rows, lab, pip, gap = g["rows"], 190, 21, 6
    rh, top = 23, 34
    h = top + len(rows) * rh + 14
    out = [f'<svg viewBox="0 0 620 {h}" xmlns="http://www.w3.org/2000/svg">',
           '<g stroke="none" font-family="IBM Plex Mono, monospace">',
           f'<text x="0" y="13" font-size="8.6" letter-spacing="1.6" fill="var(--ink3)">'
           f'{g.get("head","ARCHITECTURE CHARACTERISTICS")}</text>',
           f'<text x="620" y="13" font-size="8.6" text-anchor="end" fill="var(--ink2)">'
           f'{g.get("scale","1 = weak   5 = strong")}</text>', '</g>']
    for i, r in enumerate(rows):
        name, score = r[0], int(r[1])
        note = r[2] if len(r) > 2 else ""
        y = top + i * rh
        strong = score >= 4
        col = "var(--acc)" if strong else "var(--ink)"
        out.append(f'<text x="{lab-12}" y="{y+4}" font-size="10" text-anchor="end" '
                   f'font-family="IBM Plex Mono, monospace" fill="var(--ink)">{name}</text>')
        for k in range(5):
            x = lab + k * (pip + gap)
            fill = col if k < score else "none"
            op = ' opacity=".92"' if k < score else ''
            out.append(f'<rect x="{x}" y="{y-8}" width="{pip}" height="13" fill="{fill}"'
                       f' stroke="{col if k < score else "var(--rule)"}" stroke-width="1.2"{op}/>')
        if note:
            out.append(f'<text x="{lab+5*(pip+gap)+8}" y="{y+4}" font-size="9" '
                       f'font-family="IBM Plex Mono, monospace" fill="var(--ink2)">{note}</text>')
    out.append("</svg>")
    return "\n".join(out)

GEN = {"ratings": gen_ratings}

def build_story(path: pathlib.Path) -> pathlib.Path:
    """One book chapter -> one review sheet: infographics for the topics, short
    scenes only where the book puts a decision."""
    data = json.loads(path.read_text())
    for key in ("ch", "book", "title", "pages", "gist", "read", "acc", "minute", "sections"):
        if key not in data:
            raise SystemExit(f"{path.name}: missing required key '{key}'")
    art = load_art(path.with_name(path.stem + ".art.html"))
    for i, sec in enumerate(data["sections"]):          # figures built from data
        if sec.get("gen"):
            kind = sec["gen"].get("kind")
            if kind not in GEN:
                raise SystemExit(f"{path.name}: unknown generated figure '{kind}'")
            key = f"_gen{i}"
            art[key] = GEN[kind](sec["gen"])
            sec["art"] = key
            del sec["gen"]
    used = [s["art"] for s in data["sections"] if s.get("art")]
    missing = sorted(set(used) - set(art))
    if missing:
        raise SystemExit(f"{path.name}: no drawing for {', '.join(missing)} "
                         f"in {path.stem}.art.html")
    for spare in sorted(k for k in set(art) - set(used) if not k.startswith("_gen")):
        print(f"  ! {path.stem}.art.html: '{spare}' is drawn but never placed")
    # only ship the drawings the sheet actually uses
    data["art"] = {k: art[k] for k in used}
    body = (T / "chapter.body.html").read_text().replace(
        "__DATA__", json.dumps(data, ensure_ascii=False))
    html = (HEAD.format(title=data["title"])
            + css("base.css") + accent_css(data["acc"]) + css("chapter.css")
            + "</style>\n" + body)
    out = ROOT / ("story-" + data["ch"] + ".html")
    out.write_text(html)
    dec = sum(1 for s in data["sections"] if s.get("k") == "decision")
    print(f"{path.name:16} -> {out.name:34} {len(data['sections']):2} sections, "
          f"{len(set(used)):3} figures, {dec} decisions, {len(html):,} bytes")
    return out


# ---------------------------------------------------------------- dispatch

def expand(names):
    for n in names:
        stem = n.removesuffix(".json").removeprefix("story/")
        if stem == "story":
            yield from (p.stem for p in sorted(STORY.glob("ch-*.json")))
            yield "serial"
        else:
            yield stem

args = sys.argv[1:]
targets = list(expand(args)) if args else (
    [p.stem for p in sorted((ROOT / "data").glob("*.json"))]
    + [p.stem for p in sorted(STORY.glob("ch-*.json"))] + ["serial"])

for stem in targets:
    if stem == "atlas":
        continue
    if stem in ("serial", "index"):
        build_serial()
    elif stem.startswith("ch-"):
        build_story(STORY / (stem + ".json"))
    else:
        build(ROOT / "data" / (stem + ".json"))

if not args or "atlas" in [a.removesuffix(".json") for a in args]:
    build_atlas()
