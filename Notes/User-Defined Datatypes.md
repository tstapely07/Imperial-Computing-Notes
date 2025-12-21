---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
Haskell provides many datatypes, such as `Bool`, but datatypes can also be defined manually: ^631f6d
```Haskell
data Bool where
	True :: Bool
	False :: Bool

data Integer where
	0 :: Integer
	1 :: Integer
	...
```

Anything starting with a **capital letter** can be defined as a datatype:
```Haskell
data Cowboy where
	Good :: Cowboy
	Bad :: Cowboy
	Ugly :: Cowboy
```
Equivalently, we can write:
```Haskell
data Cowboy = Good | Bad | Ugly
```
Note the constructors such as `Good` and `Bad` also **need capitals**.

Functions can use user-defined datatypes:
```Haskell
trust :: Cowboy -> Bool
trust Good = True
trust x = False
```
This example shows how we can also [[Pattern Matching|pattern match]] on our datatype.