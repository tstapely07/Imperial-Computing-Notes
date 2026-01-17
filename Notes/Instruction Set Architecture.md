---
date: 2026-01-13
tags:
  - first-year
  - M40005
---
**Instruction set architecture**, **ISA**, provides an **abstraction** of **hardware resources** to **software**. 
>[!Info]
>One **ISA** can be implemented in multiple ways, e.g. both **Intel** and **AMD** support the **x86 ISA**.

# CISC and RISC
There are two main **ISA** approaches, **CISC**, and **RISC**:
* Complex Instruction Set Computers - **CISC**:
	* Dense code
	* Variable format
	* Simple compiler
	* Powerful instruction set
* Reduced Instruction Set Computers - **RISC**:
	* Simple instructions
	* Fixed format
	* Optimising compiler
	* Fast
	* Low development cost
	* Adaptable to new technology
>[!Info]
>Most **ISAs** are now **RISC based**, except for the **x86 ISA**.

# Instructions
Instructions consist of **two parts**, an **opcode** and an **operand**.

**Opcode** specifies its function, while the **operand** specifies the information or data needed to carry out that function.
The **RISC-V** processor has **4** main instruction types, which will be detailed later.

# RISC-V
Benefits of **RISC-V**:
* Open standard, managed by the **RISC-V Foundation**:
	* Free from licensing fees and restrictions.
* Wide variety of implementations, from small edge devices to large servers.
* Easy customisation:
	* Support for **vector extensions** targeting efficient AI, HPC, etc.
* Growing ecosystem:
	* Used commercially by **NVIDIA**, **Qualcomm**, **Samsung**, etc.

![[Pasted image 20260113145053.png|400]]

There are **4** types of instructions:
* R-type - register
* I-type - immediate
* S-type - store
* U-type - upper immediate

The R-type includes arithmetic, comparison, and logical operations.

The I-type instructions cover loading a value from memory into a register, and arithmetic operations when a constant is involved.

The S-type instructions handle storing to memory.
A variation, called SB-type, or B-type, is used for conditional branching.

U-type instructions cover instructions involving data in upper bits of a register.
The UJ-type, or J-type instructions cover unconditional jumps to instructions in memory.
The UJ-type instructions can be considered a variation of the U-type, since they share the same shape.