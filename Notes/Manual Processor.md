---
date: 2026-04-09
tags:
  - first-year
  - M40001
---
We will construct a manually programmed $8$-[[Binary|bit]] processor, which utilises a common input for both **data** and **instructions**, as per **von Neumann architecture**:
* ![[Pasted image 20260409195832.png|410]]

We will require:
* [[Registers]] to store input data, the final result, and the current instruction.
* A **carry register** to store the carry-out from calculations.
* An [[Arithmetic and Logic Unit (ALU) (Systems)|ALU]].
* A [[Shift Registers|shift register]].

A simple **data path diagram** might be:
* ![[Pasted image 20260409200243.png|382]]
This diagram gives some information:
* All the **arithmetic** and **shift** operations are done purely using [[Combinatorial Circuits]], without any additional **registers**.
* The chosen **arithmetic** and **shift** operation is determined by **bits** in the **instruction register**.
* No further computation can be carried out on the **results register**.

The **ALU** will take this form:
* ![[Pasted image 20260409200420.png|300]]
It will offer the following functions:
* ![[Pasted image 20260409200441.png|205]]
* Additionally, when $C_{in}=1$:
	* $A+B$ becomes $A+B+1$.
	* $A-B$ becomes $A-B-1$
	* $B-A$ becomes $B-A-1$.
	* All other operations are unchanged.
We can easily define the **arithmetic** operations, using our [[Ripple Through Carry Adder|adder]] and [[Binary Subtraction|subtractor]] from before:
* ![[Pasted image 20260409201058.png|390]]
Now, we can use a [[Multiplexers|multiplexer]], combined with basic [[logic gates]] for the other **ALU** functions:
* ![[Pasted image 20260409201133.png|302]]
We also need an additional **multiplexer** to determine $C_{out}$:
* ![[Pasted image 20260409201203.png|317]]
To make our $4$-**bit** **ALU** work with $8$ **bits**, we can simply use [[functional design]] and connect two of them:
* ![[Pasted image 20260409201748.png]]
As a final addition, we add a $2$-to-$1$ **multiplexer**, that allows $C_{in}$ to be a constant $1$, or the $C_{out}$ from the previous computation, allowing us to chain operations when dealing with numbers larger than $8$-**bits**. 
* ![[Pasted image 20260409202334.png|501]]
* Note that when we need $C_{in}=0$, we can do so by setting $C=0$.

While we could use a **shift register** like before, we do not need to store the result in the same register.
* This means we can avoid the need for a complex [[Synchronous Circuits|synchronous circuit]] that uses [[Clocks|clock]] timings, and instead create a purely **combinatorial circuit**, using **multiplexers**.
We will implement the following functions:
* ![[Pasted image 20260409202621.png|451]]
They are achieved by the following circuit:
* ![[Pasted image 20260409202633.png|442]]

After this design work, the **data path diagram** is much more detailed:
* ![[Pasted image 20260409202728.png|512]]

To wire **instruction register** to the various **multiplexers**, we must decide on an instruction format:
* ![[Pasted image 20260409203131.png|395]]
* **Bits** $6,5,4$ determine the function in the **ALU** or **shifter**.
* **Bit** $0$ determines the input to the $A$ **register**.
* **Bit** $1$ determines the input to the $C_{in}$ of the **ALU**.
* **Bit** $2$ determines the input to the $RES$ **register**.
* **Bits** $3$ and $7$ are currently unused.

The **control unit** or **controller** must ensure that the necessary steps to execute an instruction are carried out in the correct order. 
All instructions will take $5$ steps to execute, as follows:
1. Load the $IR$ **register**.
2. Load the $A$ **register**.
3. Load the $B$ and $C$ **registers**.
4. Load the $IR$ **register**.
5. Load the $RES$ and $C$ **registers**.
We will assume that the data input lines are externally controlled, and will hold the correct input at each step.
We can implement the **controller** as a [[Synchronous Circuits|synchronous]] [[Sequential Circuits|sequential circuit]], with the following [[Finite State Machines|finite state machine]]:
* ![[Pasted image 20260409204002.png|255]]
We can assign the **states** in the most **intuitive** order:
* ![[Pasted image 20260409204409.png|319]]
We can use [[Karnaugh maps]] to get [[Boolean Algebra|Boolean expressions]] for the outputs:
* ![[Pasted image 20260409204522.png|393]]
Now we define the **state transition table**:
* ![[Pasted image 20260409205520.png|400]]
And again, we obtain **Boolean equations** using **K-maps**:
* ![[Pasted image 20260409205617.png|375]]
* In practice, we would check the **don't-cares**, but that will be omitted for brevity here.

We want all our **outputs** to be synchronised with the main **clock**, perhaps like so:
* ![[Pasted image 20260409205724.png|413]]
However, this would mean that the **state register** for the **controller** and the **registers** in the **processor** change on the same clock edge, risking a race hazard.
To resolve this, we can use a NAND gate to add some delay to the **outputs**:
* ![[Pasted image 20260409205840.png|493]]