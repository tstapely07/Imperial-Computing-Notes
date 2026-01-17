---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - M40009
---
`All` checks if **every** element in the structure satisfies the given predicate.
```Haskell
all :: (a -> Bool) -> [a] -> Bool
all p [] = True
all p (x:xs) = p x && all p xs
```

`all` can also be defined in terms of a [[Foldr|fold]]:
![[Fold-Map Fusion#^613e3e]]


>[!Example]
>```Haskell
>all even [2,4,6] = True
>all even [1,2,3] = False
>all even [1,3,5] = False
>```
