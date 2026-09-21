---
date: 2025-12-25
tags:
  - first-year
  - M40009
  - haskell
---
**Sequencing computations** is usually achieved with `;`:
```Haskell
p ; q ; r
```
This operation must be associative:
```Haskell
(p ; q) ; r = p ; (q ; r)
```
Understanding **associativity** is at the heart of  **monoids**.

We may ask when [[Foldr|foldr]] and [[Foldl|Foldl]] return the same values.   
>[!Example]
>```Haskell
>foldl (+) 0 = foldr (+) 0
>```
>```Haskell
>foldl (*) 1 = foldr (*) 1
>```

This holds more generally for:
```Haskell
mappend :: a -> a -> a
mempty :: a
```
>[!Info]
>`mappend` is **associative** - `(x mappend y) mappend z = x mappend (y mappend z)`.
>`mempty` is **unital** - `x mappend mempty = x = mempty mappend x`

When those two **laws** hold, the following holds:
```Haskell
foldl (mappend) mempty = foldr (mappend) mempty
```

When `mappend` and `mempty` obey these laws, we call it a monoid, written:
```Haskell
<a, mappend, mempty>
```

There are many more examples of **monoids**:
* `<Naturals, +, 0>`
* `<Naturals, *, 1>`
* `Booleans, ||, False`
* `Booleans, &&, True`

The **Boom hierarchy** classifies **monoids** based on their properties.
Two more properties it includes are:
* **Commutativity** - `x mappend y = y mappend x`
* **Idempotence** - `x mappend x = x`

|                                 | unital       | associative  | commutative  | idempotent   |
| ------------------------------- | ------------ | ------------ | ------------ | ------------ |
| `<Tree a, Fork, Tip>`           | $\checkmark$ | $\times$     | $\times$     | $\times$     |
| `<[a], ++, []>`                 | $\checkmark$ | $\checkmark$ | $\times$     | $\times$     |
| `<Bag a, Bag Union, Empty Bag>` | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$     |
| `<Set a, Set Union, Empty Set`  | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ |


