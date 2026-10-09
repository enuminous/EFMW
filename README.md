# EFMW Tutor and MillieComplex

A structured Next.js tutor for learning EFMW concepts step by step, alongside an inspectable Python prototype for recursive state tracking.

## EFMW Tutor

The web app uses local JSON only. The `/api/tutor` route is a placeholder for a future OpenAI-backed tutor.

Run it locally:

```bash
npm install
npm run dev
```

## MillieComplex EFMW AGI — v2.0.0

[`MillieComplex EFMW AGI.py`](MillieComplex%20EFMW%20AGI.py) is a deterministic, EFMW-inspired state model. It adds:

- A bounded recurrent vector update with configurable feedback and update rate.
- A signed logarithmic scalar transform, with explicit finite-value handling.
- Memory records with source and epistemic-status fields; disk persistence is opt-in.
- A state-stability diagnostic that reports internal vector change only.
- An optional Hugging Face text-generation adapter, loaded only when explicitly constructed.
- A local deterministic demo and built-in self-tests.

Run the demo and checks with Python 3:

```bash
python3 "MillieComplex EFMW AGI.py" --demo
python3 "MillieComplex EFMW AGI.py" --self-test
```

To persist demo memory, pass a path explicitly:

```bash
python3 "MillieComplex EFMW AGI.py" --demo --memory ./agi_memory.json
```

The optional Transformers adapter requires `torch` and `transformers`; constructing it loads the selected model and may download model weights. It is never created on import or by the default demo. There is no network-accessible server or dynamic module execution in the default model.

## Scope

This is a research prototype. The state-stability score measures change in an internal vector; it does not establish truth, consciousness, intelligence, or a physical law. The token hash encoder is a deterministic feature sketch, not a semantic embedding. A formal proof about the code or its equations would not by itself validate a model of nature.
