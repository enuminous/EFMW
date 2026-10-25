import Lean
import EFMWTheory

open Lean in
run_cmd do
  let env ← getEnv
  let allowed : Array Name := #[``propext, ``Classical.choice, ``Quot.sound]
  let mut count := 0
  for (name, info) in env.constants.toList do
    if (`EFMWMetatheory).isPrefixOf name then
      if info.isUnsafe then
        throwError "Unsafe declaration {name}"
      let (_, state) := ((CollectAxioms.collect name).run env).run {}
      for ax in state.axioms do
        unless allowed.contains ax do
          throwError "Unapproved axiom {ax} used by {name}"
      count := count + 1
  if count == 0 then
    throwError "No declarations audited"
  logInfo m!"Metatheory interface axiom audit passed: {count} declarations."
