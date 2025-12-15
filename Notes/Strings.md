---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
Many languages support strings, like `"hello"`. In Haskell, a **string is a [[Lists|list]] of `Char`**. 
`"Hello" : [Char]`.
Instead of having to write `Char`, we can use a **type synonym**:
```Haskell
type String = [Char]
```
Now we can write `"Hello" : String`.
> [!Info]
> Haskell provides this type synonym by default.
