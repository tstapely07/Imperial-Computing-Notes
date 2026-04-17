---
date: 2026-04-14
tags:
  - first-year
  - M40007
---
A **dirty write anomaly** occurs when two different [[transactions]] write to the same **data item** before either of them has **committed**.
* $T_1$ writes $x$. Before $T_1$ commits, $T_2$ overwrites $x$.
* If $T_1$ or $T_2$ need to **abort** later, the **DBMS** struggles to determine which value should be **restored**.

Neither [[Serialisability and Recoverability|serialisable]] or **recoverable** **histories** prevent **dirty writes**.

> [!Example]
> Here is a **dirty write** that happens to **not** be **serialisable**:
> * ![[Pasted image 20260414105354.png|408]]