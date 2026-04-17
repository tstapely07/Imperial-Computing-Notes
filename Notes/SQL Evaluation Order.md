---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
[[SQL Data Manipulation Language (DML)|SQL]] clauses are evaluated in the following order:
1. **FROM**
2. **WHERE**
3. [[SQL Group By|GROUP BY]]
4. [[SQL Having|HAVING]]
5. [[SQL Select|SELECT]]
6. [[SQL Order By|ORDER BY]]

This explains why we cannot use aliases from a `SELECT` in a `WHERE` or `HAVING` clause, but we can in the final `ORDER BY`.