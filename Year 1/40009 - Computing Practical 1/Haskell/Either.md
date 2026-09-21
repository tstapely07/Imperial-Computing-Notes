---
date: 2025-12-20
tags:
  - first-year
  - haskell
  - M40009
---
Like `Maybe`,  `Either`  provides another way to fix the **dangerous** [[Pattern Matching on Lists#^8e321b|head]]  function.
```Haskell
data Either a b where
	Left :: a -> Either a b
	Right :: b -> Either a b
```
>[!Example]
>```Haskell
>Right 12 :: Either String Int
>Right 12 :: Either Bool Int
>Right 12 :: Either a Int
> 
>Left "Hello" :: Either String Int
>Left "Hello" :: Either String String
>Left "Hello" :: Either String b
>```

Now we could define:
```Haskell
safeHead ::  [a] -> Either String a
safeHead [] = Left "Empty list"
safeHead (x:xs) = Right x
```
