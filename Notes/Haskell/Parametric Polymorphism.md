---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
So far, all the [[Types, Values, and Functions#^22b73f|functions]] we've seen have been monomorphic.
They operate over fixed given types, such as `Int` and `Char`.
Sometimes we want a function that operates over multiple types.

The simplest function is the identity function, it simply returns what is passed.
```Haskell
idInt :: Int -> Int
idInt  x = x

idBool :: Bool -> Bool
idBool x = x
```

^2fc2b7

These functions have different types, so they cannot be equal.
However they seem to behave similarly.
We can generalise them into a polymorphic function:
```Haskell
id :: forall a . a -> a
id x = x
```


Now we could rewrite our original identity functions like this:
```Haskell
idInt :: Int -> Int
idInt = id @Int

idBool :: Bool -> Bool
idBool = id @Bool
```


^0e8644
>[!Info]
>The `forall a`, and the `@Int` are usually optional, Haskell can normally, but not always, figure them out.
>

Here are two more polymorphic functions:
```Haskell
const :: a -> b -> a
const x y = x

ignore :: a -> b -> b
ignore x y = y
```

Now let's define a polymorphic function using a [[Where Clauses|where clause]]. ^75baa4
```Haskell
unzip :: [(a, b)] -> ([a], [b])
unzip [] = ([], [])
unzip ((x, y):xys) = (x:xs, y:ys))
	where
		xs :: [a]
		ys :: [b]
		(xs, ys) = unzip xys
```
>[!Warning]
>This function actually **doesn't type check**.

Because we didn't write `forall` in the top type, GHC added it, but everywhere.
This means it thinks the types `a` and `b` in the `where` clause are different to `a` and `b` in the main function.
>[!Success]
>To solve this we change the type of `unzip` to:
>```Haskell
>unzip :: forall a b . [(a, b)] -> ([a], [b])
>```
>This way, GHC knows that the `a` and `b` defined later  are the same thing.
>Alternatively, we could have just removed the second type signature.

>[!Tip]
>Parametrically polymorphic functions always do the same thing regardless of the type of `a`. 
>To give different types different implementations, we use [[Ad-Hoc Polymorphism|ad-hoc polymorphism]].

