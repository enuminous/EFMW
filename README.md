# EFMW — review entry point

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/EFMW) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#core-efmw-and-review)

<details open>
<summary><strong>On this page</strong></summary>

- [Which object is canonical?](#which-object-is-canonical)
- [Focused review and next tests](#focused-review-and-next-tests)
- [Search page and local engine](#search-page-and-local-engine)
- [MillieComplex EFMW model v2.1.0](#milliecomplex-efmw-model-v210)
- [EFMW Tutor](#efmw-tutor)
- [Scope](#scope)
- [Connected physics research units](#connected-physics-research-units)


</details>

**Related repositories:** [Monolithic_102_EFMW](https://github.com/enuminous/Monolithic_102_EFMW) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [EFMW_Post156_Zoo_Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit) · [papers](https://github.com/enuminous/papers) · [QST](https://github.com/enuminous/QST) · [EFMW-FULL](https://github.com/enuminous/EFMW-FULL) · [EFMW-Axioms](https://github.com/enuminous/EFMW-Axioms) · [EFMW-EXP-001](https://github.com/enuminous/EFMW-EXP-001) · [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


> **REVIEW · frozen target, 25 October 2026**
>
> **Canonical:** [Monolithic-102-Zoo-Lean4 · `efmw-review-2026-10-25`](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/tree/efmw-review-2026-10-25), commit [`01f51acb0b0e564105dcf7f14cc55998d41b91ce`](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/tree/01f51acb0b0e564105dcf7f14cc55998d41b91ce).
> **Pins:** root Lean **4.19.0** (no Mathlib); analytic Lean **4.28.0**, Mathlib **`8f9d9cff6bd728b17a24e163c9402775d9e6a365`**. All transitive pins are retained in the source manifests.
> **One build command:** `bash scripts/review.sh` from this repository, with Git, Python 3 and elan/Lake installed. It fetches the tag, verifies its full SHA, builds and audits both frozen packages, checks coverage, then builds the separate metatheory scaffold.
> **Coverage:** [coverage.json](coverage.json) · **Open work:** [obligations table](review/OPEN_OBLIGATIONS.md) · **Exact lock:** [review-lock.json](review-lock.json).
> **Observed frozen-source CI:** [successful run 38793976970](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/actions/runs/38793976970). This is a build result, not independent scientific review.

The review snapshot contains **53 structural encodings, 15 analytic models, one partial specialization and 33 open analytic entries**. ME-003 is proved only for the stated flat Minkowski specialization. A structural encoding or a conditional mathematical theorem does not establish the original physical interpretation.

## Which object is canonical?

| Object | Role for this review |
|---|---|
| `enuminous/Monolithic-102-Zoo-Lean4@01f51acb0b0e564105dcf7f14cc55998d41b91ce` | **Canonical.** Frozen catalogue and ME-003 specialization. Use the tag above and retain the full SHA in review records. |
| `enuminous/Monlithic_EFMW_102_Lean4@58f743bd44929049928d0b1d8beee9403c549a0d` | **Historical.** Earlier Aristotle package. Reviews of this object remain reviews of that object; they do not transfer to the canonical target. |
| Later commits in `Monolithic-102-Zoo-Lean4` | Subsequent research, including linearized gravity. Not silently included in this frozen snapshot. |

These hashes name different repositories, not interchangeable versions of one reviewed object. The canonical designation resolves review routing; it does not invalidate or absorb the older work. Never move this tag. A future scope change gets a new tag and review record.

## Focused review and next tests

- [ME-007 contracted-Bianchi review brief](review/BIANCHI_REVIEW.md): one consistency obligation, exact assumptions and a two-sentence request.
- [Alternative Zoo limiter](https://github.com/enuminous/Monolithic-Zoo-Lean4/blob/main/ALTERNATIVE_REPORT.md): executable PASS / FAIL / UNRESOLVED / N/A report, separate from the main Zoo report.
- [September 2 null-arm status](review/NULL_ARM_2026-09-02.md): original artifact recovery and reproducibility requirements.
- [Metatheory target](metatheory/README.md): a Lean theory interface and an explicitly unproved interpretability target.

<details>
<summary>Existing tutor, prototype and historical navigation</summary>

# EFMW Tutor and MillieComplex

> **External reviewers: START HERE → [Reviewed scope and reproduction guide](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/REVIEW_START_HERE.md) · [What this does not claim](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/WHAT_THIS_DOES_NOT_CLAIM.md) · [Claims-to-evidence register](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/CLAIMS_EVIDENCE_REGISTER.md).** These documents index evidence; they do not certify every repository.


This repository combines the EFMW tutoring project with an inspectable recursive state-model prototype and a simple search interface.

## Search page and local engine

The root [index.html](index.html) is a centered, minimal search page. It submits questions to the local Python engine at `/api/tutor`.

Run the page and engine locally:

```bash
python3 "MillieComplex EFMW AGI.py" --serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000).

By default, the engine updates its EFMW-inspired state and returns diagnostics, but it has no text-generation backend. To enable generated answers, install `torch` and `transformers`, then explicitly provide a compatible Hugging Face causal-language-model ID:

```bash
python3 "MillieComplex EFMW AGI.py" --serve --model-name MODEL_ID
```

This loads model weights at server startup and may require substantial memory or a download. The server binds only to `127.0.0.1`; it is intended for local use. Memory remains in-process unless a path is explicitly provided with `--memory ./agi_memory.json`.

## MillieComplex EFMW model v2.1.0

The Python prototype provides:

- A bounded recurrent vector update with configurable feedback and update rate.
- A signed logarithmic scalar transform.
- Provenance-aware memory records and optional JSON persistence.
- A state-stability diagnostic describing internal vector change only.
- An optional language adapter that is loaded only when explicitly requested.
- A local demo and four built-in checks.

Run the demo and checks:

```bash
python3 "MillieComplex EFMW AGI.py" --demo
python3 "MillieComplex EFMW AGI.py" --self-test
```

## EFMW Tutor

The Next.js tutoring app remains a separate interface. The v1 web app uses local JSON only; its `/api/tutor` route is a placeholder for future OpenAI-backed tutoring.

```bash
npm install
npm run dev
```

## Scope

This is a research prototype. The token-hash encoder is a deterministic feature sketch, not a semantic embedding. The state-stability score measures change in an internal vector; it does not establish truth, consciousness, intelligence, or a physical law. A formal result about this implementation would not by itself validate a model of nature.

</details>

<!-- ENUMINOUS-RESEARCH-CHAIN:START -->
## Connected physics research units

**Established-theory reconstructions and baseline laboratories:** [Standard-Model-Reduction](https://github.com/enuminous/Standard-Model-Reduction) · [Higgs-Gauge-Lab](https://github.com/enuminous/Higgs-Gauge-Lab) · [EFMW-Physics-Lab](https://github.com/enuminous/EFMW-Physics-Lab)

**Proposed quantum-geometry bridge:** [Base888-Quantum-Geometry](https://github.com/enuminous/Base888-Quantum-Geometry) · [QST-001](https://github.com/enuminous/Quantum-Gravity/blob/main/QST-001.md) · [QST-002](https://github.com/enuminous/QST/blob/main/QST-002.md)

**EFMW definitions, pressure-cycle model, and spacetime investigations:** [Canonical 102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean review](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [RHC-001: Rahasya pressure-cycle formalization](https://github.com/enuminous/papers/blob/main/RHC-001-EFMW-Rahasya-Pressure-Cycle-Formalization.md) · [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian) · [Cosmology](https://github.com/enuminous/Cosmology)

> **Interpretation:** Cross-links represent research dependencies and comparisons. The Standard Model and continuum gravity are inputs in current QST calculations; their emergence from Base888 and the physical status of the pressure cycle remain **UNRESOLVED**.
<!-- ENUMINOUS-RESEARCH-CHAIN:END -->
