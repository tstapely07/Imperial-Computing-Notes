---
date: 2026-04-13
tags:
  - first-year
  - M40007
---
> [!Abstract]  Definition
> An [[Attributes|attribute]] $A$ of a [[Relations|relation]] $R$ is **prime** if there is some [[FDs and Keys|minimal key]] $X$ of $R$ such that $A\subseteq X$.
> * Any other **attribute** $B\in Attrs(R)$ is **non-prime**.

> [!Example]
> For example, for the **relation** $R(A,B,C,D,E,F)$, with [[Functional Dependencies|FDs]] $A\to BCE$, $C\to D$, $BD\to F$, $EF\to B$, $BE\to A$:
> * The **minimal keys** are $A$, $BE$ and $EF$.
> * So $A,B,E,F$ are **prime attributes**.
> * $C,D$ are **non-prime attributes**.
