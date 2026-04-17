---
date: 2026-04-10
tags:
  - first-year
  - M40016
---
We define the **radius of convergence**, $R$, as the maximum distance from the **centre point** of a [[power series]] within which the [[series]] is guaranteed to **converge**.
For all $|x-x_0| \lt R$, the **series** **converges**.

> [!Note]
> This assumes that the **power series** faithfully represents the original function.
> * For example, for a [[Taylor series]] we assume that the **Lagrange remainder** $R_n(x)\to0$.

One way to find where a **power series** **converges** is using the [[Root Test|root test]]:
$$L=\limsup_{n\to\infty} \sqrt[n]{|a_n(x-x_0)^n|}$$
This simplifies to:
$$L = \limsup_{n \to \infty} \left( \sqrt[n]{|a_n|} \cdot |x-x_0| \right) $$
And then we can pull out the $|x|$ since it is constant with respect to $n$ to get:
$$L = |x-x_0| \cdot \left( \limsup_{n \to \infty} \sqrt[n]{|a_n|} \right)$$
For future, we can simply carry out the **root test** on the **coefficients**:
$$r=\limsup_{n \to \infty} \sqrt[n]{|a_n|} $$
We now have $L=|x-x_0|\cdot r$
The **series** **converges** when $L\lt1$,and so when $|x-x_0|\cdot r\lt 1$, or when $|x-x_0|\lt \frac{1}{r}$.
* This means that here we have the **radius of convergence**, $R=\frac{1}{r}$.
* When $r\gt 0$, the **series** **converges** strictly for $|x-x_0|\lt  R$
* When $r=0$, we say $R=\infty$, and so the **series** **converges** for all $x\in\mathbb{R}$.
* When $r=\infty$, we essentially have $R=0$, and so the series only converges for the trivial point $x=x_0$.

> [!Example]
> Let's find the **radius of convergence** of a **Taylor series** we've found [[Taylor Series#^bf52d6|before]], $\ln x$ centred at $x=2$:
> $$\ln x =  \ln 2 + \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n \cdot 2^n} (x-2)^n$$
> We have $|a_n|=\frac{1}{n\cdot 2^n}$
> Applying the **root test** gives:
> $$r = \limsup_{n \to \infty} \sqrt[n]{\frac{1}{n \cdot 2^n}}$$
> This is equal to:
> $$r = \lim_{n \to \infty} \frac{1}{\sqrt[n]{n} \cdot \sqrt[n]{2^n}}$$
> Now, we know that $\lim_{n\to\infty} \sqrt[n]{n}=1$, and clearly we have $\sqrt[n]{2^n}=2$, so we get:
> $$r=\frac{1}{1\cdot 2}=\frac{1}{2}$$
> So the **radius of convergence** is $\frac{1}{r}=\frac{1}{1/2}=2$

> [!Example]
> The [[Maclaurin series]] of $f(x)=e^x$ is as follows:
> $$e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\dots=\sum_{n=0}^\infty \frac{x^n}{n!}$$
> Applying the **root test** gives:
> $$r=\limsup_{n\to\infty} \sqrt[n]{\frac{1}{n!}}=\limsup_{n\to\infty} \frac{1}{\sqrt[n]{n!}}$$
> It is a known result that $\sqrt[n]{n!}\to\infty$ as $n\to\infty$, so we have $r=0$, and so $R=\infty$.
> This means the **series** converges for all $x\in\mathbb{R}$.