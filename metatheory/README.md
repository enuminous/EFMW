# EFMW theory interface and open interpretability target

Lean 4.28.0; standard library only. Run `lake build` and
`lake env lean -DwarningAsError=true Audit.lean` here, or the front-door command.

`EFMW p` is a theory object **parameterized by a formal presentation `p`**.
Its background theory, sentences, consequence relation, 102 catalogue meanings,
and selected hypotheses are explicit. The catalogue is not automatically turned
into 102 true axioms: selected assumptions must be marked hypotheses, while
definitions and candidate conclusions have separate roles.

The open proposition is:

```lean
InterpretabilityTarget p target
```

It asks for a translation preserving derivations and contradiction into a
specified target theory. No concrete `p`, physical target theory, or witness of
this proposition is supplied. This is an interface and a research obligation,
not yet a first-order presentation or an interpretability result for EFMW.
Its deliberately abstract consequence relation must be replaced/instantiated
with concrete proof rules and checked translations before making that claim.

Two general conditional facts are proved: an interpretation preserves axioms,
and consistency of the target transfers to the source **if** such an
interpretation exists. These are standard structural facts; neither establishes
EFMW's consistency or physical validity.

## Required work

1. Fix a language and bind each catalogue row to actual typed mathematical syntax.
2. Separate definitions, independent hypotheses and desired conclusions; freeze the selection.
3. Specify proof rules and derive the consequence relation rather than furnishing arbitrary provability assertions.
4. Name a target theory with its axioms and logical strength; define the translation.
5. Prove translated assumptions and preservation of each inference rule without assuming the desired physical conclusions.
6. Demonstrate that the translation preserves the intended physical/mathematical meaning; avoid trivial translations into unrelated provable sentences.

Compiling this interface discharges none of these six obligations.
