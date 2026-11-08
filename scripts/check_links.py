#!/usr/bin/env python3
"""Check every font url still resolves, and Fontshare facts still match their API.

Usage: python3 scripts/check_links.py

Fails on dead links or Fontshare fact drift. Warns when a link lands on a known non-font page
(strike notice, parked domain). Needs the internet; run it by hand. Standard library only.
"""
import json
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "fonts.json").read_text())
UA = {"User-Agent": "no-slop-type link check"}
# Final URLs that mean "the site is up, but this isn't the font page".
SOFT_FAIL = ["velvetyne.fr/greve", "parked", "domain-for-sale"]


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as res:
        return res.status, res.geturl(), res.read()


def check_url(f):
    try:
        status, final, _ = fetch(f["url"])
    except urllib.error.HTTPError as e:
        return ("fail", f["id"], f"HTTP {e.code} {f['url']}")
    except Exception as e:  # DNS, timeout, TLS
        return ("fail", f["id"], f"{type(e).__name__}: {e} {f['url']}")
    if any(s in final for s in SOFT_FAIL):
        return ("warn", f["id"], f"{f['url']} lands on {final}")
    return ("ok", f["id"], None)


def check_fontshare():
    _, _, body = fetch("https://api.fontshare.com/v2/fonts?limit=200")
    api = {f["slug"]: f for f in json.loads(body)["fonts"]}
    problems = []
    for f in DATA["fonts"]:
        if f["license"] != "FFL":
            continue
        slug = f["url"].rstrip("/").rsplit("/", 1)[1]
        a = api.get(slug)
        if not a:
            problems.append(f"{f['id']}: '{slug}' no longer in the Fontshare API")
            continue
        styles = a["styles"]
        live = {
            "weights": sorted({s["weight"]["weight"] for s in styles if not s["is_variable"]}),
            "italics": any(s["is_italic"] for s in styles),
            "variable": any(s["is_variable"] for s in styles),
        }
        for key, value in live.items():
            if f[key] != value:
                problems.append(f"{f['id']}: {key} is {f[key]} in fonts.json, {value} on Fontshare")
    return problems


def main():
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check_url, DATA["fonts"]))
    fails = [r for r in results if r[0] == "fail"]
    warns = [r for r in results if r[0] == "warn"]
    for _, fid, msg in warns:
        print(f"  ⚠︎ {fid}: {msg}")
    for _, fid, msg in fails:
        print(f"  ✗ {fid}: {msg}")

    drift = check_fontshare()
    for msg in drift:
        print(f"  ✗ {msg}")

    ok = len(results) - len(fails) - len(warns)
    print(f"\n{ok} links ok, {len(warns)} warnings, {len(fails)} dead, {len(drift)} Fontshare mismatches")
    sys.exit(1 if fails or drift else 0)


if __name__ == "__main__":
    main()
