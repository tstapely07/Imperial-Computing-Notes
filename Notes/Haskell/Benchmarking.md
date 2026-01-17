---
date: 2025-12-21
tags:
  - first-year
  - haskell
  - M40009
---
There is a lot of **confusing syntax** involved with **benching** that isn't necessarily worth memorising.
A key point is then requirement for [[Adding Strictness|strictness]].

Since Haskell is [[Lazy vs Eager Evaluation|lazy]], we have to make sure it fully evaluates the expression we're trying to **benchmark**.

The standard `let !y = f x` isn't enough, since this only evaluates enough to expose the top-most constructor.
>[!Example]
>If we were benching [[Scanl|scanl]]:
>```Haskell
>scanl (+) 0 [0..10000]
>= 0 : scanl (+) (0+0) [1.10000]
>```
>The evaluation would stop here. 

>[!Tip]
>To ensure the expression is fully evaluated, we use `nf` - **normal form**.
>This can be [[Imports|imported]] as `import Test.Tasty.Bench (bench, nf)`.

The **general syntax** for a basic benchmark would be:
```Haskell
import Test.Tasty.Bench (bench, nf)
bench "foldr bench" (nf (foldr (+) 0) [1..100])
```

To compare two implementations we should define anything consistent in a `where` clause, to ensure fairness:
```Haskell
bench "foldl bench" (nf (foldl' (+) 0) xs)
bench "foldl' bench" (nf (foldl' (+) 0) xs)
	where 
		xs = [1..1000]
```


