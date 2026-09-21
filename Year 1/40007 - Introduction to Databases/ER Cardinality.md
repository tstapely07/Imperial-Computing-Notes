---
date: 2026-04-10
tags:
  - first-year
  - M40007
---

We will use **look-here cardinality constraints**.
The **constraint** $L:U$ attached between the [[ER Entities|entity]] $E_1$ and the [[ER Relationships|relationship]] $R$ means that:
* An **upper bound cardinality constraint** $U$ states that each instance of $E_1$ may appear at most $U$ times in $R$.
* A **lower bound cardinality constraint** $L$$ states that each instance of $E_1$ must appear at least $L$ times in $R$.
* Setting $U=N$ indicates no upper limit.

> [!Example]
> Here, each person works in exactly $1$ department, but each department by employ any number of people:
> * ![[Pasted image 20260410130309.png|508]]

> [!Note]
>  Although we normally stick to $0$, $1$, and $N$, $L$ and $U$ may be any number.
>  