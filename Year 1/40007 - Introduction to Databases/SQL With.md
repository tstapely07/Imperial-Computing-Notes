---
date: 2026-04-06
tags:
  - first-year
  - M40007
---
In [[SQL Data Manipulation Language (DML)|SQL]], we can define a **temporary** named result using `WITH`, and then reference it later in the **query**.
* This is useful when we want to reference the same result multiple times.

```SQL
WITH decimal(digit) AS (VALUES (0), (1), (2), (3), (4), (5), (6), (7), (8), (9))
SELECT hundred.digit*100 + ten.digit*10 + unit.digit AS n
FROM decimal AS unit
	 CROSS JOIN decimal as ten
	 CROSS JOIN decimal as hundred
```
