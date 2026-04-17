---
date: 2026-04-09
tags:
  - first-year
  - M40001
---
> [!Abstract] Definition
> A **shift register** is a [[Registers|register]] where the [[Edge-Triggered D-Type Flip-Flop|edge-triggered D-type flip-flops]] are chained together.
> * The output of one **flip-flop** is connected to the input of the **flip-flop** to tis right.
> * This means that on each falling [[Clocks|clock edge]], the data from one **flip-flop** is loaded into the **flip-flop** to its right.

The uses of a **shift register** include:
* [[Serial and Parallel Conversion]]
* [[Binary Arithmetic with Shift Registers]]

We can combine these uses into single **multipurpose shift register**.
We define the four modes as:
* $00$ - hold.
* $01$ - shift right.
* $10$ - shift left.
* $11$ - parallel load.
Clearly, switching modes is done by switching the input to each **flip-flop**.
* We can achieve this using a $4$-way [[Multiplexers|multiplexer]].
This **multipurpose shift register** can be any length, since all the **flip-flops** share the same **clock** and **selection bits**.
Here is the circuit:
* ![[Pasted image 20260409120930.png|530]]
Each individual stage is connected as follows:
* ![[Pasted image 20260409120924.png|346]]