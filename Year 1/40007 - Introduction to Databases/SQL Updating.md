---
date: 2026-04-06
tags:
  - first-year
  - M40007
---
We can **update** values in a **table** using `UPDATE`.
> [!Example]
> ```SQL
> UPDATE account
> SET type = 'deposit'
> WHERE no = 100
> ```

The `WHERE` clause is optional, but should virtually always be included.