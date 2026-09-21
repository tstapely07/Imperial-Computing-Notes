---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - M40009
---
`unzip` turns a list of pairs into two lists:
```Haskell
unzip :: [(a, b)] -> ([a], [b])
unzip [] = ([], [])
unzip ((x, y):xys) = (x:xs, y:ys)
	where
		(xs, ys) = unzip xys
```