---
date: 2026-04-18
tags:
  - first-year
  - M40005
---
Here's an example of a **switch** **statement**:
* ![[Pasted image 20260418160536.png|322]]
* Here, `5` and `6` result in the same case, `2` is a fall-through case, and the case for `4` is missing.
* Basically, this example has everything that could occur in a **switch statement**.
In [[x86]], the **compiler** uses a **jump table**.
* For each `case` in the `switch`, an address is stored in the **jump table**, like this:
	* ![[Pasted image 20260418162801.png|242]]
		* `.section .rodata` indicates we are declaring **data**, not [[Instruction Format|instructions]].
		* `.align 8` ensures we are $8$-[[Binary|byte]] **aligned**.
		* `.quad` indicates each piece of data (each address) is $64$-**bits**.
We then use an **indirect** [[Jump Instructions|jump]],  `jmp *.L4(,%rdi,8)`, which, instead of jumping to the result of the formula, it jumps to the **address** stored at this result.
* This calculates `.L4 + (%rdi * 8)` to find the correct **address**, where `%rdi` is the value we are **switching**.
For safety, we first check bounds, to ensure we don't try and calculate an address outside our **jump table**.
* By doing an unsigned `ja` check, which will jump to the default case, we also catch **negative cases**, since these wrap around to large **integers**.
Our **switch statement** from before gets translated to something like this in assembly, using the **jump table** shown earlier:
```x86
switch_ex:
	movq %rdx, %rcx
	cmpq $6, %rdi
	ja .L8              # default
	jmp *.L4(,%rdi, 8)  # jump table
```
We then must actually implement each case at the given labels, like this:
* ![[Pasted image 20260418163418.png|470]]
	* Note how at the end of `.L5`, which corresponds to case $2$, we then **jump** to `.L6`, to implement the fall-through from the `switch.`
* ![[Pasted image 20260418163426.png|472]]

This approach doesn't work for a **sparse** `switch` **statement** such as this one:
* ![[Pasted image 20260418164015.png|286]]
The **jump table** would require $1000$ entries. 
* A translation into standard `if-then-else` would require up to $9$ tests.
Instead, we use a **binary** **decision tree** like this:
* ![[Pasted image 20260418164127.png|609]]
In **assembly**, our **sparse** `switch` ends up looking something like this:
* ![[Pasted image 20260418164216.png|606]]