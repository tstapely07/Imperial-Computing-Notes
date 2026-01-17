---
date: 2025-12-22
tags:
  - first-year
  - haskell
  - M40009
---
**Haskell Language Extensions** are optional features that allow the use of **syntax**, **compiler behaviour**, and other features that are not part of the **official** Haskell standards.

To **enable** an extension, we write a special type of comment:
```Haskell
{-# LANGUAGE NumericUnderscores #-}
```
This extension allows writing numbers like `1_000_000` instead of `1000000`.
