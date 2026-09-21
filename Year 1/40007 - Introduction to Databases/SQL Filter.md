---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
In [[SQL Data Manipulation Language (DML)|SQL]], we can use `FILTER` combined with [[SQL Group By|aggregate functions]] to represent data spread across many **rows** as **columns**, making the data simpler to read.
* We essentially add a new **column** for each possible value.
* The `FILTER` only looks at the given **group**, if a `GROUP BY` clause is used.

> [!Example]
> Here's a query to see how many of each type of account a branch has:
> ```SQL
> SELECT branch.sortcode,
> 	   branch.bname,
> 	   COUNT(no) FILTER (WHERE type='current') AS CURRENT,
> 	   COUNT(no) FILTER (WHERE type='deposit') AS DEPOSIT,
> 	   COUNT(no) FILTER 
> 		   (WHERE type IN ('current','deposit')) IS NOT TRUE) AS other,
> FROM account JOIN branch ON account.sortcode = branch.sortcode
> GROUP BY branch.sortcode, branch.bname
> ORDER BY branch.sortcode, branch.bname
> ```
> This query returns:
> * ![[Pasted image 20260408174554.png|517]]