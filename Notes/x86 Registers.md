---
date: 2026-04-17
tags:
  - first-year
  - M40005
---
[[x86]] has **16** general-purpose integer [[Registers]], each $64$-[[binary|bits]] wide.
* We can also specifically access the lower portions of a **register**:
	* The prefix `r`, e.g. `%rax`, refers to the full $64$-bit **register**.
	* The prefix `e`, e.g. `%eax`, refers to the lower $32$ **bits**.
	* No prefix, e.g. `%ax`, refers to the lower $16$ **bits**.
	* The suffix `l` or `b`, e.g. `%al` or `%r8b` refers to the lower $8$ **bits**.

The various **registers** and their **roles** are given here:
* ![[Pasted image 20260417214442.png|474]]
* The **caller-saved registers** can be freely overwritten by the **callee**.
* If the **callee** wants to overwrite the **callee-saved registers**, it must save these **values** itself, and restore the original **values** before returning **control** back to the **caller**. 
	* For more explanation, see [[x86 Control Flow|control flow]].
* Also note the `%rsp` register is reserved for the **stack pointer**.

> [!Note]
> The **PC register** is not grouped with these **general-purpose registers**, but it is worth noting that it is called `%rip`.