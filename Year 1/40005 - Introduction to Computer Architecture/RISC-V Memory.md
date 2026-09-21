---
date: 2026-04-16
tags:
  - first-year
  - M40005
---
[[RISC-V Architecture|RISC-V]] uses **byte addressable memory**, meaning each **byte** has a unique address.
* Since each **word** is $32$-[[Binary|bits]], **word addresses** must always **increment** by $4$.
**RISC-V** is **little-endian**, which means the **LSB** of a **word** is in stored in the **lowest** memory address:
* ![[Pasted image 20260416161838.png|524]]

**RISC-V** has four main addressing modes used to access **data**:
* **Register addressing**: the **data** is located in [[registers]], like in **R-type instructions**.
* **Immediate addressing**: the **data** is a **constant** embedded directly within the **instruction**, like in **I-type** or **U-type** **instructions**.
* **Base addressing**: the **data** is in **memory**, and the **address** is calculating by adding some **immediate** **offset** to a **base** **value** stored in a **register**.
* **PC-relative addressing**: the target **address** is calculated relative to the **PC**, like in **B-type** or **J-type branches**.