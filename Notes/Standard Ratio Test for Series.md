---
date: 2026-03-26
tags:
  - first-year
  - M40016
---
Let $\sum_{n\ge1} a_n$ be a [[series]] with **positive**.

> [!Theorem]
> If for all $n\ge1$, $\frac{a_{n+1}}{a_n}\le l\lt 1$, then $\sum a_n$ **converges**. 

Proof:
Since $\frac{a_{n+1}}{a_n}\le l$, we have $a_{n+1}\le la_n$.
Continuing this logic, as in the [[Standard Ratio Test for Sequences|ratio test for sequences]] yields:
$$a_{n+1}\le la_n\le l^2a_{n-1}\le\dots\le l^na_1$$
Summing these **bounds** gives us:
$$\sum_{n=1}^{\infty} a_{n+1} \le \sum_{n=1}^{\infty} l^n \cdot a_1 = a_1 \sum_{n=1}^{\infty} l^n$$
Now since $l\lt 1$, the right side is a **convergent** **geometric series**.
So the [[Sequences|sequence]] of **partial sums** is **bounded**, so the [[Series with Non-Negative Terms|series of non-negative terms]] **converges**.

> [!Theorem]
> If for all $n\ge1$, $\frac{a_{n+1}}{a_n}\ge 1$, then $\sum a_n$ **diverges**.
 
Proof:
Since $\frac{a_{n+1}}{a_n}\ge 1$, we have $a_{n+1}\ge a_n$, for all $n$, and so $a_n\not\to0$ as $n\to\infty$.
