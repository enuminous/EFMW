# EFMW — review entry point

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


<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/EFMW) · [Published page](https://enuminous.github.io/EFMW/)

<details>
<summary>Recent repositories (9)</summary>

- [Oroboros](https://github.com/enuminous/Oroboros) · [README](https://github.com/enuminous/Oroboros/blob/main/README.md) · [Page](https://enuminous.github.io/Oroboros/)
- [P-NP](https://github.com/enuminous/P-NP) · [README](https://github.com/enuminous/P-NP/blob/main/README.md) · [Page](https://enuminous.github.io/P-NP/)
- [Research-Program](https://github.com/enuminous/Research-Program) · [README](https://github.com/enuminous/Research-Program/blob/main/README.md) · [Page](https://enuminous.github.io/Research-Program/)
- [I-Have-Guts](https://github.com/enuminous/I-Have-Guts) · [README](https://github.com/enuminous/I-Have-Guts/blob/main/README.md) · [Page](https://enuminous.github.io/I-Have-Guts/)
- [Wrights-Law](https://github.com/enuminous/Wrights-Law) · [README](https://github.com/enuminous/Wrights-Law/blob/main/README.md) · [Page](https://enuminous.github.io/Wrights-Law/)
- [Aristotle-eNuminous](https://github.com/enuminous/Aristotle-eNuminous) · [README](https://github.com/enuminous/Aristotle-eNuminous/blob/main/README.md) · [Page](https://enuminous.github.io/Aristotle-eNuminous/)
- [Multiverse-Simulator](https://github.com/enuminous/Multiverse-Simulator) · [README](https://github.com/enuminous/Multiverse-Simulator/blob/main/README.md) · [Page](https://enuminous.github.io/Multiverse-Simulator/)
- [accelerando-8192](https://github.com/enuminous/accelerando-8192) · [README](https://github.com/enuminous/accelerando-8192/blob/main/README.md) · [Page source](https://github.com/enuminous/accelerando-8192/blob/main/docs/index.html)
- [Codex-888](https://github.com/enuminous/Codex-888) · [README](https://github.com/enuminous/Codex-888/blob/main/README.md) · [Page](https://enuminous.github.io/Codex-888/)

</details>

<details>
<summary>Repository indexes (1)</summary>

- [index.html](https://github.com/enuminous/EFMW/blob/main/index.html) · [Open page](https://enuminous.github.io/EFMW/index.html)

</details>
<!-- ENUMINOUS-NETWORK:END -->

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
