---
date: 2026-04-15
tags:
  - first-year
  - M40005
---
The **datapath** of a **processor** is simply the path for processing **data** through the **CPU**:
* The **control unit** reads the **opcode** of the **instructions**, and determines what **datapath** should be taken.
At its simplest level, the **datapath** for [[Von Neumann architecture]] looks like this:
* ![[Pasted image 20260415110516.png|402]]

To define the **datapath** for [[RISC-V Architecture|RISC-V]], we will first define the different **datapaths** for the different **instructions**, such as **R-type** and **I-type**.
* We can then combine this using [[multiplexers]].
* Finally, we will implement a **control** **unit**, to **control** the **multiplexers**.

The **datapath** for **R-type instructions** is simple:
* We just read the values from the two specified [[registers]].
* We then use these as the inputs to the [[Arithmetic and Logic Unit (ALU) (Architecture)|ALU]], and store the result in the indicated **register**.
* The instruction the **ALU** should perform is determined using the `opcode` and the `funct7` and `funct3` fields.
For example, the instruction `add x9, x20, x21`, meaning `reg[9]=reg[20]+reg[21]` has a **datapath** that looks like this:
* ![[Pasted image 20260416210955.png|292]]

For **I-type instructions**, we still read one value from the **registers**, but the other **input** value to the **ALU** comes from the **immediate** **value** embedded in the **instruction**.
* This is a $12$-**bit** constant, so we must pass it through an `Imm Gen` block, to **sign** **extend** it to $64$ **bits**.
* Again, the **ALU** **control input** is determined using `opcode` and `funct3` fields, and the output is stored in the indicated **register**.
For example, the instruction `addi x15, x1, -50`, which means `reg[15]=reg[1] - 50` has a **datapath** that looks like this:
* ![[Pasted image 20260416211234.png|322]]

If we compare the two **datapaths** we have so far, the main difference is the second **ALU** **input**.
By adding a **multiplexer**, we can combine these two **datapaths**. 
These two images show the combined **datapaths**, and the role the **multiplexer** plays:
* ![[Pasted image 20260416211519.png|323]]![[Pasted image 20260416211500.png|309]]

For **I-type instructions** involving **loading**, we now add a path from the **ALU output** to memory, and this result is fed back to the **destination** **register**.
* We toggle between this, and the standard **ALU output** using another **multiplexer**.
For example, the instruction `ld rd, imm(rs1)`, which means `reg[rd]=mem[reg[rs1]+sgx(imm[11:0])]` has the following **datapath**:
* ![[Pasted image 20260416211913.png|426]]

**S-type** (**store**) **instructions** are similar, except that the value in `rs2` is what should be stored in the calculated memory address.
* So we simply route this value from `rs2` to the write data input to the **memory** block.
For the instruction `sd rs2, imm(rs1)`, meaning `mem[reg[rs1]+sgx(imm[11:0])]=reg[rs2]`, the **datapath** looks like this:
* ![[Pasted image 20260416212349.png|390]]

So far, we've had this floating `instructions` input. 
* Now, lets extend what this actually is, by including the **instruction memory**, and also including the **PC**.
* The **PC** input is given by a **multiplexer**, that either increases it by some **immediate value**, using an [[Ripple Through Carry Adder|adder]], or simply increments it by $4$.
	* Note that we increment by $4$ because we use [[RISC-V Memory|byte-addressable memory]], and instructions are $4$ **bytes**.
We end up with this new **datapath diagram**:
* ![[Pasted image 20260416212735.png|433]]

For **B-type instructions**, we already have the required **hardware** to implement them:
For the instruction `beq rs1, rs2, label`, which means `if reg[rs1]==reg[rs2], goto PC+label`, we have the following **datapath**:
* ![[Pasted image 20260416212918.png|434]]
* The equality is indicated by the **zero** **flag** on the **ALU**, which is then passed to `PCSrc`.
* Also note the **left shift**, this is because we have `imm[0]=0]` implied.

Let's now define the **ALU control input**, which is determined by the **ALU control block**.
* The **control input** is $4$ **bits**, and is determined by two **bits** from the **control unit**, `ALUOp`, and `funct3` and `funct7`, where applicable.
The **ALU control** is determined by this **truth table**:
* ![[Pasted image 20260416213747.png|561]]
* For **load** and **store** **instructions**, the **ALU** simply needs to `add`, and for **branch** **instructions**, it needs to `subtract` to test equality.
So now we have the following [[Sequential Circuits|circuit]] diagram:
* ![[Pasted image 20260416213911.png|491]]

In the previous **diagram**, there are blue **control signals** that need to be set for each **instruction**:
* $3$ **multiplexer** **signals** - `PCSrc`, `ALUSrc`, and `MemtoReg`.
* $2$ **memory** **signals** - `MemRead` and `MemWrite`.
* $1$ **register** **signal** - `RegWrite`.
* $2$ **ALU control signals** - $2$ `ALUOp` **bits**.
These are determined by the **control unit**, which sets these **signals** using the `opcode`, as this **diagram** explicitly illustrates:
* ![[Pasted image 20260416214234.png|481]]

For example purposes, we can highlight our **example datapaths** from earlier over this full **diagram**.
**R-type**, e.g. `add`:
* ![[Pasted image 20260416214423.png|444]]
**I-type**, e.g. `ld` (load):
* ![[Pasted image 20260416214529.png|562]]
**B-type**, e.g. `beq`:
* ![[Pasted image 20260416214503.png|560]]
* Note there is a small error in this **datapath**, the second **ALU input** should be a **register**, rather than an **immediate value**.

