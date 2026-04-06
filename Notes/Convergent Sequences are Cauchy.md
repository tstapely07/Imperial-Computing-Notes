---
date: 2026-03-24
tags:
  - first-year
  - M40016
---
> [!Theorem]
> If a **sequence** $(a_n)_{n\ge1}$ **converges**, then $(a_n)_{n\ge1}$ is a **Cauchy sequence**.

Proof:
Let $\epsilon\gt 0$.
Because $\lim_{n\to\infty}a_n=A$, we can choose $\epsilon=\frac{\epsilon}{2}$ and know that there exists an $N\in\mathbb{N}$ such that for all $n\gt N$:
$$|a_n-A|\lt \frac{\epsilon}{2}$$
Now take $m,n\gt N$. We want to consider the distance $|a_n-a_m|$.
By adding and subtracting $A$ we obtain:
$$|a_n-a_m|=|a_n-a+a-a_m|$$
We can apply the [[Triangle Inequality (Calculus)|inequality]] to get:
$$|a_n-a_m|\le |a_n-a|+|a-a_m|=|a_n-a|+|a_m-a|$$
Now since $m,n\gt N$, we can conclude that:
$$|a_n-a|+|a_m-a|\lt \frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon$$
And so for all $m,n\gt N:|a_n-a_m|\lt\epsilon$, and so the sequence is **Cauchy**.
