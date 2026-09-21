---
date: 2026-04-19
tags:
  - first-year
  - M40005
  - lecturers/abbas-edalat
---
A **stack** is a last-in, first-out **data structure**.
* In [[x86]], the **stack** grows downward, towards lower [[x86 Memory Layout|memory addresses]].
The `%rsp` [[x86 Registers|register]] is the **stack pointer**, and always points to the **top** element of the **stack**.
* Note how this is the **lowest memory address**.

To add **data**, using `pushq Src`, `%rsp` is first **decremented** by $8$, to make space for $64$-**bits**, and then data is written to the new **address** indicated by `%rsp`.
To remove **data**, using `popq Dest`, the contents at the **address** stored in `%rsp` are saved to `Dest`, and then `%rsp` is **incremented** by $8$.

As a rule, the **stack** must be $16$-[[Binary|byte]] **aligned** at the moment of a **function call**.
* So `%rsp` must be a **multiple** of $16$.
* This may mean allocating $16$ **bytes**, even when we only need to store $8$.