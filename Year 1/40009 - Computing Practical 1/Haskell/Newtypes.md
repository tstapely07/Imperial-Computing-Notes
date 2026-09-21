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

>[!Tip]
>Where possible, `newtype` should be used over  `data`, which defines a new [[User-Defined Datatypes|datatype]]. 
>This is because `data` has a **runtime cost**, and therefore a **performance penalty**.
>`newtype` has **no runtime penalty**.

>[!Info]
>There is also [[Type Aliases using `type`|type]], which also has no runtime impact, but has no type-safety.


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

[[Typeclasses]] must have a **unique instance** for a **given type**.
If we take [[Monoids|monoids]] as an example:
```Haskell
class Monoid m where
	mempty :: m
	mappend :: m -> m -> m
```
We have **two** options for `Monoid Int`, either `+` or `*`.
This is not allowed, and is why there is no `Monoid Int` built in, but we can use **newtypes** to solve this:
```Haskell
newType Sum = Sum Int
newType Product = Product Int
```
Now we can define:
```Haskell
instance Monoid Sum where
	mempty :: Sum
	mempty = Sum 0
	
	mappend :: Sum -> Sum -> Sum
	mappend (Sum x) (Sum y) = Sum (x+y)
```
And we can do similar with `Monoid Product`.
Both `Sum` and `Product`, as well as `Any` and `All`, which are **newtypes** on `Bool` can be [[Imports|imported]] from the `Data.Monoid` [[Modules|module]].


Another **useful** way of using **newtypes** is to **alter** an **existing instance's behaviour**.
One way to **sort** a [[Lists|list]] backwards is:
```Haskell
sortReverse :: Ord a => [a] -> [a]
sortReverse = reverse . sort
```
But this requires **two passes**.
We can do it in **one pass** using `Down`, which is defined in the `Data.Ord` [[Modules|module]].
```Haskell
newType Down a = Down a deriving Eq
instance Ord a => Ord (Down a) where
	Down x <= Down y = x >= y
```
Now we can write:
```Haskell
sortReverse :: Ord a => [a] -> [a]
sortReverse = sortOn Down
```
