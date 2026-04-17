---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
In [[SQL Data Manipulation Language (DML)|SQL]], `GROUP BY` takes multiple **rows** with the same values in specified columns, and combines them into a single summary **row**.
* Every column in the `SELECT` must either be listed in the `GROUP BY`, or have some **aggregate function** applied to it.

> [!Note]
> A `GROUP BY` clause will group all `NULL` values into one single `NULL` summary **row**.

The **aggregate** **functions** we can apply to the grouped columns are:
* `SUM` - sums the values of all **rows** in the **group**.
* `COUNT` - counts the number of [[SQL Null|non-null]] **rows** in the **group**.
	* Instead of `COUNT(column)`, we can write `COUNT(*)` to include **rows** with `NULL`.
* `AVG` - averages the **non-null** **rows** in the **group**.
* `MIN` - returns the minimum value in the **group**.
* `MAX` - returns the minimum value in the **group**.
* `ANY_VALUE` - returns a random **non-null** value from the **group**.
* `ARRAY_AGG` - returns an array of all the values of the **group**.
* `STDDEV_POP` - calculates the **standard deviation** of the **group**.

> [!Note]
> We can nest [[SQL Data Processing Functions|data processing functions]] like `COALESCE` within these **aggregate functions**, such as to handle `NULL` values.

> [!Note]
> By default, the **aggregate functions** use [[SQL Bags and Sets|bag]] based mechanics, so we may need to use `DISTINCT`.
> * For example, `COUNT(DISTINCT no)`


> [!Example]
> This **diagram** shows a **table** after a `GROUP BY`, with the colours representing the **groups**:
> * ![[Pasted image 20260408152007.png|631]]
> ```SQL
> SELECT no,
> 	   SUM(amount) AS balance,
> 	   COUNT(amount) AS trans
> FROM movement
> GROUP BY no
> ```
> This query, with the same `GROUP BY` as the diagram above, returns the following:
> * ![[Pasted image 20260408152019.png|254]]