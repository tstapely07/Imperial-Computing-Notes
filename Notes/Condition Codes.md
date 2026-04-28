---
date: 2026-04-18
tags:
  - first-year
  - M40005
---
In [[x86]], the **processor**, as well as the standard [[x86 Registers|registers]], has a set of **single-bit** [[registers]] known as the **condition codes** or **flags**:
* **CF** - **carry** **flag** - set if there was a **carry** **out**.
* **ZF** - **zero** **flag** - set if the result was exactly $0$.
* **SF** - **sign** **flag** - set if the result was **negative**.
* **OF** - **overflow** **flag** - set if there was a **two**'s **complement** **overflow**.
Every [[x86 Arithmetic Operations|arithmetic operation]], apart from [[The lea Instruction|lea]], **implicitly** sets these **flags** based on its result.

There are also two **instructions** that **explicitly** set these **flags**:
* `cmp{suf} b, a` computes `a - b` to set the **flags**, but discards the **result**.
* `test{suf} b, a` computes `a & b` to set the **flags**, but discards the **result**.
