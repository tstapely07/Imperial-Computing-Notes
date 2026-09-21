---
date: 2026-04-10
tags:
  - first-year
  - M40016
---
We can use [[power series]] to solve **linear differential equations** of the form $y''+ay'+by=0$.

We first assume a solution, $y=\sum a_n x^n$.
We then [[Differentiation|differentiate]] term-by-term to get $y$ and $y'$.
We can then substitute and group the coefficients.

Solve $y'-y=0$.
Let $y=a_0+a_1x+a_2x^2+\dots$
This means $y'=a_1+2a_2x+3a_3x^2+\dots$.
Substituting gives:
$$(a_1 + 2a_2x + 3a_3x^2+\dots) - (a_0 + a_1x + a_2x^2+\dots) = 0$$
Grouping terms then yields:
$$(a_1 - a_0) + (2a_2 - a_1)x + (3a_3 - a_2)x^2+\dots = 0$$
Since each **coefficient** must equal $0$, we have:
* $a_1=a_0$
* $a_2=\frac{a_1}{2}=\frac{a_0}{2!}$
* $a_3=\frac{a_2}{3}=\frac{a_3}{3!}$
This gives:
$$y=a_0(1+x+\frac{x^2}{2}+\dots)$$
We now recognise the **power series**, giving us our final answer:
$$y=a_0e^x$$
