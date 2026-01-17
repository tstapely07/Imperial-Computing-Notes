---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - M40009
---
`any` checks if **at least one** element in the structure satisfies the given predicate.
```Haskell
any :: (a -> Bool) -> [a] -> Bool
any p [] = False
any p (x:xs) = p x || any p xs
```

`any` can also be defined in terms of a [[Foldr|fold]]:
![[Fold-Map Fusion#^87e4fa]]

>[!Example]
>```Haskell
>any even [2,4,6] = True
>any even [1,2,3] = True
>any even [1,3,5] = False
>```

