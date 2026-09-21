---
date: 2026-04-07
tags:
  - first-year
  - M40016
---
> [!Theorem]
> Suppose $f:[a,b]\to\mathbb{R}$ is a **function** that is [[Integration|integrable]].
> We can define $g(x)$ that calculates the **area** under $f$ from some fixed point $a$ up to $x$:
> $$g(x)=\int_a^x f(t)\;dt$$
> Let $x_0 \in(a,b)$ if $f$ is [[Continuity|continuous]] at $x_0$, then $g$ is [[Differentiation|differentiable]] at $x_0$, and its **derivative** is the simply the original function evaluated at that point:
> $$g'(x_0)=f(x_0)$$

Proof:
By the [[Limits|limit]] definition of the **derivative** we want to evaluate:
$$g'(x_0)=\lim_{h\to0} \frac{g(x_0+h)-g(x_0)}{h}$$
By our definition of $g(x)$:
$$g(x_0 + h) - g(x_0) = \int_a^{x_0 + h} f(t)\;dt - \int_a^{x_0} f(t)\;dt$$
This is equivalent to simply $\int_{x_0}^{x_0+h} f(t)\;dt$, and so we have:
$$g'(x_0)=\frac{\int_{x_0}^{x_0+h}f(t)\;dt}{h}$$
Let $\epsilon\gt 0$. Because $f$ is **continuous** at $x_0$, there exists some $\delta\gt 0$ such that for any $t$:
$$|t-x_0|\lt \delta\implies |f(t)-f(x_0)|\lt \epsilon$$
This can be rewritten as:
$$f(x_0)-\epsilon\lt f(t)\lt f(x_0)+\epsilon$$
Now, if we choose some $h\lt \delta$, since $t$ is in $[x_0,x_0+h]$, we have $|t-x_0|\lt \delta$.
* This means the **inequality** on $f(t)$ hold for the entire **subinterval**, and so we can **integrate** the **inequality** from $x_0$ to $x_0+h$.
* Note that **integrating** causes the strict $\lt$ to relax to a $\le$. 
We get:
$$\int_{x_0}^{x_0+h} f(x_0)-\epsilon\; dt \le \int_{x_0}^{x_0+h} f(t)\; dt \le \int_{x_0}^{x_0+h} f(x)+\epsilon\;dt$$
Since the left and right sides of the **inequality** are constants, we get:
$$h(f(x_0) - \epsilon) \le \int_{x_0}^{x_0 + h} f(t) dt \le h(f(x_0) + \epsilon)$$
Dividing through by $h$ gets:
$$f(x_0) - \epsilon \le \frac{\int_{x_0}^{x_0 + h} f(t) dt}{h} \le f(x_0) + \epsilon$$
Which we know from earlier is equivalent to:
$$f(x_0) - \epsilon \le \frac{g(x_0 + h) - g(x_0)}{h} \le f(x_0) + \epsilon$$
Since this holds for any $\epsilon\gt 0$, taking the **limit** as $h\to 0$ forces the middle term to be exactly equal to $f(x_0)$, and hence, as desired, we obtain:
$$g'(x_0)=f(x_0)$$

