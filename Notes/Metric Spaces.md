---
date: 2026-04-14
tags:
  - first-year
  - M40016
---
> [!Abstract] Definition
> A **metric space** is an **underlying set** $X$ and some **distance function** or **metric** $d:X\times X\to\mathbb{R}^+$ with the properties:
> * $d(x,y)=0\iff x=y$ - **identity of indiscernibles**.
> 	* The distance between two points is zero if and only if they are the exact same point.
> * $d(x,y)=d(y,x)$ for all $x,y\in X$ - **symmetry**.
> 	* The distance between two points is the same in either direction.
> * $d(x,z)\le d(x,y)+d(y,z)$ for all $x,y,z\in X$ - **triangle inequality**.
> 	* The direct path is always the shortest path.

> [!Example] Examples
> Here are some example **metrics** to measure **distance** between two vectors $x=(x_1,x_2)$ and $y=(y_1,y_2)$.
> **Euclidean** - standard straight-line distance:
> $$d_2(x,y) = \sqrt{(x_1-y_1)^2 + (x_2-y_2)^2}$$
> **Manhattan** - grid based distance:
> $$d_1(x,y) = |x_1-y_1| + |x_2-y_2|$$
> **Maximum norm** - the largest single coordinate difference:
> $$d_\infty(x,y) = \max(|x_1-y_1|, |x_2-y_2|)$$

> [!Abstract] Definition
> A **norm** is the distance from the point $x$ to the origin $(0,0)$, it is denoted by **double bars**.

> [!Example]
> For example, the **Euclidean norm** is :
> $$\|x\|_2 = d_2(0,x) = \sqrt{x_1^2 + x_2^2}$$

**Metric spaces** let us redefine the [[Limits|limit]] definition of [[continuity]] in any **dimension**.
A **function** $f(x)$ is **continuous** at $x_0$ if for all $\epsilon\gt0$ there exists some $\delta\gt0$ such that:
$$d(x, x_0) \lt \delta \implies d(f(x), f(x_0)) \lt \epsilon$$