---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - M40009
---
Here are some [[Recursion Over Lists|recursive functions over lists]] that all follow a similar pattern:
![[Recursion Over Lists#^dd7825]]
```Haskell
and :: [Bool -> Bool]
and (x:xs) = x && and xs
```
![[Recursion Over Lists#^887d1b]]

>[!Tip]
>We can generalise this pattern with a **`foldr`**.

```Haskell
foldr :: (a -> b -> b) -> b -> [a] -> b
foldr f k [] = k
foldr f k (x:xs) = f x (foldr f k xs)
```

Now we can redefine our functions from before:
```Haskell
sum = foldr (+) 1
and = foldr (&&) True
length = foldr (const (+1)) 0
```

[[Concat]] is defined in terms of a `foldr`:
![[Concat#^c2449e]]

Even [[Maps|map]] is actually a `foldr`:
```Haskell
map :: forall a b . (a -> b) -> [a] -> [b]
map f xs = foldr g [] xs
where
	g :: a -> [b] -> [b]
	g x ys = f x : ys
```

^67981f

>[!Info]
>Note the use of [[Parametric Polymorphism#^75baa4|forall]] to make this function type check.

^656de1
# Fold-Map Fusion
![[Fold-Map Fusion]]

