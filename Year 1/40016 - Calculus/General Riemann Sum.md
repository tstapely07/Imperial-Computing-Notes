---
date: 2026-04-07
tags:
  - first-year
  - M40016
---
An alternative definition of the [[Integration|integral]], as opposed to [[Lower and Upper Sums|upper sums]] and **lower sums** is using general sample points.
Let $P$ be a [[Partition (Calculus)|partition]] of $[a,b]$ defined by $a=r_0\lt r_1\lt \dots \lt r_n=b$.
Instead of finding the [[Supremum and Infimum|supremum]] or **infimum** of each **subinterval**, we can pick any arbitrary point $c_i$ inside the **subinterval** $[r_{i-1},r_i]$.
The **Riemann sum** is then:
$$S(f, P)=\sum_{i=1}^n (r_i-r_{i-1})f(c_i)$$

If a **function** is **integrable**, then regardless how $c_i$ is chosen, as $||P||\to 0$, the **sum** will always converge to the exact same value: $\int_a^b f(x)\;dx$.
