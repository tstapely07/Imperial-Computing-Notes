---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - M40009
---
A zip functions pairs the elements from two lists in order: ^d8d4ac
```Haskell
zip :: [a] -> [b] -> [(a,b)]
zip (x:xs) (y:ys) = (x, y) : zip xs ys
```

^2d9442

>[!Example]
>```Haskell
>zip [1,2,3] ['a','b','c'] = [(1,'a'), (2,'b'), (3,'c')]
>zip [True, False] [1,2,3] = [(True,v 1), (False, 2)]
>```

^154031

>[!Tip]
>To combine the elements from two lists in a different way, we can use [[ZipWith|zipWith]].


>[!Tip]
>The opposite of `zip` is [[Unzip|unzip]]

