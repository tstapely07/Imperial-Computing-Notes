---
date: 2026-04-06
tags:
  - first-year
  - M40007
---
> [!Warning]
> One way to carry out a **join** in [[SQL Data Manipulation Language (DML)|SQL]] is to write two **tables** in the `FROM` clause of a [[SQL Select|SELECT]], and then use a `WHERE` clause.
> * But writing multiple tables in the `FROM` clause is bad practice and should never be done.

Instead, **SQL** provides a number of **join** operators:
* `CROSS JOIN` is equivalent to the [[Primitive Operators|relational algebra product]].
* `NATURAL JOIN` is equivalent to [[Derived Operators|natural join]] in **relational algebra**.
* `JOIN ON` is like a **theta join**.
* `JOIN USING` is a shorthand for `JOIN ON` when the **column names** are identical.

The following **SQL** queries are all equivalent, and return the following table:
* ![[Pasted image 20260406100218.png|619]]

Classic **SQL**:
```SQL
SELECT branch.*, no, type, cname, rate
FROM branch, account
WHERE branch.sortcode = account.sortcode
```

`CROSS JOIN`:
```SQL
SELECT branch.*, no, type, cname, rate
FROM branch CROSS JOIN account
WHERE branch.sortcode = account.sortcode
```

`NATURAL JOIN`:
```SQL
SELECT *
FROM branch NATURAL JOIN
	 account
```

`JOIN ... ON`:
```SQL
SELECT branch.*, no, type, cname, rate
FROM branch JOIN account
	 ON branch.sortcode = account.sortcode
```

`JOIN ... USING`:
```SQL
SELECT branch.*, no, type, cname, rate
FROM branch JOIN account
	 USING (sortcode)
```
