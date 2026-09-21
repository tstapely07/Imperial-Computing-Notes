---
date: 2026-04-06
tags:
  - first-year
  - M40007
---
Unlike **relational algebra**, which strictly uses **sets**, [[SQL Data Manipulation Language (DML)|SQL]] uses both **sets**, and **bags**.

A [[SQL Select|SELECT]] does not eliminate duplicates, and so returns a **bag** by default.
* To make a `SELECT` return a **set**, we use the `DISTINCT` keyword, and write `SELECT DISTINCT`.
* `DISTINCT` can be omitted when the `SELECT` includes a **key**, since this already guarantees no duplicates.

The [[SQL Set Operators|set operators]] default to **set** semantics. 
* To instead retain duplicates, we use the `ALL` keyword, such as `UNION ALL`

> [!Note]
> There is no need for a `DISTINCT` or `ALL` around `FROM` and `WHERE`, since these cannot introduce any duplicates, and any existing duplicates can be removed in the `SELECT`.