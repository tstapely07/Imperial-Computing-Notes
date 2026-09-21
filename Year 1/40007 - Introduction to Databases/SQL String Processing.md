---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
**ANSI** [[SQL Data Manipulation Language (DML)|SQL]] offers a number of **string processing functions**:
* `CHAR_LENGTH(str)` returns the number of characters in a string.
* `TRIM(str)` removes leading and trailing white spaces.
* `TRIM(LEADING pattern FROM str)` removes a custom list of characters from the start of a string.
* `TRIM(TRAILING pattern FROM str)` removes a custom list of characters from the end of a string.
* `POSITION(substr IN str)` finds the index of a substring within a string.
* `SUBSTRING(str FROM start FOR no)` extracts `no` characters from a string, starting from the index `start`.
* `str1 || str2` concatenates two strings together.
* `UPPER(str)` converts a string to all capitals.
* `LOWER(str)` converts a string to all lowercase.

> [!Warning]
> Note that **SQL** is $1$-indexed.