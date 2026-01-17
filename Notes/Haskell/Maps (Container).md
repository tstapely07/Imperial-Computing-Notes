---
date: 2025-12-24
tags:
  - first-year
  - M40009
  - haskell
---
**Maps** are a close relative of [[Sets|sets]]. While a `Set` is just a collection of **keys**. A `Map` associates a **key** with a **value**.
Like a `Set`, it is typically implemented as a **balanced binary search [[Trees|tree]]**, so lookups are **very fast**.

Normally, we [[Imports|import]] the `Map` [[Modules|module]] like this:
```Haskell
import Data.Map (Map)
import Data.Map qualified as Map
```
This prevents **name clashes**, but allows us to write the constructor `Map`, rather than `Map.Map`.

We can define a `Map` from a [[Lists|list]] like so:
```Haskell
fromList :: Ord k => [(k, a)] -> Map k a
```
We can also create an **empty map** or a **singleton** map:
```Haskell
empty :: Map k a
singleton :: k -> a -> Map k a
```

We can convert back to a [[Lists|list]]:
```Haskell
toList :: Map k a -> [(k, a)]
```
>[!Info]
>The list will be **sorted** by the **keys**.


If we **only** want the **keys** or **values**, there are functions for these:
```Haskell
keys :: Map k a -> [k]
keys = map fst . toList

elems :: Map k a -> [a]
elems = map snd . toList
```


There is a [[Types, Values, and Functions|function]] for **adding** a key-value pair:
```Haskell
insert :: Ord k => k -> a -> Map k a -> Map k a
```
>[!Info]
>If a value **already exists** for the given key, it is **overwritten**.

There is also a function for **deleting** a key-value pair, given a **key**:
```Haskell
delete :: Ord k => k -> Map k a -> Map k a
```
>[!Info]
>If the **key** does not exist, then `delete` returns the original `Map`.

There are a few ways to query a `Map`.
`member` returns whether **key** is a member of the **map**:
```Haskell
member :: Ord k => k -> Map k a -> Bool
```
>[!Example]
>```Haskell
>member 5 (fromList [(5,'a'), (3,'b')]) == True
>```

`lookup` returns the **value** at a given **key**:
```Haskell
lookup :: Ord k => k -> Map k a -> Maybe a
```
>[!Info]
>If the value is not found, it returns `Nothing`.

The `!?` [[Operators|operator]] behaves very similarly to `lookup`:
```Haskell
(!?) :: Ord k => Map k a -> k -> Maybe a
```

If we are **sure** that a **key** exists in the `Map`, we can use `!`:
```Haskell
(!) :: Ord k => Map k a -> k -> a
```
This is equivalent to `fromJust . lookup`.
This [[Operators|operator]] crashes if the **key** is **not found**.

`findWithDefault` is like `!`, but returns a **default value** if the key is **not found**:
```Haskell
findWithDefault : Ord k => a -> k -> Map k a -> a
```
>[!Example]
>```Haskell
>findWithDefault 'c' 7 (fromList [(5,'a'), (3,'b')]) = 'c'
>```

Here are some functions that differentiate `Map` from a simple [[Lists|list]] of [[Primitive Types and Values#^f1e733|pairs]].
`insertWith` takes a **combining function** for the case where a key **already exists**:
```Haskell
insertWith :: Ord k => (a -> a -> a) -> k -> a -> Map k a -> Map k a
```

`adjust` updates a value at a **specific key** with the result from a function:
```Haskell
adjust :: Ord k => (a -> a) -> k -> Map k a -> Map k a
```
When the **key** is not in the `Map`, the original `Map` is returned.

`update` is like `adjust`, but takes an `(a -> Maybe a)` function:
```Haskell
update :: Ord k => (a -> Maybe a) -> k -> Map k a -> Map k a
```
When the function returns `Nothing`, the **key** is deleted.

>[!Info]
>These functions all have variants that include the **key** as an argument to the provided function:
>```Haskell
>insertWithKey :: 
>	Ord k => (k -> a -> a -> a) -> k -> a -> Map k a -> Map k a
>adjustWithKey :: Ord k => (k -> a -> a) -> k -> Map k a -> Map k a
>updateWithKey 
>	:: Ord k => (k -> a -> Maybe a) -> k -> Map k a -> Map k a
>``` 

**Maps** implement many of the standard [[Higher-Order Functions|higher-order functions]]:
* [[Map (Function)]]
	* As well as `mapWithKey :: (k -> a -> b) -> Map k a -> Map k b`.
* [[Filter]]
	* As well as `filterWithKey :: (k -> a -> Bool) -> Map k a -> Map k a`.
* [[Foldr]]
	* As well as `foldrWithKey :: (k -> a -> b -> b) -> b -> Map k a -> b`.
* [[Foldl]]
	* As well as `foldlWithKey :: (a -> k -> b -> a) -> a -> Map k b -> a`.

There are methods for the **standard set operations**.
`union`  combines two maps:
```Haskell
union :: Ord k => Map k a -> Map k a -> Map k a
```
>[!Info]
>If a **key** is in both maps, the value from the **left argument**  is kept.

There is also `unionWith` and `unionWithKey` where we can choose how to combine values when a key is in **both maps**:
```Haskell
unionWith :: Ord k => (a -> a -> a) -> Map k a -> Map k a -> Map k a
unionWithKey :: Ord k => (k -> a -> a -> a) -> Map k a -> Map k a -> Map k a
```

Likewise, we have `intersection`, which is `left-biased`, as well as `intersectionWith` and `intersectionWithKey`:
```Haskell
intersection :: Ord k => Map k a -> Map k b -> Map k a
intersectionWith :: Ord k => (a -> b -> c) -> Map k a -> Map k b -> Map k c
intersectionWithKey :: Ord k => (k -> a -> b -> c) -> Map k a -> Map k b -> Map k c
```

Finally, we have `difference`, which returns every **key** from the **first map** that is not in the **second map**:
```Haskell
difference :: Ord k => Map k a -> Map k b -> Map k a
```
`differenceWith`  is similar, but a **key** is **only removed** if the combining function returns **Nothing**:
```Haskell
differenceWith :: Ord k => (a -> b -> Maybe a) -> Map k a -> Map k b -> Map k a
```
>[!Info]
>If the function returns `Just`, then the value is **updated** instead.


Lets use a `Map`  to define a **useful function**.
`group` can be [[Imports|imported]] from `Data.List`, and bundles **adjacent equal** elements into sub-lists.
To be useful, we normally need to use `group . sort`, which is **annoying**.
Let's define `groupBy`,  which **is not in** base Haskell:
```Haskell
groupBy f [] = empty
groupBy f (x:xs) = insertWith (++) (f x) [x] (groupBy f xs)
```
Or even better, with a [[Foldr|fold]]:
```Haskell
groupBy f = foldr (\x -> Map.insertWith (++) (f x) [x]) Map.empty
```
>[!Example]
>```Haskell
>groupBy id [1,2,1,1,4,2] = fromList [(1,[1,1,1]),(2,[2,2]),(4,[4])]
>```

