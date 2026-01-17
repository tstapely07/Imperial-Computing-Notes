---
date: 2026-01-16
tags:
  - first-year
  - M40008
---

> [!Abstract] Definition
> A [[Graphs|graph]] is **planar** if it **can** be drawn so that no [[Arcs|arcs]] cross.

Here, the cube graph is **planar**, even though the first drawing of it has crossing arcs:
* ![[Pasted image 20260116172535.png|200]]
* ![[Pasted image 20260116172454.png|200]]

Here are two **non-planar** graphs, with our best attempts at avoiding crossing arcs:
* $K_5$ is the **complete graph** on $5$ [[Nodes|nodes]]:
	* ![[Pasted image 20260116172651.png|200]]
	* ![[Pasted image 20260116172703.png|200]]
* $K_{3,3}$ is the **complete bipartite graph** on 2sets of 3 nodes: ^93d837
	* ![[Pasted image 20260116172746.png|200]]
	* ![[Pasted image 20260116172757.png|200]]

>[!Theorem]
>A graph is **planar** if it does not contain a [[Subgraphs|subgraph]] [[Homeomorphism|homeomorphic]] to $K_5$ or $K_{3,3}$.

>[!Info] Fact
>If a **simple graph** is planar, it can always be redrawn so that all the arcs are **non-intersecting straight lines**. 

Although it is not obvious whether a given graph is **planar**, there is a **linear time** algorithm to test for it.
* So testing **planarity** is **low complexity**.

