---
date: 2025-12-21
tags:
  - first-year
  - haskell
  - M40009
---
In Haskell, there are multiple ways to achieve **conditional branching**.

Where possible, **[[Pattern Matching|pattern matching]]** should **always** be chosen.

Sometimes, we want to branch based on a **predicate**. In this case, either **[[Guards|guards]]** or **[[If Expressions|if expressions]]** must be used.
Both are **logically equivalent**, but **guards** are preferred, due to their **cleaner syntax**.