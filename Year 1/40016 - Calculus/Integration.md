---
date: 2026-03-27
tags:
  - first-year
  - M40016
---
To formally define the **integral** of a **bounded function** $f:[a,b]\to\mathbb{R}$, we use the concept of [[Partition (Calculus)|partitions]] and [[lower and upper sums]].

> [!Abstract] Definition
> The **lower integral** is the [[Supremum and Infimum|supremum]] of all **lower sums**:
> $$\underline{\int}_a^b f(x)\;dx = \sup_P S^l(f, P)$$

> [!Abstract] Definition
> The **upper integral** is the **infimum** of all **upper sums**:
> $$\overline{\int}_a^b f(x)\;dx=\underset{P}{\inf}S^u(f,P)$$

> [!Abstract] Definition
> $f$ is **Riemann integrable** if:
> $$\underline{\int}_a^b f(x)\;dx=\overline{\int}_a^b f(x)\;dx$$

> [!Abstract] Definition
> If a function is **Riemann integrable**, then the common value of the **lower integral** and **upper integral** is known as its **Riemann integral**:
> $$\int_a^bf(x)\;dx$$

> [!Example]
> Let's prove that $f(x)=x^2$ is indeed **integrable**, and that $\int_0^1x^2\;dx=\frac{1}{3}$ 
> Let $P_n$ be a **partition** that divides the **interval** $[0,1]$ into $n$ equal **subintervals**.
> The points of the **partition** are therefore $r_i=\frac{i}{n}$ for $i=0,1,2,\dots,n$.
> The width of every interval ($r_i-r_{i-1}$) is exactly $\frac{1}{n}$.
> Because $f(x)=x^2$ is strictly increasing on $[0,1]$, the **supremum** in any subinterval $[r_{i-1},r_i]$ is always $r_i$, so we get:
> $$\begin{gather}S^u(x^2,P_n)=\sum_{i=1}^n\left( \frac{1}{n} \right)\left( \frac{i}{n} \right)^2\\
> =\frac{1}{n^3}\sum_{i=1}^n i^2\\
> = \frac{1}{n^3} \frac{n(n+1)(2n+1)}{6}
> \end{gather}$$
> As $n\to\infty$, this **converges** to $\frac{1}{3}$.
> The **infimum** in any **subinterval** is always $r_{i-1}$, so we can obtain:
> $$
> \begin{gather}S^l(x^2,P_n)=\sum_{i=1}^n\left( \frac{1}{n} \right)\left( \frac{i-1}{n} \right)^2\\
> =\frac{1}{n^3}\sum_{i=1}^n (i-1)^2\\
> = \frac{1}{n^3} \frac{(n-1)n(2n-1)}{6}
> \end{gather}$$
> Again, as $n\to\infty$, this **converges** to $\frac{1}{3}$.
> Now we have $S^u(x^2,P_n)=S^l(x^2,P_n)=\frac{1}{3}$, and so $\underline{\int}_0^1 x^2\;dx=\overline{\int}_0^1 x^2\;dx=\frac{1}{3}$, and so we can conclude that:
> $$\int_0^1x^2\;dx=\frac{1}{3}$$

For any **integrable functions** $f$ and $g$, the following properties apply:
If $f(x)\ge 0$ for all $x\in [a,b]$, then $\int_a^b f(x)\;dx\ge 0$
* By extension, if $f(x)\ge g(x)$ for all $x\in[a,b]$ then $\int_a^b f(x)\;dx\ge\int_a^b g(x)\;dx$.
For any constants $c,d\in\mathbb{R}$:
$$\int_a^b(cf(x)+dg(x))\;dx=c\int_a^bf(x)\;dx+d\int_a^bg(x)\;dx$$
For any point $a\le c\le b$:
$$\int_a^bf(x)\;dx=\int_a^cf(x)\;dx+\int_c^bf(x)\;dx$$
We can extend the [[Triangle Inequality (Calculus)|triangle inequality]]:
$$\left|\int_a^bf(x)\;dx\right|\le \int_a^b \left|f(x)\right|\;dx$$




