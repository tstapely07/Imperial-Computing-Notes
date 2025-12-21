---
date: 2025-12-20
tags:
  - first-year
  - haskell
  - M40009
---
Sometimes we want a new [[User-Defined Datatypes|datatype]] that is **very similar** to another, but is of a **different type**.
For example, we may want to differentiate between £5, $5, and just the number 5.
To do this we use `newtype`:
```Haskell
newtype GBP = Pence Int
```
>[!Info]
>Here, `Pence` is the constructor.

Now we can write something like `Pence 100 :: GDP`.

Adding **instances** of [[Typeclasses]] to **newtypes** can be done manually:
```Haskell
instance Num GBP where
	Pence x + Pence y = Pence (x + y)
```
Since `GBP` is essentially the same as `Int`, these **instances** can be derived:
```Haskell
newtype GBP = Pence Int
	deriving (Num, Eq, Show)
```

