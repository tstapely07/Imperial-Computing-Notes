---
date: 2026-04-08
tags:
  - first-year
  - M40008
---
> [!Abstract] Definition
> A [[Decision Problems|decision problem]] $D(x)$ is in **class NP** if there is a **verification problem** $E(x,y)$ in [[class P]], and a **polynomial** $p(n)$ such that:
> * $D(x)\iff \exists y.E(x, y)$
> * If $E(x,y)$ then $|y| \le p(|x|)$

The variable $y$ acts as a **guess**.
* It must be **polynomially bounded** in $x$, otherwise it would take too long to simply read $y$.

For example, the [[Hamiltonian Paths and Circuits|Hamiltonian path]] problem, determining if a [[Graphs|graph]] has a [[Paths|path]] that visits every [[Nodes|node]] exactly once is **class NP**:
* Checking all paths takes $n!$ time.
* However, if we guess a list, ($y$) of **paths**, we can check in **p-time** that it is some permutation of $nodes(G)$, and that the successive nodes are **adjacent**.


