---
date: 2026-04-20
tags:
  - first-year
  - M40018
---
Unlike [[40018 - Discrete Mathematics, Logic, and Reasoning|reasoning]] about [[Haskell]], [[Kotlin]] has **side-effects**.

We specify **imperative programs** in the following way:
```Code
// PRE: P
{ some_code }
// POST: Q
```
This specification expresses that if the **state** satisfies $P$, then after the execution of `some_code`, the **state** will satisfy $Q$.
* $P$ is the **pre-condition** of `some_code`.
* $Q$ is the **post-condition** of `some_code`.

For example:
* ![[Pasted image 20260420193949.png]]
Note that there is an implicit **universal** **quantification** across the whole **specification**.