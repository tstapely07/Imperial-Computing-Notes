---
date: 2025-12-15
tags:
  - first-year
  - haskell
  - M40009
---
> [!Tip]
> Functions are **more efficient** when they are tail recursive.
A tail recursive function just call itself with different argument.

^3fbd9a

```Haskell
isPower2 :: Int -> Bool
isPower2 0 = False
isPower2 1 = True
isPower2 n
	| n `mod` 2 /= 0 = False
	| otherwise = isPower2 (n `div` 2)	
```


Functions can be made to be **tail recursive** by creating a [[Helper Functions|helper function]] with an [[Accumulating Parameters|accumulating parameter]]:
```Haskell
sum :: [Int] -> Int
sum xs = go 0 xs
	where
		go :: Int -> [Int] -> Int
		go y [] = y
		go y (x:xs) = go (y + x) xs
```

^9f5315

>[!Info]
>Here, the **helper function** `go` is **tail-recursive**.

