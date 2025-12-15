---
date: 2025-12-14
tags:
  - first-year
  - haskell
  - M40009
---
`ConcatMap` is another useful function:
```Haskell
concatMap :: (a -> [b]) -> [a] -> [b]
concatMap f [] = []
concatMap f (x:xs) = f x ++ concatMap f xs
```
>[!Example]
>Using a [[Lambda Expressions|lambda expression]]  we can duplicate each letter in a [[Strings|string]]:
>```Haskell
>concatMap  (\x -> [x, x]) "hello" = "hheelllloo"
>```

We can write our recursive definition of `concatMap` in a **better** way, using two functions we've seen before, [[Concat|concat]] and [[Maps|map]], and [[Function Composition (.)|function composition]]:
>[!Success]
>```Haskell
>concatMap f xs = (concat . map f) xs
>```

>[!Info]
>Or even [[Point Free Functions|point free]]:
>```Haskell
>concatMap = (concat .) . map
>```
>This can be more clearly derived by treating the `.` **[[Operators|operator]]** as a **prefix function** `(.)`:
>```Haskell
>concatMap f = concat . (map f)
>concatMap f = (.) concat (map f))
>``` 
>Now this is in the form `g(h(x))`, where `g` is `(.) concat`, `h` is `map`  and `x` is `f`.
>So we can use `.` to turn `g(h(x)) into (g . h) x`:
>```Haskell
>concatMap f = ((.) concat) . map) f
>```
>Finally, we can drop the `f`, and turn the `(.)` [[Types, Values, and Functions#^22b73f|prefix function]] back into an [[Operators|infix operator]]:
>```Haskell
>concatMap = (concat .) . map
>```
>>[!Warning]
>>But perhaps we are guilty of [[Function Composition (.)#^e704cd|going too far with function composition]].

^714fe7








