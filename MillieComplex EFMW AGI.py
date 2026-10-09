"""A small, inspectable EFMW-inspired recursive state model.

This is a research prototype, not an AGI and not a physical field solver.
Its scalar map and state-stability score are explicit mathematical operations.
They do not measure truth, consciousness, intelligence, or physical coherence.

Run a deterministic demonstration:
    python "MillieComplex EFMW AGI.py" --demo

Run built-in checks:
    python "MillieComplex EFMW AGI.py" --self-test

Serve the local page and API (a text model is optional):
    python "MillieComplex EFMW AGI.py" --serve
    python "MillieComplex EFMW AGI.py" --serve --model-name MODEL_ID

Persistence is opt-in. Without --memory, learned records live only in memory.
No model is downloaded, no modules are auto-loaded, and no server is started.
"""
from __future__ import annotations

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import hashlib
import json
import math
import os
import re
import tempfile
import time
import unittest
from urllib.parse import urlsplit
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Optional, Protocol

TOKEN_RE = re.compile(r"[\w'-]+", flags=re.UNICODE)
MODEL_VERSION = "2.1.0"


def efmw_scalar(value: float) -> float:
    """Original prototype's signed logarithmic transform, made total at zero."""
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("efmw_scalar requires a finite value")
    if value == 0.0:
        return 0.0
    return math.copysign(math.log1p(abs(value)), value)


@dataclass(frozen=True)
class AgentConfig:
    dimensions: int = 8
    update_rate: float = 0.35
    feedback_gain: float = 0.20
    max_state: float = 2.0

    def __post_init__(self) -> None:
        if not isinstance(self.dimensions, int) or self.dimensions < 2:
            raise ValueError("dimensions must be at least 2")
        if not all(math.isfinite(x) for x in (
            self.update_rate, self.feedback_gain, self.max_state
        )):
            raise ValueError("configuration values must be finite")
        if not 0.0 < self.update_rate <= 1.0:
            raise ValueError("update_rate must be in (0, 1]")
        if not 0.0 <= self.feedback_gain <= 1.0:
            raise ValueError("feedback_gain must be in [0, 1]")
        if self.max_state <= 0.0:
            raise ValueError("max_state must be positive")


@dataclass
class MemoryRecord:
    record_id: str
    topic: str
    content: str
    source: str
    epistemic_status: str
    created_at: float


@dataclass
class StepResult:
    step: int
    state: list[float]
    state_stability: Optional[float]
    state_change: Optional[float]
    memory_matches: list[str]
    interpretation: str = (
        "State stability describes change in this model's internal vector; "
        "it is not a truth or consciousness measure."
    )


class LanguageAdapter(Protocol):
    """Interface for an explicitly configured text-generation backend."""

    def generate(self, prompt: str, *, max_new_tokens: int = 128) -> str:
        ...


class TransformersAdapter:
    """Optional Hugging Face backend, loaded only when explicitly constructed.

    This class requires torch and transformers, and may download model weights.
    It is deliberately never instantiated automatically by this module.
    """

    def __init__(self, model_name: str, device: Optional[str] = None) -> None:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer

        self.torch = torch
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)
        self.model.eval()

    def generate(self, prompt: str, *, max_new_tokens: int = 128) -> str:
        if not 1 <= max_new_tokens <= 2048:
            raise ValueError("max_new_tokens must be between 1 and 2048")
        encoded = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        with self.torch.no_grad():
            output = self.model.generate(
                **encoded,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                pad_token_id=self.tokenizer.eos_token_id,
            )
        prompt_tokens = encoded["input_ids"].shape[-1]
        return self.tokenizer.decode(
            output[0][prompt_tokens:], skip_special_tokens=True
        )


