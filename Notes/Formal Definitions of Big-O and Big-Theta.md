---
date: 2026-03-03
tags:
  - first-year
  - M40008
---
To rigorously classify the [[Orders of Complexity|order]] of **algorithms**, we use formal mathematical bounds.

For the following two definitions:
* Let $\mathbb{R}^+=\set{x\in \mathbb{R}:x\ge 0}$
* Let $f,g:\mathbb{N}\to\mathbb{R}^+$

**Big-O** - Upper Bound:
> [!Abstract] Definition
> $f$ is $O(g)$ $\iff \exists m \in \mathbb{N},\exists c\in\mathbb{R}^+\text{ such that } \forall n \geq m, f(n)\leq c \cdot g(n)$
> 
> $f$ is $O(g)$ if and only if there exists some starting point $m$ and some constant multiplier $c$ such that $f(n)$ is always less than or equal to $c\cdot g(n)$ for all $n$ past that starting point.

**Big-Theta** - Tight Bound:
> [!Abstract] Definition
> $f$ is $\Theta(g)\iff f\text{ is }O(g)\;\land\;g\text{ is }O(f)$
> 
> $f$ is $\Theta(g)$ if and only if they bound each other - meaning they grow at the exact same rate.

Here's a **trivial example**:
* Let's prove that $8n^2+300n+70$ is $O(n^2)$.
* We need to find a multiplier $c$ and a starting point $m$ such that:
	* $8n^2 + 300n + 70 \le cn^2 \quad \forall n \ge m$
* Since the dominant term is $8n^2$ lets pick a multiplier $c$ that is strictly larger, say $c=9$.
* We need to check if $9n^2$ eventually outgrows our function:
	* $9n^2 - (8n^2 + 300n + 70) \ge 0$
	* $n^2 - 300n - 70 \ge 0$
* We need a sufficiently large starting point, so let's guess $m=1000$.
	* $(1000)^2-300(1000)-70\ge 0$ is obviously true.
* We successfully found a valid constant $c$ and a starting point $m$, so $8n^2+300n+70$ is indeed $O(n^2)$.



