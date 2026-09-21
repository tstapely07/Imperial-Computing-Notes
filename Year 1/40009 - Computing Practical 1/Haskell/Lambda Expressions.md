---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
We've seen how we can define and name a [[Types, Values, and Functions#^22b73f|function]], but we not every function needs a name, some can be **anonymous**.
We can write lambda expressions using `\`.
For example, `\x -> x + 1` defines an anonymous function that increments its parameter, `x`.

Anonymous functions can also take [[Multiple Parameters|multiple parameters]], here is one that adds two values:
```Haskell
(\x y -> x + y)
```

Lambda functions can be given a name:
```Haskell
addOne \x -> x + 1
```
This is **exactly equivalent** to:
```Haskell
addOne x = x + 1
```
> [!Info]
> More formally, `f x = y` and `f = \x -> y` are equivalent.


> [!Tip]
> Lambda expressions are convenient when using [[Higher-Order Functions|higher-order functions]], such as a `map` or a `foldl`/`foldr`.

