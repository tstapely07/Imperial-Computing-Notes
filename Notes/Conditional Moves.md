---
date: 2026-04-18
tags:
  - first-year
  - M40005
---
Implementing [[x86 Conditional Branching|conditional branching]] using [[jump instructions]] and **branching** ends up being slow.
* To solve this, [[x86]] introduced **conditional move** [[Instruction Format|instructions]].
* `cmov*` essentially means `if (Test) Dest <- Src`.
We can replace `*` with the same **suffixes** as in [[Jump Instructions|jump]] and [[set instructions]], which use the [[condition codes]].

For our same [[C]] code as before:
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
This translates to:
```x86
abs_diff:
	movq %rdi %rax    # x
	subq %rsi, %rax   # res = x-y
	movq %rsi %rdx
	subq %rdi, %rdx   # eval = y-x
	cmpq %rsi, %rdi
	cmovle %rdx, %rax # if <=, res = eval
	ret
```

> [!Warning]
> In some cases, **conditional moves** are not suitable:
> * When both values are computationally expensive.
> * When both values may cause side effects.
> * For risky computations, such as null-checking.
 