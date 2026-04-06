---
date: 2026-03-27
tags:
  - first-year
  - M40016
---
For a given [[Partition (Calculus)|partition]] $P$, we define the **lower sum** and **upper sum** by looking at the [[supremum and infimum]] values of the **function** $f(x)$ within each **subinterval** $[r_{i-1}, r_i]$:
* The **lower sum** $S^l$ forms rectangles using the **lowest point** of $f(x)$ in each **subinterval**:
$$S^l(f,P)=\sum_{i=1}^n(r_i-r_{i-1})\inf_{x\in[r_{i-1},r_i]}f(x)$$
* The **upper sum** $S^u$ forms rectangles using the **highest point** of $f(x)$ in each **subinterval**:
$$S^l(f,P)=\sum_{i=1}^n(r_i-r_{i-1})\sup_{x\in[r_{i-1},r_i]}f(x)$$
