---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
We can write **recursive** queries in [[SQL Data Manipulation Language (DML)|SQL]] to allow a query to reference itself, searching for things such as **transitive connections**.
The general form is:
```SQL
WITH RECURSIVE name(col1, col2,...) AS (
	SELECT ...
	FROM ...
	WHERE ...
	
	UNION
	
	SELECT ...
	FROM ... JOIN name ON ...
)
SELECT * 
FROM name
```

The [[SQL Set Operators|union]] is executed repeatedly until no further rows are added to the answer.
* The top half of the query is where the starting point.

> [!Warning]
> It is important to use `UNION` not `UNION ALL`, to avoid infinite recursion if the loop bounced between the same two entries.


> [!Example]
> This query finds anyone who transitively came into contact with anyone visiting on the `11/Jan/99`:
> ```SQL
> WITH RECURSIVE contact(sdate, cname, tdate) AS (
> 	SELECT tdate as sdate,
> 		   cname,
> 		   tdate
> 	FROM account NATURAL JOIN movement
> 	WHERE tdate='11/Jan/1999'
> 	
> 	UNION
> 	
> 	SELECT contact.sdate,
> 		   account.cname,
> 		   movement.tdate
> 	FROM account
> 		 JOIN movement ON account.no = movement.no
> 		 JOIN contact ON contact.cname=account.cname 
> 					  OR contact.tdate=movement.tdate
> )
> SELECT * 
> FROM contract
> ```
> Here is each iteration of the query, showing how it terminates when no new **rows** are added:
> 1. ![[Pasted image 20260408175601.png]]
> 2. ![[Pasted image 20260408175615.png]]
> 3. ![[Pasted image 20260408175625.png]]
> 4. ![[Pasted image 20260408175632.png]]

  