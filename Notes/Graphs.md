---
date: 2026-01-15
tags:
  - first-year
  - M40008
---

> [!Abstract] Definition
> An **undirected graph** is a set $N$ of [[Nodes|nodes]], and a set $A$ of [[Arcs|arcs]] such that each $a\in A$ is associated with an unordered pair of nodes - the **endpoints** of $a$.

* ![[Pasted image 20260115114434.png|200]]
>[!Info]
>Notation:
>* $G$ - a **graph**
>* $nodes(G)$ - the **nodes** of $G$
>* $arcs(G)$ - the **arcs** of $G$

Graphs may contain **parallel arcs**, **loops**, and **disconnected components**:
* ![[Pasted image 20260115114509.png|300]]

> [!Abstract] Definition
> A graph is **simple** if it has no **parallel arcs** and no **loops**.

**Parallel arcs** model multiple connections, for **robustness** against **failures** of **arcs**.

Two ways to represent **graphs** are:
* [[Adjacency Matrices|Adjacency matrices]]
* [[Adjacency Lists|Adjacency lists]]
