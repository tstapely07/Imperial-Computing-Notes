---
date: 2026-02-16
tags:
  - first-year
  - M40008
---
Let $R\subseteq X^2$ be a **binary relation**.
The **transitive closure** of $R$ is $R^+ = \bigcup\limits_{k=1}^{\infty} R^k$.
If $X$ is **finite** and $|X|=n$ then $R^+=\bigcup\limits_{k=1}^nR^k$

We can interpret $R$ as a [[Directed Graphs|directed graph]] $G$. The [[nodes]] of $G$ are just the members of $X$.
There is an [[arcs|arc]] from $x$ to $y$ iff $R(x,y)$.
* There will not be any parallel arcs, but we could have **loops** like $R(x,x)$.
We can clearly see that $R^K(x,y)$ iff there is a [[Paths|path]] of length $k$ from $x$ to $y$.
So $R^+(x,y)$ iff there is a **path** of length $\geq 1$ from $x$ to $y$.

Suppose $X=\{1,\dots,n\}$. Clearly, if we set:
$$A[i, j] = \begin{cases} 1 & \text{if } R(i, j) \\ 0 & \text{otherwise} \end{cases}$$
then $A$ is the [[Adjacency Matrices|adjacency matrix]] of $G$. 
We can compute $R^K$ using [[Matrices|matrix]] multiplication:
* $R^k(i,j)$ iff $A^k[i,j]>0$. ^6cd841
* So if $B=\sum_{k=1}^nA^k$ then $R^+(i,j)$ is true iff $B[i,j]>0$.

While this is mathematically correct, it is **computationally expensive**. 
[[Warshall's algorithm]] is a far more **efficient** method.