---
date: 2025-12-20
tags:
  - first-year
  - haskell
  - M40009
---
**Any** implementation of equality **must** satisfy the following laws to **make sense**:

* Reflexive: `x == x`.
* Symmetric: `x == y` iff `y == x`.
* Transitive: `x == y` and `y == z` implies `x == z`.
* Extensional: `x == y` implies `f x == f y`.
