---
date: 2026-04-07
tags:
  - first-year
  - M40016
---

> [!Abstract] Definition
> For a **function** $f:(a,b)\to\mathbb{R}$, the **derivative** of $f$ at point $x_0\in(a,b)$, if it exists, is defined by:
> $$f'(x_0)=\lim_{x\to x_0} \frac{f(x)-f(x_0)}{x-x_0}$$
> * If this limit exists, we say $f$ is **differentiable** at $x_0$.

> [!Note]
> $\frac{d}{dx}f(x)$ is equivalent to $f'(x)$

> [!Example]
> Let $f(x)=x^2$. To find the **derivative** at some $x_0$:
> $$f'(x_0)=\lim_{x\to x_0} \frac{x^2-x^2_0}{x-x_0}$$
> By factoring, we obtain:
> $$=\lim_{x\to x_0} \frac{(x-x_0)(x+x_0)}{x-x_0}=\lim_{x\to x_0} (x+x_0)=x_0+x_0=2x_0$$

If $f(x)$ and $g(x)$ are **differentiable**, the following properties apply:
* $(f+g)'(x)=f'(x)+g'(x)$
* $(af)'(x)=af'(x)$
* $(fg)'(x)=f'(x)g(x)+f(x)g'(x)$
* If $h(x)=f(g(x))$ then $h'(x)=f'(g(x))g'(x)$
* $\left( \frac{f}{g} \right)'(x)=\frac{f'(x)g(x)-f(x)g'(x)}{g(x)^2}$

The **sign** of the **derivative** tells us how the **func#tion** behaves locally:
* If $f'(x_0)\gt 0$ then $f$ is **strictly increasing** around $x_0$.
* If $f'(x_0)\lt 0$ then $f$ is **strictly decreasing** around $x_0$.
If $f$ is **differentiable** at $x_0$ and $x_0$ is a local maximum or minimum, then $f'(x_0)=0$.


> [!Theorem]
> If a **function** $f$ is **differentiable** at $x_0$, then $f$ must be [[Continuity|continuous]] at $x_0$.

Proof:
To prove **continuity** at $x_0$, we must show that $\lim_{x\to x_0}f(x)=f(x_0)$. 
This is equivalent to showing:
$$\lim_{x\to x_0}(f(x)-f(x_0))=0$$
We can multiply and divide by $(x-x_0)$:
$$\lim_{x\to x_0}(f(x)-f(x_0))=\lim_{x\to x_0} \left(\frac{f(x)-f(x_0)}{x-x_0}\cdot(x-x_0)\right)$$
Now, by the [[Limits|limit]] **product law**, this is equal to:
$$= \left( \lim_{x\rightarrow x_0} \frac{f(x) - f(x_0)}{x - x_0} \right) \cdot \left( \lim_{x\rightarrow x_0} (x - x_0) \right)$$
Now the first limit is exactly $f'(x_0)$, and the second is clearly $0$, we have: $f'(x_0)\cdot 0=0$.
Since the difference between the **limit** and the actual value is $0$, the **function** is **continuous**.

> [!Warning]
> The converse is not necessarily true.
> For example, $f(x)=|x|$ is **continuous** everywhere, but is not **differentiable** at $x=0$.