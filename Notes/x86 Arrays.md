---
date: 2026-04-20
tags:
  - first-year
  - M40005
---
In [[C]], an **array** `T A[L]` is a **contiguously allocated region** of [[x86 Memory Layout|memory]].
* The **total memory** used is therefore $L\times sizeOf(T)$.
**Arrays** are stored by a pointer to the **memory address** of start of the block.
* We can then access any element by using the **formula** `base + (index * scale)`

For example, with this **C** function:
```C
int get_digit(int val[], int dig) {
	return val[dig];
}
```
The **assembly** translation is:
```x86
get_digit:
	movslq %esi, %rsi
	movl (%rdi, %rsi, 4), %eax
	ret
```

When we **iterate** using over an **array** using a [[x86 Loops|loop]], we can more efficiently track indices by storing a **pointer** and incrementing it on each iteration.
For example, here's a loop over an array in **C**:
```C
void digit_inc(int val[], int len) {
	int i;
	for (i=0; i<len; i++)
		val[i]++;
	return ;
}
```
First, let's write this using a `do-while` and a **pointer**:
```C
void digit_inc(int val[], int len) {
	if (len>0) {
		int *ptr = val;
		int *vend = val+len;
		do {
			*ptr = *ptr + 1;
			ptr++
		} while (ptr != vend);
	}
	return;
}
```
And now the **assembly** translation is clear:
```x86
digit_inc:
	testl %esi, %esi
	jle .L1
	movq %rdi, %rax
	leal -1(%rsi), %edx
	leaq 4(%rdi, %rdx, 4), %rdx
.L3:
	addl $1, (%rax)
	addq $4, %rax
	cmpq %rdx, %rax
	jne .L3
.L1:
	rep ret
```
