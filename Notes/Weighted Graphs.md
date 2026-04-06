---
date: 2026-02-04
tags:
  - first-year
  - M40008
---
Many networks have a cost associated with each [[Arcs|arc]].
We call these costs **weights**.

> [!Abstract] Definition
> A **weighted graph** $(G,W)$ is a [[Simple Graphs|simple]] [[Graphs|graph]] $G$ together with a weight function $W:\operatorname{arcs}(G)\to \mathbb{R}^+$.

For example:
* ![[Pasted image 20260204130812.png|400]]

Since we are trying to minimise cost, the restriction to **simple graphs** is sensible:
* If there are two **parallel arcs** we will always choose the cheaper.
* If there is a loop then we will never wish to use it.

With **simple graphs**, an **arc** can be specifies by giving its endpoints, e.g. $(1,2)$.
The **weight function** acts on pairs of [[Nodes|nodes]], e.g. $W(1,2)$, which is of course equal to $W(2,1)$.
