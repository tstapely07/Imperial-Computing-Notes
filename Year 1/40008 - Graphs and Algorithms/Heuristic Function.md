---
date: 2026-02-10
tags:
  - first-year
  - M40008
---
A **heuristic function** function $h(x)$ **estimates** the distance from any [[Nodes|node]] `x` to the finish node.

> [!Example]
> If we were dealing with cities on a map, $h$ could be the **Euclidean distance**.

A **heuristic function** is **consistent** if:
* For any adjacent [[Nodes|nodes]] $x,y$ we have $h(x)\leq W(x,y)+h(y)$
* $h(finish)=0$.
Our **Euclidean distance** example is clearly **consistent**.

A **heuristic function** is **admissible** if for any node $x$ we have $h(x)\leq \text{the weight of the shortest path from x to the goal}$. 
* i.e. an **admissible heuristic function** always **underestimates**.

A **consistent heuristic function** is **admissible**:
* We have $h(x) \leq W(x,y)+h(y)$.
* If we repeat this logic for every step of the path, we get:
* $h(x)\leq \text {sum of all edge weights}+h(finish)$
* Since $h(finish)=0$, we are left with $h(x)\leq \text{total path weight}$.
