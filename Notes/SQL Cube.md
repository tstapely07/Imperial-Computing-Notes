---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
In [[SQL Data Manipulation Language (DML)|SQL]], `CUBE` is another variant of [[SQL Group By|grouping]] that behaves like a [[SQL Roll Up|roll up]], but with every possible combination, rather than a simple hierarchy.

> [!Example]
> ```SQL
> SELECT cname,
> 	   sortcode,
> 	   type,
> 	   COUNT(no) AS qty
> FROM account
> GROUP BY CUBE(cname, sortcode, type)
> ORDER BY cname, sortcode, type
> ```
> This query returns:
> * ![[Pasted image 20260408170512.png|248]]