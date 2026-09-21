---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
We have seen tuples like `(x,y)` as values of type `(a,b)` [[Primitive Types and Values|already]].
So we could define:
```Haskell
add :: (Int, Int) -> Int
add (x,y) = x + y
```
> [!Warning]
> This forces pattern matching on a pair, and is **not** idiomatic haskell.

Consider these two basic functions
```Haskell
plusOne :: Int -> Int
plusOne x = x + 1

plusTwo :: Int -> Int
plusTwo x = x + 2
```

We might want a more general function:
```Haskell
plus :: Int -> (Int -> Int)
plus 1 = plusOne
plus 2 = plusTwo
```
> [!Info]
> This function produces a function of type `Int -> Int`

To define plus for any `x`, we can use a [[Lambda Expressions|lambda expression]] to write:
```Haskell
plus :: Int -> (Int -> Int)
plus x = \y -> x + y
```
To understand this, notice that:
```Haskell
plusOne = \y -> 2 + y
plusTwo = \y -> 1 + y
```

To go one step further, we can define plus **as if** it has multiple arguments:
```Haskell
plus :: Int -> (Int -> Int)
plus x y = x + y
```
This **behaves exactly the same** as the previous plus function.
> [!Info]
> The precedence of associativity of functions states that `a -> (b -> c) === a -> b -> c`.
> So we could write the type of `plus` as `Int -> Int -> Int` without ambiguity.

>[!Warning]
>Note that `a -> (b -> c) /= (a -> b) -> c`


