---
date: 2026-03-02
tags:
  - first-year
  - M40008
---
Exact solutions, such as the [[Bellman-Held-Karp algorithm]] to the [[Travelling Salesman Problem (TSP)|TSP]] take too long, but we often still want an **approximate** solution.

Once approach, is the **nearest neighbour heuristic (NNH)**, which always chooses the shortest available [[Arcs|arc]]:
![[Pasted image 20260302173019.png|518]]
However, this can sometimes fail dramatically.
Suppose we change the **weight** of $(1,3)$ from $5$ to $500$. 
* This **arc** should clearly avoid it, but the **NNH** is forced to choose it on the last step.
* ![[Pasted image 20260302173129.png|188]]
