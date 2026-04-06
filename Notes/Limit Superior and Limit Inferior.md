---
date: 2026-03-26
tags:
  - first-year
  - M40016
---
> [!Abstract] Definition
> **Limit superior**:
> Let $b_n=\sup_{m\ge n}a_m$. 
> * The [[Sequences|sequence]] $(b_n)_{n\ge1}$ represents the **upper bounds** of the **tails** of $(a_n)_{n\ge1}$.
> $$\limsup_{n\to\infty} a_n=\lim_{n\to\infty} b_n$$
> * $\limsup_{n\to\infty} a_n$ is the greatest [[Limits|limit]] of any valid [[Subsequences|subsequence]] of $(a_n)_{n\ge1}$.

> [!Abstract] Definition
> **Limit inferior**:
> Let $c_n=\inf_{m\ge n}a_m$. 
> * The **sequence** $(b_n)_{n\ge1}$ represents the **lower bounds** of the **tails** of $(a_n)_{n\ge1}$.
> $$\liminf_{n\to\infty} a_n=\lim_{n\to\infty} c_n$$
> * $\liminf_{n\to\infty} a_n$ is the least **limit** of any valid [[Subsequences|subsequence]] of $(a_n)_{n\ge1}$.

> [!Example]
> For $(a_n)_{n\ge1}=(-1)^n$, the values oscillate between $-1$ and $1$. 
> * This means that $\limsup_{n\to\infty}a_n=1$ and $\liminf_{n\to\infty}a_n=-1$.

All **limits** of **subsequences** of $(a_n)_{n\ge1}$ will fall between the $\liminf$ and the $\limsup$.
If $L$ is the **limit** of any **subsequence** of $(a_n)_{n\ge1}$ then:
$$\liminf_{n \to \infty} a_n \le L \le \limsup_{n \to \infty} a_n$$

The standard **limit** exists if and only if the $\lim inf$ and $\lim sup$ are exactly equal:

$$\liminf_{n \to \infty} a_n = \limsup_{n \to \infty} a_n = L\iff \lim_{n \to \infty} a_n = L$$
