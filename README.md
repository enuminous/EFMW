# EFMW Tutor and MillieComplex

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
