---
date: 2025-12-15
tags:
  - first-year
  - haskell
  - M40009
---
We've seen how we can make a function [[Tail Recursion|tail recursive]] by using a [[Helper Functions|helper function]]  with an [[Accumulating Parameters|accumulating parameter]].
![[Tail Recursion#^9f5315]]

Or here, with `rev`:
![[Accumulating Parameters#^3b249c]]

>[!Tip]
>We can generalise this pattern to a **`foldl`**.

```Haskell
foldl :: (b -> a -> b) -> b -> [a] -> b
foldl f k [] = k
foldl f k (x:xs) = foldl f (f k x) xs
```
>[!Info]
>`foldl` generalises [[Tail Recursion|tail recursion]] for [[Recursion Over Lists|lists]].

>[!Warning]
>Let's consider this **tail recursive** version of `sum`:
>```Hasklell
>sum [1,2,3]
>= go 0 [1,2,3]
>= go (0+1) [2,3]
>= go ((0+1)+2) [3]
>= go (((0+1)+2)+3) []
>= (((0+1)+2)+3)
>= ...
>```
>The problem here is [[Lazy vs Eager Evaluation#^bc785e|lazy evaluation]] results in the accumulating parameter becoming  this **long chain** that must be **stored in memory** before proceeding.
>If we just added as we went, this would be a **single value**.
>We therefore have a **[[Memory Leaks|memory leak]]**.

^1a2f86

To avoid this, we must [[Adding Strictness|add strictness]], using a **bang annotation**.
```Haskell
sum' :: [Int] -> Int
sum' xs = go 0 xs
	where
		go :: Int -> [Int] -> Int
		go !y [] = y
		go !y (x:xs) = go (y+x) xs
```

^4cb27d

Since **`foldl`** may **leak memory**, we should **[[Adding Strictness|add strictness]]**:
```Haskell
foldl' :: (b -> a -> b) -> b -> [a] -> b
foldl' f k [] = k
foldl' f k (x:xs) = foldl' f k' xs
	where
		!k' = f k x
```
>[!Info]
>To use `foldl'`, we must [[Imports|import]] it from `Data.List`.


