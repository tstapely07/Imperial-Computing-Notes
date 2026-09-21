---
date: 2026-04-14
tags:
  - first-year
  - M40007
---
A **lost update anomaly** occurs when two [[transactions]] read the same original value, and both write a new value based on it.
*  $T_1$ **reads** $x$, then $T_2$ **reads** $x$, then $T_1$ **writes** $x$, then $T_2$ **writes** $x$.
* $T_1$'s **write** is **lost**.

[[Serialisability and Recoverability|Serialisable histories]] never suffer from **lost updates**.
* Note that a **history** with a **lost update** can still be **recoverable**.

> [!Example]
> Here, $w_1[b_{34}]$ is a **lost update**:
> * ![[Pasted image 20260414102832.png]]

