---
date: 2026-04-06
tags:
  - first-year
  - M40007
---
[[SQL Data Manipulation Language (DML)|SQL]] `UNION` implements [[Primitive Operators|relational algebra]] $\cup$.
**SQL** `EXCEPT` implements **relational algebra** $-$.
**SQL** `INTERSECT` implements **relational algebra** $\cap$.

Note that the two **tables** must be [[union compatible]].

For example, $\pi_{no}account-\pi_{no}movement$ would be:
```SQL
SELECT no
FROM account
EXCEPT 
SELECT no
FROM movement
```

