---
date: 2026-01-27
tags:
  - first-year
  - M40008
---

> [!Abstract] Definition
> An **Euler path** is a [[Paths|path]] which uses each [[Arcs|arc]] exactly once.

> [!Abstract] Definition
> An **Euler circuit** is a [[Cycles|cycle]] which uses each [[Arcs|arc]] exactly once.

> [!Theorem]
> A [[Connectedness|connected]] [[Graphs|graph]] has an **Euler path** iff there are $0$ or $2$ odd [[Nodes|nodes]].
> A [[Connectedness|connected]] [[Graphs|graph]] has an **Euler circuit** iff every [[Nodes|node]] has even [[Degrees|degree]].

Using this theorem, we can determine whether an **Euler path** or **Euler circuit** exists, just be counting the number of odd [[Nodes|nodes]], giving us an $O(n^2)$ algorithm.

This proves that the **Konigsberg Bridge Problem** is impossible, by considering the corresponding [[Graphs|graph]]:
* ![[Pasted image 20260127235704.png|300]]
* ![[Pasted image 20260127235714.png|150]]
* The [[Nodes|nodes']] have [[Degrees|degrees]] `3,3,3,5`, meaning 4 odd [[Nodes|nodes]], so there are no **Euler paths** or **Euler circuits**.

To find an **Euler path** or **Euler circuit** for a given [[Graphs|graph]], we can use the following approach:
* We first identify the endpoints, which for an **Euler path** must be the $2$ odd nodes, if they exist, otherwise any nodes are acceptable.
* We then pick some path between these endpoints.
* Any unused arcs can then be completed through side journeys.
* Combining the side journeys with the main path gives the final [[Paths|path]].

For example:
* ![[Pasted image 20260128000141.png|400]]
* The endpoints must be $4$ and $7$, since they have odd [[Degrees|degree]].
* One [[Paths|path]] joining them could be `4,8,7,6,4,3,8,7`.
* We then need some side journeys to cover every [[Arcs|arc]], these are `3,2,1,3`, `4,5,4`, and `6,6`.
* Now we can get the complete **Euler path** of `4,5,4,8,7,6,6,4,3,2,1,3,8,7`.
* Since this [[Graphs|graph]] has two nodes of odd [[Degrees|degree]], it does not have a **Euler circuit**.
