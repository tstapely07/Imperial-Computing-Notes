---
date: 2026-01-27
tags:
  - first-year
  - M40008
---

> [!Abstract] Definition
> A **cycle**, (sometimes called a **circuit**) is a [[Paths|path]] which:
> * Finishes where it starts.
> * Has at least one [[Arcs|arc]].
> * Does not use the same [[Arcs|arc]] twice.

In this example, **cycles** include `1,2,3,4,1` and `3,3` but not `2,5,2`:
* ![[Pasted image 20260127224144.png|300]]

> [!Abstract] Definition
> A [[Graphs|graph]] with **no cycles** is called **acyclic**.

If a graph has $n$ [[Nodes|nodes]], then if it has $\geq n$ [[Arcs|arcs]] then it contains a **cycle**.

To actually find a **cycle**, we can use [[Depth-First Search (DFS)|DFS]]:
* If we encounter a **node** that we have already visited (except by backtracking), then that **node** can be reached by two different routes from the start node.
* Therefore there is a **cycle** in the **graph**.
Conversely, if we **never** encounter an already visited **node**, the **graph** is in fact a [[Trees - Graphs|tree]], with **no cycles**.