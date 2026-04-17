---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
In [[SQL Data Manipulation Language (DML)|SQL]], we can use `ORDER BY` to present data from a [[SQL Select|SELECT]] in a different order.
* Note that the data itself is not changed.
The default is ascending order (`ASC`), but we can also specify descending (`DESC`) order.

We can add the suffix `NULLS LAST` or `NULLS FIRST` to specify how [[SQL Null|NULL]] should be handled.

We can also sort by more columns, **lexicographically**, in the case of **ties**, we simply separate the **column names** by commas.
* When doing so, we are able to mix and match `ASC`/`DESC`, and the use of `NULLS FIRST`/`NULLS LAST`.
