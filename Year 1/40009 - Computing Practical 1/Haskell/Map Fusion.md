---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - M40009
---
Maps have a **nice optimisation** when using [[Function Composition (.)|function composition]]:
```Haskell
map g . map f = map (g . f)
```

Without the `(.)` operator that function composition provides, we would have to write something like:
```Haskell
map g (map f xs) = map gf xs
	where
		gf x = g (f x)
```
