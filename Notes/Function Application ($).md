---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - M40009
---
`($)` is a [[Higher-Order Functions|higher-order function]]  that simply applies a function to arguments.
```Haskell
($) :: (a -> b) -> a -> b
f $ x = f x
```
It applies functions but with **low precedence**.
This means it can be used **instead of brackets**.
>[!Example]
>```Haskell
>head (map (+1) (filter even [1..10])) = 3
>head $ map (+1) $ filter even [1..10] = 3
>```

