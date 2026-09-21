---
date: 2025-12-24
tags:
  - first-year
  - haskell
  - M40009
---
Much like we categorise [[Types, Values, and Functions|values]] into [[Types, Values, and Functions|types]],  we can also classify **types** into **kinds**.
```Haskell
7 :: Int :: *
True :: Bool :: *
Just 'a' :: Maybe Char :: *
```
These all have **kind** `*`.
They represent **concrete values**.

```Haskell
Tree :: * -> *
[] :: * -> *
Maybe :: * -> *
```
These have **kind** `* -> *`.
They are **type constructors** that need another **type** to become a **concrete type**.

```Haskell
Either :: * -> * -> *
```
`Either` is a **type constructor** that requires **two types**.

```Haskell
(->) :: * -> * -> *
(a ->) :: * -> *
(-> a) :: * -> * 
```
This is valid, in the same way that:
```Haskell
(+) :: Int -> Int -> Int
(1 +) :: Int -> Int
(+ 1) :: Int -> Int
```
>[!Info]
>We can **partially apply** types.

