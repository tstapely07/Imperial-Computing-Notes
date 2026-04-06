---
date: 2026-04-06
tags:
  - first-year
  - M40007
---
`IN` tests if a **specific value** exists inside some **set**, often generated from a **subquery**.
> [!Example]
> ```SQL
> SELECT no
> FROM account
> WHERE type = `current`
> AND no IN (SELECT no
> 		   FROM movement
> 		   WHERE amount > 500)
> ```
> Is equivalent to:
> ```SQL
> SELECT DISTINCT account.no
> FROM account JOIN movement
> 	 ON account.no = movement.no
> WHERE type = 'current'
> AND amount > 500
> ```

`EXISTS` tests whether a **subquery** returns any rows at all.
> [!Example]
> To get the names of people without a deposit account, we could write:
> ```SQL
> SELECT DISTINCT cname
> FROM account
> WHERE NOT EXISTS
> 	(SELECT cname
> 	FROM account as deposit_account
> 	WHERE type = 'deposit'
> 	AND account.cname = deposit_account.cname)
> ```
> An equivalent alternative using `IN` is:
> ```SQL
> SELECT DISTINCT cname
> FROM account
> WHERE cname NOT IN
> 	(SELECT cname
> 	FROM account
> 	WHERE type = 'deposit')
> ```

Most **queries** involving [[SQL Set Operators|EXCEPT]] can be written using `NOT EXISTS`:
```SQL
SELECT no
FROM account
EXCEPT 
SELECT no 
FROM movement
```
Is equivalent to:
```SQL
SELECT no
FROM account
WHERE NOT EXISTS (SELECT no
				  FROM movement
				  WHERE no=account.no)
```

> [!Abstract] Definition
> A **subquery** that references the **outer query**, as in the example for `EXISTS`, is known as a **correlated subquery**.
> * This **subquery** is executed once for each row of the outer `WHERE` clause.

**SQL** also defines `SOME` and `ALL`, which work as expected:
* These are like [[any]] and [[all]] in [[Haskell]].

Branches that only have current accounts:
* ![[Pasted image 20260406110724.png|140]]
```SQL
SELECT bname
FROM branch
WHERE 'current' = ALL (SELECT type
					   FROM account
					   WHERE branch.sortcode = account.sortcode)
```

Branches that have a deposit account:
* ![[Pasted image 20260406110745.png|138]]
```SQL
SELECT bname
FROM branch
WHERE 'deposit' = SOME (SELECT type
						FROM account
						WHERE branch.sortcode = account.sortcode)
```

> [!Note]
> We know from [[40018 - Discrete Mathematics, Logic|first order logic]] that $\neg\exists\neg=\forall$, and the same holds for `SOME` and `ALL`.
> The following queries are equivalent, both returning:
> * ![[Pasted image 20260406111058.png|90]]
> ```SQL
> SELECT no
> FROM account
> WHERE 500 >= ALL (SELECT amount 
> 				 FROM movement
> 				 WHERE account.no = movement.no)
> ```
> ```SQL
> SELECT no
> FROM account
> WHERE NOT 500 < SOME (SELECT amount 
> 				 FROM movement
> 				 WHERE account.no = movement.no)
> ```

