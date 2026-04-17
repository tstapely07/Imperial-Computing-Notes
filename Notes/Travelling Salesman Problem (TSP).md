---
date: 2026-02-16
tags:
  - first-year
  - M40008
---
**>![Note] The Travelling Salesman Problem
>Given a [[Complete Graph|complete]] [[Weighted Graphs|weighted graph]] $(G,W)$, find a way to tour the [[graphs|graph]] visiting each [[Nodes|node]] **exactly once** and travelling the shortest possible distance.

The **TSP** is clearly related to both the [[Hamiltonian Paths and Circuits|Hamiltonian circuit problem]] and the [[Shortest Path Problem|shortest path problem]], since our goal is to find a **Hamiltonian circuit** which is of minimum **weight**.
* Finding a **Hamiltonian circuit** is trivial, since we have assumed that the graph is **complete**.
* The difficulty is finding the shortest **Hamiltonian circuit**, which involves checking $n!$ different **circuits**.

Like the **Hamiltonian circuit problem**, the **TSP** is [[NP-Complete|NP-complete]], so we [[Intractability via NP-Completeness|assume]] there is no **polynomial solution**.
* There is a better algorithm than just checking every possible tour, which runs in $O(n^22^n)$.

> [!Note]
> If a graph is not **complete**, we could simply add [[arcs]] with extremely high weights, that would never actually be chosen, to **complete** the **graph**.

