---
date: 2026-04-12
tags:
  - first-year
  - M40001
---
**Buses** carry data, and are shared between many circuits.
* This aims to reduce the physical wiring complexity in a computer.

The **address lines** that go to multiple [[static RAM]] [[Synchronous Circuits|circuits]] are collectively referred to as the **address bus**.
The **data-in** and **data-out lines** from multiple **static RAM** circuits are grouped together in **bytes** or [[Memory Word Sizes|words]] as **data buses**.
The **control lines** carry such as the [[Clocks|system clock]] and **read signals** form the **control bus**.

Since the **data-in** and **data-out lines** are never used simultaneously, we can use a single **bi-directional** bus for both sets of **lines**. 
* If we attempted to use normal AND or NAND [[Logic Gates|gates]], as in the image below, then the [[Synchronous Circuits|circuit]] would **short-circuit**, since we have both a $1$ and a $0$ on the same **wire**:
	* ![[Pasted image 20260412102737.png|200]]
* We must instead use a [[Tri-State Buffers|tri-state buffer]].
