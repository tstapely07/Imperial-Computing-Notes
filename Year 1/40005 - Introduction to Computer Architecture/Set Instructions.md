---
date: 2026-04-18
tags:
  - first-year
  - M40005
---
In [[x86]], `set*` instructions, such as `sete` for equal or `setg` for greater, read the [[condition codes]], and set a **single-byte** [[x86 Registers|register]] to $1$ if the condition is true, or $0$ if it is false.
The full list of instructions is given here:
* ![[Pasted image 20260418121556.png|509]]

For example, to implement this [[C]] code:
```C
int gt(int x, int y) {
	return x > y
}
```
We would write the following **assembly**:
```x86
cmpl %esi, %edi  # compare x : y
set g %al        # al = x>y 
movzbl %al, %eax # zero rest of %rax
```
* Note the use of `movzbl` to ensure the rest of the **register** is set to $0$.
* When we set a $32$-**bit** register, the top $32$-**bits** are automatically cleaned for us, which is why we are able to only use `movzbl %al, %eax`, instead of `movzbq %al, %rax`.

