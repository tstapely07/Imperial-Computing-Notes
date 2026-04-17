---
date: 2026-04-09
tags:
  - first-year
  - M40001
---
Most processing inside a computer is carried out in **parallel** to maximise speed.
However, in communications, **serial data** is used, where the [[Binary|bits]] are sent one after another.

**Shift** [[registers]] are used to convert streams of **serial data** into **parallel**.
Here's a $4$-**bit** **serial** to **parallel** converter:
* ![[Pasted image 20260409114915.png|429]]

Converting from **parallel** to **serial** is done in two distinct stages:
* First the **parallel data** is loaded onto the **flip-flops**.
* Then the data is shifted out in **serial** form.
The circuit must be able to switch the input to the **flip-flops** between the **parallel** source, and the previous **flip-flop's** output.
* This is achieved using [[Multiplexers|multiplexers]].
Here's a $4$-**bit** **parallel** to **serial** converter:
* ![[Pasted image 20260409115908.png|370]]
* The **parallel output** is not used in the conversion, but may be useful elsewhere.