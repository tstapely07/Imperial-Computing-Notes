---
date: 2026-03-24
tags:
  - first-year
  - M40016
---
> [!Theorem]
> Every **bounded** [[Sequences|sequence]] of real numbers has a **convergent** [[Subsequences|subsequence]].

Proof:
The [[Monotone Subsequence Theorem]] states that every **sequence** has a **monotonic** **subsequence**.
* We assume this sequence is **increasing**. The proof for if it were **decreasing** is symmetrical.
This **subsequence** is **bounded** by the same **bounds** as the original **sequence**.
The [[Completeness Axiom]] states that the set of **terms** in the **sequence** has a [[Supremum and Infimum|supremum]] in $\mathbb{R}$:
$$L=\sup(A)$$
By definition of the **supremum**, if we decrease it by any amount $\epsilon\gt 0$, $L-\epsilon$ must no longer be an **upper bound**.
* This means there must be at least one term in the sequence, $x_N$, such that:
$$L-\epsilon\lt x_N\le L$$
Since the sequence is **increasing**, we now know that for all $n\ge N$:
$$L-\epsilon\lt x_n\le L$$
And so we reach the exact definition of the [[Limits|limit]]:
$$\forall \epsilon > 0, \exists N\in\mathbb{N} \text{ such that } \forall n > N : |x_n - L| < \epsilon$$
So the **subsequence** is indeed **convergent**.

