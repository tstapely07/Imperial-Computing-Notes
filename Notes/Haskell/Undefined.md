---
date: 2025-12-21
tags:
  - M40009
  - first-year
  - haskell
---
When writing in Haskell, sometimes we have **not finished** the implementation to one [[Types, Values, and Functions|function]], but we want to **compile** the program to test **another function**.
We may also need to leave the **function's signature** in place.

To solve these issues, we can use `undefined`.
`undefined` is defined circularly:
```Haskell
undefined :: a
undefined = undefined
```
**Returning** it would cause a program to blow up, but **GHC** catches this and raises an error.

For example:
```Haskell
calculateValue :: Int -> Int
calculateValue x
	| x > 0 = x * 2
	| otherwise = undefined
```
>[!Example]
>Here, `calculateValue 2` would return `4`, as intended, even though the rest of the function has not been completed.