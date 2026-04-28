---
date: 2026-04-18
tags:
  - first-year
  - M40005
---
In [[x86]], **conditional branching** is handled by [[jump instructions]] looking at [[condition codes]].
For example, this [[C]] code:
```C
long abs_diff(long x, long y) {
	long result;
	if (x > y)
		result = x-y;
	else
		result = y-x;
	return result;
}
```
Could be translated to this **assembly**:
```x86
abs_diff:
	cmpq %rsi, %rdi 
	jle .L4
	movq %rdi, %rax
	subq %rsi, %rax
	jmp .L5
.L4:
	movq %rsi, %rax
	subq %rdi, %rax
.L5:
	ret
```
* Essentially we first test the condition. If it is false, we **jump** to the `else` branch. If it is true we continue, and then unconditionally **jump** to the return, to skip the `else`.
