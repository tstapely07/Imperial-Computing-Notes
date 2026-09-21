---
date: 2026-03-23
tags:
  - first-year
  - M40016
---
> [!Lemma]
> If a [[Sequences|sequence]] $(a_n)_{n\gt1}$ **converges** to a **non-zero** [[Limits|limit]], its terms are eventually strictly bounded away from zero.

Formally, if $\lim_{n\to\infty}a_n=A$ and $A\neq 0$, then $\exists N\;s.t.\; \forall n\gt N:|a_n|\gt \frac{|A|}{2}$.
Proof:
Let $\epsilon=\frac{|A|}{2}$, since $A\neq 0$, we have $\epsilon\gt 0$.
Since $(a_n)_{n\gt1}$ **converges**, we know $\exists N\in\mathbb{N}\;s.t.\forall n\gt N:|a_n-A|\lt \frac{|A|}{2}$
Now we apply the [[Triangle Inequality (Calculus)|reverse triangle inequality]] to the left side:
$$||a_n|-|A||\le |a_n-A|\lt \frac{|A|}{2}$$
This strictly implies that the distance between $|a_n|$ and $|A|$ is less than $\frac{|A|}{2}$:
$$-\frac{|A|}{2}\lt |a_n|-|A|\lt \frac{|A|}{2}$$
Adding $|A|$ to all parts of the inequality gives us bounds for $|a_n|$:
$$\frac{|A|}{2}\lt|a_n|\lt \frac{3|A|}{2}$$
Now we can conclude that $\forall n\gt N$:
$$|a_n|\gt \frac{|A|}{2}$$
This means that all terms after $N$ are closer to $A$ than they are to $0$, strictly bounding them away from $0$.