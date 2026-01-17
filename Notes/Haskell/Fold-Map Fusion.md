---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - M40009
---
Like [[Map Fusion|map fusion]] combines **two maps**, we can also combine a **map** and a **fold**.
```Haskell
foldr f k . map g = foldr (f . g) k
```

Where can we use this?
We can redefine [[Any|any]] and [[All|all]]:
```Haskell
any :: (a -> Bool) -> [a] -> Bool
any p = foldr ((||) . p) False
```

^87e4fa

```Haskell
all :: (a -> Bool) -> [a] -> Bool
all p = foldr ((&&) . p) True
```

^613e3e

Fold-map fusion extends to functions defined in terms of a fold, so we could have written:
```Haskell
all :: (a -> Bool) 
all p xs = (and . map p) xs
```

# Proof
We can prove that fold-map fusion is a **true law** by **induction** over the input list:

Our **inductive hypothesis** is:
```Haskell
(foldr f k . map g) xs = (foldr (f . g) k) xs
```

The **base case** is for `xs = []`:
```Haskell
LHS = (foldr f k . map g) []
    = foldr f k (map g []) -- (f . g) x = f(g(x))
    = foldr f k []
    = k
    
RHS = (foldr (f . g) k) []
    = foldr (f . g) k []
    = k
    
LHS = RHS
```
So the base case **holds**.

For the **inductive case** we assume the **inductive hypothesis** and prove for `x:xs`:
```Haskell
LHS = (foldr f k . map g) (x:xs)
    = foldr f k (map g (x:xs))
    = foldr f k (g x : map g xs)  -- map
    = f (g x) (foldr f k (map g xs)) -- foldr
    = f (g x) (foldr (f . g) k xs) -- inductive hypothesis
    = ((f . g) x) (foldr (f . g) k xs) -- (.)
    = foldr (f . g) k (x:xs) -- foldr
    = RHS
```

So **proved by induction** for all input lists.