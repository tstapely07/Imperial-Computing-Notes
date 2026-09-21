---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
Standard [[SQL Joins|joins]] in [[SQL Data Manipulation Language (DML)|SQL]] only return **rows** when there is a successful match.
* If we want to retain **all rows** from a **table**, even if they did not match anything in the other **table**, we use an **outer join**.

There are three types of **outer joins**:
A **left join** (`LEFT JOIN`), written $R\overset{L}\bowtie S$, returns every **row** in $R$, even if no **rows** in $S$ match.
* In the cases where no row in $S$ matches a **row** from $R$, the columns of $S$ are filled with [[SQL Null|NULL]].
A **right join** (`RIGHT JOIN`), written $R\overset{R}\bowtie S$, returns every **row** in $S$, even if no **rows** in $R$ match.
* In the cases where no row in $R$ matches a **row** from $S$, the columns of $R$ are filled with `NULL`.
An **outer join** (`OUTER JOIN`), written $R\overset{O}\bowtie S$ returns every **row** in $R$, even if no **row** in $S$ matches, and also every **row** in $S$, even if no **row** in $R$ matches. 
* This is equivalent to:
$$R\overset{O}\bowtie{S}\equiv (R\overset{L}\bowtie{S})\cup (R\overset{R}\bowtie{S})$$

```SQL
SELECT account.no, movement.amount
FROM account LEFT JOIN movement
			 ON account.no = movement.no
			 AND movement.amount < 0
```
* ![[Pasted image 20260408123655.png|198]]

> [!NOTE]
> All of these **joins** also have a `NATURAL` variant, for example `NATURAL LEFT JOIN`.