class MemoryStore:
    """Provenance-aware memory; disk persistence is explicitly opt-in."""

    def __init__(self, path: Optional[Path] = None) -> None:
        self.path = Path(path).expanduser() if path else None
        self.records: list[MemoryRecord] = []
        if self.path and self.path.exists():
            self._load()

    def learn(
        self,
        topic: str,
        content: str,
        *,
        source: str = "user-provided",
        epistemic_status: str = "unverified input",
    ) -> MemoryRecord:
        topic, content = topic.strip(), content.strip()
        if not topic or not content:
            raise ValueError("topic and content must be non-empty")
        if not source.strip() or not epistemic_status.strip():
            raise ValueError("source and epistemic_status must be non-empty")
        digest = hashlib.sha256(
            f"{time.time_ns()}\0{topic}\0{content}".encode("utf-8")
        ).hexdigest()[:16]
        record = MemoryRecord(
            record_id=digest,
            topic=topic,
            content=content,
            source=source.strip(),
            epistemic_status=epistemic_status.strip(),
            created_at=time.time(),
        )
        self.records.append(record)
        self._save()
        return record

    def recall(self, query: str = "", limit: int = 5) -> list[MemoryRecord]:
        if limit < 1:
            return []
        terms = {t.casefold() for t in TOKEN_RE.findall(query)}
        def rank(record: MemoryRecord) -> tuple[int, float]:
            haystack = {t.casefold() for t in TOKEN_RE.findall(
                record.topic + " " + record.content
            )}
            return (len(terms & haystack), record.created_at)
        ranked = sorted(self.records, key=rank, reverse=True)
        if terms:
            ranked = [record for record in ranked if rank(record)[0] > 0]
        return ranked[:limit]

    def _load(self) -> None:
        assert self.path is not None
        try:
            payload = json.loads(self.path.read_text(encoding="utf-8"))
            self.records = [MemoryRecord(**item) for item in payload]
        except (OSError, json.JSONDecodeError, TypeError, KeyError) as exc:
            raise ValueError(f"Could not load memory file {self.path}: {exc}") from exc

    def _save(self) -> None:
        if self.path is None:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = json.dumps([asdict(r) for r in self.records], indent=2)
        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", dir=self.path.parent,
            prefix=self.path.name + ".", suffix=".tmp", delete=False
        ) as handle:
            temp_path = Path(handle.name)
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        try:
            os.replace(temp_path, self.path)
        finally:
            temp_path.unlink(missing_ok=True)


class MillieComplexModel:
    """Deterministic recursive state tracker inspired by the supplied sketch."""

    def __init__(
        self,
        config: AgentConfig = AgentConfig(),
        memory: Optional[MemoryStore] = None,
    ) -> None:
        self.config = config
        self.memory = memory or MemoryStore()
        self.state = [0.0] * config.dimensions
        self.steps = 0

    def encode(self, text: str) -> list[float]:
        """Stable signed token hashing into a bounded vector; not an embedding."""
        counts = [0.0] * self.config.dimensions
        tokens = TOKEN_RE.findall(text.casefold())
        for token in tokens:
            digest = hashlib.sha256(token.encode("utf-8")).digest()
            slot = int.from_bytes(digest[:4], "big") % self.config.dimensions
            sign = 1.0 if digest[4] & 1 else -1.0
            counts[slot] += sign
        scale = max(1.0, math.sqrt(len(tokens)))
        return [max(-1.0, min(1.0, value / scale)) for value in counts]

    def process(self, text: str) -> StepResult:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        previous = self.state[:]
        observation = self.encode(text)
        rate = self.config.update_rate
        gain = self.config.feedback_gain
        limit = self.config.max_state
        candidate = [
            efmw_scalar(x + gain * old)
            for x, old in zip(observation, previous)
        ]
        self.state = [
            max(-limit, min(limit, (1.0 - rate) * old + rate * new))
            for old, new in zip(previous, candidate)
        ]
        self.steps += 1
        differences = [a - b for a, b in zip(self.state, previous)]
        change = math.sqrt(sum(d * d for d in differences) / len(differences))
        stability = math.exp(-change)
        matches = [r.record_id for r in self.memory.recall(text, limit=3)]
        return StepResult(
            step=self.steps,
            state=[round(v, 6) for v in self.state],
            state_stability=round(stability, 6),
            state_change=round(change, 6),
            memory_matches=matches,
        )

    def respond(
        self,
        prompt: str,
        adapter: Optional[LanguageAdapter] = None,
        *,
        max_new_tokens: int = 128,
    ) -> dict[str, object]:
        """Update the state and optionally delegate language generation.

        Without an adapter, response is None rather than a fabricated answer.
        The adapter's text is not treated as evidence for the state metric.
        """
        step = self.process(prompt)
        if adapter is None:
            response = None
            status = "no language backend configured"
        else:
            response = adapter.generate(prompt, max_new_tokens=max_new_tokens)
            status = "language generated by configured adapter"
        return {
            "response": response,
            "language_status": status,
            "state": asdict(step),
        }

    def learn(
        self,
        topic: str,
        content: str,
        *,
        source: str = "user-provided",
        epistemic_status: str = "unverified input",
    ) -> dict[str, object]:
        record = self.memory.learn(
            topic, content, source=source, epistemic_status=epistemic_status
        )
        processed_length = efmw_scalar(len(content))
        return {
            "record_id": record.record_id,
            "topic": record.topic,
            "processed_length": round(processed_length, 6),
            "source": record.source,
            "epistemic_status": record.epistemic_status,
            "note": "The scalar is a transform of character count, not semantic learning.",
        }

    def snapshot(self) -> dict[str, object]:
        return {
            "model_version": MODEL_VERSION,
            "steps": self.steps,
            "state": [round(v, 6) for v in self.state],
            "memory_records": len(self.memory.records),
            "state_metric_scope": "internal state change only; not truth or awareness",
        }


