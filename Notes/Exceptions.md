---
date: 2026-04-17
tags:
  - first-year
  - M40005
---
Sometimes we need to interrupt the standard **control flow**.

> [!Abstract] Definition
> **Exceptions** are an **unexpected event** triggered from **inside** the **processor**, such as an unknown **opcode** or an [[Arithmetic and Logic Unit (ALU) (Architecture)|arithmetic overflow]].

>[!Abstract] Definition
> **Interrupts** are an **unexpected event** triggered from the **external environment**, such as a keypress or an input/output request.

To handle these an **exception** we must:
* Save the cause of the **exception** in a new [[Registers|register]], the **cause register**.
	* We have a new **control signal** from the **control unit** to the **cause register**, `IntCause`, where `IntCause=0` means "unknown opcode", for example.
* To know where to restart from, we save the address of the **instruction** that caused the **exception** into the **exception PC** (**EPC**) **register**, another new **register**.
* Now, the **OS** forces the **PC** to jump to a specific, **hardcoded** **exception** **address** in [[RISC-V Memory|memory]], where the code to handle the relevant **exception** is **located**.
	* The code at this **exception address**, can inspect the **cause register** to work out what happened.
This diagram shows the **control flow** when handling an **exception**:
* ![[Pasted image 20260417115439.png|413]]

To implement this in the [[datapath]], we first add two additional inputs to the PC source [[Multiplexers|multiplexer]]:
* ![[Pasted image 20260417115643.png|366]]
If we also add the two new registers, our **datapath** now looks like this:
* ![[Pasted image 20260417115723.png|455]]
* Note the constant **exception address** of $0x8000 0180$.

All that is left is to modify our [[State Transition Tables|state transition diagram]]:
* ![[Pasted image 20260417115839.png|444]]
* Note that for now, we are only considering $2$ possible **exceptions**, unknown **opcode**, and **overflow**.
