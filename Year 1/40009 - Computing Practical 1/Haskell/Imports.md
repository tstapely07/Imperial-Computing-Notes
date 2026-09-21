---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
At the top of a [[Modules|module]], we also find imports. There are three main types of import.

**Regular imports** import all or some of the contained functions into scope.
```Haskell
import Data.Char (chr)
import Data.List
```

Imports can import everything from a module **except** for some specific things:
```Haskell
import Prelude hiding (unzip)
```
>[!Info]
>`Prelude` is imported by default.
>If we want to define our own `unzip` then we have to hide it.

**Qualified imports** import a module, but we can only use things from inside it if we specify its **entire name** first.
We can rename a module locally using `as name`.
```Haskell
import Data.Char qualified
import Data.Char qualified as CharacterTools
```

These different types of imports can be used in combination with each other. 
>[!Tip]
>People will often **explicitly import types** from some modules, and then **qualified import the functions** separately to avoid name clashes.
>We could give multiple modules the **same name** with `as`, and use them as if the modules were merged together.

