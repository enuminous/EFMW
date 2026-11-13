# EFMW Cross-Repository Audit — Initial Evidence Report (2026-11-13)

**Status: PARTIAL / UNRESOLVED.** This report is an actual static inspection of 12 core repository READMEs at recorded blob SHAs, plus a repository-name discovery search returning 162 entries. It is **not** a complete source-tree, dataset, proof, build, link-target, or historical-commit audit.

## Inspected entry points

| Repository | README blob SHA | Unified nav marker | Explicit evidence-boundary wording |
|---|---|---|---|
| EFMW | 0dfe70d7974d930462ea44cd94d3cedebc228e6e | yes | yes |
| papers | fc6c8427d09b354bf15c40f9745fd2750bd8f62e | yes | yes |
| Monolithic-102-Zoo-Lean4 | 9a62de83639c15058935808c5ea7ff8d07c89884 | yes | yes |
| EFMW-EXP-001 | cb7c77ffb59758e2c08ba317ccb5039acc552457 | yes | yes |
| EFMW-FULL | 4914023e10c7b7a2f90e3168199c6f170dbd0aa7 | yes | yes |
| EFMW_Post156_Zoo_Audit | 4078b0d9bc3e9fd24b633839a35ddf38662430f8 | yes | yes |
| Tortoise | 74e309b0ce00da325694bbf1e1d7523b71227bf0 | yes | yes |
| Geometry | 48c0e0f6d0dcf1bf9e26c1ecfec1bc3506ef080c | **no** | **no lexical match** |
| Information-Tensor | b61cdab0a5da6d287a5a8e5daf0bca94066b075a | **no** | yes |
| Cosmology | 1e5bfdc467f78cab68ce29aeb2d23370ede931bc | yes | yes |
| EFMW-Lagrangian | 243ab3403603a175f526748b10004b900bd4cb9a | yes | yes |
| Monolithic | 14391f277d80194202f3915a5233b58e32fe3cca | yes | yes |

**Observed:** 10/12 have the unified navigation marker; 11/12 match the heuristic evidence-boundary wording. Missing markers do not prove missing navigation or scientific misrepresentation. Geometry's README explicitly states that physical detection remains unresolved, despite not matching the chosen evidence-boundary phrase.

## High-priority coherence issues

1. **Repository census drift:** prior index states 135 public repositories on 2026-10-27; current GitHub repository search `user:enuminous` returns 162 entries. Differences require a revision-aware census; no claim that all 27 are new.
2. **Canonical theorem scope:** 102-equation frozen Lean review distinguishes structural encodings, conditional mathematical results, and unresolved physical claims. ME-003's flat specialization is not a general curved-space proof.
3. **Replication boundary:** EFMW-FULL preserves historical EXP-001 implementations, not an independent second replication.
4. **Physical null:** HYP-001A naive null false-positive rate 99.9%; nuisance-adjusted rate 9.9%, above nominal 5%. Physical coupling remains unestablished.
5. **Introspection protocol:** INT-001 has no frozen 300-item corpus, custodian, numeric minimum effect or recall floor; no confirmatory PASS may be claimed.
6. **Navigation gap:** Geometry and Information-Tensor lack the unified marker in inspected README revisions. Add navigation without changing their experimental conclusions.
7. **Scientific claims:** link graphs are not proof graphs. Every claimed derivation needs a typed edge, source revision, and independent evidence level.

## Required full audit stages

- Inventory every accessible repository, default-branch head, file tree, licenses, releases, and frozen tags.
- Build a source-hashed index of all claim-bearing Markdown, Lean, Python, JSON, notebooks, and datasets.
- Extract and verify cross-repository and relative links; label typed relationships.
- Detect identical files and near-duplicates without conflating independent replications.
- Rebuild pinned Lean projects, verify assumptions and theorem scopes, and inspect CI at frozen SHAs.
- Re-execute frozen experiments in isolated environments; verify calibration, null controls, and negative results.
- Produce equation-level and dataset-level provenance maps; reconcile contradictory status claims.
- Publish independent-review findings with PASS/FAIL/UNRESOLVED, evidence paths, and explicit untested scope.

**Current verdict:** navigation coverage PARTIAL; complete EFMW coherence, code and empirical audit UNRESOLVED.
