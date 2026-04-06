---
date: 2026-03-26
tags:
  - first-year
  - M40016
---
> [!Theorem]
> A [[series]] with **non-negative terms** **converges** if and only if its [[Sequences|sequence]] of **partial sums** is **bounded above**.

Proof:
Suppose we have a **series** $\sum_{n\ge1} a_n$ where every **term** is **non-negative**.
Each **partial sum**, is simply the previous one, plus some **non-negative** number:
$$S_{n+1} = S_n + a_{n+1}$$
So $S_{n+1}\ge S_n$, and the **sequence** of **partial sums** is **monotonically increasing**.
Since the **sequence** is **monotonic** it is either:
* **Bounded**, in which case it **converges** to its [[Supremum and Infimum|supremum]].
* **Unbounded**, in which case it tends to $+\infty$.

> [!Example]
> Claim: 
> The **series** $\sum_{n=1}^\infty \frac{1}{n^2}$ **converges**.
> Proof:
> Since $1/n^2\gt 0$ for all $n\ge1$, this is a **series** of **non-negative terms**.
> Therefore it **converges** if the **sequence** of **partial sums** is **bounded above**.
> For all $n\ge2$:
> $$\frac{1}{n^2} < \frac{1}{n(n-1)}=\frac{1}{n-1}-\frac{1}{n}$$
> So, for $S_n=1+\frac{1}{2^2}+\frac{1}{3^2}+\dots+\frac{1}{n^2}$, we have:
> $$S_n < 1 + \left(\frac{1}{1} - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \dots + \left(\frac{1}{n-1} - \frac{1}{n}\right)$$
> This **telescoping series** collapses to $S_n < 1 + 1 - \frac{1}{n}$, or:
> $$S_n < 2 - \frac{1}{n}$$
> Because $\frac{1}{n}$ is **positive**, we guarantee that $S_n\lt 2$ for all $n$, and is therefore **bounded above**.
> Therefore the **series** indeed **converges**.
> 