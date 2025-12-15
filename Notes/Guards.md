---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
Sometimes we use a Bool to guard an equation:
```Haskell
fact :: Integer -> Integer
fact 0 = 1
fact n 
	| n < 0 = error "error"
	| otherwise = n * fact (n-1)
```
Otherwise is equivalent to `true`, and is therefore used as a catch-all.

> [!Warning]
> Do not be tempted to write something like
> ```Haskell
> fact n
> 	| n == 0 = 1
> 	| ...
> ```
> Guards are not as efficient as pattern matching.
> A pattern match should **always** be used where possible.

Like with [[Pattern Matching|pattern matching]], guards are matched top-down until a predicate evaluates to `true`.
If there is no match then an error is raised.