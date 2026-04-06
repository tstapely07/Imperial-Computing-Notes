---
date: 2026-03-24
tags:
  - first-year
  - M40016
---
> [!Theorem]
> If a **function** $f:[a,b]\to\mathbb{R}$ is [[Continuity|continuous]] on the **closed interval** $[a,b]$ then $f$ is **bounded** on that interval.

The proof is by **contradiction**:
Assume $f$ is not **bounded** above on $[a,b]$ 
If there is no **upper bound**, then for every $n\in\mathbb{N}$ we can find at least one $x_n\in[a,b]$ such that the **function's** output is strictly greater than $n$.
* This means we can construct a sequence $(x_n)_{n\ge1}$ where for all $n$:
$$f(x_n)\gt n$$
Now, since every $x_n\in[a,b]$, $(x_n)_{n\ge1}$ is a **bounded sequence**.
* By the [[Monotone Subsequence Theorem]] and the [[Completeness Axiom]], we know that $(x_n)_{n\ge1}$ must contain a **convergent** [[Subsequences|subsequence]].
* Let $(x_{n_k})_{k\ge1}$ be this **subsequence**, and let it **converge** to some [[Limits|limit]] $x_0$.
Since the **interval** is **closed**, the **limit** $x_0$ must also lie within $[a,b]$.
This means that, since $f$ is **continuous** everywhere in $[a,b]$:
$$\lim_{k\to\infty}f(x_{n_k})=f(x_0)$$
Because $f$ is a real-valued **function**, $f(x_0)$ must also be a finite real number.
However also, by the definition of our sequence, it must be true that $f(x_{n_k})\gt n_k$. 
* So as $k\to\infty$, $n_k\to\infty$, and therefore $f(x_{n_k}) \to \infty$.
This means that the outputs both approach a finite number, $f(x_0)$ but also that they explode to $\infty$.
* This is impossible, and therefore a **contradiction**.

Therefore $f$ must be **bounded above**.