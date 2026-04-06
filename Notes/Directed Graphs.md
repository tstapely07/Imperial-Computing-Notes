---
date: 2026-01-28
tags:
  - first-year
  - M40008
---

> [!Abstract] Definition
> A **directed graph** is a set $N$ of [[Nodes|nodes]] and a set $A$ of [[Arcs|arcs]] such that  each $a\in A$ is associated with an **ordered** pair of **nodes** (the **endpoints** of $a$).

In diagrams, the **arcs** are shown with arrows going from the **source node** to the **target node**.
In a path $a_1,\dots,a_n$ in a **directed graph** the **source** of $a_{i+1}$ must match the **target** of $a_i$.
If for any pair of nodes $x,y$ there is at most one **arc** from $x$ to $y$, we can refer to this **arc** as $(x,y)$.

> [!Note]
> By convention, in this course, a **graph** is **undirected** by default, unless otherwise stated to be **directed**.

