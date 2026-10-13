# EFMW Tutor and MillieComplex

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
