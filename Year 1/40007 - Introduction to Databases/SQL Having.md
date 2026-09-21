---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
Whilst `WHERE` filters individual **rows** before [[SQL Group By|grouping]], `HAVING` can be used after a `GROUP BY` to filter the new **summary rows** after **grouping**.
* `HAVING` is executed after the `GROUP BY` but before the `SELECT`, so we cannot use [[SQL Aliases|aliases]] defined in the `SELECT` clause, we must instead write out the **aggregate function** in full.

> [!Tip]
> One use of `HAVING` is to filter out data that could cause a division by zero error within the `SELECT` clause.

> [!Example]
> ```SQL
> SELECT account.no,
> 	   account.cname,
> 	   SUM(movement.amount) AS balance
> FROM account NATURAL JOIN movement
> WHERE movement.amount > 200
> GROUP BY account.no,
> 	     account.cname
> HAVING COUNT(movement.no) > 1
>        AND SUM(movement.amount) > 1000
> ```
> This query returns:
> * ![[Pasted image 20260408153249.png|278]]