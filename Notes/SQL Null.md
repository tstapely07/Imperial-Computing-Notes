---
date: 2026-04-06
tags:
  - first-year
  - M40007
---
In [[SQL Data Manipulation Language (DML)|SQL]], `NULL` generally represents data that might be present in the [[Universe of Discourse (UoD)|UoD]], but the value is currently unknown.
* `NULL` is handled using a three valued logic system, with values of `TRUE`, `FALSE`, and `UNKNOWN`.
* If a `WHERE` clause evaluates to `UNKNOWN`, then that **row** is **not** included.

This logic system includes all the standard rules between `TRUE` and `FALSE`, but also rules including:
* `TRUE AND UNKNOWN = UNKNOWN`
* `FALSE AND UNKNOWN = FALSE`
* `TRUE OR UNKNOWN = TRUE`
* `FALSE OR UNKNOWN = UNKNOWN`
* `NOT UNKNOWN = UNKNOWN`

> [!Warning]
> Comparing equality with `NULL`, as in `X = NULL` is always `UNKNOWN`, even `NULL = NULL` is `UNKNOWN`.
> * Instead, we can use `IS NULL` and `IS NOT NULL`
> * There is also `IS NOT TRUE`, to catch rows that evaluate to `FALSE` or `UNKNOWN`, and likewise, there is an `IS NOT FALSE`.
> 	* Note that `IS NOT TRUE` is not the same as `IS FALSE`.

Normally, with $R(\underline{A})$ and $S(B)$, with $A$ and $B$ not nullable, the following statements are all equivalent:
```SQL
SELECT A
FROM R
EXCEPT
SELECT B
FROM S
```
```SQL
SELECT A
FROM R
WHERE NOT EXISTS
	(SELECT * 
	 FROM S
	 WHERE S.B=R.A)
```
```SQL
SELECT A 
FROM R
WHERE A NOT IN 
	(SELECT B
	 FROM S)
```
But if $A$ or $B$ is **nullable**, then the equivalences no longer hold.
* If a single `NULL` exists in the subquery, then `NOT IN` collapses to `UNKNOWN`, and so the zero rows are returned.
* The `EXCEPT` considers `NULL` to be equal to `NULL`, and so removes `NULL` from $A$ if it is present in $B$, whereas `NOT EXISTS` does not.
For example:
* `R = 1, NULL`
* `S = 2, NULL`
* The first query returns `1`.
* The second query returns `1, NULL`.
* The third query returns nothing.
  ```
