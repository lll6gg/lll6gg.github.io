#!/usr/bin/env python3
"""Refresh GitHub star counts in assets/star_counts.json.

Run locally whenever you want fresh numbers:

    python3 scripts/update_stars.py
    git add assets/star_counts.json
    git commit -m "Refresh star counts"
    git push

The script walks every github/stars or dynamic/json badge URL in
_pages/about.md, queries the GitHub REST API once per unique repo, and
writes the result to assets/star_counts.json. If a single repo's call
fails, its previous value in the JSON is preserved. If you have a
GITHUB_TOKEN in your environment, it is used for higher rate limits.
"""
import json
import os
import re
import sys
import time
from pathlib import Path

import urllib.request
import urllib.error

ROOT = Path(__file__).resolve().parents[1]
ABOUT_MD = ROOT / "_pages" / "about.md"
OUT_JSON = ROOT / "assets" / "star_counts.json"
OUT_JSON.parent.mkdir(parents=True, exist_ok=True)

REPO_PATTERNS = [
    re.compile(r"img\.shields\.io/github/stars/([\w.-]+/[\w.-]+)"),
    re.compile(r"%5B%27([\w.-]+/[\w.-]+)%27%5D"),
    re.compile(r"github\.com/([\w.-]+/[\w.-]+)(?:[/)\s\"'])"),
]


def discover_repos() -> set[str]:
    text = ABOUT_MD.read_text()
    repos: set[str] = set()
    for pat in REPO_PATTERNS:
        for m in pat.findall(text):
            repo = m.split("?")[0].rstrip("/")
            # Drop trailing path segments (e.g. tree/main/UI-S1)
            owner, _, rest = repo.partition("/")
            name = rest.split("/")[0]
            if owner and name:
                repos.add(f"{owner}/{name}")
    return repos


def load_previous() -> dict:
    if OUT_JSON.exists():
        try:
            return json.loads(OUT_JSON.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def fetch_stars(repo: str, token: str | None) -> int | None:
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "star-counts-updater")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            payload = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"  ! HTTP {e.code} for {repo}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  ! {type(e).__name__} for {repo}: {e}", file=sys.stderr)
        return None
    stars = payload.get("stargazers_count")
    if stars is None:
        return None
    return int(stars)


def main() -> int:
    repos = discover_repos()
    print(f"discovered {len(repos)} repo(s)")

    data = load_previous()
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        print(
            "note: no GITHUB_TOKEN in env; using unauthenticated "
            "(60 req/hour limit)",
            file=sys.stderr,
        )

    successes = 0
    for repo in sorted(repos):
        stars = fetch_stars(repo, token)
        if stars is not None:
            data[repo] = stars
            print(f"  ✓ {repo}: {stars}")
            successes += 1
        else:
            kept = data.get(repo)
            if kept is None:
                print(f"  - {repo}: no previous value, will skip in JSON")
            else:
                print(f"  - {repo}: keeping previous value {kept}")
        time.sleep(0.2)

    OUT_JSON.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(f"wrote {OUT_JSON} ({successes}/{len(repos)} refreshed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
