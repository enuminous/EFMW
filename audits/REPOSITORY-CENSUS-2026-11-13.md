# EFMW repository census — 2026-11-13

**Discovery method:** connected GitHub repository search `user:enuminous`, two pages of 100. **Returned:** 162 repository entries. Repository metadata are a snapshot of search results, not proof of exhaustive historical coverage. Source tree, full commit graph, build and dataset inspection were **not performed** by this census.

The previous navigation index reported 135 public repositories on 2026-10-27; this census returns 162 repository entries. A +27 count difference is **not** a verified creation count.

[Machine-readable inventory](REPOSITORY-CENSUS-2026-11-13.csv)

## Audit status
- Repository name/metadata discovery: COMPLETED for returned results
- All-file source-hash inventory: UNRESOLVED
- Complete internal/external link checking: UNRESOLVED
- Semantic equation-level contradiction detection: UNRESOLVED
- Lean/kernel rebuilds: NOT EXECUTED
- Independent empirical replay: NOT EXECUTED

## Required controls
1. Pin every repository default branch to an immutable commit.
2. Recursively enumerate trees and hash every file, retaining ignored and large-file exceptions.
3. Build typed edges: navigation, implements, derives, tests, replicates, contradicts, supersedes.
4. Identify exact and near duplicates, but do not count copied implementations as independent replication.
5. Parse and validate relative links, citations, theorem claims, dependency pins, and datasets.
6. Execute tests in isolated, pinned environments and preserve logs.
7. Assign PASS, FAIL or UNRESOLVED per check, with source paths and independent review.

No global EFMW PASS is justified by this census.
