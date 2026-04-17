---
date: 2026-04-13
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> A **minimal cover** $S_c$ of a **set** of [[Functional Dependencies|FDs]] $S$ has the properties that:
> * All the **FDs** in $S$ can be derived from $S_c$.
> 	* This means $S^+=S^+_c$.
> * It is not possible to form a new set $S_c'$ by deleting an **FD** from $S_c$, or deleting an [[Attributes|attribute]] from an **FD** in $S_c$, and $S_c'$ still be able to derive all the **FDs** in $S$.

A **set** of **FDs** may have more than one **minimal cover**.

> [!Example]
> Let's find the **minimal cover** of $S=\set{A\to B, BC\to A, A\to C, B\to C}$.
> * Since $B\to C$, we can replace $BC\to A$ with $B\to A$.
> * Now $S'=\set{A\to B, B\to A, A\to C, B\to C}$
> 
> One next step could be to observe that since $A\to B,B\to C\models A\to C$, we can remove $A\to C$.
> * This leaves us with $S_c=\set{A\to B, B\to A, B\to C}$.
> 
> Alternatively, we could observe that, since $B\to A,A\to C\models B\to C$, we can remove $B\to C$.
> * This leaves us with $S_c=\set{A\to B, B\to A, A\to C}$.
> 
> Here, we ended up with two, equally valid, **minimal covers**.

