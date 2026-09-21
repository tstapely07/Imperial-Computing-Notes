---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - M40009
---
There is an **isomorphism** between these functions:
```Haskell
(a, b) -> c ~= a -> b -> c
```
These means that the two different ways of writing the function are **equivalent** and we can **freely convert** between them.

The `curry` function takes a function that takes a **[[Primitive Types and Values#^f1e733|pair]]** and converts it into a standard Haskell function that takes **[[Multiple Parameters|two arguments]]**:
```Haskell
curry :: ((a, b) -> c) -> (a -> b -> c)
curry f x y = f (x, y)
```
>[!Example]
>It's harder to think of an example for `curry` using only standard functions, since almost every standard function is **already curried**.
>But we can observe:
>```Haskell
>curry fst = const
>```


The `uncurry` function does the **opposite**, taking a standard function of **two arguments** and converting it into a function that takes a **pair**:
```Haskell
uncurry :: (a -> b -> c) -> ((a, b) -> c)
uncurry f (x, y) = f x y
```
>[!Example]
>```Haskell
>pairAdd :: (Int, Int) -> Int
>pairAdd = uncurry add
>```
>>[!Example]
>>```Haskell
>>pairAdd (1,2) = 3
>>```


>[!Info]
>`curry` and `uncurry` are **opposites** of each other:
>```Haskell
>curry . uncurry = id
>uncurry . curry = id
>```
>This proves the **isomorphism** we stated earlier.

