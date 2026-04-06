---
date: 2025-12-21
tags:
  - first-year
  - "#haskell"
  - M40009
---
Trees can have many shapes. 

`Tree a`  is a **binary tree** that stores data at **every `Node`**:
```Haskell
data Tree a where
	Tip :: Tree a 
	Node :: (Tree a) -> a -> (Tree a) -> Tree a
```

^3e68b5

>[!Example]
>```
>Tip :: Tree a
>.
>```
>```
>Node Tip False Tip :: Tree Bool
>      False
> 	 /  \
>     .    .
>```
>```
>Node (Node  Tip 7 Tip) 5 Tip :: Tree Int
>           5
>         /  \
>         7   .
>        /  \
>      .     .
>```

`Bush a` is a **binary tree** that stores data at **every `Leaf`**
```Haskell
data Bush a where
	Leaf a -> Bush a 
	Fork :: Bush a -> Bush a -> Bush a
```
>[!Example]
>```
>Leaf 1 :: Bush Int
>1
>```
>```
>Fork (Leaf True) (Leaf False) :: Bush Bool
>
>    /  \
>True False
>```
>```
>Fork (Leaf 'a') (Fork (Leaf 'b') (Leaf 'c')) :: Bush Char
>
>    /  \
> 'a'   / \
>     'b' 'c'  
>```

`Rose a` stores data at every **`Bloom`  point**.
```Haskell
data Rose a where
	Bloom :: a -> [Rose a] -> Rose a
```

^3c4865

>[!Example]
>```
>Bloom 1 [] ::  Rose Int
>1
>```
>```
>Bloom  'a' [Bloom 'b' [], Bloom 'c' [], Bloom 'd', []] :: Rose Char
>        'a'
>      /  |  \
>    'b' 'c' 'd'
>```
>```
>Bloom 5 [Bloom 7 [], Bloom 3 [Bloom 2[]]] :: Rose Int
>      5
>     / \
>    7   3
>        |
>        2
>```

We use these [[User-Defined Datatypes|datatypes]] by  [[Pattern Matching|pattern matching]].
`size` finds the number of elements in the tree:
```Haskell
size :: Tree a -> Int
size Tip = 0
size (Node lt x rt) = size lt + 1 + size rt
```

`height` finds the length of the longest path from the root:
```Haskell
height :: Tree a -> Int
height Tip = 0
height (Node lt x rt) = 1 + max (height lt) (height rt)
```

We can check if an element is in an **ordered** tree:
```Haskell
elemTree :: Ord a  => a -> Tree a -> Bool
elemTree x Tip = False
elemTree x (Node lt y rt)
	| x < y = elemTree x lt
	| x == y = True
	| x > y = elemTree x rt
```

We can also flatten a **tree** into a **[[Lists|list]]**:
```Haskell
flatten :: Tree a -> [a]
flatten Tip = []
flatten (Node lt x rt = flatten lt ++ [x] ++ flatten rt
```

If we assume the tree is **sorted**, we can **insert values** into it:
```Haskell
insertTree :: Ord a => a -> Tree a -> Tree a
insertTree x Tip = Node Tip x Tip
insertTree x (Node lt y rt)
	| x <= y = Node (insertTree x lt) y rt
	| otherwise = Node lt y (insertTree x rt)
```
Now we have a way to build a **sorted tree** from **any list**:
```Haskell
grow xs = foldr insertTree Tip xs
```

^42cf5e

Using `grow` and `flatten` we can write a **sorting algorithm**:
```Haskell
tSort :: Ord a => [a] -> [a]
tSort = flatten . grow
```
>[!Info]
>This is an implementation of **tree sort**.


>[!Info]
[[Syntax Trees|Syntax trees]] are another type of tree.
