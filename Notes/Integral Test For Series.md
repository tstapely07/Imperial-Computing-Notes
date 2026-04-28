---
date: 2026-04-07
tags:
  - first-year
  - M40016
---
> [!Theorem]
> Suppose $f:[1,\infty)\to\mathbb{R}$ is a **function** such that for all $x\in[1,\infty)$:
> * $f(x)\gt 0$ - the function is **strictly positive**.
> * For any $x\lt y,f(y)\lt f(x)$ - the function is **strictly decreasing**.
> Then the [[series]] $\sum_{n=1}^\infty f(n)$ and the [[Improper Integrals|improper integral]] $\int_1^\infty f(x)\;dx$ **converge** or **diverge** together.
> * We can therefore use the **improper integral** to test for **convergence** of the **series**.

Proof:
We can represent the **series** as rectangles of width $1$.
* By shifting these rectangles over or under the curve $f(x)$, we can **bound** the [[Integration|integral]].
For some $N$, evaluating the **right-endpoints** will give an **underestimate**:
$$f(2)+f(3)+\dots+f(N)\le \int_1^N f(x)\;dx$$
Evaluating the **left-endpoints** gives an **overestimate**:
$$\int_1^Nf(x)\;dx\le f(1)+f(2)+\dots+f(N-1)$$
Since the **partial sums** of the **series** are **bounded** by the **integral**, if the **integral** **converges**, the [[Sequences|sequence]] of **partial sums** must **converge**, and so the **series converges**.
* Likewise, if the **integral** tends to $\infty$, the **partial sums** are also forced to $\infty$.

Let $f(x)=\frac{1}{x^{1+c}}$ where $c\gt 0$.
We evaluate the **improper integral**:
$$\int_{1}^{\infty} \frac{1}{x^{1+c}} dx = \lim_{b\to\infty}\int_1^b \frac{1}{x^{1+c}}=\lim_{b\to\infty} \left[ -\frac{x^{-c}}{c} \right]_{1}^{b} = \frac{1}{c}$$
Since $\frac{1}{c}$ is a **finite number**, the **improper integral converges**, and so the **series** converges for $c\gt 0$.