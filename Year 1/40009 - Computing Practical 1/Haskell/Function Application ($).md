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

^2c28d9

^c4fe8c
>[!Info]
>Technically, `($)` is just a special version of `id` that only accepts [[Types, Values, and Functions|functions]].

It applies functions but with **low precedence**.
This means it can be used **instead of brackets**.
>[!Example]
>```Haskell
>head (map (+1) (filter even [1..10])) = 3
>head $ map (+1) $ filter even [1..10] = 3
>```

