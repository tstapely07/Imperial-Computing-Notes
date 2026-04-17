---
date: 2026-04-15
tags:
  - first-year
  - M40005
---
The **RISC-V** [[Instruction Set Architecture (ISA)|ISA]] is an example of a **modern RISC architecture**.
* It features $32$ [[registers]], $x0\to x31$, which are each $64$ [[Binary|bits]].
* **Register** $x0$ always holds $0$, and $x1$ is used for the **return address**.
* It uses a **word length** of $32$ **bits**, meaning all **instructions** are $32$ **bits**.

It uses a **load-store architecture**:
* This means we attempt to keep data in the **processor** for as long as possible before writing back to **memory**, minimising **memory** access.
* Most **instructions** only involve **registers**, and we have special **instructions** dedicated to accessing **memory**.

There are $6$ different **instruction formats**.
We will use the following shorthand to represent the possible fields:
* `opcdode` - $7$ **bits** - identifies the **instruction**.
* `rd` - $5$ **bits** - identifies the **destination regiser**.
* `rs1` - $5$ **bits** - identifies the first **source register**.
* `rs2` - $5$ bits - identifies the second **source** **register**.
* `funct3` - $3$ bits and `funct7` - $7$ bits - additional **opcode** **fields** used when `opcode` alone isn't sufficient to identify the **instruction**.
* `imm` - an **immediate value**, of varying length - used a for **memory** **offsets** or **hardcoded** **constants**.

**R-type** (**register**) **instructions** are used for computation involving only **registers**.
* They take the form `funct7`-`rs2`-`rs1`-`funct3`-`rd`-`opcode`.
For example, `add x9, x20, x21`, which means `x19=x20+x21` would be written:
* ![[Pasted image 20260415112800.png|573]]

**I-type** (**immediate**) **instructions** are used when a **memory** **offset** or **arithmetic** **constant** is stored within the **instruction** itself. 
* This **immediate** **value** is $12$ bits.
* They take the form `imm[11:0]`-`rs1`-`funct3`-`rd`-`opcode`.
For example, `ld x14, Astart(x2)`, which means `x14=M[Astart+x2]`, with `Astart=8` is written:
* ![[Pasted image 20260415113146.png|635]]
Also, `addi x15, x1, -50`, which means `x15=x1-50` is written:
* ![[Pasted image 20260415113220.png|644]]
Note that `rs1` and `rd` are in the same **bit** **locations** are they were in **R-type**, to simplify hardware.

**S-type** (**store**) **instructions** are used to store a **register's value** back into **memory**.
* Because there is no **destination** **register** being written to, `rd` is replaced by the lower **bits** of the **immediate** **value**, giving a $12$ **bit** value.
* These **instructions** take the form `imm[11:5]`-`rs2`-`rs1`-`funct3`-`imm[4:0]`-`opcode`.
For example, `sd x14, Astart(x2)`, which means `M[Astart+x2]=x14`, with `Astart=8` is written:
* ![[Pasted image 20260415114234.png|620]]

**B-type** (or **SB-type**) (**branch**) **instructions** are a variant of **S-type** **instructions**, and are used for **conditional** **branching**.
* They have the same layout as **S-type instructions**, but the **immediate** **value** **bits** are shuffled around to allow the processor to calculate jump distances more efficiently.
* **Memory** **addresses** are always even numbers, so `imm[0]=0` can be implied and omitted, allowing us to represent a $13$ bit **immediate** **value**.
* These **instructions** take the form: `imm[12]`-`imm[10:5]`-`rs2`-`rs1`-`funct3`-`imm[4:1]`-`imm[11]`-`opcode`.
For example, `beq x19, x10, Label`, which means `if x10==x19 goto Label`, where `Label` is $16$ byte offset, is written:
* ![[Pasted image 20260415114222.png|619]]

**U-type** (**upper** **immediate**) **instructions** are used to load a value into the **upper** **bits** of a **register**:
* These take the form: `imm[31:12]`-`rd`-`opcode`.
For example, `lui x10, 0x87654`, which would set `x10=0x87654000`, is written:
* ![[Pasted image 20260415114617.png|592]]
To load a large value into a **register**, say `0x87654321` into `x10`, we would first do `lui x10, 0x87654`, followed by a `addi x10, x10, 0x321` to add the lower **bits**.

**J-type** (or **UJ-type**) (**jump**) **instructions** are a variant of **U-type instructions**, used for **unconditional** **jumps** to **instructions** in **memory**.
* They use the same layout as **U-type instructions**, but the **immediate** **bits** are shuffled, for hardware efficiency.
* They have the layout `imm[20][10:1][11][19:12]`-`rd`-`opcode`.
* Like for B-type instructions, `imm[0]=0` is **implied**.
For example, `jal x1, 32`, which saves the address of the next **instruction** in `x1` and then jumps $32$ **bytes**, is written:
* ![[Pasted image 20260415114957.png|597]]