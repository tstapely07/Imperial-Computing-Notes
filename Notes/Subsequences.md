---
date: 2026-03-23
tags:
  - first-year
  - M40016
---
> [!Abstract] Definition
> Let $(a_n)_{n\ge1}$ be a [[Sequences|sequence]]. Assume we have a **strictly increasing sequence** of **positive integers**:
> $$n_1\lt n_2\lt n_3\lt n_4\lt \dots \quad\text{where } n_i\in\mathbb{N}^+$$
> Then the **sequence** ($a_{n_i})_{i\ge1}$ is called a **subsequence** of $(a_n)_{n\ge1}$.
> 

Essentially, a **subsequence** is just a new **sequence** formed by removing some **terms** from the original **sequence**, without changing the order of the remaining **terms**.

> [!Example] Examples
> Let our parent **sequence** be $(a_n)_{n\ge1}=(-1)^n\Rightarrow -1,1,-1,1,-1,1,\dots$
> * The even **subsequence** - let $n_i=2i$, the **subsequence** is $(a_{2i})_{i\ge1}=1,1,1,1,\dots$.
> * The odd **subsequence** - let $n_i=2i-1$, the **subsequence** is $(a_{2i-1})_{i\ge1}=-1,-1,-1,-1,\dots$.
> 

> [!Theorem]
> Suppose $\lim_{n\to\infty}a_n=a$. Then every **subsequence** $(a_{n_i})_{i\ge1}$ also **converges** to $a$ as $i\to\infty$.

Proof:
Let $\epsilon\gt 0$. We need to find an integer $N$ such that for all $i\gt N$, $|a_{n_i}-a|\lt\epsilon$.
Because the parent **sequence** **converges**, we know there exists an $N\in\mathbb{N}$ such that for all $n\gt N$:
$$|a_n-a|\lt \epsilon$$
For any **strictly increasing** sequence of integers, it must be true that $n_i\ge 1$ for all $i\ge 1$.
Therefore, if we choose $i\gt N$, it guarantees that $n_i\ge i\gt N$.
Since $n_i\gt N$, $|a_{n_i}-a|\lt \epsilon$.
Since there exists $N$ for any $\epsilon\gt 0$:
$$\lim_{i\to\infty}a_{n_i}=a$$

