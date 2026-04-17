---
date: 2026-04-07
tags:
  - first-year
  - M40016
---
From the [[mean value theorem]] we have:
$$f(x)=f(x_0)+(x-x_0)f'(c)$$
* Where $c$ is some point between $x_0$ and $x$.

> [!Abstract] Definition
> If $f:[a,b]\to\mathbb{R}$ is [[Continuity|continuous]], and all its [[Differentiation|derivatives]] up to $n$ then we can expand this to the **Taylor series**:
> $$f(x)=f(x_0)+(x-x_0)f'(x_0)+\frac{(x-x_0)^2}{2!}f''(x_0)+\dots+\frac{(x-x_0)^{n-1}}{(n-1)!}f^{(n-1)}(x_0)+R_n(x)$$

> [!Abstract] Definition
> The final term, $R_n(x)$ is known as the **Lagrange error**, is defined in terms of some $x^*$ that is between $x$ and $x_0$:
> $$R_n(x)=\frac{(x-x_0)^n}{n!}f^{(n)}(x^*)$$
> * Although it is generally not possible to calculate $x^*$, since it is **bounded** between $x$ and $x_0$ we can **bound** the error.
> * If, in the worst case, the error **converges** to $0$ as $n\to\infty$ then the **Taylor** [[series]] perfectly equals the function.

> [!Example]
> The **Taylor series** for $\sin x$ at $x=0$ is as follows:
> $$\sin x = x-\frac{x^3}{3!}+\frac{x^5}{5!}-\dots$$
> Since every **derivative** is $\pm \sin x$ or $\pm \cos x$, $f^n(x^*)$ is **bounded** by $1$, and so the error is **bounded** by $\frac{1}{n!}|x|^n$, which **converges** to $0$ for all $x$..

> [!Example]
> The **Taylor series** for $f(x)=\frac{1}{1-x}$ at $x=0$ is:
> $$\frac{1}{1-x}=1+x+x^2+x^3+\dots$$
> Here, the remainder is $\frac{x^n}{1-x}$. We therefore require $|x|\lt 1$ for $R_n(x)\to 0$ to hold as $n\to\infty$, and therefore for the approximation to hold.

> [!Example]
> As an example for a series not centred at $x=0$, we construct the **Taylor series** for $\ln x$, centred at $x_0=2$.
> We first find a few derivatives:
> * $f(x)=\ln x$ so $f(2)=\ln 2$.
> * $f'(x)=x^{-1}$ so $f'(2)=\frac{1}{2}$.
> * $f''(x)=- x^{-2}$ so $f''(2)=-\frac{1}{2^2}$.
> * $f'''(x)=2x^{-3}$ so $f'''(2)=\frac{2}{2^3}$
> In general:
> $$f^{(n)}(2)=(-1)^{n+1} \frac{(n-1)!}{2^n}$$
> This gives the **Taylor series**:
> $$\ln x = \ln 2 + \sum_{n=1}^{\infty} \frac{(-1)^{n+1} (n-1)!}{n! \cdot 2^n} (x-2)^n$$
> Which we can simplify to:
> $$\ln x = \ln 2 + \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n \cdot 2^n} (x-2)^n$$

^bf52d6
