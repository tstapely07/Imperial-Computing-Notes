---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - M40009
---
We've seen the regular [[Zip|zip]]:
![[Zip#^d8d4ac]]
![[Zip#^2d9442]]
![[Zip#^154031]]

Now suppose we want to combine the elements from the lists in different ways:
```Haskell
zipWith :: (a -> b -> c) -> [a] -> [b] -> [a]
zipWith f (x:xs) (y:ys) = f x y : zipWith f xs ys
zipWith _ _ _ = []
```
Recall that we can treat **[[Operators|operators]]** like **[[Types, Values, and Functions#^22b73f|functions]]**:
![[Operators#^6fac04]]
>[!Example]
>This means we can write:
>```Haskell
>zipWith (+) [1,2,3] [10,20,30] = [11,22,33]
>```

Using the comma  operator we can define our original [[Zip|zip]]:
![[Operators#^f31bbb]]
```Haskell
zip :: [a] -> [b] -> [(a, b)]
zip xs ys = zipWith (,) xs ys
```
