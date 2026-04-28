---
date: 2026-04-15
tags:
  - first-year
  - M40005
---
The **instruction set architecture** (**ISA**) offers an **abstraction** of the **hardware resources** to the **software**.
* Essentially, it is all the parts of the **processor** that a programmer needs to be able to understand to write **assembly**, such as [[RISC-V Architecture|RISC-V]] or [[x86]].

In general, there are two approaches.
**Complex Instruction Set Computers** (**CISC**) use a powerful **instruction** **set** with a variable format.
* This results in dense code and a simpler **compiler**.
* However, **instructions** take more time to **execute**,  due to their **complexity**.
**Reduced Instruction Set Computers** (**RISC**) use a simple **instruction** **set** with a fixed format.
* With a good **compiler**, **RISC** can be faster, since each **instruction** is **executed** faster.

> [!Note]
> The **physical** **implementation** of an **instruction set architecture** in **silicon** is known as the **microarchitecture**.
