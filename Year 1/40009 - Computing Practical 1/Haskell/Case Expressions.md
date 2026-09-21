---
date: 2025-12-21
tags:
  - first-year
  - haskell
  - M40009
---
**Case expressions** are used when we want to [[Pattern Matching|pattern match]] within a [[Types, Values, and Functions|function]], and we can't do it in the **definition**.
One case where this occurs is when we want to **pattern match** on the result from a function call:
```Haskell
getAge :: String -> Int
getAge name = case lookup name database of
	Just age -> age
	Nothing -> error "No age for this name"
	where 
		database = [("Tom", 18), ("Anish", 18)]
```
>[!Info]
>This example uses `lookup`, which has the following **type signature**:
>```Haskell
>lookup :: Eq a => a -> [(a, b)] -> Maybe b
>```

