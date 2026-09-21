---
date: 2025-12-21
tags:
  - first-year
  - haskell
  - M40009
---
`scanl` behaves very similarly to [[Foldl|foldl]].
The difference is that, while `foldl` collapses a [[Lists|list]] into a single value, `scanl` returns a list of all the intermediate results.
```Haskell
scanl :: (b -> a -> b) -> b -> [a] -> [b]
scanl f k [] = [k]
scanl f k (x:xs) = k : scanl f (f k x) xs
```
>[!Example]
>```Haskell
>scanl (+) 0 [1,2,3,4] = [0,1,3,6,10]
>```
>In contrast, `foldl (+) 0 [1,2,3,4] = 10`

