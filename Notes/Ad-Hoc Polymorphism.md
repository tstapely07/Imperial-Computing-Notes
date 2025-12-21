---
date: 2025-12-20
tags:
  - first-year
  - haskell
  - M40009
---
Sometimes we have functions that are **overloaded** but with **different implementations** for **different types**.
For example, we have:
```Haskell
x :: Int
y :: Int
------------
x + y :: Int
```
But we could also have:
```Haskell
x :: Double
y :: Double
---------------
x + y :: Double
```
This shows `+` is defined for `Int` and `Double`.

Another example is equality:
```Haskell
x :: Int
y :: Int
--------------
x == y :: Bool

x :: Char
y :: Char
--------------
x == y :: Bool
```
However, we **can't** compare **all** values, even if they have the same type.
**[[Types, Values, and Functions|Functions]]** cannot be compared. 
If they could, we would be able to solve the [[Halting Problem|halting problem]], since we could compare if a program equalled a function that was known to halt.

![[Typeclasses#^96a000]]
![[Typeclasses#^70dbd6]]
![[Typeclasses#^68e598]]
![[Typeclasses#^89c7bb]]

Now using the `Eq` [[Typeclasses|typeclass]] we can define more interesting [[Polymorphism|polymorphic functions]]:
```Haskell
elem :: Eq a => a -> [a] -> Bool
elem x [] = False
elem x (y:ys) = x == y || elem x ys
```

With the `Ord` [[Typeclasses#^b61a45|typeclass]], we can define a function to insert into a sorted [[Lists|list]]:
```Haskell
insert :: Ord a => a -> [a] -> [a]
insert x [] = [x]
insert x (y:ys)@yss
	| x <= y = x : yss
	| otherwise = y : insert x ys
```
Using this and the [[Higher-Order Functions|higher-order function]] [[Foldr|foldr]], we can write an **insertion sort** in **one line**:
```Haskell
isort :: Ord a => [a] -> [a]
isort xs = foldr insert [] xs
```
