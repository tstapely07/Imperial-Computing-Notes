---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
[[Pattern Matching|Earlier]] we saw the recursive factorial function. Its definition relied on itself.
```Haskell
fact 0 = 1
fact n = n * fact (n-1)
```
This function is evaluated like so:
```Haskell
fact 3
= 3 * fact (2)
= 3 * (2 * fact(1))
= 3 * (2 * (1 * fact(0)))
= 3 * (2 * (1 * 1))
= 3 * (2 * 1)
= 3 * 2
= 6
```

Functions can also be mutually recursive.
```Haskell
even :: Int -> Bool
even 0 = True
even n = odd (n-1)

odd :: Int -> Bool
odd 0 = False
odd n = even (n-1)
```

![[Tail Recursion#^3fbd9a]]

