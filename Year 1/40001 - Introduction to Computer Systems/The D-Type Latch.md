---
date: 2026-04-06
tags:
  - first-year
  - M40001
---
The **set** and **reset** inputs to an [[The R-S Flip-Flop|R-S Flip-Flop]] are not very convenient.
The **D-type latch** extends the **flip-flop**, such that:
* $D=0\to S=0,R=1$
* $D=1\to S=1,R=0$
The **latch** controls the input to the **flip-flop**.
* ![[Pasted image 20260406142514.png|422]]
* If the **latch** is set to $1$, then $Q$ matches the input $D$.
* If the **latch** is $0$, then $S=R=1$ due to the NAND [[Logic Gates|gates]], and so the output $Q$ is unchanged.

For brevity, we represent a **D-type latch** with the following symbol:
* ![[Pasted image 20260406142630.png|186]]

Because $Q$ mirrors $D$ for the duration that the **latch** is $1$, there can be fluctuations if $D$ changes multiple times while the **latch** is open.
* This is solved by the [[Edge-Triggered D-Type Flip-Flop]]


