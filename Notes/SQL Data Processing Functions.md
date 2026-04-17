---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
[[SQL Data Manipulation Language (DML)|SQL]] offers many **data processing functions**:
* An **processing** intended to appear in a result set should be placed in the `SELECT` clause.
* In contrast, any **processing** intended to filter data should be placed in the `WHERE` clause.

`COALESCE(val1, val2, ...)` returns the first non-[[SQL Null|null]] value from the provided list.
* This is useful to provide a default value to replace `NULL` with.
`GREATEST(val1, val2, ...)` returns the greatest value from `val1, val2, ...`.
* However, this returns `NULL` if any of the values in the list are `NULL`.
`LEAST(val1, val2, ...)` returns the least value from `val1, val2, ...`.
* Again, this returns `NULL` if any of the values in the list are `NULL`.
`CAST(val AS type)` converts a value to the specified datatype.

> [!Example]
> Here's an example of both `COALESCE` and `GREATEST`:
> ```SQL
> SELECT no,
> 	   COALESCE(rate, 0.00) AS curent_rate,
> 	   GREATEST(COALESCE(rate, 0.00), 5.30) AS new_rate
> FROM account 
> ```
> * ![[Pasted image 20260408121738.png|237]]