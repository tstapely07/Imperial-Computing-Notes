---
date: 2026-04-06
tags:
  - first-year
  - M40007
---
**SQL** `SELECT` implements $\pi$, $\sigma$, and $\times$ from [[Primitive Operators|relational algebra]]:
* This **SQL**:
```SQL
SELECT A1,...,An
FROM R1,...,Rm
WHERE P1
AND ...
AND Pk
```
* Is exactly equivalent to:
$$\pi_{A_1,\dots A_n}\sigma_{P_1\land\dots\land P_k}(R_1\times \dots\times R_m)$$

We must never have an ambiguous column name in a **SQL** statement.
* We can prefix a **name** with its **parent table name** to remove ambiguity.

`SELECT *` is the same as no **projection**, and so indicates all columns.
`SELECT tablename.*` indicates all columns from a single **table**.