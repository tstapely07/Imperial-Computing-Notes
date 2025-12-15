---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - M40009
---
We have already seen filters in [[List Comprehensions|list comprehensions]]:
```Haskell
[x | x <- xs, p x]
```
This allows us to write:
```Haskell
evens :: [Int] -> [Int]
evens xs = [x | x <- xs, even x]
```
Without a comprehension, we write:
```Haskell
evens :: [Int] -> [Int]
evens [] = []
evens (x:xs)
	| even x = x : evens xs
	| otherwise = evens xs
```

>[!Tip]
>We can capture this pattern using  a **`filter`**

```Haskell
filter :: (a -> Bool) -> [a] -> [a]
filter p [] = []
filter p (x:xs) 
	| p x = x : filter p xs
	| otherwise = filter p xs
```

Now we could simply write:
```Haskell
evens :: [Int -> Int]
evens xs = filter even xs
```
Or [[Point Free Functions|point free]]:
```Haskell
evens :: [Int -> Int]
evens = filter even
```

