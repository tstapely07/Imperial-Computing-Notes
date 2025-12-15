---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
A **module** is a collection of functions, data declarations, etc which are bundled together to be used in other places.
We can specify exactly what we want to be visible with a set of names after the module name.
```Haskell
module MyModule (MyFunc) where
```
This says that `MyFunc` is the only thing that `MyModule` exposes.
If we [[Imports|imported]] `MyModule` elsewhere, we can **only** access `MyFunc`, not anything else defined in the file.
>[!Tip]
>This is useful to hide details of how something is actually implemented in a module.
>It can also prevent a user from violating any assumptions we've assumed to be true if they only use certain functions.

At the top of a module, we also find [[Imports|imports]].