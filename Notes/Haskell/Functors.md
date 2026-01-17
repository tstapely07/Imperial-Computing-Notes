---
date: 2025-12-24
tags:
  - first-year
  - haskell
  - M40009
---
Recall `map`:
![[Map (Function)#^76f328]]

There are some laws that `map` must follow
```Haskell
map id = id
map f . map g = map (f . g)
```
These tell us that  `map` cannot change the **size** of a list.
It also cannot change the **ordering** of the elements.

We can define a `map` function for **other data structures**, like [[Trees|trees]].
For example for:
![[Trees#^3e68b5]]
We could write:
```Haskell
mapTree :: (a -> b) -> Tree a -> Tree b
map Tree f Tip = Tip
mapTree f (Node lt x rt) = Node (mapTree f lt) (f x) (mapTree f rt)
```

Or another example:
```Haskell
data RoseBush a = Flower a | Vine [RoseBush a]
```
For this structure, we could write:
```Haskell
mapRose :: (a -> b) -> RoseBush a -> RoseBush b
mapRose f (Flower x) = Flower (f x)
mapRose f (Vine rbs) = Vine (map (mapRose f) rbs)
```

>[!Info]
>In all these cases, the **type signature** looks like:
>```
>? :: ? t => (a -> b) -> t a -> t b
>```
>Where `t` is a **type constructor**.


The `Functor` [[Typeclasses|typeclass]] abstracts over **type constructors** of [[Kinds|kind]] `* -> *`:
```Haskell
class Functor (t :: * -> *) where
	fmap :: (a -> b) -> t a -> t b
```

Haskell doesn't verify these, but **valid instances** of `Functor` must adhere to some **laws**:
* **Identity law**:  `fmap id = id`.
* **Composition law**: `fmap (f . g) = fmap f . fmap g`.

Let's define some **instances**:
[[Lists]]:
```Haskell
instance Functor [] where
	fmap  = map
```

[[Maybe]]:
```Haskell
instance Functor Maybe where
	fmap f Nothing = Nothing
	fmap f (Just x) = Just (f x)
```

[[Either]]:
```Haskell
instance Functor (Either x) where
	fmap f (Left x) = Left x
	fmap f (Right y) = Right (f y)
```
>[!Info]
>To make `Either` a **functor** we had to provide the first parameter.
>This **partially applied** the **type constructor**, so that `Either x :: * -> *` as required.
>**Functors** always map over the **last** **type variable**.

`RoseBush`:
```Haskell
instance Functor RoseBush where
	fmap :: (a -> b) -> RoseBush a -> RoseBush b
	fmap f (Flower x) = Flower (f x)
	fmap f (Vine rbs) = Vine (fmap (fmap f) rbs)
```
>[!Info]
>Here we used `fmap` in our definition for `fmap`, which allowed us to `map` over the **list functor** too.

Even [[Types, Values, and Functions|functions]] are **functors**:
```Haskell
instance Functor (x ->) where
	fmap :: (a -> b) -> (x -> a) -> (x -> b)
	fmap = (.)
```
>[!Info] 
>[[Map (Function)|Mapping]] over a **function** is [[Function Composition (.)|function composition]].

>[!Warning]
>```Haskell
>instance Functor (-> x) where
>	fmap :: (a -> b) -> (a -> x) -> (b -> x)
>	fmap = undefined
>```
>**Functors** only work for **producers** of a type `a` but not **consumers**.

>[!Tip]
>Writing these **instances** is very mechanical.
>GHC can usually `derive Functor` and save us this work. 

`fmap` lets us "peek" underneath the "wrapper". 
For example:
![[Maybe#^e9c9f3]]
![[Maybe#^32202d]]

But what if we want to add two `Maybe Num`?
```Haskell
addMaybe :: Num a => Maybe a -> Maybe a -> Maybe a
addMaybe Nothing my = Nothing
addMaybe (Just x) my = fmap (x+) my
```

^6edbc4

>[!Info]
>We have to manually [[Pattern Matching|pattern match]] over the first  `Maybe`.

This shows that `fmap` is great for **one container**, but it fails when we need to combine more than one.
To solve this, we need a new abstraction, [[Applicatives|applicatives]].

>[!Info]
>`fmap` is also written as an [[Operators|operator]]:
>```Haskell
>(<$>) :: Functor f => (a -> b) -> f a -> f b
>```


