---
date: 2026-03-26
tags:
  - first-year
  - M40016
---
> [!Theorem]
> Let $\sum_{n=1}^\infty a_n$ be a [[series]] of **positive terms**.
> Let $\sum_{n=1}^\infty c_n$ be a [[series]] of **positive terms** that **converges** to $C$.
> Let $\sum_{n=1}^\infty d_n$ be a [[series]] of **positive terms** that **diverges**.
> 
> For some $n\in\mathbb{N}$ and $\lambda\gt 0\in \mathbb{R}$:
> * If $a_n \le \lambda c_n$ for all $i\ \gt N$ then $\sum_{n=1}^\infty a_n$ **converges**.
> * If $a_n \ge \lambda d_n$ for all $i\ \gt N$ then $\sum_{n=1}^\infty a_n$ **diverges**.

Proof:
For the first case, multiplying a **convergent sequence** by a constant results in another **convergent sequence**.
* Because the **tail** of $a_n$ after index $N$ is **bounded above** by this **convergent sequence**, the [[Sequences|sequence]] of **partial sums** is **bounded**, and so it **converges**.
For the second case, the **tail** of $a_n$ is **bounded below** by a divergent series, which forces $a_n$ to also **diverge**.


