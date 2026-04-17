---
date: 2026-04-10
tags:
  - first-year
  - M40007
---
Since [[SQL Data Manipulation Language (DML)|SQL]] is **relationally complete**, it can fully support all the [[Primitive Operators|operators]] of the **relational algebra**.
As part of this, we can put a [[SQL Select|SELECT]] statement in a `FROM` clause.
* When we do so, we must use an [[SQL Aliases|alias]] to name the resulting **table**.

> [!Example]
> ```SQL
> SELECT no,
> 	   SUM(amount) AS balance,
> 		ROUND(100*SUM(amount)/total,1) AS pc
> FROM movement CROSS JOIN
> 	 (SELECT SUM(amount) AS total
> 	  FROM movement) AS total_balance
> GROUP BY no, total
> ORDER BY no
> ```
> This query returns:
> * ![[Pasted image 20260408161857.png|266]]