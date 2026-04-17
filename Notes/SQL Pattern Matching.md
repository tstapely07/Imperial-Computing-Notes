---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
In **ANSI** [[SQL Data Manipulation Language (DML)|SQL]], we can test strings against patterns, using the `LIKE` operator in a `WHERE` clause.
* `_` matches exactly one character.
* `%` matches any number of characters, including 0.
* We can use `ESCAPE` to define an escape character, for example `ESCAPE '\'`, which we can use for if we need to treat `_` or `%` as actual characters.

> [!Example]
> Customers whose first initial is `P`, and have a second initial:
> ```SQL
> SELECT DISTINCT cname
> FROM account
> WHERE cname LIKE '%, P._.'
> ```