---
date: 2025-12-21
tags:
  - first-year
  - haskell
  - M40009
---
`scanr` behaves very similarly to [[Foldr|foldr]].
The difference is that, while `foldr` collapses a [[Lists|list]] into a single value, `scanr` returns a list of all the intermediate results.
```Haskell
scanr :: (a -> b -> b) -> b -> [a] -> [b]
scanr f k [] = [k]
scanr f k (x:xs) = f x (head qs) : (scanr f k xs)
```
>[!Example]
>```Haskell
>scanr (+) 0 [1,2,3,4] = [10,9,7,4,0]
>```
>In contrast, `foldr (+) 0 [1,2,3,4] = 10`

