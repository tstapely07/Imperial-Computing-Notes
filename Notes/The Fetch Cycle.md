---
date: 2026-04-12
tags:
  - first-year
  - M40001
---
To retrieve data from [[Static RAM|memory]], we need to follow a number of steps.
* Each step [[Register Transfer|transfers]] data from one [[Registers|register]] to another.
Overall, this process is the **fetch cycle**.

For example, fetching the next instruction, and loading it into the [[Connecting RAM to a Processor|instruction register]] requires the following steps:
* $MAR\leftarrow PC$
* $MDR\leftarrow RAM[MAR],PC\leftarrow PC+1$
* $IR\leftarrow MDR$

As seen [[Register Transfer|before]], to transfer data between **registers**, we can set the required paths by using [[multiplexers]] for the **source**.
* We then use a [[decoders|decoder]] to and NAND [[Logic Gates|gates]] the **system** [[Clocks|clock]] so only the **destination registers** is written to.
* ![[Pasted image 20260412114735.png|204]]

We can design the **controller** using a [[Synchronous Circuits|synchronous]] [[Sequential Circuits|sequential circuit]], with the following [[Finite State Machines|finite state machine]]:
* ![[Pasted image 20260412114832.png|223]] 
* Note that in practice, the **execute** step will require multiple states.
We now design the [[State Transition Tables|state transition table]]:
* ![[Pasted image 20260412114918.png|299]]
* Note that a $0$ sets the **MAR** **input multiplexer** to the **PC** **output**.
* Also, a $0$ sets the **PC input multiplexer** to the **incrementer output**.
Assuming the [[Boolean Algebra|Boolean equations]] were obtained and [[Circuit Minimisation|minimised]], we can construct the final circuit:
* ![[Pasted image 20260412115059.png|304]]
