---
date: 2026-03-23
tags:
  - first-year
  - M40016
---
> [!Theorem]
> Let $(a_n)_{n\ge1}$, $(b_n)_{n\ge1}$, and $(c_n)_{n\ge1}$ be [[sequences]]. If $\lim_{n\to\infty}=L$ and $\lim_{n\to\infty}b_n=L$, and $\exists N_0\in\mathbb{N}\;s.t.\; \forall n\gt N_0:a_n\le c_n\le b_n$ then $\lim_{n\to\infty}c_n=L$.

Proof:
Let $\epsilon\gt 0$.
Because $\lim_{n\to\infty}a_n=L,\exists N_1\;s.t.\;\forall n\gt N_1:L-\epsilon\lt a_n\lt L+\epsilon$.
Because $\lim_{n\to\infty}b_n=L,\exists N_2\;s.t.\;\forall n\gt N_2:L-\epsilon\lt b_n\lt L+\epsilon$.
* Note that this is the same as the standard [[Limits|limit]] definition of $|a_n-L|\lt\epsilon$, but unpacked, since this form is more useful for later.
Now let $N=\max(N_0,N_1,N_2)$. For all $n\gt N$, the **sequence** bounds and both limit conditions hold simultaneously, therefore:
$$L-\epsilon\lt a_n\le c_n\le b_n\lt L+\epsilon$$
Now extracting $c_n$ from the middle of the inequality gives:
$$L-\epsilon\lt c_n\lt L+\epsilon$$
This is equivalent to:
$$|c_n-L|\lt \epsilon$$
Since for any $\epsilon\gt 0$ we found an $N$ such that $|c_n-L|\lt\epsilon$ for all $n\gt N$, we can conclude that $\lim_{n\to\infty}c_n=L$.


We can use the **sandwich theorem** to prove that the sequence $(a_n)_{n\gt1}=\frac{\sin n}{n}$.
We know that $\forall n:-1\le\sin n\le 1$
Now we can divide the inequality by $n$. Since $n\gt1$, $n$ is **strictly positive**, so the inequality signs do not flip:
$$-\frac{1}{n}\le \frac{\sin n}{n}\le \frac{1}{n}$$
Since $\lim_{n\to\infty}(-\frac{1}{n})=0$ and $\lim_{n\to\infty}(\frac{1}{n})=0$, we can apply the **sandwich theorem**, and conclude that the inner sequence must also converge to the same limit, and so:
$$\lim_{n\to\infty}\frac{\sin n}{n}=0$$