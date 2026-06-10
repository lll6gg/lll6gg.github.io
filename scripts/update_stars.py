#!/usr/bin/env python3
"""Refresh star counts for every github/stars badge referenced in about.md.

On per-repo failure we keep the previous value; on global failure (e.g. the
whole API is down) the existing JSON is left untouched so the badges keep
showing the last good number.
"""
import json
import os
import re
import sys
import time
from pathlib import Path

import requests

ABOUT_MD = Path("_pages/about.md")
OUT_DIR = Path("results")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_JSON = OUT_DIR / "star_counts.json"

# Match owner/repo in shields URLs and our own dynamic JSON badges
REPO_PATTERNS = [
    re.compile(r"img\.shields\.io/github/stars/([\w.-]+/[\w.-]+)"),
    re.compile(r"%5B%27([\w.-]+/[\w.-]+)%27%5D"),  # %5B'owner/repo'%5D
    re.compile(r"\['([\w.-]+/[\w.-]+)'\]"),
]


def discover_repos() -> set[str]:
    text = ABOUT_MD.read_text()
    repos: set[str] = set()
    for pat in REPO_PATTERNS:
        for m in pat.findall(text):
            # strip query-string artefacts
            repos.add(m.split("?")[0])
    return repos


def load_previous() -> dict[str, int | None]:
    # Workflow seeds this from the star-stats branch into ./results/.
    if OUT_JSON.exists():
        try:
            return json.loads(OUT_JSON.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def fetch_stars(repo: str, headers: dict[str, str]) -> int | None:
    try:
        r = requests.get(
            f"https://api.github.com/repos/{repo}",
            headers=headers,
            timeout=15,
        )
    except requests.RequestException as e:
        print(f"  ! network error for {repo}: {e}", file=sys.stderr)
        return None
    if r.status_code != 200:
        print(f"  ! HTTP {r.status_code} for {repo}", file=sys.stderr)
        return None
    try:
        return int(r.json().get("stargazers_count"))
    except (ValueError, TypeError):
        print(f"  ! malformed payload for {repo}", file=sys.stderr)
        return None


def main() -> int:
    repos = discover_repos()
    print(f"discovered {len(repos)} repo(s)")

    data = load_previous()
    token = os.environ.get("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "star-counts-updater",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    successes = 0
    for repo in sorted(repos):
        stars = fetch_stars(repo, headers)
        if stars is not None:
            data[repo] = stars
            print(f"  ✓ {repo}: {stars}")
            successes += 1
        else:
            kept = data.get(repo)
            if kept is None:
                # First time we see this repo and the call failed — leave the
                # key absent so shields doesn't render a confusing zero.
                print(f"  - {repo}: no previous value, skipping")
            else:
                print(f"  - {repo}: keeping previous value {kept}")
        # Be a courteous client even with auth in place.
        time.sleep(0.2)

    OUT_JSON.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(f"wrote {OUT_JSON} ({successes}/{len(repos)} refreshed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
