---
date:
tags:
  - first-year
  - M40001
---
When designing [[synchronous circuits]], such as [[Synchronous Binary Counters|binary counters]], we follow a universal set of steps:
1. Determine the number of states required.
2. Determine the state [[State Transition Tables|transitions]].
3. Choose how the states will be represented:
	* A [[Edge-Triggered D-Type Flip-Flop|flip-flop]] per state.
	* Fewer **flip-flops** representing a [[binary]] number to store state.
4. Express the **state sequencing logic** as [[Boolean Algebra|Boolean expressions]] and minimise using [[Karnaugh maps]]
5. Express the **output logic** as **Boolean expressions** and minimise using **Karnaugh maps**.

In step 3, we must also choose how states are assigned.
* Different assignments can have an impact on the size of the final circuit.
* One way to test this is by trying every combination, but this quickly becomes unfeasible.
**Isomorphic assignments** are achieved by completing one or more columns.
* These result in the same circuit, since [[Edge-Triggered D-Type Flip-Flop|flip-flops]] have both $Q$ and $Q'$ as outputs.
When checking all states is unfeasible, we can use two **heuristics**:
* All states that have the same next state for the same input should be given adjacent assignments.
* The next states of a state produced by applying adjacent inputs should be given adjacent state assignments.

> [!Success] Tip
> In an exam, it is usually sufficient to pick the obvious choice of assignment.