---
date: 2026-01-27
tags:
  - first-year
  - M40008
---
> [!Abstract] Definition
> A [[Graphs|graph]] is **connected** if there is a [[Paths|path]] joining any two [[Nodes|nodes]].

This [[Graphs|graph]] is not **connected**, but it has two [[Connected Components|connected components]]:
* ![[Pasted image 20260127222332.png|300]]

> [!Abstract] Definition
> A [[Directed Graphs|directed graph]] is **strongly connected** if for any $x,y\in nodes(G)$, there is a path from $x$ to $y$.

To determine if a **graph** is **connected**, we can easily adapt [[Depth-First Search (DFS)|DFS]] or [[Breadth-First Search (BFS)|BFS]] to return a list of visited **nodes**. 
* If this list is the same as the complete list of **nodes**, then the graph is **connected**.
* This gives us an $O(m+n)$ algorithm to determine whether a graph is **connected**.