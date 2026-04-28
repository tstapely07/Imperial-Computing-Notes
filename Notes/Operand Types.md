---
date:
tags:
---
In [[x86]], the **operand** or **operands** given to an [[Instruction Format|instruction]] can be one of three types:
* A constant **immediate value**.
	* This is prefixed by a `$`, for example `$-536` or `$0x1F`.
* A **register**, indicating where the **data** is located.
	* This is prefixed by a `%`, for example `%rax` or `%r13`.
* A **memory address**, indicating where the **data** is stored.
	* This is wrapped in `()`, for example `(%rax)` would be the **data** at the **memory location** given by the **address** stored in `%rax`. 
	* We can also give an **immediate address**, which we write with no brackets, e.g. `0x120`.

As an example, let's see how a [[C]] function to swap two **pointers** gets translated to **assembly**, using [[the mov instruction]]:
```C
void swap(int* xp, int* yp) {
	int t0 = *xp;
	int t1 = *yp;
	*xp = t1;
	*yp = t0;
}
```
Becomes:
```x86
swap: 
	movl (%rdi), %eax
	movl (%rsi), %edx
	movl %edx, (%rdi)
	movl %eax, (%rsi)
	ret
```
* Note that the [[x86 Registers|registers]] `%rdi` and `%rsi` are used since they are the default **registers** for the first and second **function** **arguments**.
