---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - M40009
---
Suppose we have a function `ord`:
```Haskell
ord :: Char -> Int
ord 'a' = 97
ord 'b' = 98
```
Now suppose we want to convert some list `xs :: Char` into `[Int]`
>[!Example]
>`['h','e','l','l','o']`
>to
>`[104,101,108,108,111]`

We could define `ords` using [[Recursion Over Lists|recursion]]:
```Haskell
ords :: [Char] -> [Int]
ords [] = []
ords (x:xs) = ord x : ords xs
```

The `succ` function adds 1 to an integer.
Suppose we wanted to add 1 to every element in a list:
```Haskell
succs :: [Int] -> [Int]
succs [] = []
succs (x:xs) = succ x : succs xs
```

>[!Tip]
>This pattern can be captured using the **`map`** function:

```Haskell
map :: (a -> b) -> [a] -> [b]
map f [] = []
map f (x:xs) = f x : map f xs
```

Alternatively, map can be defined in terms of a [[Foldr|`foldr`]]: 
![[Foldr#^67981f]]
![[Foldr#^656de1]]

Now, we could have written `ords` and `succs` as:
```Haskell
ords xs = map ord xs

succs xs = map succ xs
```

>[!Info]
>A [[List Comprehensions|list comprehension]] is a map:
>```Haskell
>[f x | x <- xs] = map f xs
>```

#  Map Fusion
![[Map Fusion]]