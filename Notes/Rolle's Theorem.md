---
date: 2026-04-07
tags:
  - first-year
  - M40016
---

> [!Theorem]
> Suppose, for some **function** $f:[a,b]\to\mathbb{R}$:
> * $f$ is [[Continuity|continuous]] on the **closed interval** $[a,b]$.
> * $f$ is [[Differentiation|differentiable]] on the **open interval** $(a,b)$.
> * The endpoints are at the same height: $f(a)=f(b)$.
> Then there exists at least one point $c\in (a,b)$ such that $f'(c)=0$.

Proof:
By the [[extreme value theorem]] the **function** must have a **maximum** and **minimum**.
* If at least one of these is inside the **interval**, then the **derivate** at this point must be $0$.
* If they are only at the endpoints, then the function must be a flat line, meaning the **derivate** is $0$ everywhere.
