---
date: 2026-03-26
tags:
  - first-year
  - M40016
---
> [!Theorem]
> Let $\sum_{n=1}^\infty$ be a [[series]] with **positive terms**.
> Suppose the [[Limits|limit]] of the ratio of consecutive terms exists:
> $$\lim_{n\to\infty} \frac{a_{n+1}}{a_n}=L$$
> * If $L\lt 1$ the **series converges**.
> * If $L\gt 1$ the **series diverges**.
> * If $L=1$, the test is **inconclusive**.

Proof:
For case $L\lt 1$.
Since $L\lt 1$, we can choose some $r$ such that $L\lt r\lt 1$.
By definition of a **limit**, there exists some $N\in\mathbb{N}$ such that for all $n\ge N$:
$$\frac{a_{n+1}}{a_n}\le r$$
Therefore, after index $N$, the **tail** of the **series** satisfies the [[Standard Ratio Test for Series|standard ratio test]] with $l=r\lt 1$.
This means that the **tail** **converges**.
The finite number of terms before $N$ do not affect **convergence**, so the entire series **converges**.

For case $L\gt 1$:
By definition of a **limit**, there exists some $N\in \mathbb{N}$ such that for all $n \ge N$:
$$\frac{a_{n+1}}{a_n}\ge 1$$
And so $a_{n+1}\ge a_n$.
This means that from index $N$ onwards, the terms are **monotonically increasing**.
Since the terms are **positive**, this guarantees that $a_n\not\to 0$ as $n\to\infty$.
Since the **sequence** of **terms** does not approach $0$, the series **diverges**.

