#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
command -v git >/dev/null
command -v python3 >/dev/null
command -v lake >/dev/null || { echo 'Install elan/Lake and put it on PATH.' >&2; exit 2; }
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
readarray -t source_lock < <(python3 - "$root/review-lock.json" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))['canonical']
for key in ['repository', 'tag', 'commit']:
    print(d[key])
PY
)
git clone --quiet --branch "${source_lock[1]}" --single-branch "https://github.com/${source_lock[0]}.git" "$work/source"
test "$(git -C "$work/source" rev-parse HEAD)" = "${source_lock[2]}"
python3 "$root/scripts/check_review.py" "$work/source"
(
  cd "$work/source"
  lake build
  lake env lean -DwarningAsError=true Audit.lean
  python3 scripts/test_axiom_audit.py
  git diff --exit-code -- lean-toolchain lakefile.lean lake-manifest.json
)
(
  cd "$work/source/analysis"
  lake exe cache get
  lake build
  python3 scripts/check_coverage.py
  lake env lean -DwarningAsError=true Audit.lean
  python3 scripts/test_axiom_audit.py
  git diff --exit-code -- lean-toolchain lakefile.toml lake-manifest.json
)
(
  cd "$root/metatheory"
  lake build
  lake env lean -DwarningAsError=true Audit.lean
)
echo 'PASS: pinned source builds, axiom audits, coverage and separate metatheory scaffold.'
echo 'Open mathematical and empirical obligations remain open; see review/OPEN_OBLIGATIONS.md.'
