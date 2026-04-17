---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
In [[SQL Data Manipulation Language (DML)|SQL]], we can use a `CASE` statement to return alternate values based on conditions.
It has two forms:
* `CASE expr WHEN v1 THEN r1 WHEN v2 then r2 ... END`
	* This form compares `expr` against values directly.
* `CASE WHEN cond1 THEN r1 WHEN cond2 THEN r2 ... END`
	* This form evaluates the Boolean conditions independently.
We can give a `CASE` statement an `ELSE` clause.
* If no condition is met, and no `ELSE` clause is provided, then the `CASE` statement returns [[SQL Null|NULL]].

This `CASE` statement is used to classify interest rates:
```SQL
SELECT no,
	   COALESCE(rate, 0.00) AS rate,
	   CASE 
	   WHEN rate>0 and rate<5.5 
	   THEN 'low rate'
	   WHEN rate>=5.5
	   THEN 'high rate'
	   ELSE 'zero rate'
	   END AS interest_class
FROM account
```
* ![[Pasted image 20260408122508.png|361]]