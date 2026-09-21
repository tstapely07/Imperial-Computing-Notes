---
date: 2026-04-18
tags:
  - first-year
  - M40005
---
In [[x86]], `lea` stands for **load effective address**.
* The **syntax** is `lea{suffix} src, dest`.
* Here, `src` must be some [[Memory Addressing Modes|memory address]].
* `lea` computes the **address**, but doesn't fetch from memory, and instead stores the **address** in the [[x86 Registers|register]] `dest`, acting like only the first half of a [[The mov Instruction|mov instruction]].
This means we can use it to compute expressions of the form `x+k*y`, using highly optimised hardware.
* For example, `leaq (%rdi, %rdi, 2), %rax` is equivalent to `%rax = %rdi+%rdi*2 = %rdi*3`.
