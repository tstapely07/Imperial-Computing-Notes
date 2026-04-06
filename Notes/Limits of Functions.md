---
date: 2026-03-24
tags:
  - first-year
  - M40016
---

> [!Definition]
> Let $f$ be a real-valued **function**. We say that $f(x)\to l$ as $x\to x_0$ if for **every** [[Sequences|sequence]] $(x_n)_{n\ge1}$ that **converges** to $x_0$, the corresponding **sequence** of functions outputs $f(x_n)$ **converges** to the [[Limits|limit]] $l$.

> [!Abstract] Definition
> Equivalently, we say $f(x)\to l$ as $x\to x_0$ if for every $\epsilon\gt 0$, there exists a $\delta \gt 0$ such that if $0\lt |x-x_0|\le \delta$ then $|f(x)-l|\lt \epsilon$.

> [!Example]
> Function: $f(x)=\sin\left( \frac{1}{x} \right)$. 
> Claim: the **limit** as $x\to 0$ does not exist.
> Proof:
> To prove a **limit** does not exist, we need to find two different **sequences** that both **converge** to $0$, but their corresponding **sequences** of outputs converge to two different limits.
> 1. Let $(x_n)_{n\ge1}=\frac{1}{2n\pi+\frac{\pi}{2}}$
> 	* As $n\to\infty$, $x_n\to 0$.
> 	* $f(x_n)=\sin(2n\pi+\frac{\pi}{2})$, so $f(x_n)=1$ for all $n$.
> 	* Therefore the **sequence** of outputs **converges to** $1$.
> 2. Let $(y_n)_{n\ge1}=\frac{1}{2n\pi+\frac{3\pi}{2}}$
> 	* As $n\to\infty,y_n\to0$.
> 	* $f(y_n)=\sin(2n\pi+\frac{3\pi}{2})$, so $f(y_n)=-1$ for all $n$.
> 	* Therefore the **sequence** of outputs **converges** to $-1$.
> Since $1\neq-1$, the **function** approaches different values when different paths are taken, and so $\lim_{x\to0}\sin\left( \frac{1}{x} \right)$ does not exist.

> [!Example]
> Function: $f(x)=x\sin(\frac{1}{x})$. 
> Claim: $\lim_{x\to0}x\sin(\frac{1}{x})=0$.
> Proof:
> Let $\epsilon\gt 0$.
> We want to find a $\delta\gt0$ such that if $0\lt |x-0|\le \delta$, then $\left|x\sin\left( \frac{1}{x} \right)-0\right|\lt\epsilon$.
> Since $\left|x\sin\left( \frac{1}{x} \right)\right|=|x|\left|sin(\frac{1}{x})\right|$, and $\sin x$ is **bounded** between $-1$ and $1$, we know that for all $x\neq 0$:
> $$|x|\cdot\left|sin\left(\frac{1}{x}\right)\right|\le |x|$$
> So to obtain $|x|\left|\sin\left(\frac{1}{x}\right)\right|\le \epsilon$ as desired, we can set $\delta=\epsilon$.
> Now, since $0\lt |x|\le \delta$, it follows that, it follows that:
> $$\left|x\sin\left(\frac{1}{x}\right)\right| \le |x| \le \delta = \epsilon$$
> Since a valid $\delta$ exists, we can conclude, as desired, that:
> $$\lim_{x\to0}x\sin(\frac{1}{x})=0$$

^330a97

Just like with **sequences**, we can perform arithmetic on **limits** of **functions**.
Suppose $f(x)\to l$ and $g(x)\to k$ as $x\to x_0$:
* $af(x)\pm bg(x)\to al\pm bk$
* $f(x)g(x)\to lk$
* $\frac{f(x)}{g(x)}\to \frac{l}{k}$  (provided $k\neq 0$).



