---
date: 2026-04-18
tags:
  - first-year
  - M40005
---
In [[x86]], the most heavily used [[Instruction Format|instruction]] is `mov`, which copies data from a **source** to a **destination**.
* The syntax is `mov{suffix} Source, Destination`.

We can use almost any combination of [[Operand Types|operands]]:
- **Immediate** $\rightarrow$ **Register** (`movl $0x4, %eax`)
- **Immediate** $\rightarrow$ **Memory** (`movl $-147, (%rax)`)
- **Register** $\rightarrow$ **Register** (`movl %eax, %edx`)
- **Register** $\rightarrow$ **Memory** (`movl %esi, (%rcx)`)
- **Memory** $\rightarrow$ **Register** (`movl (%rax), %eax`)

However, we cannot do a **memory** $\to$ **memory** transfer in a single **instruction**.
* We must instead move it from **RAM** to a [[x86 Registers|register]], and then use another **instruction** to move it from that **register** back to **RAM**.

There are two variants on `mov` that handle moving a **smaller source value** to a **larger destination**.
* The **destination** must be a **register**.
* `movz` fills the remaining bits of the **destination** with a $0$, whereas `movs` **sign extends**.
The syntax is `movz{source suffix}{destination suffix} Source, Destination`, or the same for `movs`.

> [!Example] Examples
> For example, `movzbq %al, %rbx` carries out the operation shown here:
> * ![[Pasted image 20260418113207.png|509]] 
> And this image shows `movsbl (%rax), %ebx`, where we only look at a single **byte** of **memory**:
> * ![[Pasted image 20260418113338.png|560]]