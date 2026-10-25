import Std

/-! A theory interface, not a formalization of 102 physical equations.
The sentence meanings, inference rules and axiom selection remain explicit inputs.
No interpretation of the actual EFMW corpus is asserted to exist. -/
namespace EFMWMetatheory

universe u v

/-- A deductive theory with explicit syntax, assumptions and consequence relation. -/
structure Theory where
  Sentence : Type u
  axiomSet : Sentence → Prop
  derives : Sentence → Prop
  contradiction : Sentence
  derives_axiom : ∀ s, axiomSet s → derives s

/-- Presentations must distinguish definitions, hypotheses and candidate conclusions.
Having a catalogue identifier does not make a sentence an axiom or a theorem. -/
inductive Role where
  | definition | hypothesis | candidateConclusion
  deriving DecidableEq, Repr

structure Presentation where
  background : Theory.{u}
  catalogueSentence : Fin 102 → background.Sentence
  role : Fin 102 → Role
  selectedAssumption : Fin 102 → Prop
  selected_is_hypothesis : ∀ i, selectedAssumption i → role i = .hypothesis
  efmwDerives : background.Sentence → Prop
  includes_background : ∀ s, background.derives s → efmwDerives s
  includes_selected : ∀ i, selectedAssumption i → efmwDerives (catalogueSentence i)

/-- The EFMW theory object is parameterized by the still-required formal presentation. -/
def EFMW (p : Presentation.{u}) : Theory.{u} where
  Sentence := p.background.Sentence
  axiomSet := fun s => p.background.axiomSet s ∨
    ∃ i, p.selectedAssumption i ∧ p.catalogueSentence i = s
  derives := p.efmwDerives
  contradiction := p.background.contradiction
  derives_axiom := by
    intro s h
    rcases h with h | ⟨i, hi, rfl⟩
    · exact p.includes_background s (p.background.derives_axiom s h)
    · exact p.includes_selected i hi

/-- This interface is for proof-preserving translations. A concrete implementation
must justify inference preservation from specified proof rules, not assume a result. -/
structure Interpretation (source : Theory.{u}) (target : Theory.{v}) where
  translate : source.Sentence → target.Sentence
  preserves_contradiction : translate source.contradiction = target.contradiction
  preserves_derivations : ∀ s, source.derives s → target.derives (translate s)

def Consistent (t : Theory.{u}) : Prop := ¬ t.derives t.contradiction

/-- OPEN TARGET: a definition of the desired proposition, with no inhabitant supplied. -/
def InterpretabilityTarget (p : Presentation.{u}) (target : Theory.{v}) : Prop :=
  Nonempty (Interpretation (EFMW p) target)

/-- A general conditional metatheorem; it proves no particular theory consistent. -/
theorem consistency_transfer {s : Theory.{u}} {t : Theory.{v}}
    (i : Interpretation s t) (ht : Consistent t) : Consistent s := by
  intro hs
  apply ht
  rw [← i.preserves_contradiction]
  exact i.preserves_derivations s.contradiction hs

theorem interpretation_preserves_axioms {s : Theory.{u}} {t : Theory.{v}}
    (i : Interpretation s t) (a : s.Sentence) (ha : s.axiomSet a) :
    t.derives (i.translate a) :=
  i.preserves_derivations a (s.derives_axiom a ha)

end EFMWMetatheory
