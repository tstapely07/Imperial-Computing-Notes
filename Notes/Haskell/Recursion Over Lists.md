---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
There are many useful things we can do by [[Recursive Functions|recursing]] over lists.

We can add up all the values in a list:
```Haskell
sum :: [Int] -> Int
sum [] = 0
sum (x:xs) = x + sum xs
```

^dd7825

>[!Info]
>This is an **inductive definition**, because `sum (x:xs)` is defined in terms of the smaller `sum xs`.

Or we could find the length of the list:
```Haskell
length :: [a] -> Int
length [] = 0
length (x:xs) = 1 + length xs
```

^887d1b

>[!Info]
>Length is [[Parametric Polymorphism|polymorphic]], it works for a list of **any type**.

Here is a function two concatenate two lists:
```Haskell
(++) :: [a] -> [a] -> [a]
[] ++ ys = ys
(x:xs) ++ ys = x : (xs ++ ys)
```
>[!Info]
>`(++)` is a **function**, but `++` is an **operator**.
>>[!Example]
>>`[1,2,3] ++ [4,5,6] = [1,2,3,4,5,6]`

Sometimes we might want the first few values from a list:
```Haskell
take :: Int -> [a] -> [a]
take 0 _ = []
take n [] = []
take n (x:xs) = x : take (n-1) xs
```

Alternatively, we might want a list **without** the first few values.
```Haskell
drop :: Int -> [a] -> [a]
drop 0 xs = xs
drop n [] = []
drop n (x:xs) = drop (n-1) xs
```
>[!Success]
>Note `drop` is tail recursive, and so very efficient.

The (!!!) function is used to extract a single value from a list at an index:
```Haskell
(!!) :: [a] -> Int -> a
(x:xs) !! 0 = x
(x:xs) !! n = xs !! (n-1)
[] !! n = error "Can't !! empty lists!"
```
>[!Info]
>Here we use the [[Error Function|error function]] to define a case for an invalid index.
>>[!Example]
>>`[3,1,4,1,5] !! 0 = 3
>>`[3,1,4,1,5] !! 2 = 4>

