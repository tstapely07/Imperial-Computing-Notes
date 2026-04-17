---
date: 2026-04-13
tags:
  - first-year
  - M40007
---
We can turn a [[Relations|relation]] $R$ into a [[relational schema]] in [[Boyce-Codd Normal Form (BCNF)|BCNF]] with the following **algorithm**:
1. Given $R$ and a set of [[Functional Dependencies|FDs]] $S$, find an **FD** $X\to A$ that causes $R$ to violate **BCNF**.
	* i.e. with $X$ not a [[FDs and Keys|super-key]].
2. Decompose $R$ into $R_a(Attrs(R)-A)$ and $R_b(XA)$.
	* Since the **relations** share $X$, and $X\to A$, this is [[Lossless-Join Decomposition|lossless]].
3. Project $S$ onto the new **relations** and repeat the process, until no **FDs** violate **BCNF**.

Note that this is **very** similar to the [[Generating 3NF|algorithm for 3NF]].

> [!Example]
> ![[Pasted image 20260413211945.png]]

Unlike [[Third Normal Form (3NF)|3NF]], we cannot always preserve all **functional dependencies** in **BCNF**.
* Specifically, we cannot in the case where we have **overlapping** [[FDs and Keys|minimal keys]], and an **attribute** from one of those **keys** **functionally determines** an **attribute** in the other. 
This loss of **FDs** is the trade-off of **BCNF** in order to entirely eliminate **data redundancy**.

> [!Example]
> In the **example** above, we lost the **FD** $\set{no,street,town,county}\to postcode$.
> * This is because $\set{no,street,town,county}$ and $\set{no,postcode}$ are both **minimal keys**, and they share the attribute $no$.
> * The problematic **FD** was $postcode\to \set{street,town,county}$. This violated **BCNF**, since $postcode$ is not a **super-key**. By decomposing on this **FD**, we separate $\set{street,town,county}$ and $no$ into separate **tables**, losing the **FD**.