---
date: 2026-04-16
tags:
  - first-year
  - M40005
---
In our previous [[datapath]], not all **instructions** have the same number of steps, as this table illustrates:
* ![[Pasted image 20260416220659.png|495]]
However, since every **instruction** must finish in a single [[Clocks|clock]] **tick**, the **clock speed** is limited by the time it takes to execute a `load` **instruction**.
* This limits [[performance]].

If we use **multiple cycles** per **instruction**, then different **instructions** can take different numbers of **cycles**.
* We can reuse hardware, such as combining our **instruction memory** and **data memory**into a single block that is used twice in different **cycles**.
* Another way to reuse hardware is removing the need for extra [[Ripple Through Carry Adder|adders]] for the **PC**, we can just reuse the [[Arithmetic and Logic Unit (ALU) (Architecture)|ALU]].

We need some way to store **data** between the **cycles** of an **instruction's execution**.
To do this, we add new **internal** [[registers]]:
* The **instruction register** (**IR**) holds the $32$-[[Binary|bit]] **instruction** fetched from [[RISC-V Memory|memory]].
* The **memory data register** (**MDR**) holds **data** just read from **memory**.
* The **registers** `A` and `B` hold **values** just read from the main block of **registers**.
* The **register** `ALUOut` holds the result from the **ALU**.

We can break the **load instruction** up into $5$ **cycles**, as shown in this **colour-coded diagram**.
* ![[Pasted image 20260416222124.png|423]]
* Note that the [[multiplexers]] have been omitted for simplicity.

We make a few more key changes to our **processor**:
* We add a **multiplexer** on the first ALU input.
	* This switches between register $A$ and the PC.
* We extend our **multiplexer** on the second ALU input.
	* This now switches between **register** $B$, an **immediate** **value**, or a constant $4$ to increment the PC by.
* We implement a new **comparator** **block**, to compute comparisons for **branch** **instructions** without occupying the **ALU**.
	* This has inputs from **registers** $A$ and $B$, and a control input `BrUn` to indicate whether the number is [[Signed Binary Arithmetic|signed]] or [[Unsigned Binary Arithmetic|unsigned]].
	* It outputs two **flags**, `BrEq`, which is $1$ iff $A=B$, and `BrLt` which is $1$ iff $A\lt B$.
	* It is optimised to do this without carrying out the full [[Binary Subtraction|subtraction]].

Our **multi-cycle datapath** consists of $5$ different **cycles**:
1. **IF** - **instruction fetch**.
2. **ID** - **instruction** **decode**.
3. **EX** - **execute** (**ALU** **operations**).
4. **MEM** - **memory** **access**.
5. **WB** - **register** **write** **back**.
We've already seen how **load instructions** consist of all $5$ **cycles**.

**R-type instructions** can be broken into **cycles** $1,2,3,5$, making $4$ **cycles** total:
* ![[Pasted image 20260416223716.png|398]]
* ![[Pasted image 20260416223735.png|399]]
* ![[Pasted image 20260416223750.png|403]]
* ![[Pasted image 20260416223803.png|409]]

**B-type instructions** only require $3$ **cycles** - $1,2,3$:
* ![[Pasted image 20260416223834.png|417]]
* ![[Pasted image 20260416223845.png|418]]
* ![[Pasted image 20260416223901.png|428]]
	* Now the benefit of our **comparator block** is clear, since the **comparison** and the **address calculation** can happen **simultaneously**.
	* Note that `PCWrite` is set based on the `BrEq`/`BrLt` **flags**, and the `funct3` identifier in the **instruction**.


As we did for the **single-cycle datapath**, we must implement a **control unit**.
We can illustrate it explicitly like so:
* ![[Pasted image 20260416225228.png|488]]
The [[State Transition Tables|state transitions]] essentially depend on the **instruction type**, which we illustrate here, both in full, and in a table:
* ![[Pasted image 20260416225314.png|366]]
* ![[Pasted image 20260416225434.png|555]]
Observe that we assigned numerical states to in our table. Now we can draw a **state transition diagram**:
* ![[Pasted image 20260416225516.png|503]]
By manually tracing the **datapath**, we can replace the [[Register Transfer|register transfers]] with the actual **control signals**:
* ![[Pasted image 20260416225559.png|490]]
* Note for the **write** **signals**, writing `PCWrite` means `PCWrite=1`, for example.
We can implement these **state transitions** using a [[Finite State Machines|finite state machine]]:
* ![[Pasted image 20260416225751.png|495]]
* This stores the **state** as a $4$-**bit** number.
* The input is the `opcode`, and the output is all $15$ **control signals**.

One way to implement this [[Combinatorial Circuits|combinatorial logic]] is using **ROM**.
* Instead of actually computing the **output** through [[logic gates]], we can simply store the entire **truth table** in **ROM**. 
* The **inputs** are the **address**, and the data stored at that **address** makes up the **outputs**.