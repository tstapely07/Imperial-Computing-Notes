---
date: 2026-01-16
tags:
  - M40008
---
An [[Adjacency Matrices|adjacency matrix]] gives **efficient access** to any [[Arcs|arc]] in a [[Graphs|graph]].
However, some algorithms rely on looking at **all arcs** incident on a given [[Nodes|node]].
* Here, an [[Adjacency Lists|adjacency list]] would be more suitable.
This is particularly the case, if the **matrix** has a lot of zeroes, i.e. the graph is [[Sparse Graph|sparse]].

For $n$ [[Nodes|nodes]] and $m$ [[Arcs|arcs]]:
* The [[Adjacency Matrices|adjacency matrix]] has size $n^2$.
* The [[Adjacency Lists|adjacency list]] has size $\leq n+2m$.

Clearly, for a [[Sparse Graph|sparse graph]], an [[Adjacency Lists|adjacency list]] would result in less storage space.
