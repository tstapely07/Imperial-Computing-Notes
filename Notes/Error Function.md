---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
```Haskell
error :: String -> a
```
The error function crashes, and outputs a message to the user.
```Haskell
error2 :: Int -> Int
error2 2 = error "It was two!"
error2 n = n
```
