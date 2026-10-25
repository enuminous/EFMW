#!/usr/bin/env python3
"""Check the front-door ledger against the exact, clean frozen source tree."""
import collections
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def check(source):
    lock = json.loads((ROOT / "review-lock.json").read_text())["canonical"]
    coverage = json.loads((ROOT / "coverage.json").read_text())
    def git(*args):
        return subprocess.check_output(["git", "-C", str(source), *args], text=True).strip()
    assert git("rev-parse", "HEAD") == lock["commit"], "Wrong source commit"
    assert not git("status", "--porcelain", "--untracked-files=no"), "Modified tracked source"
    assert coverage["canonical_commit"] == lock["commit"]
    assert coverage["canonical_tag"] == lock["tag"]
    assert coverage["canonical_repository"] == lock["repository"]
    assert (source / "lean-toolchain").read_text().strip() == lock["lean_root"]
    assert (source / "analysis/lean-toolchain").read_text().strip() == lock["lean_analysis"]
    manifest = json.loads((source / "analysis/lake-manifest.json").read_text())
    assert next(p["rev"] for p in manifest["packages"] if p["name"] == "mathlib") == lock["mathlib_analysis"]
    digest = hashlib.sha256((source / "canonical/CANONICAL_102.md").read_bytes()).hexdigest()
    assert digest == coverage["canonical_source_sha256"] == lock["canonical_source_sha256"]
    original = json.loads((source / "zoo/equation-audit.json").read_text())["records"]
    analytic = json.loads((source / "analysis/coverage.json").read_text())["entries"]
    overlay = {r["id"]: r for r in analytic}
    expected = []
    for row in original:
        entry = {"id": row["id"], "formula": row["formula"],
                 "root_status": row["lean_status"],
                 "review_status": "structural_encoding" if row["lean_status"] == "typed_core" else overlay[row["id"]]["status"],
                 "source_obligation": row["immediate_obligation"], "dependencies": row["dependencies"]}
        if row["id"] in overlay:
            entry["analytic"] = overlay[row["id"]]
        expected.append(entry)
    assert coverage["entries"] == expected, "Coverage drift from pinned source"
    assert len(expected) == 102
    counts = dict(collections.Counter(r["review_status"] for r in expected))
    assert counts == coverage["counts"]
    print(json.dumps({"status": "PASS", "check": "source_identity_and_coverage", "commit": lock["commit"], "counts": counts}))


if __name__ == "__main__":
    check(Path(sys.argv[1]).resolve())
