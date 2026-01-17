---
date: 2025-12-22
tags:
  - first-year
  - haskell
  - M40009
---
We've seen [[Trees|trees]], and their `grow` function to turn a [[Lists|list]] into a tree:
![[Trees#^42cf5e]]
However, when the list is **sorted**, it will produce a **biased tree** that only grows in **one direction**.
This degrades **binary tree search** to `O(n)`.
The solution is to implement trees that **balance themselves**.
This is too complex to do ourselves, but Haskell defines a `Set` to serve this purpose.
Like in [[400018 - Discrete Mathematics, Logic|discrete maths]], sets contain **no duplicate elements**.

Normally, we [[Imports|import]] the `Set` [[Modules|module]] like this:
```Haskell
import Data.Set (Set)
import Data.Set qualified as Set
```
This prevents **name clashes**, but allows us to write the constructor `Set`, rather than `Set.Set`

We create a **set** from a [[Lists|list]] like so:
```Haskell
fromList :: Ord a => [a] -> Set a
```
>[!Example]
>```Haskell
>xs = set.fromList [1,2,3]
>```

>[!Info]
>Most [[Types, Values, and Functions|functions]] and operations on **sets** have an `Ord` [[Typeclasses#^06ed67|constraint]], which the **set** requires to be **self-balancing**.
>

We can also create an **empty set** and a **singleton set**:
```Haskell
empty :: Set a
singleton :: a -> Set a
```

We can convert back to a list:
```Haskell
toList :: Set a -> [a]
```

We can add elements **very efficiently**:
```Haskell
insert :: Ord a => a -> Set a -> Set a
```
Likewise, there is a method for **removing** an element.
```Haskell
delete :: Ord a => a -> Set a -> Set a
```
>[!Info]
>If the element is **not in** the set, the set is returned **unchanged**.

There is also an **efficient** method for querying membership:
```Haskell
member :: Ord a => a -> Set a -> Bool
```

There are methods for the standard set operations:
```Haskell
union :: Ord a => Set a -> Set a -> Set a
intersection :: Ord a => Set a -> Set a -> Set a
difference :: Ord a => Set a -> Set a -> Set a
disjoint :: Ord a => Set a -> Set a -> Bool
```

Here are some more useful methods:
```Haskell
null :: Set a -> Bool
size :: Set a -> Int

isSubsetOf :: Ord a => Set a -> Set a -> Bool
isProperSubsetOf :: Ord a => Set a -> Set a -> Bool
```

**Sets** also implement some of the standard [[Higher-Order Functions|higher-order functions]], including:
* [[Foldr]]
* [[Foldl]]
* [[Filter]]
* [[Partition]]
* [[Map (Function)]]
>[!Warning]
>`Set.map` can be dangerous.
>Because **sets** contain **no duplicates**, `Set.map` can change the size of the set.

>[!Tip]
>For **debugging**, we can use `showTree` and `showTreeWith`.
>`putStrLn`  should be used  to output the string they return as intended.
>>[!Example]
>>```Haskell
>>putStr $ showTreeWith True True $ fromList [1,2,3,4,5] =
4
|
+--2
|  |
|  +--1
|  |
|  +--3
|
+--5 
>>```
>>

Here's one useful function we can define with **sets**.
Firstly, we have `nub`:
```Haskell
nub :: Eq a => [a] -> [a]
```
`nub` removes duplicates from a [[Lists|list]].
It does it in `O(n^2)` [[Time Complexity|time complexity]].

When we have **ordered data** we can do better.
`nubOrd` can be [[Imports|imported]] from `Data.Containers.ListUtils`:
```Haskell
nubOrd :: forall a . Ord a => [a] -> [a]
nubOrd xs = nub' Set.empty xs
	where
		nub' :: Set a -> [a] -> [a]
		nub' _ [] = []
		nub' seen (x:xs)
			| Set.member x seen = nub' seen xs
			| otherwise = x : nub' (Set.insert x seen) xs
```
This is **more efficient**.
We could also have simply done:
```Haskell
nubNotOrd :: Ord a => [a] -> [a]
nubNotOrd = Set.toList . Set.fromList
```
But this **doesn't preserve ordering**.