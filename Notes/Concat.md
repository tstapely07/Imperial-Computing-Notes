---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - M40009
---
`concat` concatenates multiple lists into a single list.
```Haskell
concat :: [[a]] -> [a]
concat [] = []
concat (xs:xss) = xs ++ concat xss
```
>[!Example]
>```Haskell
>concat [[3, 4], [5, 6]] = [3, 4, 5, 6]
>```

>[!Tip]
>`concat` is best defined using a [[Foldr|fold]]:
>
```Haskell
concat :: [[a]]  -> [a]
concat xss = foldr (++) [] xss
```

^c2449e

