---
date: 2026-03-23
tags:
  - first-year
  - M40016
---
> [!Theorem]
> If $\lim_{n\to\infty} a_n=A$ and $\lim_{n\to\infty} b_n=B$ then $\lim_{n\to\infty}\left( \frac{a_n}{b_n} \right)=\frac{A}{B}$

Proof:
By basic algebra, we can rewrite the division of the two [[sequences]] as a **product**:
$$\frac{a_n}{b_n} = a_n \cdot \left(\frac{1}{b_n}\right)$$
Because $\lim_{n\to\infty}b_n=B\neq 0$, we know by the [[Reciprocal Law of Limits|reciprocal rule]] that:
$$\lim_{n \to \infty} \left(\frac{1}{b_n}\right) = \frac{1}{B}$$
Now, because $\lim_{n \to \infty} a_n = A$ and $\lim_{n \to \infty} \left(\frac{1}{b_n}\right) = \frac{1}{B}$, both **sequences** **converge**. This means we can apply the [[Product Law of Limits|product rule]]:
$$\begin{gather}
\lim_{n \to \infty} \left( a_n \cdot \frac{1}{b_n} \right) = \left( \lim_{n \to \infty} a_n \right) \cdot \left( \lim_{n \to \infty} \frac{1}{b_n} \right)\\
=A\cdot \left( \frac{1}{B} \right)=\frac{A}{B}
\end{gather}$$
So we can conclude:
$$\lim_{n \to \infty} \left( \frac{a_n}{b_n} \right) = \frac{A}{B}$$
