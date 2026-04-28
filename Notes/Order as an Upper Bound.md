---
date: 2026-03-03
tags:
  - first-year
  - M40008
---
Sometimes the exact [[Orders of Complexity|order]], the [[Formal Definitions of Big-O and Big-Theta|Big-Theta]], of a computational problem is unknown.

For example, take [[Matrices|matrix multiplication]]:
* We know that the standard **matrix multiplication** algorithm is exactly $\Theta(n^3)$.
* However, because there may be a faster algorithm out there, we say the problem of **matrix multiplication** is currently bounded at $O(n^3)$.

We know the theoretical **lower bound** must be $\Theta(n^2)$, since any algorithm must inspect all $n\times n$ elements of the **matrix**.
* Over decades, computer scientists have continuously found new algorithms to push the $O$ upper bound closer to the $\Theta(n^2)$ lower bound.
* One example, is [[Strassen's Algorithm]], which is $\Theta(n^{\log 7})\approx\Theta(n^{2.807})$.
* 