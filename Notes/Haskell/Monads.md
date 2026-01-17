---
date: 2025-12-24
tags:
  - first-year
  - haskell
  - M40009
---
Like [[Applicatives|applicatives]] can be implemented by **either** `liftA2` or `(<*>)`, **monads** can be defined by either `join` or `(>>=)` - pronounced "bind".

`join` is able to flatten structures:
```Haskell
joinMaybe :: Maybe (Maybe a) -> Maybe a
joinMaybe Nothing = Nothing
joinMaybe (Just mx) = mx
```
>[!Info]
>Using `joinMaybe`, we can fix our previous problems:
>![[Applicatives#^3d7a89]]
>```Haskell
>joinMaybe (liftA2 safeDiv (safeDiv 3 1) (safeDiv 5 2)) = Just 1
joinMaybe (liftA2 safeDiv (safeDiv 10 2) (pure 0)) = Nothing
>```

Similarly, on [[Lists|lists]]:
```Haskell
joinList : [[a]] -> [a]
joinList [] = []
joinList (xs:xss) = xs ++ joinList xss
```
In other words, `joinList = concat`.

The `join` function generalises [[Concat|concat]] for all **monadic** structures.

We also have `(>>=)`:
```Haskell
(>>=) :: Monad m => m a -> (a -> m b) -> m b
```
>[!Info]
>`(>>=)` consumes one thing to produce another.
>If we have an `m a` we can extract the `a` from inside and use it to make an `m b`.

One example is `bindMaybe`:
```Haskell
bindMaybe :: Maybe a -> (a -> Maybe b) -> Maybe b
bindMaybe Nothing f = Nothing
bindMaybe (Just x) f = f x
```
>[!Info]
>In the `Nothing` case, there was no `a` to apply `f` to so we had to return `Nothing`.
>In the `Just` case, we had an `a`, so we were able to call  `f x` to get a `Maybe b` back.
>In other words, `f` was **only applied if** `Maybe a` was **successful**.

We could define `bindList`:
```Haskell
bindList :: [a] -> (a -> [b]) -> [b]
bindList [] f = []
bindList (x:xs) = f x ++ bindList xs f
```
>[!Info]
>This is just like the definition of [[ConcatMap|concatMap]], just with the arguments flipped.

Like `join` **generalised** `concat`, `bind` **generalises** `concatMap`.
Like we can define `concatMap` in terms of `map` and `concat` as `concatMap = concat . map`,  we can write:
```Haskell
(>>=) :: Monad m => m a -> (a -> m b) -> m b
mx >>= f = join (fmap f mx)
```

And like `concat = concatMap id`, we can write:
```Haskell
join :: Monad m => m (m a) -> m a
join mmx = mmx >>= id
```

Finally, like we have `map f = concatMap (x -> [f x])`:
```Haskell
liftM :: Monad m => (a -> b) -> m a -> m b
liftM f mx = mx >>= (\x -> pure (f x))
```

Now we can define our [[Typeclasses|typeclass]]:
```Haskell
class Applicative m => Monad m where
	return :: a -> m a 	
	(>>=) :: m a -> (a -> m b) -> m b
```
>[!Info]
>`join` is not part of the **typeclass**, we can define it like we did above.
>`return` exists for **historical reason**, since `Monad` **predates** its current superclass `Applicative`.
>We can now write `return = pure`.

Here are some `Monad` **instances**.
These follow from what we previously wrote, just with their **correct names**:
[[Maybe]]:
```Haskell
instance Monad Maybe where
	return = pure	
	(>>=) :: Maybe a -> (a -> Maybe b) -> Maybe b
	Nothing >>= f = Nothing
	Just x >>= f = f x
```

[[Lists]]:
```Haskell
instance Monad [] where
	return = pure
	(>>=) :: [a] -> (a -> [b]) -> [b]
	xs >>= f = concatMap f xs
```

>[!Info]
>**Instances** of `Monad` **must obey** the [[Monad Laws|monad laws]].

We saw how `join` can **fix** our `safeDiv` **problems**.
How about with `(>>=)`:
```Haskell
join (liftA2 safeDiv (safeDiv 10 2) (safeDiv 6 3))
= 
safeDiv 10 2 >>= (\m -> 
	safeDiv 6 3 >>= (\n -> 
		safeDiv m n 
	)
)
```
This `(>>=)` version looks **very different** and quite **hard to read**.

With [[Lists|lists]] there was a clean way to write `concatMap` and `map` - a [[List Comprehensions|list comprehension]].
```Haskell
[x + y | x <- xs, y <- ys] = concatMap (\x -> map (x+) ys) xs
```
>[!Info]
>Or alternatively with [[Applicatives|applicatives]]:
>```Haskell
>[x + y | x <- xs, y <- ys] = liftA2 (+) xs ys
>```

Similarly, for **monads** we have **do-notation**:
```Haskell
do 
	m <- safeDiv 10 2
	n <- safeDiv 6 3
	safeDiv m n
```
Every `<-` represents a `>>=`, in the same way that every `<-` in a **list comprehension** represents a `concatMap`.
Unlike **list comprehensions**, **do-notation** does **not** have to end in with a `map`.
>[!Tip]
>Instead of separating lines with a **new line**, we can also use a **semicolon - `;`**.
>We can also **optionally** wrap the **body** of **do-notation** with `{}`.

>[!Info]
>We can translate between `(>>=)` and **do-notation**:
>```Haskell
>do 
>	x <- p
>	f x
>```
>Is equivalent to:
>```Haskell
>p >>= (\x -> f x)
>```
>Which is just:
>```Haskell
>p >>= f
>```

We've seen how `liftA2` can also be written in terms of **do-notation**.
This means that defining an **instance** of `Monad` will give us `Applicative` "for free".
`liftA2` and `(<*>)` are called `liftM2` and and `ap`, and are defined like:
```Haskell
liftM2 :: Monad m => (a -> b -> c) -> m a -> m b -> m c
liftM2 f mx my = do
	x <- mx
	y <- my
	pure (f x y)

ap :: Monad m => m (a -> b) -> m a -> m b
ap mf mx = do
	f <- mf
	x <- mx
	pure (f x)
``` 
>[!Tip]
>In general, in a **do-block**, if **none** of the **results** are used until the **last line**, **and** the last line is a `pure` or `fmap`, then that **do-block** could have been written [[Applicatives|applicatively]].
>In other words, **applicatives** can be used when things we perform in **sequence** do **not** depend on each other's **results**.
>

>[!Info]
>Another useful `Monad` is [[IO Monad|IO]].

`Monad` has lots of other useful tools:
`mapM` **applies** a function that returns a **monadic value** to every element in a [[Lists|list]], and returns the list of results **inside** the monad:
```Haskell
mapM :: Monad m => (a -> m b) -> [a] -> m [b]
```
There is also `mapM_` which behaves the same, but **discards the result**:
```Haskell
mapM_ :: Monad m => (a -> m b) -> [a] -> m ()
```
`mapM_` is useful when we **only care** about the **side effects**, like printing an output.
>[!Example]
>```Haskell
>filenames = ["tests.txt", "config.json"]
>main :: IO ()
>main = do
>	contents <- mapM readFile filenames
>	mapM_ putStrLn filenames
>```

`forM` and `forM_` are just like `mapM` and `mapM_` but with the arguments flipped:
```Haskell
forM :: Monad m => [a] -> (a -> m b) -> m [b]
forM_ :: Monad m => [a] -> (a -> m b) -> m ()
```
These are used when we want to write the loop body as a **large block** of code **after** the list.
`forM_` is the most common way to write a **foreach loop** in Haskell.
>[!Example]
>```Haskell
>main = forM_ [1..3] (\n -> do
>	putStrLn ("Processing item number " ++ show n)
>)
>```

`when` executes an action if a boolean condition is `True`:
```Haskell
when :: Applicative f => Bool -> f () -> f ()
```
>[!Info]
>`when` is used to avoid the need for an `else return ()`.

`guard` is used with Monads that support **failure**, like [[Maybe]].
If the condition is `False`, it stops the whole computation, e.g. by returning `Nothing`:
```Haskell
guard :: Bool -> f ()
```
>[!Example]
>```Haskell
>validateAge :: Int -> Maybe Int
>validateAge age = do
>	guard (age >= 0 && age <= 120)
>	return age
>```

`void` runs a **monadic action** and then ignores the result, replacing it with `()`:
```Haskell
Functor f => f a -> f ()
```
>[!Example]
>If we want to **wait** until the user inputs **anything**:
>```Haskell
>waitEnter :: IO ()
>waitEnter = vooid getLine
>```

We can use `let` to bind **pure values** inside **do-notation**:
```Haskell
printSquare :: IO ()
printSquare = do
	input <- getLine
	let val = read input
	let squared = vall * val
	print sqaured
```
This is unlike the `<-` which is used for **monadic values**.

The `(>=>)` [[Operators|operator]] is like the `(.)` operator for [[Function Composition (.)|function composition]], but for **monadic functions**:
```Haskell
(>=>) :: Monad m => (a -> m b) -> (b -> m c) -> (a -> m c)
f >=> g = \x -> do
	y <- f x
	g y
```
>[!Warning]
>Unlike `(.)`, which flows **right-to-left**, `(>=>)` flows **left-to-right**.

>[!Example]
>```Haskell
>readInt :: String -> Maybe Int
>readInt s
>	| all isDigit s = Just (read s)
>	| otherwise = Nothing
>
>isPositive :: Int -> Maybe Int
>isPositive n
>	| n > 0 = Just n
>	| otherwise = Nothing
>
>combined :: String -> Maybe Int
>combinedCheck = readInt >=> isPositive
>```

There is also `(<=<)` which flows **right-to-left** just like `(.)`:
```Haskell
(<=<) :: Monad m => (b -> m c) -> (a -> m b) -> (a -> m c)
f <=< g = \x -> do
	y <- g x
	f y
```