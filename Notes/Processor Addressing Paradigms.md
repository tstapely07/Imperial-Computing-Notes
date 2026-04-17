---
date: 2026-04-16
tags:
  - first-year
  - M40005
---
We can classify different [[Instruction Set Architecture (ISA)|architectures]] by how they address **memory** and store **temporary operands**.

In **stack architectures**, **operands** are implicitly specified at the top of a **stack**:
* e.g. `push A`, `push B`, `add`.
* Pros: **dense code** and a **simple evaluation model**.
* Cons: lacks **random access**, and is slow if the **stack** is stored in **memory**.
In **accumulator architectures**, one **operand** is implicitly kept in a single designated [[Registers|register]], called the **accumulator**:
* e.g. `load A`, `add B`, `store C`.
* Pros: minimal **internal** **storage** required and **short** **instructions**.
* Cons: requires **frequent**, **slow** **memory** **accesses**
* This **architecture** can be thought of as a special case of **register** **based** **architectures**, just with only a **single** **register**.
In **register based architectures**, **explicit** **operands** are loaded into a bank of fast **registers**:
* e.g. `load R1 A`, `add R2, R1, B`, `store C, R2`.
* Pros: **faster** **access** than **memory**, reduces **memory** **traffic**, **compiler** **friendly**, improves **code** **density**.
* Cons: requires **longer** **instructions**, since **operands** must be explicitly named.