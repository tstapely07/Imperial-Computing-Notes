---
date: 2026-04-13
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> For every **non-trivial** [[Functional Dependencies|FD]], $X\to A$ on some [[Relations|relation]] $R$, either:
> * $X$ is a [[FDs and Keys|super-key]].
> * $A$ is [[Prime Attributes|prime]].

Every **non-key** [[Attributes|attribute]] depends on the **key**, the **whole key**, and **nothing but the key**.

> [!Example]
> For example, for the **relation** $R(A,B,C,D,E,F)$, with **FDs** $A\to BCE$, $C\to D$, $BD\to F$, $EF\to B$, $BE\to A$:
> * The **minimal keys** are $A$, $BE$ and $EF$.
> * So $A,B,E,F$ are **prime attributes**.
> * $C,D$ are **non-prime attributes**.
>
> The **decomposition** $R_1(B,D,F), R_2(A,B,C,D,E)$ is not in **3NF**, since for the **FD**
 $C\to D$, $C$ is not a **super-key**, and **D** is not-prime. 
 > One **decomposition** that is in **3NF** could be $R_1(A,B,C,E,F),R_2(C,D)$.
 
 
