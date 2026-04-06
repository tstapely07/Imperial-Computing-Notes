---
date: 2026-01-28
tags:
  - first-year
  - M40008
---
A **spanning tree** of a [[Graphs|graph]] is a [[Subgraphs|subgraph]] which is a [[Trees - Graphs|tree]], and **spans** all the [[nodes]].

> [!Abstract] Definition
> Let $G$ be a **graph**.
> A **non-rooted tree** $T$ is said to be a **spanning tree** for $G$ if $T$ spans $G$, i.e.
> * $T$ is a **subgraph** of $G$.
> * $nodes(T)=nodes(G)$.
> 

Any [[Connectedness|connected]] **graph** has a **spanning tree**.
One **spanning tree** could be obtained by the following algorithm:
* If the **graph** $G$ has a [[Cycles|cycle]] $C$, then remove any [[Arcs|arc]] $x$ to $y$ of $C$.
* There is still a path between $x$ and $y$, using the remainder of $C$, so $G$ remains **connected** and all **nodes** remain present.
* Repeat until all cycles are removed.

**Spanning trees** are not necessarily unique.
Any two **spanning trees** for the same **graph** with $n$ **nodes** must have the same number of **arcs**, $n-1$:
* ![[Pasted image 20260128153816.png|400]]

