---
date: 2026-03-26
tags:
  - first-year
  - M40016
---
The [[Limit Ratio Test for Series|limit ratio test]] requires $\lim_{n\to\infty}| \frac{a_{n+1}}{a_n}|$ to exist. 
* Where it doesn't, such as for **oscillating sequences**, we can use the **root test**, which relies on the [[Limit Superior and Limit Inferior|limit superior]].

For any [[Sequences|sequence]] $(a_n)_{n\ge1}$, the following **inequality** holds:
$$0 \le \liminf \left|\frac{a_{n+1}}{a_n}\right| \le \liminf \sqrt[n]{|a_n|} \le \limsup \sqrt[n]{|a_n|} \le \limsup \left|\frac{a_{n+1}}{a_n}\right|$$
Note that the $n$-th root is bounded between the ratio bounds, making it a **stronger** condition.

To test for the [[absolute convergence]] of a [[series]] $\sum_{n=1}^\infty a_n$, we evaluate $L=\limsup_{n\to\infty} \sqrt[n]{|a_n|}$:
* If $L\lt 1$, the **series** **converges absolutely**.
* If $L\gt 1$, the **series** **diverges**.
* If $L=1$, the test is **inconclusive**.

Because the $\limsup$ always exists, and **root** is **bounded** below the **ratio**, the **root test** can prove **convergence** in cases when the **ratio test** fails.


> [!Example]
> Let $a_{2n}=\frac{1}{2^n}$, and $a_{2n+1}=\frac{1}{3^n}$ for all $n\ge 0$.
> This gives the **series**:
> $$1+1+\frac{1}{2}+\frac{1}{3}+\frac{1}{2^2}+\frac{1}{3^2}+\frac{1}{2^3}+\frac{1}{3^3}+\dots$$
> $\lim_{n\to\infty}| \frac{a_{n+1}}{a_n}|$ alternates between $0$ and $\infty$, and so does not exist.
> However $\limsup_{n\to\infty} \sqrt[n]{|a_n|}$ does exist.
> For the **even terms** ($k=2n$):
> $$\sqrt[k]{a_k} = \sqrt[2n]{\frac{1}{2^n}} = \left(\frac{1}{2^n}\right)^{\frac{1}{2n}} = \frac{1}{2^{n/2n}} = \frac{1}{2^{1/2}} = \frac{1}{\sqrt{2}}$$
> For the **odd terms** ($k=2n+1$):
> $$\sqrt[k]{a_k} = \sqrt[2n+1]{\frac{1}{3^n}} = \left(\frac{1}{3^n}\right)^{\frac{1}{2n+1}} = \frac{1}{3^{\frac{n}{2n+1}}}$$
> As $n\to\infty$, $\frac{n}{2n+1}\to \frac{1}{2}$, and so the **limit** of this [[Subsequences|subsequence]] is $\frac{1}{\sqrt{3}}$.
> Since $\frac{1}{\sqrt{2}}\gt \frac{1}{\sqrt{3}}$:
> $$L = \limsup_{k\to\infty} \sqrt[k]{|a_k|} = \frac{1}{\sqrt{2}}$$
> Finally, because $L=\frac{1}{\sqrt{2}}\lt 1$, the **series** **converges**.
