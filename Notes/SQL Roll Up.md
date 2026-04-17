---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
In [[SQL Data Manipulation Language (DML)|SQL]], we can use `ROLL UP` for [[SQL Group By|grouping]] when data has a natural hierarchy.
* It generates subtotals for each level of the hierarchy, and finally produces a grand total.
* Once a level is no longer relevant, it is replaced by [[SQL Null|NULL]].


> [!Example]
> This query uses `ROLL UP`:
> ```SQL
> SELECT cname,
> 	   account.no,
> 	   mid,
> 	   SUM(amount) AS amount
> FROM account LEFT JOIN movement
> 	 ON account.no = movement.no
> GROUP BY ROLLUP(cname, account.no, mid)
> ORDER BY cname, account.no, mid
> ```
> In this query, we first get the subtotal grouped by each individual movement, then the subtotal grouped by each account, then the subtotal grouped by each person, then an overall total, a bit like having these 4 individual outputs:
> * ![[Pasted image 20260408165838.png|283]]
> * ![[Pasted image 20260408165845.png|223]]
> * ![[Pasted image 20260408165856.png|176]]
> * ![[Pasted image 20260408165906.png|73]]
> Together, with `NULL` values filled in where necessary, we get the following final output:
> * ![[Pasted image 20260408170014.png|379]]