---
date: 2026-04-10
tags:
  - first-year
  - M40016
---
> [!Abstract] Definition
> A **function** is **analytic** if it has a valid [[Taylor series]] expansion that perfectly represents the function for a [[radius of convergence]] $R\neq 0$.

Most **functions** are both **smooth** and **analytic**, but a **function** can be [[Smooth Functions|smooth]] without being **analytic**.
Here's one example:
$$f(x)=\begin{cases}e^{-\frac{1}{x^2}}& x\neq 0\\0 &x=0 \end{cases}$$
The **function** is **smooth** since it can be differentiated infinitely many times, but for every **derivative**:
$$\lim_{x\to0}f^{(n)}(x)=0$$
This means its **Taylor series** at $x=0$ is all $0$s, and so fails to represent $f(x)$.
* Therefore the **function** is not **analytic** around $x=0$.