---
date: 2026-04-18
tags:
  - first-year
  - M40005
---
When we want to use **data** from **memory** as an [[Operand Types|operand]] in [[x86]], there is a general form to calculate the exact [[Binary|byte]] that we want to address.
* This makes accessing **structs** and **arrays** much easier.

We write our **addresses** `Imm(rb, ri, s)` .
* This evaluates to `Address = R[rb] + (R[ri]*s) + Imm`.
* `rb` is the **base register**, such as the beginning of an **array**
* `ri` is the **index register**, such as the **index** of an **array**.
	* Note that this can be almost any [[x86 Registers|register]], but not `%rsp`.
* `s` is the **scale**, and must be `1`, `2`, `4`, or `8`. It corresponds to the **byte-size** of the **datatype**.
* `Imm` is the **displacement**, which we often use for **structs**.

There are also many special cases, which act as **shorthand** forms:
* `(rb)` $\to$ `R[rb]`
* `Imm(rb)` $\to$ `R[rb] + Imm`
* `(rb, ri)` $\to$ `R[rb] + R[ri]`
* `Imm(rb, ri)` $\to$ `R[rb] + R[ri] + Imm`

