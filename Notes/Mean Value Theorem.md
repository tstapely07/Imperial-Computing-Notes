---
date: 2026-04-07
tags:
  - first-year
  - M40016
---
The **mean value theorem** is an extension of [[Rolle's theorem]].

> [!Theorem]
> Suppose $f:[a,b]\to\mathbb{R}$ is **continuous** on $[a,b]$ and **differentiable** on $(a,b)$.
> Then there exists at least one point $c\in (a,b)$ such that:
$$f'(c)=\frac{f(b)-f(a)}{b-a}$$

This tells us at some point $c$, the **instantaneous rate of change** must be equal to the average **rate of change** over the whole **function**.

If we replace $b$ with $x$ and $a$ with $x_0$ we can derive that:
$$f(x)=f(x_0)+f'(c)(x-x_0)$$
This tells us that we can calculate $f(x)$ by starting some point $f(x_0)$ and moving along a tangent slope $f'(c)$.
* While this isn't necessarily useful for finding exact values, since $c$ is unknown, it allows us to **bound** the error, if we know $f'(c)$ is **bounded**.