---
date: 2026-04-10
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> Sometimes in [[ER Modelling|ER]], we can have [[ER Subsets|subsets]] that are **disjoint** to each other.
> We can specify the **disjointness** of [[ER Entities|entities]] $E_1\dots E_n$ to enforce that:
> $$\forall x,y \; x \neq y \implies E_x\cap E_y=\emptyset$$

This is identified by a **hexagon**.

> [!Example]
> For example, no **person** can be both an `email_user` and `non_email_user`:
> * ![[Pasted image 20260410150849.png|488]]

To map  **disjointness** to a [[relational schema]], the best we can do is treat each **entity** $E_1,\dots,E_n$ as a **subset**.
* We have no simple way to enforce **disjointness**.

> [!Example]
> ![[Pasted image 20260410155437.png]]

