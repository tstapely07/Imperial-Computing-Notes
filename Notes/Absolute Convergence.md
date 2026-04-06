---
date: 2026-03-26
tags:
  - first-year
  - M40016
---

> [!Abstract] Definition
> A [[series]] $\sum_{n=0}^\infty a_n$ **absolutely converges** if the corresponding **series** of the **absolute values** of its **terms** **converges**:
> $$\sum_{n=0}^\infty a_n\text{ is absolutely convergent}\iff\sum_{n=0}^\infty |a_n|\text{ is convergent}$$

> [!Example]
> The **alternating** [[harmonic series]] is given by:
> $$\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \dots$$
> This is **convergent**.
> However, taking the **absolute value** of the **terms** yields the standard **harmonic series**, which we know to be **divergent**.
> * Therefore the **alternating harmonic series** is not **absolutely convergent**.
> 

> [!Theorem]
> If a **series** $\sum_{n=1}^\infty a_n$ is **absolutely convergent**, then it is **convergent**.

Proof:
Let $(S_n)_{n\ge1}$ denote the [[Sequences|sequence]] of **partial sums** of the original **series**.
*  $S_n=\sum_{i=1}^n a_i$
Let $(C_n)_{n\ge1}$ denote the **sequence** of **partial sums** of the **absolute values**.
* $C_n=\sum_{i=1}^n |a_i|$
Because the **series** **converges absolutely**, we know that $(C_n)_{n\ge1}$ **converges**.
* Because $(C_n)_{n\ge1}$ **converges**, it must be a [[Cauchy sequence]], since [[convergent sequences are Cauchy]].
Therefore, for any $\epsilon \gt 0$, there exists an $N$ such that for all $m,n\gt N$, we have:
$$|C_m-C_n|\lt \epsilon$$
Now consider the difference between the **partial sums** of the original **series**:
$$|S_m - S_n| = \left| \sum_{i=n+1}^m a_i \right|$$
By the [[Triangle Inequality (Calculus)|triangle inequality]], we have:
$$\left| \sum_{i=n+1}^m a_i \right| \le \sum_{i=n+1}^m |a_i|$$
Now, notice that $\sum_{i=n+1}^m |a_i|=|C_m-C_n|$, so we get:
$$|S_m-S_n|=\left| \sum_{i=n+1}^m a_i \right| \le \sum_{i=n+1}^m |a_i|=|C_m-C_n|\lt \epsilon$$
Now since $|S_m-S_n|\lt \epsilon$, $(S_n)_{n\ge1}$ is also a **Cauchy sequence**.
* [[Cauchy sequences are convergent in the reals]], and so $(S_n)_{n\ge1}$ **converges**.
Since the **sequence** of **partial sums** **converges**, the original series $\sum a_n$ is indeed **convergent**.