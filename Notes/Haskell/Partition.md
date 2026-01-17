---
date: 2025-12-24
tags:
  - first-year
  - haskell
  - M40009
---
`partition` on [[Lists|lists]] can be [[Imports|imported]] from `Data.List`.
It splits a **list** into **two [[Primitive Types and Values#^594903|tuples]]**, one of elements that **satisfy** the **predicate** and one of  elements that don't:
```Haskell
import Data.List (partition)
partition :: (a -> Bool) -> [a] -> ([a],[a])
```
>[!Example]
>```Haskell
>partition (> 3) [1,5,2,4,3] = ([5,4],[1,2,3])
>```

