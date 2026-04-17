---
date: 2026-04-10
tags:
  - first-year
  - M40016
---
A **power series** is an **infinite polynomial** of the form:
$$f(x)=a_0+a_1 (x-x_0)+a_2(x-x_0)^2+\dots=\sum_0^\infty a_n (x-x_0)^n$$
A [[Taylor series]] is one example of a **power series**.

Within their [[radius of convergence]], **power series** behave exactly like standard **polynomials**.
Let $f(x)=\sum a_n x^n$ with **radius** $R_1$ and $g(x)=\sum b_n x^n$ with **radius** $R_2$. We have:
* $f(x)\pm g(x)=\sum (a_n\pm b_n)x^n$
* $f(x)g(x)=a_0b_0+(a_0b_1+a_1b_0)x+(a_0b_2+a_1b_1+a_2b_0)x^2+\dots$ 
	* In general, $f(x)g(x)=\sum_{n=0}^\infty c_nx^n$ where $c_n=\sum_{k=0}^n a_kb_{n-k}$.
* For both cases, the resulting series has **radius of convergence** $R=\min(R_1,R_2)$.
* These properties only hold when $f(x)$ and $g(x)$ are centred around the same point.
We can [[Differentiation|differentiate]] and [[Integration|integrate]] a **power series** term-by-term:
* $f'(x)=a_1+2a_2x+3a_3x^2+\dots$
* $\int f(x)\;dx=a_0x+\frac{a_1x^2}{2}+\frac{a_2x^3}{3}+\dots$
* The **radius of convergence** is unchanged when **differentiating** or **integrating**.

> [!Tip]
> We can use algebra to find the **power series** for complex functions using the **power series** of simpler functions.
> * For example, to find $\sin(2x^4)$, we can take $\sin(u)=u-\frac{u^3}{3!}+\frac{u^5}{5!}-\dots$ and substitute $u=2x^4$.
> 