def run_demo(memory: Optional[MemoryStore] = None) -> None:
    model = MillieComplexModel(memory=memory)
    model.learn(
        "EFMW hypothesis",
        "EFMW proposes recursive coherence across interacting states.",
        source="demo fixture",
        epistemic_status="hypothesis, not independently validated here",
    )
    prompts = [
        "A system observes its neighboring states.",
        "It updates its estimate using the previous state.",
        "A second observation changes the internal vector.",
        "The model records the source and status of remembered claims.",
    ]
    print("Deterministic EFMW-inspired state-model demo (not an LLM):")
    for prompt in prompts:
        result = model.process(prompt)
        print(json.dumps({"input": prompt, **asdict(result)}, ensure_ascii=False))
    print("Final snapshot:")
    print(json.dumps(model.snapshot(), indent=2))


def run_server(
    host: str,
    port: int,
    memory: MemoryStore,
    adapter: Optional[LanguageAdapter],
) -> None:
    """Serve the bundled page and a same-origin, localhost-only model API."""
    model = MillieComplexModel(memory=memory)
    static_root = Path(__file__).resolve().parent

    class Handler(BaseHTTPRequestHandler):

        def _json(self, status: int, payload: dict[str, object]) -> None:
            raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(raw)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(raw)

        def do_GET(self) -> None:
            path = urlsplit(self.path).path
            if path == "/api/health":
                self._json(200, {
                    "model_version": MODEL_VERSION,
                    "language_backend": adapter is not None,
                    "state_metric_scope": "internal state change only",
                })
                return
            if path not in ("/", "/index.html"):
                self.send_error(404, "No such page")
                return
            try:
                raw = (static_root / "index.html").read_bytes()
            except OSError:
                self.send_error(404, "index.html is missing")
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(raw)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(raw)

        def do_POST(self) -> None:
            if urlsplit(self.path).path != "/api/tutor":
                self.send_error(404, "No such endpoint")
                return
            try:
                size = int(self.headers.get("Content-Length", "0"))
                if size < 1 or size > 16_384:
                    self._json(413, {"error": "Send a prompt of at most 16 KB."})
                    return
                payload = json.loads(self.rfile.read(size))
                prompt = payload.get("prompt") if isinstance(payload, dict) else None
                if not isinstance(prompt, str) or not prompt.strip():
                    self._json(400, {"error": "Enter a non-empty prompt."})
                    return
                if len(prompt) > 8_000:
                    self._json(413, {"error": "Prompt is too long (8,000 characters max)."})
                    return
                result = model.respond(prompt, adapter)
                if adapter is None:
                    self._json(503, {
                        "error": "The EFMW state engine ran, but no language-generation model is configured. Start the server with --model-name MODEL_ID to enable text answers.",
                        "diagnostics": result["state"],
                    })
                    return
                self._json(200, {
                    "response": result["response"],
                    "diagnostics": result["state"],
                    "model_version": MODEL_VERSION,
                })
            except (json.JSONDecodeError, UnicodeDecodeError):
                self._json(400, {"error": "Request body must be valid UTF-8 JSON."})
            except (TypeError, ValueError):
                self._json(400, {"error": "Request must include a valid prompt."})

        def log_message(self, format: str, *args) -> None:
            # Keep the local log useful without echoing submitted prompt text.
            super().log_message(format, *args)

    server = ThreadingHTTPServer((host, port), Handler)
    server.daemon_threads = True
    print(f"MillieComplex {MODEL_VERSION} at http://{host}:{port}/")
    if adapter is None:
        print("State diagnostics enabled; configure --model-name for generated text.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()


class ModelTests(unittest.TestCase):
    def test_transform_is_odd_and_zero_safe(self) -> None:
        self.assertEqual(efmw_scalar(0), 0.0)
        self.assertAlmostEqual(efmw_scalar(-3), -efmw_scalar(3))

    def test_state_is_finite_and_bounded(self) -> None:
        model = MillieComplexModel()
        for _ in range(100):
            result = model.process("recursive state update; local evidence")
        self.assertTrue(all(math.isfinite(x) for x in result.state))
        self.assertTrue(all(abs(x) <= model.config.max_state for x in result.state))
        self.assertGreaterEqual(result.state_stability, 0.0)
        self.assertLessEqual(result.state_stability, 1.0)

    def test_memory_round_trip_and_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "memory.json"
            store = MemoryStore(path)
            store.learn("test", "remember this", source="fixture", epistemic_status="test")
            loaded = MemoryStore(path)
            found = loaded.recall("remember")
            self.assertEqual(len(found), 1)
            self.assertEqual(found[0].source, "fixture")
            self.assertEqual(found[0].epistemic_status, "test")

    def test_no_backend_is_reported_without_fabricating_text(self) -> None:
        result = MillieComplexModel().respond("What is EFMW?")
        self.assertIsNone(result["response"])
        self.assertEqual(result["language_status"], "no language backend configured")
        self.assertIn("state", result)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--demo", action="store_true", help="run a deterministic local demo")
    modes.add_argument("--self-test", action="store_true", help="run built-in checks")
    modes.add_argument("--serve", action="store_true", help="serve index.html and the local model API")
    parser.add_argument(
        "--memory", type=Path, default=None,
        help="opt into JSON persistence at this path (otherwise memory is in-process only)",
    )
    parser.add_argument("--host", default="127.0.0.1", help="bind address; defaults to localhost")
    parser.add_argument("--port", type=int, default=8000, help="local web port")
    parser.add_argument(
        "--model-name", default=None,
        help="optional Hugging Face causal language-model ID (loads weights on server start)",
    )
    args = parser.parse_args()
    if args.self_test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(ModelTests)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        raise SystemExit(0 if result.wasSuccessful() else 1)
    if args.serve:
        if not 1 <= args.port <= 65535:
            parser.error("--port must be between 1 and 65535")
        if args.host != "127.0.0.1":
            parser.error("The local model server binds only to 127.0.0.1")
        adapter = TransformersAdapter(args.model_name) if args.model_name else None
        run_server(args.host, args.port, MemoryStore(args.memory), adapter)
        return
    # Running the file defaults to the local demo; disk persistence requires
    # the user to pass --memory explicitly.
    run_demo(memory=MemoryStore(args.memory))


if __name__ == "__main__":
    main()
