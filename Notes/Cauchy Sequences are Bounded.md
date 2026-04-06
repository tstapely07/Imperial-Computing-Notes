---
date: 2026-03-23
tags:
  - first-year
  - M40016
---
> [!Theorem]
> Every [[Cauchy sequence]] is **bounded**.

Proof:
Let $\epsilon=1$. Because the sequence is **Cauchy**, there exists an $N\in\mathbb{N}$ such that for all $m,n\gt N$:
$$|a_n-a_m|\lt 1$$
Now let $n=N+1$. Clearly this maintains that $n\gt N$. Substituting this into the inequality gives:
$$|a_{N+1}-a_m|\lt 1$$
We want to find a bound for $|a_m|$. To do so, we first add and subtract the term $a_{N+1}$ inside the absolute value:
$$|a_m| = |a_m - a_{N+1} + a_{N+1}|$$
Now, we apply the [[Triangle Inequality (Calculus)|triangle inequality]]:
$$|a_m|=|a_m - a_{N+1} + a_{N+1}| \le |a_m - a_{N+1}| + |a_{N+1}|$$
Now, we know that $|a_m - a_{N+1}| < 1$, and so:
$$|a_m|\lt 1+|a_{N+1}|$$
This proves that every term after index $N$ is **bounded** by the constant $1+|a_{N+1}|$.
Now we can simply define $k$ as the max of the finite number of terms before $N$, and this bound for every term after $N$:
$$k = \max(|a_1|, |a_2|, \dots, |a_N|, 1 + |a_{N+1}|)$$
So for all $n\in\mathbb{N}^+,|a_n|\le k$, and so the **Cauchy sequence** is **bounded**.

