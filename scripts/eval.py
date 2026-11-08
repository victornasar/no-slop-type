#!/usr/bin/env python3
"""Run the /find-font briefs headlessly and check each answer against fonts.json.

Usage:
  python3 scripts/eval.py                 run every brief once
  python3 scripts/eval.py --runs 3        run every brief 3 times (catches flaky behaviour)
  python3 scripts/eval.py --only bakery   run one brief
  python3 scripts/eval.py --model sonnet  pass a model to claude
  python3 scripts/eval.py --recheck DIR   re-score saved answers without calling Claude

Each call runs `claude -p "/find-font <brief>"` from an empty temp folder, read-only.
Raw answers are saved to evals/runs/<timestamp>/. Standard library only.
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = json.loads((ROOT / "fonts.json").read_text())
BRIEFS = json.loads((ROOT / "evals" / "briefs.json").read_text())["briefs"]
BY_ID = {f["id"]: f for f in FONTS["fonts"]}
VOICE = {"loud", "experimental", "playful"}


def ask(brief, model):
    cmd = ["claude", "-p", f"/find-font {brief}", "--add-dir", str(ROOT),
           "--allowedTools", "Read", "Glob", "Grep"]
    if model:
        cmd += ["--model", model]
    with tempfile.TemporaryDirectory() as empty:
        res = subprocess.run(cmd, cwd=empty, capture_output=True, text=True, timeout=600)
    return res.stdout if res.returncode == 0 else f"[claude exited {res.returncode}]\n{res.stdout}\n{res.stderr}"


def parse_picks(answer):
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", answer, re.S)
    for block in reversed(blocks):
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            continue
        if isinstance(data.get("picks"), list):
            return data["picks"]
    return None


def candidates(role, scripts):
    """Fonts that pass AGENTS.md step 2 for this role."""
    out = []
    for f in FONTS["fonts"]:
        if role not in f["use"] or not set(scripts) <= set(f["scripts"]):
            continue
        if role == "body" and not (f["italics"] and len(f["weights"]) >= 2):
            continue
        if role == "ui" and len(f["weights"]) < 3:
            continue
        out.append(f)
    return out


def score(b, answer):
    """Return a list of failure messages; empty means pass."""
    picks = parse_picks(answer)
    if picks is None:
        return ["no ```json {\"picks\": ...}``` block in the answer"]
    fails = []
    scripts = b.get("scripts", [])
    roles = {}
    for p in picks:
        role, ids = p.get("role"), p.get("ids") or []
        roles[role] = ids
        unknown = [i for i in ids if i not in BY_ID]
        if unknown:
            fails.append(f"{role}: unknown ids {unknown}")
            continue
        expected = min(3, len(candidates(role, scripts)))
        if len(ids) != expected:
            fails.append(f"{role}: {len(ids)} ids, expected {expected}")
        for i in ids:
            f = BY_ID[i]
            if role not in f["use"]:
                fails.append(f"{role}: {i} lacks use tag '{role}'")
            if role == "body" and not (f["italics"] and len(f["weights"]) >= 2):
                fails.append(f"body: {i} needs italics and 2+ weights")
            if role == "ui" and len(f["weights"]) < 3:
                fails.append(f"ui: {i} needs 3+ weights")
            missing = set(scripts) - set(f["scripts"])
            if missing:
                fails.append(f"{role}: {i} lacks scripts {sorted(missing)}")
            if b.get("category") and f["category"] != b["category"]:
                fails.append(f"{role}: {i} is {f['category']}, expected {b['category']}")

    for alts in b.get("roles", []):
        if not any(r in roles for r in alts):
            fails.append(f"missing role: one of {alts}")

    tops = [BY_ID[ids[0]] for ids in roles.values() if ids and ids[0] in BY_ID]

    if b.get("pair") and len(tops) >= 2:
        a, c = tops[0], tops[1]
        if a["category"] == c["category"] and a["id"] != c["id"]:
            fails.append(f"pair: {a['id']} and {c['id']} are both {a['category']}")
        if not (set(a["feel"]) & set(c["feel"]) or "neutral" in a["feel"] + c["feel"]):
            fails.append(f"pair: {a['id']} and {c['id']} share no feel and neither is neutral")
        if sum(bool(set(f["feel"]) & VOICE) for f in (a, c)) > 1:
            fails.append(f"pair: both {a['id']} and {c['id']} are loud/experimental/playful")

    if b.get("replaces"):
        entry = next(x for x in FONTS["avoid"] if x["name"] == b["replaces"])
        first = picks[0]["ids"][0] if picks and picks[0].get("ids") else None
        if first not in entry["instead"]:
            fails.append(f"top pick {first} is not in {b['replaces']}'s replacements {entry['instead']}")

    if b.get("public_repo"):
        ffl = [f["id"] for f in tops if f["license"] == "FFL"]
        warned = re.search(r"public repo", answer, re.I)
        if ffl and not warned:
            fails.append(f"FFL top pick {ffl} without a public-repo warning")

    if b.get("top_use") and not any(b["top_use"] in f["use"] for f in tops):
        fails.append(f"no top pick has use '{b['top_use']}'")

    if b.get("top_feel_any") and not any(set(b["top_feel_any"]) & set(f["feel"]) for f in tops):
        fails.append(f"no top pick has feel in {b['top_feel_any']}")

    return fails


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--only", action="append")
    ap.add_argument("--model")
    ap.add_argument("--recheck", type=Path, help="re-score a saved run folder")
    args = ap.parse_args()

    briefs = [b for b in BRIEFS if not args.only or b["id"] in args.only]
    if not briefs:
        sys.exit(f"no briefs match {args.only}")
    jobs = [(b, n) for b in briefs for n in range(1, args.runs + 1)]

    if args.recheck:
        out = args.recheck
        answers = {}
        for b, n in jobs:
            path = out / f"{b['id']}-{n}.md"
            if path.exists():
                answers[(b["id"], n)] = path.read_text()
    else:
        out = ROOT / "evals" / "runs" / time.strftime("%Y%m%d-%H%M%S")
        out.mkdir(parents=True)
        print(f"Running {len(jobs)} call(s), saving to {out.relative_to(ROOT)}/ …", flush=True)
        with ThreadPoolExecutor(max_workers=4) as pool:
            results = pool.map(lambda j: (j, ask(j[0]["brief"], args.model)), jobs)
            answers = {}
            for (b, n), answer in results:
                (out / f"{b['id']}-{n}.md").write_text(answer)
                answers[(b["id"], n)] = answer

    failed = 0
    for b, n in jobs:
        answer = answers.get((b["id"], n))
        label = f"{b['id']}" + (f" #{n}" if args.runs > 1 else "")
        if answer is None:
            print(f"  ? {label}: no saved answer")
            failed += 1
            continue
        fails = score(b, answer)
        if fails:
            failed += 1
            print(f"  ✗ {label}", *fails, sep="\n      ")
        else:
            print(f"  ✓ {label}")

    print(f"\n{len(jobs) - failed}/{len(jobs)} passed. Answers in {out}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
