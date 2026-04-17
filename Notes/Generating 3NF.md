---
date: 2026-04-13
tags:
  - first-year
  - M40007
---
We can turn a [[Relations|relation]] $R$ into a [[relational schema]] in [[Third Normal Form (3NF)|3NF]] with the following **algorithm**:
1. Given $R$ and a set of [[Functional Dependencies|FDs]] $S$, find an **FD** $X\to A$ that causes $R$ to violate **3NF**.
	* i.e. with $A$ [[Prime Attributes|non-prime]] and $X$ not a [[FDs and Keys|super-key]].
2. Decompose $R$ into $R_a(Attrs(R)-A)$ and $R_b(XA)$.
	* Since the **relations** share $X$, and $X\to A$, this is [[Lossless-Join Decomposition|lossless]].
3. Project $S$ onto the new **relations** and repeat the process, until no **FDs** violate **3NF**.

> [!Example]
> Suppose $R(A,B,C)$ has **FD set** $S=\set{A\to B, B\to C}$.
> The only **key** is $A$, and so $B\to C$ violates **3NF**.
> * Decomposing $R$ into $R_1(A,B)$ and $R_2(B,C)$ results in two **3NF** **relations**.

> [!Example]
> ![[Pasted image 20260413210336.png|521]]

A **lossless decomposition** of $R$ with **FDs** $S$ into $R_a$ and $R_b$ **preserves functional dependencies** $S$ if the **projection** of $S^+$ onto $R_a$ and $R_b$ is equivalent to $S$.
* It is always possible to **decompose** a **relation** into **3NF** while preserving **functional dependencies**.
* Therefore to be a good **3NF decomposition**, it must preserve **FDs**.
* If necessary to artificially guarantee this, we can add in a new **table**, consisting only of the **missing FD**.
	* For example, if $X\to Y$ is missing, we can add $R_x(X,Y)$. 
	* The **decomposition** is still **lossless**, and **3NF** is still maintained, since $X$ is a **super-key** of the new table.

> [!Example]
> Suppose $R(ABC)$ with $S=\set{A\to B, B\to C, C\to A}$ is **decomposed** into $R_a(AB)$ and $R_b(BC)$.
> * $S^+=\set{A\to B, A\to C, B\to A, B\to C, C\to A, C\to B}$.
> * The **projection** of $S^+$ onto $R_a$ gives $S^+_a=\set{A\to B, B\to A}$
> * The **projection** of $S^+$ onto $R_b$ gives $S_b^+=\set{B\to C, C\to B}$.
> * If we define the **union** $S_u=S^+a\cup S_b^+$, we have the property that $S_u^+=S^+$, and so here the **FDs** are **preserved**.