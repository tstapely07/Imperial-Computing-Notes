---
date: 2026-03-22
tags:
  - first-year
  - M40016
---
> [!Theorem]
> If $\lim_{n\to\infty} a_n=A$, then $\lim_{n\to \infty}(-a_n)=-A$

Proof:
Let $\epsilon > 0$.
Because $\lim_{n \to \infty} a_n = A$, we know there exists some $N \in \mathbb{N}$ such that for all $n > N$:
$$|a_n - A| < \epsilon$$
Now examine the sequence $(-a_n)$. For all $n > N$, we have:
$$|(-a_n) - (-A)| = |-a_n + A| = |-(a_n - A)| = |a_n - A|$$
Since we already established that $|a_n - A| < \epsilon$, it directly follows that:
$$|(-a_n) - (-A)| < \epsilon$$
So $\lim_{n \to \infty} (-a_n) = -A$.