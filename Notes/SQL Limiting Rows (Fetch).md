---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
In [[SQL Data Manipulation Language (DML)|SQL]], we can use `FETCH FIRST x` or `FETCH NEXT x` to fetch only the first `x` results.
* `FETCH FIRST` and `FETCH NEXT` are **synonymous**.
* We can prefix this with `OFFSET y` to skip the first `y` results before the `FETCH`.
We must also add `ONLY` or `WITH TIES` as a suffix, to specify how **ties** should be handled.
* `FETCH FIRST x ONLY` will always output exactly `x` results.
* `FETCH FIRST x WITH TIES` may output more than `x` results, if the final result is tied to other results.

To get a meaningful, **deterministic** output, these should only be used on data that has been [[SQL Order By|ordered]] using an `ORDER BY` clause.

> [!Example]
> ```SQL
> SELECT mid, tdate, amount
> FROM movement
> ORDER BY amount DESC
> OFFSET 3
> FETCH NEXT 4 ROWS ONLY
> ```
> * ![[Pasted image 20260408144910.png|313]]


