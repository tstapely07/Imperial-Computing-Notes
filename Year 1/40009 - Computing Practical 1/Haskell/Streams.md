---
date: 2025-12-20
tags:
  - first-year
  - haskell
  - M40009
---
An **infinite** **[[Lists|list]]** of values is called a **stream**.

```Haskell
repeat :: Int -> Int
repeat x = x : repeat x
```
We can use `repeat` to define a list like `repeat 0 = [0,0,0,...]`.
>[!Tip]
>A better version of `repeat` is:
>```Haskell
>repeat :: Int -> [Int]
>repeat x = xs
>	where xs = x:xs
>```
>This is more efficient because of **sharing**.

We can create an **instance** of the `Num` **[[Typeclasses|typeclass]]** for a **stream**:
```Haskell
instance Num [Integer] where
	fromInteger :: Integer -> [Integer]
	fromInteger  = repeat x
	
	(+) :: [Integer] -> [Integer] -> [Integer]
	xs + ys = zipWith (+) xs ys
	
	-- ...
```

>[!Example]
>This lets us do **powerful** things, such as:
>```Haskell
>fibs = 0 : 1 : (fibs + tail fibs)
>```
>Note how this makes use of [[Lazy vs Eager Evaluation|lazyness]].


