---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - "#M40009"
---
A function can be defined **without** explicitly naming its arguments.

This relies on **function extensionality**, which states:
```Haskell
forall x . f x == g x -> f == g
```
If two functions give the **same output** for every input, then they are the **same function**.

>[!Example]
>```Haskell
>double :: Int -> Int
>double x = x * 2
> 
>doubles :: [Int] -> [Int]
>doubles xs = map double xs
>```
>Both of these functions can be written point free:
>```Haskell
>double x = (*2)
>  
>doubles = map doubles
>```
>>[!Info]
>>The `xs` in `doubles` can be dropped.

Here's a **challenging**, and perhaps **excessive**, example of making a function point-free, where we derived a point-free definition of [[ConcatMap|concatMap]]:
![[ConcatMap#^714fe7]]



