---
date: 2026-04-13
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> The **closure** $S^+$ of a **set** of [[Functional Dependencies|FDs]] $S$ is the **set** of all **FDs** that can be **inferred** from $S$.

For speed, we ignore:
* Trivial **FDs**, such as $X\to X$.
* **FDs** with a non-minimal LHS.
	* So ignore $XY\to Z$ if we have $X\to Z$.
* **FDs** that have multiple [[attributes]] on the RHS.
	* So treat $A\to CD$ as $A\to C$ and $A\to D$.

A **set** of **FDs** will have a **unique closure**.

> [!Abstract] Definition
> Two **sets** of **FDs**, $S$ and $T$ are equivalent if their **closures** are the **same**:
> $$S^+=T^+\iff S\equiv T$$

> [!Example]
> Let's find the **closure** of $S=\set{A\to B, A\to C, B\to A, B\to D}$
> * Since $A\to B$ and $B\to D$, we have $A\to D$.
> * Now $S'=\set{A\to B, A\to C, A\to D, B\to A, B\to D}$.
> * Since $B\to A$ and $A\to C$, we have $B\to C$.
> * This gives our result of $S^+=\set{A\to B, A\to C, A\to D, B\to A, B\to C, B\to D}$
> 
> As another example, $T=\set{A\to B, A\to C, A\to D, B\to A}$.
> * We have both, $B\to A,A\to D \models B\to D$ and $B\to A,A\to C\models B\to C$.
> * This gives our result of $T^+=\set{A\to B, A\to C, A\to D, B\to A, B\to C, B\to D}$
> 
> Notice $S^+$ and $T^+$ are the same, so $S$ and $T$ are **equivalent**:
> $$S\equiv T$$
