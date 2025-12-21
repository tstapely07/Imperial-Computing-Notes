---
date: 2025-12-13
tags:
  - haskell
  - M40009
  - first-year
---
A list is an **ordered** sequence of values of the **same type**.
Here are some lists:
```Haskell
[3,5] :: [Int]
['a','b','c'] :: [Char]
[True,False,True] :: Bool
```
These are some invalid lists:
```Haskell
[3, False]
[[3],3]
```
They are **invalid** because their elements are **not the same type**.

Lists of lists are also permitted:
```Haskell
[[3,5],[7,2]] :: [[Int]]
[[[True], [False]], [[True, True]]] :: [[[Bool]]]
```

Every type also has an empty list, such as `[] :: [Int]` and `[]: [Bool]`.
`[]` is actually a [[Parametric Polymorphism|polymorphic]] value - `[] :: forall a . [a]`.
We could write `[]@Int :: [Int]`, like we did [[Parametric Polymorphism#^0e8644|here]], but that is unnecessary.

Every list can be decomposed:
```Haskell
[3,1,4,5]
= 3 : [1,4,5]
= 3 : 1 : [4,5]
= 3 : 1 : 4 : [5]
= 3 : 1 : 4 : 5 : []
```
The `(:)`, pronounced 'cons', pulls away the first element from the list.
It is an [[Operators|operator]] of type `(:) :: a -> [a] -> [a]`.