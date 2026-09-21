---
date: 2026-03-26
tags:
  - first-year
  - M40016
---
> [!Theorem]
> As for the standard [[comparison test]]:
> Let $\sum_{n=1}^\infty a_n$ be a [[series]] of **positive terms**.
> Let $\sum_{n=1}^\infty c_n$ be a [[series]] of **positive terms** that **converges** to $C$.
> Let $\sum_{n=1}^\infty d_n$ be a [[series]] of **positive terms** that **diverges**.
> 
> * If $\lim_{n\to\infty} \frac{a_n}{c_n}\in\mathbb{R}$ exists, then $\sum_{n=1}^\infty a_n$ **converges**.
> * If $\lim_{n\to\infty} \frac{d_n}{a_n}\in\mathbb{R}$ exists, then $\sum_{n=1}^\infty a_n$ **diverges**.

Proof for **convergence**:
Assume $\lim_{n\to\infty} \frac{a_n}{c_n}=L\in\mathbb{R}$.
By definition of a [[Limits|limit]], for some $N\in\mathbb{N}$, for all $n\gt N$:
$$\left|\frac{a_n}{c_n}-L\right|\lt\epsilon$$
We can take $\epsilon =1$, and obtain:
$$\frac{a_n}{c_n}\le L+1$$
Multiplying by $c_n$ gives:
$$a_n\le (L+1)c_n$$
Now this is just the standard **comparison test**, with $\lambda=L+1$, and so the **series** indeed **converges**.

Proof for **divergence**:
Assume $\lim_{n\to\infty}  \frac{d_n}{a_n}=L\in\mathbb{R}$.
Like before, we can obtain:
$$\frac{d_n}{a_n}\le L+1$$
And then obtain:
$$a_n\ge \frac{1}{L+1}d_n$$
Again, this is the standard **comparison test**, now with $\lambda=\frac{1}{L+1}$ and so the **series** indeed **diverges**.