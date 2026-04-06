---
date: 2026-04-06
tags:
  - first-year
  - M40007
---
A **table** or **column** can be temporarily renamed using `AS`.
* One use of this is to join a table to itself.

This query lists users with both a **current** and **deposit** account, and the respective account numbers:
* ![[Pasted image 20260406101319.png|499]]
```SQL
SELECT current_account.cname,
	   current_account.no AS current_no,
	   deposit_account.no AS deposit_no
FROM account AS current_account
	 JOIN account as deposit_account
	 ON current_account.cname = deposit_account.cname
	 AND current_account.type = 'current'
	 AND deposit_account.type = 'deposit'
```

