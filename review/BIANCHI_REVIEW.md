# One-row review: ME-007 contracted-Bianchi consistency

**Target:** [ME-007 at `01f51acb0b0e564105dcf7f14cc55998d41b91ce`](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/01f51acb0b0e564105dcf7f14cc55998d41b91ce/Monolithic102/ME007.lean).
**Obligation:** `ME-007-BIANCHI`. **Current status: UNRESOLVED.**

The catalogue states `G_μν + Λ g_μν = 8πG (T_μν + κ I_μν)`.
For a Levi-Civita connection, sufficient regularity, metric compatibility,
constant Λ and nonzero constant G, contracted Bianchi requires conservation
of the **total** source. If κ is constant this is
`∇^μ T_μν + κ ∇^μ I_μν = 0`. If κ varies, retain the extra
`(∇^μ κ) I_μν` product term. Separately conserved T does not establish
conservation of I. Assuming the required conservation to prove it is circular.

The pinned file is a catalogue descriptor; it does not define nonlinear
geometry, an informational tensor, its dynamics, or a proof of that conservation
law. A valid review can therefore confirm the gap and specify the smallest
missing definitions. It is not a request to prove all 102 equations.

## Two-sentence request

Could you check only ME-007’s contracted-Bianchi consistency obligation at `enuminous/Monolithic-102-Zoo-Lean4@01f51acb0b0e564105dcf7f14cc55998d41b91ce`, with the assumptions and missing definitions recorded in this brief?
Please return either a checked derivation of total-source conservation under those assumptions or the precise missing premise/counterexample; no review of the rest of the corpus is requested.

## Later work and scope boundary

The later [linearized-gravity module](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/2ee2abd51cbe25aa54fd6c244dc67f72e5a36085/analysis/LinearizedGravity.lean)
contains a flat linearized `contracted_bianchi` result and source-necessity
theorems for other specified models. Those results are not in the canonical
snapshot and do not close the nonlinear ME-007 informational-source obligation.

## Review record

Record reviewer, reviewed full SHA, definitions inspected, build command and
outcome, theorem/premise inspected, disposition and remaining obligations.
No reviewer commitment or endorsement has been obtained by creating this brief.

Reference for the standard geometric identity and matter-source conservation: David Tong, [General Relativity, sections 3.4.1 and 4.5](https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S4.html). Applying that constraint to the proposed informational tensor is the open EFMW obligation.
