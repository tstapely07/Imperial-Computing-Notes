---
date: 2025-12-20
tags:
  - first-year
  - M40009
  - haskell
---
A **type class** allows us to implement equality for different types we choose.
Here the `Eq` typeclass is acting as an additional constraint.
```Haskell
x :: a 
y :: a
Eq a
--------------
x == y :: Bool
```

The `Eq` typeclass is defined by: ^96a000
```Haskell
class Eq a where
	(==) :: a -> a -> Bool
```

^70dbd6

This introduces: ^68e598
```Haskell
(==) :: Eq a => a -> a -> Bool
```

^89c7bb

![[Laws of Equality]]


Here is a [[User-Defined Datatypes|user-defined datatype]] for natural numbers:
```Haskell
data Nat where
	Z :: Nat
	S :: Nat -> Nat
```
We can make our own **instance** of `Eq` for a **user-defined datatype**:
```Haskell
instance Eq Nat where
	Z == Z = True
	S x == S y = x == y
	_ == _ = False
```
>[!Info]
>Haskell can sometimes derive **typeclasses** by itself.
>We write `Deriving` for this:
>```Haskell
>data Nat where
>	Z :: Nat
>	S :: Nat -> Nat
>	deriving Eq
>```

If we wanted to do do arithmetic over `Nat`, we must implement an **instance** of the `Num` **typeclass**:
```Haskell
class Num a where
	(+) :: a -> a -> a
	(-) :: a -> a -> a
	(*) :: a -> a -> a
	negate :: a -> a
	fromInteger :: Integer -> a 
	-- ...
```
Haskell can't derive `Num Nat`, so we do it manually:
```Haskell
instance Num Nat where
	Z + y = y
	S x + y = x + S y
```

>[!Example]
>For another example of implementing `Num` see [[Streams|streams]].

The `Eq` class provides **equality**.
We also want [[Operators|operators]] for **ordering**, such as `<`, `>`, `<=`, and `>=`.
To make `Ord` compatible with `Eq` we must use `Eq` in the definition of `Ord`: ^06ed67
```Haskell
class Eq a => Ord a where
	(<=) :: a -> a -> Bool
	-- ...
```
We can define an **instance** of `Ord` that implements the **lexicographic ordering** for a list: ^5b53cc
```Haskell
instance Ord a => Ord [a] where
	[] <= ys = True
	(x:xs) <= [] = False
	(x:xs) <= (y:ys) = x < y || (x == y && xs <= ys)
```
^b61a45

Sometimes we try and use values in the **terminal**, and get an **error**.
This is because GHC needs a `Show` **instance** to print things:
```Haskell
class Show a where
	show :: a -> String
```

There is also `Read`, which turns a `string` and tries to **parse** it into a [[Types, Values, and Functions|value]]:
```Haskell
class Read a where
	read :: String -> a
```

There is a law that states:
```Haskell
read . show = id
```
This is hard to stick to, so we should **always** use `Deriving (Show, Read)`, and leave it to GHC.

If we want a **typeclass** for **pretty printing**, instead of changing `Show`, we should just make one:
```Haskell
class Pretty a where
	pretty :: a -> String
```

>[!Tip]
>**Typeclasses** must have unique instances for a given type. 
>If we want to define **multiple instances**, a solution is using [[Newtypes|newtypes]].