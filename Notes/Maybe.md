---
date: 2025-12-20
tags:
  - first-year
  - haskell
  - M40009
---
We have seen the dangerous `head` and `tail` functions:
![[Pattern Matching on Lists#^8e321b]]
![[Pattern Matching on Lists#^b1207a]]
 We can solve the issue by only promising to return `Maybe a`:
```Haskell
data Maybe a where
	Nothing :: Maybe a 
	Just :: a -> Maybe a
```
>[!Info]
>Or more concisely:
>```Haskell
>data Maybe a = Nothing | Just a
>```

Now we can define:
```Haskell
safeHead :: [a] -> Maybe a
safeHead [] = Nothing
safeHead (x:xs) = Just x
```

If we want to turn a value wrapped in a `Maybe` into a [[Lists|list]], we could define:
```Haskell
toList :: Maube a -> [a]
toList Nothing = []
toList (Just x) = [x]
```

