---
date: 2026-03-22
tags:
  - first-year
  - M40016
---
> [!Theorem]
> If $\lim_{n\to\infty} a_n=A$ and $\lim_{n\to\infty} b_n=B$ then $\lim_{n\to\infty}(a_n-b_n)=A-B$

By the definition of subtraction, we can rewrite the limit:
$$\lim_{n \to \infty} (a_n - b_n) = \lim_{n \to \infty} (a_n + (-b_n))$$
By the [[Negation Law of Limits|negation law]], we know that $\lim_{n \to \infty} (-b_n) = -B$
By the [[Addition Law of Limits|addition law]], we know that the sum of two convergent sequences is the sum of their individual limits:
$$\lim_{n \to \infty} (a_n + (-b_n)) = \lim_{n \to \infty} (a_n) + \lim_{n \to \infty} (-b_n)$$
So the limit is $A+(-B)$, which is equivalent to $A-B$.
So we can conclude:
$$\lim_{n \to \infty} (a_n - b_n) = A - B$$
