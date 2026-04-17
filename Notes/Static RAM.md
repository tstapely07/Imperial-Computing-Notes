---
date: 2026-04-11
tags:
  - first-year
  - M40001
  - lecturers/chiraag-lala
---
We already know that an [[edge-triggered D-type flip-flop]] can store a [[Binary|bit]] of data.
* To be able to use it as **memory**, we need to assign some **address** to it.
* The address is simply a **binary number**.
* We can use a [[Decoders|decoder]] and AND [[Logic Gates|gates]] to enable a specific **flip-flop** only for a specific **binary address**.
This gives us the following **circuit**:
* ![[Pasted image 20260411195325.png|211]]
This architecture is called **static RAM**, or **SRAM**>
* **Reading** is [[Combinatorial Circuits|combinatorial]], since the value $Q$ can be instantly put onto the **data** line.
* **Writing** is [[Sequential Circuits|sequential]], since writing only occurs on a [[Clocks|clock pulse]]. At this time, the **address** and **data** must both be **stable**.