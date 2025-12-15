---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - "#M40009"
---
Sometimes we want to **combine two functions** to make another:
```Haskell
succ (ord 'a') = succ 97 = 98
```
This function is a Caesar cipher with a shift of  1.
We could write it:
```Haskell
cipher :: Char -> Int
cipher c = succ (ord c)
```

>[!Tip]
>The pattern of function composition can be captured by the `.` operator.

```Haskell
(.) :: (b -> c) -> (a -> b) -> (a -> c)
(g . f) x = g (f x)
```
Alternatively, we could define it using a [[Lambda Expressions|lambda expression]]:
```Haskell
(g . f) = \x -> g (f x)
```

Now we can simply write:
```Haskell
cipher x = (succ . ord) x
```
We could even write it [[Point Free Functions|point free]]:
```Haskell
cipher = succ . ord
```

Since `(.)`, returns a function, we could use it within a [[Maps|map]]:
```Haskell
ciphers :: [Char] -> [Int]
ciphers xs = map (succ . ord) xs
```

>[!Warning]
>Don't go too far with function composition:
>```Haskell
>f a b c d = (a b) (c d)
>```
>`f` could be written [[Point Free Functions|point free]] using function composition:
>```Haskell
>f = ((.) (.))
>```
>But this is **excessive**.

^e704cd




