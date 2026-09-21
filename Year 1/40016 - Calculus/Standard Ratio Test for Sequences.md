---
date: 2026-03-24
tags:
  - first-year
  - M40016
---
> [!Theorem]
> Let $(a_n)_{n\ge1}$ be a [[Sequences|sequence]] where $a_n \neq 0$ for all $n\in \mathbb{N}^+$. 
> If there exists some $r\in\mathbb{R}$ such that $0\le 1 \lt 1$, and for all n:
> $$\left| \frac{a_{n+1}}{a_n} \right| \le r$$
> Then $\lim_{n\to\infty}a_n=0$.

Proof:
By multiplying the denominator to the other side, the given condition becomes:
$$|a_{n+1}|\le r|a_n|$$
We can apply the rule repeatedly, to work backwards down the **sequence**:
$$|a_{n+1}| \le r|a_n| \le r(r|a_{n-1}|) = r^2|a_{n-1}|$$
Following this chain back to the first **term**, $a_1$, we get:
$$|a_{n+1}|\le r^n|a_1|$$
Because $0\le r\lt 1$, $\lim_{n\to\infty}r^n=0$.
Since $|a_1|$ is a constant, it follows that $\lim_{n\to\infty}r^n|a_1|=0$ as well.
By the [[Sandwich Theorem]], with $0\le |a_{n+1}|\le r^n|a_1|$, we can conclude that $\lim_{n\to\infty} |a_{n+1}|=0$, which implies $\lim_{n\to\infty} |a_n|=0$.
