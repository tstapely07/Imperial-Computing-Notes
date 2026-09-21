---
date: 2026-04-20
tags:
  - first-year
  - M40018
---
To prove some **specification** featuring [[pre-conditions and post-conditions]], such as:
```Code
// PRE: P
code
// Post: Q
```
* We must show "if property $P$ holds before the execution of `code`, then after the execution of `code` property $Q$ will hold".

We can express this formally as a **Hoare triple**:
$$\set{P}\quad\text{code}\quad \set{Q}$$

> [!Example]
> For example:
> $$\set{true}\quad\text{x=5}\quad \set{x\gt 0}$$
> * Note that we can use $true$ when we have no **pre-condition**.

Proving a **Hoare triple** is essentially a proof that $P$ modified by the **effects** of `code` implies $Q$.

> [!Example]
> So to prove our previous example, we must show that:
> $$true\land x=5\to x\gt 0$$

