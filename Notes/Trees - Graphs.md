---
date: 2026-01-28
tags:
  - first-year
  - M40008
---

> [!Abstract] Definition
> A **tree** is an [[Cycles|acyclic]], [[Connectedness|connected]], [[Rooted Graphs|rooted graph]].

> [!Abstract] Definition
> A **non-rooted tree** is an [[Cycles|acyclic]], [[Connectedness|connected]] [[Graphs|graph]].

In a **tree** there is a unique [[Paths|path]] between any two [[nodes]].
* If there were two **different** [[Paths|paths]], there would be a [[Cycles|cycle]].

![[Node Depth]]
![[Node Parent]]

> [!Theorem]
> Let $T$ be a **tree** with $n$ [[Nodes|nodes]], then $T$ has $n-1$ [[Arcs|arcs]].
> 

Proof:
* There is a 1-1 correspondence between **arcs** and **non-root nodes**.
	* Any **arc** $a$ joins a unique **non-root node** $f(a)$ to its parent.
	* Also if $x$ is a **non-root node** then there is a unique **arc** $g(x)$ which joins $x$ to its **parent**.
* Clearly $f$ and $g$ are mutual inverses.
* This holds for **non-rooted trees** too, simply make any **node** into the **root**.









