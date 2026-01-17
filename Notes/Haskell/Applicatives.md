---
date: 2025-12-24
tags:
  - first-year
  - haskell
  - M40009
---
Our `addMaybe` [[Types, Values, and Functions|function]] worked, but only for `Maybe`, not for `[]` or `Either x` or other containers:
![[Functors#^6edbc4]]
We could implement something that looks similar on [[Lists|lists]]:
```Haskell
addList :: Num a => [a] -> [a] -> [a]
addList [] ys = []
addList (x:xs) ys = fmap (x+) ys ++ addList xs ys
```
Or more **idiomatically** with a [[List Comprehensions|list comprehension]]:
```Haskell
addList xs ys = [x + y | x <- xs, y <- ys]
```
>[!Info]
>This implements [[Cartesian Product|cartesian product]].
>>[!Example]
>>```Haskell
>>addList [1,2,3] [100,200,300] = [101,201,301,102,202,302,103,203,303]
>>```

These functions **combine** two data structures to produce a **bigger structure**.
`addList` produces a list of size `m * n`.
Since `Maybe` holds `0` or `1` `a`, we can get  `0 * 0`, `0 * 1`, `1 * 0`, or `1 * 1` `a` out - `0` or `1`.

What if instead of **adding** these structures, we wanted to **multiply them**:
```Haskell
mulMaybe :: Maybe Int -> Maybe Int -> Maybe Int
mulMaybe Nothing _ = Nothing
mulMaybe (Just x) my = fmap (x*) my
```
```Haskell
mulList :: [Int] -> [Int] -> [Int]
mulList = [x * y | x <- xs, y <- ys]
```

These are basically the same as before, so let's create [[Higher-Order Functions|higher-order functions]] to capture the pattern:
```Haskell
productWithMaybe :: (a -> b -> c) -> Maybe a -> Maybe b -> Maybe c
productWithMaybe f Nothing _ = Nothing
productWithMaybe  f (Just x) my = fmap (f x) my
```
```Haskell
productWithList :: (a -> b -> c) -> [a] -> [b] -> [c]
productWithList f xs ys = [f x y | x <- xs, y <- ys]
```
Now we can simplify our definitions:
```Haskell
addList = productWithList (+)
mulList = productWithList (*)
addMaybe = productWithMaybe (+)
mulMaybe = productWithMaybe (*)
```

We can **generalise** `productWith` into a function called `liftA2`.
It belongs to a stricter [[Typeclasses|typeclass]] that is a **subclass** of [[Functors|functor]] - **applicative**.
```Haskell
liftA2 :: Applicative t => (a -> b -> c) -> t a -> t b > t c
```
>[!Info]
>`liftA2`  lifts a function on `a`, `b`, and `c` to work on values inside a structure, `t a`, `t b`, and `t c`.

In the same way we have `liftA`:
```Haskell
liftA :: Applicative t => (a -> b) -> t a -> t b
```
>[!Info]
>`liftA` makes functions that work on `a` and `b` work on `t a` and `t b`.
>It turns out that `liftA` is just another name for [[Functors|fmap]]. 

`liftA` can be defined from `liftA2`.
We know `liftA2` **multiplies lengths** - `m * n`.
We also know `liftA`, or `fmap`, keeps **length constant** - `m`.
This gives an equation `m * n = m`, so `n` must be 1.
So we need a way to create a structure of **size 1**. 
This is `pure`, another method of `Applicative:
```Haskell
pure :: Applicative t => a -> t a
```
>[!Info]
>`pure x` is the **minimal** structure containing `x` for some applicative structure `t`.
>This gives us a generic way to refer to structures of **size 1**.

Now we can actually implement `liftA` in terms of `liftA2` and `pure`:
```Haskell
liftA f mx = liftA2 (\f x -> f x) (pure f) mx
```
>[!Info]
>This definition is correct but very hard to read.
>It says to `fmap f` over an `mx`, we first wrap `f` into the minimal structure using `pure`.
>Then we use `liftA2` to combine the function in `pure f` with the values in `mx`.

The function we used was `(\f x -> f x)`. 
It looks weird, but it is actually just [[Function Application ($)|function application]]:
![[Function Application ($)#^2c28d9]]
Now we can write:
```Haskell
liftA f mx = liftA2 ($) (pure f) mx
```

Together, `liftA` and `pure` form `Applicative`.
We also have another **equally powerful** [[Operators|operator]], which we pronounce "app":
```Haskell
(<*>) :: Applicative t => t (a -> b) -> t a ->  t b
(<*>) = liftA2 ($)
```

Here's a final way to write `liftA`:
```Haskell
liftA f mx = pure f <*> mx
```

In the same way that `(<*>)` can be implemented in terms of `liftA2`, we can also implement `liftA2` in terms of `(<*>)` and `pure`:
```Haskell
liftA2 f mx my = pure f <*> mx <*> my
```
>[!Info]
>Each `(<*>)` partially applies `f`.

Following this pattern further, we could define `liftA3` and `liftA4`:
```Haskell
liftA3 :: Applicative t => (a -> b -> c -> d) -> t a -> t b -> t c -> t d
liftA3 f mx my mz = pure f <*> mx <*> my <*> mz
```
```Haskell
liftA4 :: Applicative t => (a -> b -> c -> d -> e) -> t a -> t b -> t c -> t d -> t e
liftA4 f mu mx my mz = pure f <*> mu <*> mx <*> my <*> mz
```

We can notice that the leading `pure f <*> mx` is **exactly** how we defined `liftA`.
So we can actually write our **lifts** **more idiomatically**:
```Haskell
liftA3 :: Applicative t => (a -> b -> c -> d) -> t a -> t b -> t c -> t d
liftA3 f mx my mz = f <$> mx <*> my <*> mz
```

Finally, we can look at the `Applicative` [[Typeclasses|typeclass]]:
```Haskell
class Functor t => Applicative t where
	pure :: a -> t a
	
	(<*>) :: t (a -> b) -> t a -> t b
	(<*>) = liftA2 ($)
	
	liftA2 :: (a -> b -> c) -> t a -> t b -> tc
	liftA2 f mx my = f <$> mx <*> my
```
>[!Info]
>Firstly, note that we can use `<$>` because of the [[Functors|functor]] constraint.
>Also, since `liftA2` and  `(<*>)` are defined in terms of each other, when we write an **instance** of `Applicative`, we only have to write one, to get the other for free.

Here are some **instances**:
[[Maybe]]:
```Haskell
instance Applicative Maybe where
	pure :: a -> Maybe a
	pure = Just
	
	(<*>) :: Maybe (a -> b) -> Maybe a -> Maybe b
	Nothing <*> mx = Nothing
	Just f <*> mx = fmap f mx
```

[[Either]]:
```Haskell
instance Applicative (Either e) where
	pure :: a -> Either e a
	pure = Right
	
	liftA2 :: (a -> b -> c) -> Either e a -> Either e b -> Either e c
	liftA2 f (Left x) _ = Left x
	liftA2 f (Right x) (Left y) = Left y
	liftA2 f (Right x) (Right y) = Right (f x y)
```
>[!Info]
>Here we decided to favour the first `Left` and **ignore**  the second argument, even if it was a `Left`.
>The idea here is that we can only combine two **eithers** when they are **both** `Right`.
>This again corresponds to an **error condition**, where a **left** is an **error**.

[[Lists]]:
```Haskell
instance Applicative [] where
	pure :: a -> [a]
	pure x = [x]
	
	(*) :: [a -> b] -> [a] -> [b]
	fs <*> xs = [f x | f <- fs, x <- xs]
```
>[!Info]
>While `Maybe` and `Either` handle **possibly failing** computations, the applicative for **lists** is concerned with **non-deterministic computations**.
>We can get a **list**  of **every possible outcome**.

>[!Warning]
>Although `(,)` is a [[Functors|functor]], it isn't an **applicative**. 
>Defining `pure` is **impossible**:
>```Haskell
>pure :: a -> (x,a)
>pure = undefined
>```
>We can't get an `x` from **nowhere**.

>[!Warning]
>We cannot write `deriving (Applicative)`. 
>This is because we are defining **behaviour** not just a **structure**.

There are some **laws** that **applicatives** must follow:
Identity:
```Haskell
pure id <*> x = x
```
>[!Info]
>Wrapping `id` in a structure shouldn't change its effect.

Composition:
```Haskell
pure (.) <*> u <*> v <*> w = u <*> (v <*> w)
```
>[!Info]
>**LHS** composes the function `u` with `v` first, then applies that **combined function** to `w`.
>**RHS** applies `v` to `w` then applies `u` to the result
>`RHS = LHS` shows that **associativity** still applies.


Homomorphism:
```Haskell
pure f <*> pure x = pure (f x)`
``` 
>[!Info]
>"App-ing" to `pure` things doesn't change the size.
>`pure` doesn't "do anything".

Interchange:
```Haskell
u <*> pure x = pure ($ x) <*> u
```
>[!Info]
>On the **LHS** we have a **structure of functions** that we apply to a **single** `pure` value.
>On the **RHS** we have a **structure of functions** and we **apply the operation** "apply to x" to those functions.
>Both cases must be the equivalent.
>

Here's **one example** of using **applicatives**.
With a basic `expr` [[User-Defined Datatypes|datatype]]:
```Haskell
data Expr = Add Expr Expr | Var String
```
Let's write a **part** of the `eval` function that handles **adding** two expressions. 
Either expression may have previously **failed**.
Instead of writing:
```Haskell
evalMaybe :: Expr -> [(String, Int)] -> Maybe Int
evalMaybe (Add e1 e2) ctx = case evalMaybe e1 ctx of
	Nothing -> nothing
	Just m -> case evalMaybe e2 ctx of
		Nothing -> Nothing
		Just n -> Just (m + n)
```
This is hard to read.
Using **applicatives**, we can write:
```Haskell
evalMaybe (Add e1 e2) ctx = (+) <$> evalMaybe e1 ctx <*> evalMaybe e2 ctx
```
>[!Info]
>This says:
>"Evaluate **both** `e1` and  `e2` with the context. 
>Then combine the structures - if they are both `Just`, combine them with `(+)`, otherwise the whole evaluation fails."

**Applicatives** do have **limitations**.
```Haskell
liftA2 (+) (safeDiv 3 1) (safeDiv 5 2) = Just 5
```
This is fine, but:
```Haskell
liftA2 (safeDiv) (safeDiv 3 1) (safeDiv 5 2) = Just (Just 1)
liftA2 safeDiv (safeDiv 10 2) (pure 0) = Just Nothing
```

^3d7a89

In fact:
```Haskell
liftA2 safeDiv :: Maybe Int -> Maybe -> Int -> Maybe (Maybe Int)
```
>[!Info]
>**Applicatives** are great for applying functions that **don't** return structures to structures.
>But when a function itself **returns a structure**, `Applicative` wraps it again, creating **nested layers**.
>To solve this, we need [[Monads|monads]].

