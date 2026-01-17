---
date: 2025-12-21
tags:
  - first-year
  - haskell
  - M40009
---
Syntax trees can represent expressions:
```Haskell
data Expr where
	Val :: Int -> Expr
	Var :: String -> Expr
	Add :: Expr -> Expr -> Expr
	Mul :: Expr -> Expr -> Expr
	-- ...
```
>[!Example]
>```
>(5 * (3 + 2)) + x
>         Add
>       /     \
>     Mul     Var "x"
>    /   \
> Val 5  Add
>       /   \
>   Val 3   Val 2
>```

