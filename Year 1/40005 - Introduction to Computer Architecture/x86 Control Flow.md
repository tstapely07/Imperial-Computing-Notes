---
date: 2026-04-19
tags:
  - first-year
  - M40005
---
When a **caller** **function** calls a **callee function**, it needs a way to pass control, and then eventually get it back.
* In [[x86]], this is achieved using the [[x86 Stack Mechanics|stack]].

When the [[Instruction Format|instruction]] `call label` is encountered, the **return address**, i.e. the **address** of the next **instruction** after the call, is **pushed** onto the **stack**.
* The program then [[Jump Instructions|jumps]] to the target **function's** **label**.
When the **callee** is done, it uses `ret`.
* This pops the **return** **address** off the **stack**, and **jumps** back to it.

We also need a way to pass **arguments** to a **function**.
* The first $6$ **arguments** are always placed in specific [[x86 Registers|registers]], in this order: `%rdi`, `%rsi`, `%rdx`, `%rcx`, `%r8`, `%r9`.
* Any **additional** **arguments** are pushed onto the **stack**.
* The **return value** is placed in `%rax` before **returning**.

Note that **registers** are either **callee-saved** or **caller-saved**:
* The **caller-saved registers** can be freely overwritten by the **callee**.
	* If the **caller** wants to save the **data** in these **registers**, it must push them to the **stack**, before `call`.
* The **callee-saved registers** cannot be overwritten by the **callee**.
	* If the **callee** wants to use one of them, it must push the old value to the stack first, and then pop from the stack to restore the original value before returning.

Here's what the **stack** ends up looking like:
* ![[Pasted image 20260419110337.png|382]]

As an example, here's a [[C]] **function**:
```C
long call_incr(long x) {
	long v1 = 21;
	long v2 = increment(&v1, 50);
	return x+v2
}
```
In **assembly**, this becomes:
```x86
call_incr:
	pushq %rbx         # save %rbx since it is callee-saved
	subq $16, %rsp     # allocate 16 bytes of space on the stack
	movq %rdi, %rbx    # save `x` into %rbx, since %rdi will be overriden
	movq $21, 8(%rsp)  # store v1 onto the stack at offset 8
	movl $50, %esi     # set up argument 2 for increment, the value 50
	leaq 8(%rsp), %rdi # set up argument 1 for increment, a pointer to v1
	call increment     # push return address to stack and jump to increment
	addq %rbx, %rax    # add x to the return of increment
	addq $16, %rsp     # deallocate the stack space
	popq %rbx          # restore the original value of %rbx
	ret                # pop return address and jump back to caller
	
increment:
	movq (%rdi) %rax  # store contents of memory at %rdi, 21, in %rax
	addq %rax, %rsi   # add contents of %rax to %rsi, so now %rsi=71
	movq %rsi, (%rdi) # store %rsi back into the memory address of v1
	ret               # return to call_incr
```

And here's another **function**, this time with more than $6$ **arguments**.
Here's the **C**:
```C
long call_proc() {
	long x1 = 1;
	int x2 = 2;
	short x3 = 3;
	char x4 = 4;
	proc(x1, &x1, x2, &x2, x3, &x3, x4, &x4);
	return (x1+x2)*(x3-x4);
}
```
And here's the **assembly**:
```x86
call_proc:
	# we first store the local variables
	subq $32, %rsp        # alllocate 32 bytes of space on the stack
	movq $1, 24(%rsp)     # store long x1 = 1 (8 bytes)
	movl $2, 20(%rsp)     # store int x2 = 2 (4 bytes)
	movl $3, 18(%rsp)     # store short x3 = 3 (2 bytes)
	movl $4, 17(%rsp)     # store char x4 = 4 (1 byte)
	
	# now we push the 7th and 8th arguments to the stack
	leaq 17(%rsp), %rax   # get address of x4 using leaq
	movq %rax, 8(%rsp)    # store argument 8 (&x4) onto the stack
	movl $4, (%rsp)       # store argument 7 (x4) onto the stack
	
	# now we set up arguments 1 to 6 in the correct registers
	leaq 18(%rsp), %r9    # set up argument 6 (&x3) 
	movl $3, %r8d         # set up argument 5 (x3) using 32-bit register 
	leaq 20(%rsp), %rcx   # set up argument 4 (&x2) 
	movl $2, %edx         # set up argument 3 (x2) using 32-bit register 
	leaq 24(%rsp), %rsi   # set up argument 2 (&x1) 
	movl $1, %edi         # set up argument 1 (x1) using 32-bit register
	
	# now we call the function
	call proc
	
	# now we calculate the return value
	movslq 20(%rsp), %rdx # load x2 from stack and sign-extend to 64-bit
	# x1 doesn't need sign-extending so we can use it directly from the stack
	addq 24(%rsp), %rdx   # calculate (x1+x2) and store in %rdx
	movswl 18(%rsp), %eax # load x3 fro4 stack and sign-extend to 32-bit
	movsbl 17(%rsp), %ecx # load x3 from stack and sign-extend to 32-bit
	subl %ecx, %eax       # calculate (x3-x4) and store in %eaax
	cltq                  # sign-extend the %eax to 64-bit %rax
	imulq %rdx, %rax      # multiply (x1+x2) * (x3-x4), result is in %rax
	
	# clean up and return
	addq $32, %rsp        # deallocate the 32 bytes of stack space
	ret                   # return
```

