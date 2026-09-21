---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
A list is either: ^0b6000
* `[] :: [a]` - empty
* `x:xs :: [a]` - a value `x` appended onto a list `xs`.

So we can [[Pattern Matching|pattern match]] on these two cases:
```Haskell
isEmpty :: [a] -> Bool
isEmpty [] = True
isEmpty (x:xs) = False
```
>[!Warning]
>We need to write `(x:xs)` otherwise `isEmpty x:xs` is interpreted as `isEmpty x):xs` which is **not** what we want.

We could do a deeper pattern match:
```Haskell
isSingle :: [a] -> Bool
isSingle [x] = True
isSingle xs = False
```
When we write `f [x] = ...`, we pattern match on `[x]`, which is `x:[]`.

Here are two **simple** but **dangerous** functions:
```Haskell
head :: [a] -> a
head (x:xs) = x

tail :: [a] -> [a]
tail (x:xs) = xs
```

^8e321b

The `head` function extracts the first element of **any** list, while `tail` extracts everything else.
>[!Warning]
>The problem is that these two functions are not defined for the empty list, making them [[Pattern Matching#^51a9f1|partial functions]].
>Calling `head []` would cause a program to crash.

^b1207a

