---
date: 2026-03-23
tags:
  - first-year
  - M40016
---
> [!Theorem]
> If $\lim_{n\to\infty} a_n=A\neq0$ then $\lim_{n\to\infty}\left( \frac{1}{a_n} \right)=\frac{1}{A}$

Proof:
Let $\epsilon\gt 0$.
We require $\left| \frac{1}{a_n} - \frac{1}{A} \right|\lt\epsilon$
Through some algebraic manipulation, we can reach:
$$\left| \frac{1}{a_n} - \frac{1}{A} \right| = \left| \frac{A - a_n}{a_n A} \right| = \frac{|a_n - A|}{|a_n||A|}$$
Since we know a [[Sequences|sequence]] with a **non-zero** [[Limits|limit]] is [[Bounding Away from Zero|bounded away from zero]], we know $\exists N_1\;s.t.\;\forall n\gt N_1:|a_n|\gt \frac{|A|}{2}$.
We can reciprocate both sides to get:
$$\frac{1}{|a_n|}\lt \frac{2}{|A|}$$
Using this and our previous expression, we get:
$$\frac{|a_n - A|}{|a_n||A|} < \frac{2|a_n - A|}{|A|^2}$$
Now, since $\lim_{n\to\infty}a_n=A$, we can take $\epsilon=\frac{\epsilon|A|^2}{2}$, to get:
$$\exists N_2\;s.t.\;\forall n\gt N_2:|a_n-A|\lt \frac{\epsilon|A|^2}{2}$$
Now let $N=\max(N_1,N_2)$, for all $n\gt N$:
$$\left|\frac{1}{a_n}-\frac{1}{A}\right|\lt \frac{2}{|A|^2}\left( \frac{\epsilon|A|^2}{2} \right)=\epsilon$$
So we can conclude:
$$\lim_{n\to\infty} \frac{1}{a_n}=\frac{1}{A}$$
