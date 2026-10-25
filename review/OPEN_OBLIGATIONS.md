# Open obligations at the frozen review target

Target: `enuminous/Monolithic-102-Zoo-Lean4@01f51acb0b0e564105dcf7f14cc55998d41b91ce`.
Statuses below describe obligations, not the success of compiling the catalogue.

| ID | Obligation | Status | Evidence required to close |
|---|---|---|---|
| ME-007-BIANCHI | Define the informational stress tensor and prove total-source conservation compatible with the contracted Bianchi identity. | UNRESOLVED | Geometric definitions, regularity, constant/variable-coupling convention, and a non-circular derivation of `∇^μ(T_μν + κ I_μν)=0`; distinguish necessity from existence. |
| ME-003-COVARIANT | Extend the flat `(+---)` specialization to a specified curved covariant d’Alembertian. | UNRESOLVED | Connection, inverse metric, second covariant derivatives and equivalence proof; flat result alone does not discharge it. |
| ANALYTIC-33 | Provide explicit analytic semantics for the 33 entries marked `open` in this snapshot. | UNRESOLVED | Per-row definitions and scoped theorems. See `../coverage.json`; later research must be reviewed at its own commit. |
| PHYSICAL-ID | Identify symbols, dimensions, observables, boundary conditions and established limits for physical claims. | UNRESOLVED | Specified physical models and independent empirical tests, separate from Lean builds. |
| NULL-2026-09-02 | Reproduce the historical 1,500-stream ablation and evaluate its randomized coefficient null. | UNRESOLVED | Original generator/runner, coefficient law, calibration and test seeds, endpoint definition and raw per-stream outcomes. |
| META-INTERPRETATION | Supply a non-circular interpretation into a specified target theory. | UNRESOLVED | Concrete syntax, axioms and proof rules; translation; axiom preservation; inference preservation; nontrivial scope; see `../metatheory/README.md`. |

The main Zoo report and the alternative limiter report have different purposes.
Neither label upgrades an unfinished physical or empirical obligation.
