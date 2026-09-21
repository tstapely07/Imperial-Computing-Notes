---
date: 2026-03-22
tags:
  - first-year
  - M40016
---
> [!Theorem]
> If $\lim_{n\to\infty} a_n=A$ and $\lim_{n\to\infty} b_n=B$ then $\lim_{n\to\infty}(a_n+b_n)=A+B$

Proof:
Let $\epsilon \gt 0$.
Since $a_n\to A$, $\exists N_1\in\mathbb{N}\;s.t.\; \forall n\gt N_1, |a_n-A|\lt \frac{\epsilon}{2}$
Likewise, since $b_n\to B$, $\exists N_2\in\mathbb{N}\;s.t.\; \forall n\gt N_2, |b_n-B|\lt \frac{\epsilon}{2}$

Let $N=\max(N_1,N_2)$. For all $n\gt N$, both conditions now hold simultaneously.

We need to show that $|(a_n+b_n)-(A+B)|\lt\epsilon$.
We can regroup the terms like so:
$$|(a_n)-A+(b_n)-B|$$
And now we can apply the [[Triangle Inequality (Calculus)|triangle inequality]]:
$$|(a_n)-A+(b_n)-B|\le |a_n-A|+|b_n-B|$$
We can now substitute our bounds:
$$|a_n-A|+|b_n-B|\lt \frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon$$
Therefore we have $|(a_n+b_n)-(A+B)|\lt\epsilon$, as desired.