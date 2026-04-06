---
date: 2026-03-24
tags:
  - first-year
  - M40016
---
Often, the [[Standard Ratio Test for Sequences|standard ratio test]] for [[sequences]] may fail if the **ratio** between **terms** isn't strictly bounded by $r$ for every **term** from the beginning. 
* If the [[Limits|limit]] of the ratio is $\lt 1$, the **sequence** will still eventually converge to $0$.

Let $(a_n)_{n\ge1}$ be a **sequence** where $a_n\neq 0$ for all $n\in\mathbb{N}^+$.
If the **limit** of the ratio exists, and:
$$\lim_{n\to\infty}\left| \frac{a_{n+1}}{a_n}\right|=r\lt 1$$
Then $\lim_{n\to\infty}a_n=0$.

Proof:
Let the limit of the ratio be $r\lt 1$.
We can choose a sufficiently small $\epsilon\gt 0$ such that $r+\epsilon\lt 1$.
* We now define $R=r+\epsilon$, meaning $0\le R\lt 1$.
Because the sequence of ratios **converges** to $r$, there must exist some $N\in\mathbb{N}$ such that for all $n\gt N$:
$$\left| \left| \frac{a_{n+1}}{a_n} \right| - r \right| < \epsilon$$
We can unpack this absolute value to get an **upper bound**:
$$\left| \frac{a_{n+1}}{a_n} \right| < r + \epsilon = R$$
Since for all $n\gt N$, the ratio is **strictly bounded** by $R\lt 1$, the **tail** of this **sequence** perfectly satisfises the conditions of the [[Standard Ratio Test for Sequences|standard ratio test]].
Therefore, the **tail** of the **sequence** converges to $0$, and so the entire **sequence** also converges to $0$:
$$\lim_{n\to\infty}a_n=0$$
