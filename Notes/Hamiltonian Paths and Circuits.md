---
date: 2026-01-28
tags:
  - M40008
---
> [!Abstract] Definition
> A [[Paths|path]] that visits every [[Nodes|node]] exactly once is a **Hamiltonian path**.

> [!Abstract] Definition
> A [[Cycles|cycle]] that visits every [[Nodes|node]] exactly once is a **Hamiltonian circuit**.

For example, this [[Graphs|graph]] has a **Hamiltonian path**, but no **Hamiltonian circuit**:
* ![[Pasted image 20260128000707.png|300]]

> [!Note]
> We must only consider [[Graphs#^c240f7|simple graphs]], since we can never follow a **loop**, nor can we follow more than one [[Arcs|parallel arc]] between two [[Nodes|nodes]].

The **Hamiltonian Circuit Problem (HCP)**:
* Given a graph $G$, determine whether $G$ has a **Hamiltonian circuit**.

For an **HP** to exist, the [[Graphs|graph]] must be [[Connectedness|connected]].
For an **HC** to exist, the [[Graphs|graph]] must be [[Connectedness|connected]] and each [[Nodes|node]] must have degree $\geq 2$.

But this condition is **not sufficient**, for example, this graph has no **HC**:
* ![[Pasted image 20260128130723.png|300]]

We can solve the **HCP** by a brute force approach, checking every possible circuit.
Every possible circuit can be checked in $O(n)$, and there are $n!$ possible circuits, corresponding to $n!$ permutations of the nodes.
* This is **very slow**.

A method using **dynamic programming** (the [[Bellman-Held-Karp algorithm]]) can solve the **HCP** in $O(n^22^n)$, which is better but still exponential.
In fact, **HCP** has been shown to be [[NP-Complete|NP-complete]].