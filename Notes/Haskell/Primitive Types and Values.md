---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
Primitive types and values are those that are built in to Haskell.

These include:
* [[Numbers]]: ^1a9745
	* `3 :: Integer`
	* `3 :: Int`
	* `3:: Rational`
	* `3 :: Float`
	* `3 :: Double`
* Boolean values:
	* `True :: Bool`
	* `False :: Bool`
* Characters:
	* `'a' :: Char`
	* `'&' :: Char`
* Unit:
	* `() :: ()`

We can also define pairs.
If `x :: a` and `y :: b` then `(x,y) :: (a,b)` ^f1e733
```Haskell
(True, 'q') :: (Bool, Char)
(3.0,3) :: (Float, Int)
```

We can [[Pattern Matching|pattern match]] on a pair to extract an element.
Alternatively, there are two other functions, which we use if we truly don't care about the other element of the pair.
```Haskell
fst :: (a, b) -> a
fst (x, y) = x

snd :: (a, b) -> b
snd (x, y) = y
```
>[!Example]
>```Haskelll
>fst (10, 'a') = 10
>snd (3.2, True) = True
>```


Pairs can be extended to tuples can be extended to any size: ^594903
```Haskell
(x,y,z) :: (a,b,c)
(w,x,y,z) :: (a,b,c,d)
```

> [!Warning]
> Note that `((x,y),z) /= (x,y,z)`

