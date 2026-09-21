---
date: 2025-12-21
tags:
  - first-year
  - haskell
  - M40009
---
**If expressions** are a way to achieve conditional branching in code.
For example, here is a definition of the `signum`  function:
```Haskell
signum :: Integer -> Integer
signum n = 
	if n > 0 then 1
	else if n == 0 then 0
	else -1
```

>[!Tip]
>Generally, [[Guards|guards]] are preferred over **if expressions**, since they have a **cleaner syntax**.
>But sometimes we need **guards** in an expression context.
>Like we use [[Case Expressions|case expressions]] to [[Pattern Matching|pattern match]] in an expression, we may use **if expressions** for times where we **can't** use **guards**.

**If expressions** can be made **prettier** by using a [[Language Extensions|language extension]]:
```Haskell
{-# LANGUAGE MultiWayIf #-}
```
Instead of:
```Haskell
if cond1 then body1
else if cond2 then body2
else if cond3 then body3
else body4
```
We can now write:
```Haskell
if | cond1 -> body1
   | cond2 -> body2
   | cond3 -> body3
   | otherwise -> body4
```

