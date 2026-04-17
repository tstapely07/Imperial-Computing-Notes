---
date: 2026-04-16
tags:
  - first-year
  - M40005
---
In [[RISC-V Architecture|RISC-V]], we typically work with [[Signed Integers|two's complement]].
* Some **instructions** have the suffix `u`, and work with **unsigned integers**.

In [[40001 - Introduction to Computer Systems|computer systems]], we built a $4$-[[Binary|bit]] [[Arithmetic and Logic Unit (ALU) (Systems)|ALU]], but we will know derive a $1$-**bit** **ALU**.

As before, [[Signed Binary Arithmetic|addition]] and **subtraction** can be implemented using [[Full Adder|full adders]].
* To handle potentially negating the input, in the case of **subtraction**, we can use an **XOR** [[Logic Gates|gate]] as a **programmable inverter**.

We could wire the AND gates, OR gates, and **adders** separately, with interleaving like this:
* ![[Pasted image 20260416172743.png|553]]
Instead, we choose to combine the AND and OR gates together, into an `aor` unit:
* ![[Pasted image 20260416172813.png|121]]
We can then design something like:
* ![[Pasted image 20260416172838.png|543]]
We can even combine this `aor` unit with our **full adder**, to make a new unit, called an `afa`:
* ![[Pasted image 20260416172910.png|162]]
* Note the sideways input and output for the **carry**.
The wiring can be simplified further by now grouping our `aor` units and our full adders, although some interleaving is still required:
* ![[Pasted image 20260416173004.png|635]]

Now all that is left is wiring some [[Multiplexers|multiplexers]], to indicate the desired operation, as follows:
* $d_0d_1=00$ - AND
* $d_0d_1=01$ - OR
* $d_0d_1=10$ - ADD
* $d_0d_1=11$ - SUBTRACT
We now have the following $1$-**bit** **ALU** building block:
* ![[Pasted image 20260416173223.png|198]]
These can be chained together like so:
* ![[Pasted image 20260416173252.png|593]]
* Note the additional setup logic, to initialise $C_1=d_1\cdot d_0$, so that the **bits** get **inverted**, and to initialise the **carry in** correctly.
We can implement our **overflow** **detection** by comparing the **carry-in** and **carry-out** of the **MSB**:
* If the outputs differ, then an **overflow** has occurred.
* This test can be implemented by an **XOR** **gate**.

The `slt` instruction is equivalent to `if a<b then 1 else 0`.
* We can achieve this by slightly modifying our **ALU**.
If $a\lt b$, when we have $a-b \lt 0$, and so the **MSB** of $(a-b)$ must be $1$.
* So we carry out the subtraction, but route the **MSB** back to an additional input on the **LSB** block.
* The corresponding input for all the other blocks can just be $0$
* All that remains is to add an additional **multiplexer** in each **ALU** block.
* We indicate `slt` with $d_0d_1=11$ and $S=0$.
We therefore have the following $1$-**bit ALU**, now $ALUb'$:
* ![[Pasted image 20260416174520.png|206]]
And this can be chained like so:
* ![[Pasted image 20260416174542.png|480]]

We also want some way to test equality.
* Instead of testing `a=b`, we can test `a-b=0`.
We can implement this by adding an AND gate to each of our $1$-**bit** **ALU** blocks:
* ![[Pasted image 20260416180609.png|174]]
Now, we simply set the first **input** as $1$, and we are left with a zero flag at the end:
* ![[Pasted image 20260416180638.png|550]]

In a processor, the [[Clocks|clock speed]] is limited by the slowest [[Combinatorial Circuits|combinatorial]] path. 
* Here, it is the **carry chain**, since each **adder** must wait for the carry bit from the previous **adder**.
* This design what we used is called a [[ripple through carry adder]].
One way to improve this would be a **carry select adder**:
* Here, we compute what the top of of the result would be for two options, both $C_{in}=0$ and $C_{in}=1$.
* This essentially halves the total execution time, although it requires $1.5$ times more **adders**.
Here is a **carry select adder** for $8$ **bits**, made up of three $4$-**bit** **ripple carry adders**.
* ![[Pasted image 20260416181009.png|529]]