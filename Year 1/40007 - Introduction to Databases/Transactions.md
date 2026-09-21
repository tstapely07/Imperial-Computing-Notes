---
date: 2026-04-14
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> A **transaction** is an **indivisible task** carried out by a **database management system** (**DBMS**).

We can represent [[SQL Data Manipulation Language (DML)|SQL]] **queries** as **transaction histories**.
We use the following **notation**:
* $r_n[x]$ - **transaction** $n$ **reads** data item $x$.
* $w_n[y]$ - **transaction** $n$ **writes** to data item $y$.
* $c_n$ - **transaction** $n$ **commits** - (saves successfully).
* $a_n$ - **transaction** $n$ **aborts** - (fails and rolls back changes).
* We can optionally, but rarely, include $b_n$ - **transaction** $n$ **begins**.

> [!Example]
> ![[Pasted image 20260414100749.png]]
