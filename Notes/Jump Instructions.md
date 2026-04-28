---
date: 2026-04-18
tags:
  - first-year
  - M40005
---
In [[x86]], just like we have [[set instructions]], we also have **jump instructions**, of the form `j* target`, which jumps to a different part of the code, as long as the [[condition codes]] are certain values.
Here's all the **instructions**:
* ![[Pasted image 20260418122307.png|467]]
In practice, here's when we use the various **jumps**:
* ![[Pasted image 20260418123428.png|379]]
* The exact same is true for **set**.
* Note that we shouldn't use `js`/`jns` with `cmp`, since it is not safe for **overflow**.
* We shouldn't use `ja`/`jb` with `test`, since `test` always sets `CF=0`, which interferes with the **logic** behind `ja` and `jb`.

