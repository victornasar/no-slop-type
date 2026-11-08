#!/usr/bin/env python3
"""Measure which fonts are slop: AI defaults or everywhere on the web.

Usage:
  python3 scripts/measure_slop.py              generate sites with default Claude, measure, update
  python3 scripts/measure_slop.py --no-claude  measure evals/slop-samples/ and the last saved sites only
  python3 scripts/measure_slop.py --model sonnet

A font is slop when its AI rate >= AI_RATE, or its Google Fonts popularity rank <= GOOGLE_TOP.
AI rate = share of the generated sites that load a web font which use this font (sites on system fonts
say nothing about which font AI picks). It only counts once MIN_FONT_SITES sites load a web font. The script:
  - writes evidence (ai_rate, google_rank, measured) onto every avoid entry in fonts.json
  - saves a report to evals/slop/<date>.json and the generated sites to evals/slop/sites-<date>/
  - prints suggested avoid additions and catalog fonts crossing a threshold, for a human to decide

Claude runs from empty folders with user settings, skills, plugins and MCP off, so personal taste
doesn't hide the defaults. Standard library only.
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

AI_RATE = 0.15
GOOGLE_TOP = 40
MIN_FONT_SITES = 10

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "fonts.json"
SLOP = ROOT / "evals" / "slop"
SAMPLES = ROOT / "evals" / "slop-samples"

SITES = {
    "landing page": ["a meal-kit startup", "a B2B invoicing SaaS", "an AI note-taking app",
                     "a climate-tech nonprofit", "a mobile banking app"],
    "portfolio site": ["a product designer", "a wedding photographer", "a freelance developer",
                       "an architecture studio", "an illustrator"],
    "blog": ["a personal tech blog", "a travel writer", "a food blog",
             "a company engineering blog", "a parenting newsletter"],
    "dashboard": ["SaaS revenue analytics", "server monitoring", "a CRM pipeline",
                  "a personal finance tracker", "warehouse inventory"],
    "documentation site": ["a JavaScript library", "a public REST API", "a CLI tool",
                           "an internal design system", "a database product"],
    "online shop": ["a coffee roaster", "a sneaker brand", "a houseplant store",
                    "a skincare brand", "a bookshop"],
}
PROMPTS = [f"Build a {kind} for {subject}. Reply with the complete page as a single HTML file in one code "
           f"block, nothing else."
           for kind, subjects in SITES.items() for subject in subjects]

GENERIC = {
    "serif", "sans-serif", "monospace", "cursive", "fantasy", "system-ui", "emoji", "math", "fangsong",
    "inherit", "initial", "unset", "revert", "-apple-system", "blinkmacsystemfont", "segoe ui",
    "helvetica", "helvetica neue", "arial", "georgia", "times", "times new roman", "verdana", "tahoma",
    "menlo", "monaco", "consolas", "courier", "courier new", "sf mono", "sfmono-regular",
    "liberation mono", "apple color emoji", "segoe ui emoji", "noto color emoji",
    "iowan old style", "palatino", "palatino linotype", "book antiqua", "optima", "avenir", "avenir next",
    "charter", "trebuchet ms", "gill sans", "baskerville", "hoefler text", "american typewriter", "lucida grande",
}


def generate(prompt, model):
    cmd = ["claude", "-p", prompt, "--setting-sources", "project", "--disable-slash-commands",
           "--strict-mcp-config", "--tools", ""]
    if model:
        cmd += ["--model", model]
    with tempfile.TemporaryDirectory() as empty:
        res = subprocess.run(cmd, cwd=empty, capture_output=True, text=True, timeout=900)
    return res.stdout if res.returncode == 0 else ""


def fonts_in(text):
    """Distinct intended fonts in one site: first real name per font-family, plus loaded fonts."""
    found = set()
    for stack in re.findall(r"font-family\s*:\s*([^;}\n]+)", text, re.I):
        for name in stack.split(","):
            name = name.strip().strip("'\"").strip()
            if not name or name.startswith("var(") or name.lower().startswith("ui-"):
                continue
            if name.lower() not in GENERIC:
                found.add(name)
            break  # only the first real entry is the intended font
    for query in re.findall(r"fonts\.(?:googleapis\.com|bunny\.net)/css2?\?([^\"')\s>]+)", text):
        for fam in re.findall(r"family=([^:&;|]+)", query.replace("&amp;", "&")):
            found.add(fam.replace("+", " ").strip())
    for names in re.findall(r"import\s*\{([^}]+)\}\s*from\s*['\"]next/font/google['\"]", text):
        found |= {n.strip().replace("_", " ") for n in names.split(",") if n.strip()}
    for pkg in re.findall(r"@fontsource(?:-variable)?/([a-z0-9-]+)", text):
        found.add(pkg.replace("-", " ").title())
    if re.search(r"geist/font", text):
        found.add("Geist")
    return found


def canonical(names, known):
    lookup = {k.lower(): k for k in known}
    return {lookup.get(n.lower(), n) for n in names}


def catalog_names(font):
    """'Red Hat Display / Text' -> ['Red Hat Display', 'Red Hat Text']."""
    parts = [p.strip() for p in font["name"].split(" / ")]
    first = parts[0].split()
    return [parts[0]] + [p if " " in p else " ".join(first[:-1] + [p]) for p in parts[1:]]


def google_ranks():
    raw = urllib.request.urlopen("https://fonts.google.com/metadata/fonts", timeout=30).read().decode()
    data = json.loads(raw[raw.index("{"):])
    return {f["family"]: f["popularity"] for f in data["familyMetadataList"] if f.get("popularity")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-claude", action="store_true")
    ap.add_argument("--model")
    args = ap.parse_args()

    date = time.strftime("%Y-%m-%d")
    SLOP.mkdir(parents=True, exist_ok=True)
    sites = {}  # label -> text

    if args.no_claude:
        previous = sorted(SLOP.glob("sites-*"))
        if previous:
            sites |= {f"claude/{p.name}": p.read_text() for p in previous[-1].glob("*.html")}
    else:
        out = SLOP / f"sites-{date}"
        out.mkdir(exist_ok=True)
        print(f"Generating {len(PROMPTS)} sites with default Claude (≈ a few minutes each, 6 at a time)…", flush=True)
        with ThreadPoolExecutor(max_workers=6) as pool:
            for i, text in enumerate(pool.map(lambda p: generate(p, args.model), PROMPTS)):
                if text:
                    (out / f"{i:02d}.html").write_text(text)
                    sites[f"claude/{i:02d}"] = text

    for f in sorted(SAMPLES.glob("*/*")):
        if f.is_file():
            sites[f"{f.parent.name}/{f.name}"] = f.read_text(errors="ignore")

    if not sites:
        sys.exit("No sites to measure.")

    ranks = google_ranks()
    data = json.loads(FONTS.read_text())
    known = set(ranks) | {a["name"] for a in data["avoid"]} | {n for f in data["fonts"] for n in catalog_names(f)}

    counts = Counter()
    font_sites = 0
    for text in sites.values():
        found = canonical(fonts_in(text), known)
        font_sites += bool(found)
        counts.update(found)
    n = len(sites)
    enough = font_sites >= MIN_FONT_SITES
    rate = {font: round(c / font_sites, 3) for font, c in counts.items()} if font_sites else {}

    def is_slop(name):
        return (enough and rate.get(name, 0) >= AI_RATE) or ranks.get(name, 10**6) <= GOOGLE_TOP

    for a in data["avoid"]:
        a["ai_rate"] = rate.get(a["name"], 0.0) if enough else None
        a["google_rank"] = ranks.get(a["name"])
        a["measured"] = date

    avoid_names = {a["name"] for a in data["avoid"]}
    catalog = {name: f["id"] for f in data["fonts"] for name in catalog_names(f)}
    suggest_ai = sorted((x for x in rate if enough and rate[x] >= AI_RATE and x not in avoid_names and x not in catalog),
                        key=lambda x: -rate[x])
    suggest_web = sorted((x for x, r in ranks.items() if r <= GOOGLE_TOP and x not in avoid_names and x not in catalog),
                         key=lambda x: ranks[x])
    flagged = [{"id": catalog[x], "name": x, "ai_rate": rate.get(x, 0.0), "google_rank": ranks.get(x)}
               for x in catalog if is_slop(x)]
    stale = [a["name"] for a in data["avoid"] if not is_slop(a["name"])]

    FONTS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "build.py")], check=True)

    report = {
        "measured": date, "sites": n, "sites_with_web_font": font_sites, "ai_rate_counted": enough,
        "sources": dict(Counter(label.split("/")[0] for label in sites)),
        "thresholds": {"ai_rate": AI_RATE, "google_top": GOOGLE_TOP, "min_font_sites": MIN_FONT_SITES},
        "ai_rates": dict(sorted(rate.items(), key=lambda kv: -kv[1])),
        "suggest_avoid_ai": suggest_ai, "suggest_avoid_web": suggest_web,
        "catalog_flagged": flagged, "avoid_below_threshold": stale,
    }
    (SLOP / f"{date}.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")

    print(f"\n{n} sites measured ({report['sources']}), {font_sites} load a web font. Top AI picks (share of those):")
    if not enough:
        print(f"  ⚠︎ fewer than {MIN_FONT_SITES} sites load a web font: AI rates are shown but not used.")
    for font, r in list(report["ai_rates"].items())[:15]:
        tag = "avoid" if font in avoid_names else "CATALOG" if font in catalog else "new"
        print(f"  {r:6.1%}  {font}  [{tag}]  google #{ranks.get(font, '-')}")
    print(f"\nSuggested avoid additions (AI rate ≥ {AI_RATE:.0%}): {', '.join(suggest_ai) or 'none'}")
    print(f"Suggested avoid additions (Google top {GOOGLE_TOP}): {', '.join(suggest_web) or 'none'}")
    print(f"Catalog fonts crossing a threshold: {', '.join(x['name'] for x in flagged) or 'none'}")
    label = "below both thresholds" if enough else f"not in Google top {GOOGLE_TOP} (AI data too thin to judge)"
    print(f"Avoid entries {label}: {', '.join(stale) or 'none'}")
    print(f"\nReport: {(SLOP / f'{date}.json').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
