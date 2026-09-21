---
date:
tags:
  - first-year
  - "#M40009"
  - "#haskell"
---
The order of evaluation of a function is important.
There are two main strategies.
* Normal/lazy evaluation - first evaluate the outermost term before moving inwards. ^bc785e
* Applicative/eager evaluation - first evaluate the innermost term before moving outwards.
> [!info]
> Haskell uses lazy evaluation. ^6088ff
# Example
Consider the `square` function, and the `two` function from [[Types, Values, and Functions|before]].
```Haskell
square :: Integer -> Integer
square x = x * x

two :: Integer -> Integer
two x = 2
```
## Normal/Lazy
```Haskell
square (two 5)
= two 5 * two 5
= 2 * two 5
= 2 * 2
= 4
```
## Applicative/Eager
```Haskell
square (two 5)
= square 2
= 2 * 2
= 4
```

> [!info]
> If an answer is reachable, then lazy evaluation will always find it - Church-Rosser theorem.

