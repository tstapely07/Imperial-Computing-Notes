---
date: 2025-12-15
tags:
  - first-year
  - haskell
  - M40009
---
Haskell is a **[[Lazy vs Eager Evaluation#^bc785e|lazy]]** language. 
Sometimes we want to evaluate things **[[Lazy vs Eager Evaluation#^6088ff|eagerly]]**.
This is known as adding **strictness**.

Strictness can be added using a **bang annotation**, like here:
![[Foldl#^4cb27d]]
>[!Info]
>The **bang annotation** insists that y is evaluated
>>[!Warning]
>>A **bang annotation** must be written can only be written on the **left** of an equals.

We can also force evaluation using `seq`:
```Haskell
seq :: a -> b -> b
```
>[!Info]
>`seq x y` returns `y`, but **only after** `x` has been **evaluated fully**.

To evaluate **and** return  `x` we can just write `seq x x`. 
Haskell will remember `x` and not compute it twice.

We can make parts of a [[User-Defined Datatypes|datatype]] **strict**:
```Haskell
data StrictCoords = Coords !Int !Int
```
>[!Info]
>Here the two coordinates will be evaluated **strictly**.

