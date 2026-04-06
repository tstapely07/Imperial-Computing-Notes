---
date: 2026-03-24
tags:
  - first-year
  - M40016
---
> [!Abstract] Definition
> Let $f$ be a real-valued **function** and $x_0\in\mathbb{R}$. We say $f$ is **continuous** at $x_0$ if the [[Limits|limit]] of the **function** as it approaches $x_0$ is exactly equal to the functions value at $x_0$:
> $$\lim_{x\to x_0}f(x)=f(x_0)$$

> [!Abstract] Definition
> A **function** $f:[a,b]\to\mathbb{R}$ is **continuous** if it is **continuous** at every single point $x\in [a,b]$.

Let $f(x)$ be defined as:
$$f(x) = \begin{cases} x\sin\left(\frac{1}{x}\right) & x \neq 0 \\ 0 & x = 0 \end{cases}$$
Claim: $f(x)$ is **continuous** at $x_0=0$.
Proof:
We [[Limits of Functions#^330a97|previously proved]] that $\lim_{x\to0}x\sin\left( \frac{1}{x} \right)=0$. Because this **limit** equals the functions defined value at that point ($f(0)=0$), the function is **continuous** at $x=0$.

Let $f(x)=\operatorname{Sgn}(x)$, defined as:
$$f(x) = \begin{cases} 1 & x > 0 \\ 0 & x = 0 \\ -1 & x < 0 \end{cases}$$
Claim $f(x)$ is not **continuous** at $x_0=0$.
Proof:
Let $(x_n)_{n\ge1}=\frac{1}{n}$. 
* As $n\to\infty$, $x_n\to 0$. 
* Because every term is **strictly positive**, $f(x_n)=1$ for all $n$.
* So the **sequence** of outputs **converges** to $1$.
Let $(y_n)_{n\ge1}=-\frac{1}{n}$. 
* As $n\to\infty$, $y_n\to 0$. 
* Because every term is **strictly negative**, $f(y_n)=-1$ for all $n$.
* So the **sequence** of outputs **converges** to $1$.
Since $1\neq -1$ we have two **sequences** that **converge** to $0$, but produce different **limits**.
* This means that $\lim_{x\to0}f(x)$ does not exist.
Because the **limit** does not exist, it cannot equal $f(0)$, and therefore $f(x)$ is not **continuous** at $x_0=0$.

Since **continuity** is a specific application of **limits**, the **limit laws** apply directly to **continuous functions**.
If $f$ and $g$ are **continuous** at $x_0\in\mathbb{R}$, the following functions are also continuous at $x_0$:
* $af(x)+bg(x)$
* $f(x)g(x)$
* $\frac{f(x)}{g(x)}$ (provided $g(x_0) \neq 0$)
