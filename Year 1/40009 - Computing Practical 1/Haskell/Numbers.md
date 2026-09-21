---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
Earlier, we said integer literals can assume multiple types:
```Haskell
7 :: Int
7 :: Integer
7 :: Double
```
This isn't the entire truth. 
While these are all valid instantiations of integer literals, `7` itself only has **one type**.
```Haskell
7 :: Num a => a
```
>[!Info]
>This is read as '7 has type `a`, so long as `a` is a `Num`'
>The compiler while use type inference to work out which type to use.

`Num` is a [[Typeclasses|typeclass]]. 
It defines functions that work for a **family** of different types. 

Like integer literals, literals with a decimal point also have a typeclass.
```Haskell
5.6 :: Fractional a => a
```
`Fractional` things can be perfectly represented by  fraction of two integers, called a `Rational`.

There are operations that we can use across all numbers, like `(+)`, `(*)`, `negate`, and `abs`. 
A function of type `Int -> Int` can use any of these, since `Int` is a `Num`, but we can generalise:
```Haskell
add :: Num a => a -> a
add x = x + x
```
>[!Info]
>This says that `add` works for any type `a`, as long as `a` is a `Num`.

If we want division, we either need an `Integral` type, which allows for integer-division and modulus, or a `Fractional` type for 'exact' division.
```Haskell
recip :: Fractional a => a -> a
recip x = 1 / x
```

Finally, how does `7` become an `Int` or `5.6` become a Double?
Whenever we write these numeric literals, Haskell will use two functions behind the scene to construct the number type we wanted.
```Haskell
fromInteger :: Num a => Integer -> a
fromRational :: Fractional a => Rational -> a
```

Here's one final useful function.
```Haskell
fromIntegral :: (Integral a, Num b) => a -> b
```
>[!Info]
>This takes integer-like types and turns them into any other numerical type.

