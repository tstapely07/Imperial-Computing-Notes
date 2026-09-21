---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
When using [[Lists|lists]] and [[Recursive Functions|recursion]], an accumulating parameter is a useful tool.

Here is a function to reverse values:
```Haskell
reverse :: [a] -> [a]
reverse [] = []
reverse (x:xs) = reverse xs ++ [x]
```
>[!Warning]
>Using `++` is inefficient.

Here is a better way, using an accumulating parameter:
```Haskell
rev :: [a] -> [a]
rev xs = rev' xs []
	where
		rev' :: [a] -> [a] -> [a]
		rev' [] ys = ys
		rev' (x:xs) ys = rev' xs (x:ys)
```

^3b249c

