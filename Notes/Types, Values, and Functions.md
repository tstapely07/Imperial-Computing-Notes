---
date: 2025-12-13
tags:
  - "#first-year"
  - "#haskell"
  - "#M40009"
---
In Haskell, a **type** is a **classification** of **values**.
```Haskell
5 :: Integer
``` 
This says that 5 is an integer

>[!Info]
>A  values **most general** type is its **principle type**.
>This is the type that **GHCi** would return after `:type`.


A **function** is a term of type A->B, where A and B are **types**.
A function may have an **explicit type signature**. ^22b73f
```Haskell
succ :: Integer -> Integer
succ x = x = 1
```
This defines a function where both the **domain** and **codomain** is `Integer`.

We can **apply** a function to a value by **juxtaposition**.
```Haskell
succ 41

succ (37 + 4)
```
Parentheses are only needed to specify precedence.

![[Operators#^07fced]]

Functions can **ignore** their parameters.
```Haskell
two :: Integer -> Integer
two x = 2
```
This function always returns 2, e.g. `two 42 = 2`.
>[!Info]
>Since we **don't care** about the input, we can write `_` instead to show it is ignored.
>```Haskell
>two :: Integer -> Integer
>two _ = 2
>```




 

