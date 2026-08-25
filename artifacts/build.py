#!/usr/bin/env python3
"""Build the per-phase study artifacts from artifacts/data/*.json.

Usage:  python3 artifacts/build.py            # build every phase
        python3 artifacts/build.py phase-2    # build one

Each data file produces artifacts/<name>.html, a self-contained page ready to
publish with the Artifact tool. URLs live in artifacts/artifacts.md — always
republish to the existing URL so the link the user has keeps working.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
T = ROOT / "template"
HEAD = """<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap">
<style>
"""

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
            + (T / "base.css").read_text()
            + (T / "phase.css").read_text()
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
    body = (T / "atlas.body.html").read_text().replace(
        "__DATA__", json.dumps(data, ensure_ascii=False))
    html = (HEAD.format(title="The Architect's Atlas")
            + (T / "base.css").read_text()
            + (T / "atlas.css").read_text()
            + "</style>\n" + body)
    out = ROOT / "atlas.html"
    out.write_text(html)
    n = sum(len(p["cs"]) for p in phases)
    cap = sum(1 for p in phases for c in p["cs"] if c.get("cap"))
    print(f"{'atlas.json':16} -> {'atlas.html':34} {n:2} concepts, {cap:3} captured, {len(html):,} bytes")
    return out


targets = sys.argv[1:] or [p.stem for p in sorted((ROOT / "data").glob("*.json"))]
for name in targets:
    stem = name.removesuffix(".json")
    if stem == "atlas":
        continue
    build(ROOT / "data" / (stem + ".json"))
if not sys.argv[1:] or "atlas" in [t.removesuffix(".json") for t in sys.argv[1:]]:
    build_atlas()
