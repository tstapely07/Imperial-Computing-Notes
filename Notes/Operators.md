---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
In general operators can be given types as if they were functions of [[Multiple Parameters|multiple arguments]].
```Haskell
(+) :: Int -> Int -> Int
(<=) :: Int -> Int -> Bool
```

Here's another useful operator:
```Haskell
(,) :: a -> b -> (a, b)
(,) x y = (x, y)
```

^f31bbb

>[!Info]
>Brackets are used to write **infix operators** like **prefix functions**.
>`5 + 3` is equivalent to `(+) 5 3`

^6fac04

>[!Info]
>Backticks can be used to write **prefix functions** like **infix operators**.
>`div 5 2` is equivalent to `5 'div' 2`

^07fced

