---
date: 2026-02-04
tags:
  - first-year
  - M40008
---
[[Kruskal's algorithm]] - $O(m\;log\;n)$
[[Prim's Algorithm#Prim's Algorithm with Priority Queues|Prim's algorithm with priority queue]] - $O(m\;log\;n)$
Classic **Prim's algorithm** - $O(n^2)$

On **dense** [[Graphs|graphs]] where $m$ is large, then **Kruskal's** gives $O(n^2\;log\;n)$ and classic **Prim's** is preferred.
On [[Sparse Graph|sparse]] **graphs**, where $m$ is small, say $O(n\;log\;n)$, then **Kruskal's** (or **Prim's** with **priority queue**) give better results than classic **Prim's** - $O(m\;log\;n)=O(n\;log^2\;n)$.