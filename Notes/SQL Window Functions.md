---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
**Window functions** allow you to perform [[SQL Group By|aggregate functions]] across a set of **rows**, the **window**, to get summary data, without collapsing them into a single **row**.
* The `OVER()` **function** is the keyword that turns an **aggregate function** into a **window function**.
	* For example: `SUM(amount) OVER() AS total`.
* We can isolate the calculation to specific groups within the **window**, a bit like a temporary `GROUP BY`, by using `PARTITION BY` within the `OVER` clause.
	* For example: `SUM(amount) OVER(PARTITION BY tdate) AS daily_total`.

> [!Example]
> **Windows** can often achieve the same effect as a [[SQL Subqueries|subquery]] in a [[SQL Select in From|FROM]] clause:
> ```SQL
> SELECT DISTINCT no,
>        SUM(amount) OVER (PARTITION BY no) AS balance,
>        ROUND(100*SUM(amount) OVER (PARTITION BY no) / 
> 	      SUM(amount) OVER (), 1) AS pc
> FROM movement
> ORDER BY no
> ```
> * Note that `DISTINCT` is necessary, since otherwise we have the same **row** duplicated each time the same `no` occurs.
> This query returns:
> * ![[Pasted image 20260408162045.png|264]]

Within an `OVER` clause we can also add an [[SQL Order By|ORDER BY]] to sort the **rows** within the specific **window**.
	* For example: `SUM(amount) OVER(ORDER BY tdate) AS running_total`
	* Using `ORDER BY` changes the behaviour of **aggregate functions** to a **running total**.
	* `ORDER BY` can also be combined with `PARTITION BY`.

When `ORDER BY` is used for a **window**, we get access to many more functions:
* `LEAD(A)` returns the next value of column `A` in the **window**, or [[SQL Null|NULL]].
	* There is also `LEAD(A,offset,default)`. `LEAD(A)` is the same as `LEAD(A,1,NULL)`.
* `LAG(A)` returns the last value of column `A` in the **window**, or `NULL`.
	* There is also `LAG(A,offset,default)`. `LAG(A)` is the same as `LAG(A,1,NULL)`.
* `RANK()` gives each **row** an integer rank, giving ties the same **number** and skipping the next number(s).
* `DENSE_RANK()` is like `RANK()`, but doesn't skip any numbers.
* `ROW_NUMBER()` is like `RANK()` but tied **rows** are given different numbers.
* `FIRST_VALUE(A)` gives the first value of the column $A$ in the **window**.
* `LAST_VALUE(A)` gives the last value of the column $A$ in the **window**.

Although `ORDER BY` does a running total of all the **rows** up to the current **row** by default, we can specify other behaviour, using `ROWS BETWEEN ... AND ...` or `RANGE BETWEEN ... AND ...`
* When using `ROWS`, if two **rows** have the same value, they are still processed one-by-one, whereas using `RANGE` causes **rows** with the same value to all be included in the calculation.
* `UNBOUNDED PRECEDING` counts from the beginning of the **window**.
* `n PRECEDING` counts from `n` **rows** before the current **row**.
* `CURRENT ROW` is the row being processed.
* `n FOLLOWING` counts `n` **rows** after the current **row**.
* `UNBOUNDED FOLLOWING` counts to the end of the **window**.
The default behaviour of `ORDER BY` is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.

> [!Example] Examples
> Here's an example showing the different ways to rank **rows**:
> ```SQL
> SELECT mid,
> 	   tdate,
> 	   amount,
> 	   RANK() OVER (ORDER BY tdate),
> 	   DENSE_RANK() OVER (ORDER BY tdate),
> 	   ROW_NUMBER() OVER (ORDER BY tdate)
> FROM movement
> ```
> This query returns:
> * ![[Pasted image 20260408162304.png|448]]
> 
> Here's an example of looking at other **rows** in the **window**:
> ```SQL
> SELECT mid,
> 	   amount,
> 	   LEAD(amount) OVER (ORDER BY amount DESC) as next,
> 	   LAG(amount) OVER (ORDER BY amount DESC) as previous,
> 	   ROUND(AVG(amount) OVER
> 		   (ORDER BY amount ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING), 2) AS trend
> FROM movement
> ```
> This query returns:
> * *![[Pasted image 20260408164312.png|392]]