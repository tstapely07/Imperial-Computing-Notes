---
date: 2026-01-16
tags:
  - first-year
  - M40008
---
Here is a map of some countries:
* ![[Pasted image 20260116222934.png|300]]
* The question is how many **different colours** do we need, so that countries sharing a border have **different colours**.
* In this case, the answer is $3$.

To solve the problem, we draw the [[Dual Graph|dual graph]].
Once we've drawn the **dual graph**, the problem is to colour the [[Nodes|nodes]] of a planar graph in such a way that if two **nodes** are adjacent, then they have different colours:
* ![[Pasted image 20260116223550.png|200]]


Here is a map that needs $4$ colours:
* ![[Pasted image 20260116223152.png|200]]
Its [[Dual Graph|dual graph]] is $K_4$:
* ![[Pasted image 20260116223218.png|200]]

>[!Theorem]
>The **Four Colour Theorem** states that every map can be coloured using at most $4$ colours.

> [!Abstract] Definition
> A graph $G$ is **k-colourable** if the [[Nodes|nodes]] of $G$ can be coloured using no more than $k$ colours.

From the **Four Colour Theorem**, every **simple planar graph** is $4$-colourable.#

Every **2-colourable** graph is a [[Bipartite Graphs|bipartite graph]].