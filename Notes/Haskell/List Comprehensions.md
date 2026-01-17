---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
A list comprehension is a convenient way of building a list.
```Haskell
[1..10] = [1,2,3,4,5,6,7,8,9,10]
[0,2..10] = [0,2,4,6,8,10]
```
>[!Warning]
>This works poorly with floats.

Infinite lists are also possible:
```Haskell
[0..] = [0,1,2,3,4,5,6,7,8,9,10,...]
```
This is an infinite list of all the naturals.

We can use a **`|`** to depend on a **stream**:
```Haskell
[x * 3 | x <- [0..]] [0,3,6,9,...]
```

Or we could depend on **multiple streams**, separated by **commas**:
```Haskell
[x * y | x <- xs, y <- ys]
```
If `xs = [1,2,3]` and `ys` = `[4,5]`, then this comprehension becomes `[4,5,8,10,12,15]`.
For each `x`, we iterate through all `ys`.

One stream could **depend on another stream**:
```Haskell
[x | xs <- xss, x <- xs]
```
> [!Info]
> The order is important, since it dictates the **scope** of each stream.
> Clauses to the right can depend on those to the left, but not vice versa.

Another useful comprehension is a filter:
```Haskell
[x | x <- [0..], even x] = [0,2,4,6,...]
```
This will generate `x` when the predicate is true.