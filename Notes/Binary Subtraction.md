---
date: 2026-04-09
tags:
  - first-year
  - M40001
---
One way to implement a [[binary]] subtractor is by the **borrow** and **payback** method, which has the following **truth table** for $A-B$:
* ![[Pasted image 20260409175506.png|469]]
This gets us the following [[Boolean Algebra|Boolean equations]]:
* $DIFFERENCE = A\oplus B \oplus P$
* $BORROW=B\cdot P+A'\cdot (B+P)=B\cdot P+A'\cdot (B\oplus P)$
This gives the following [[Combinatorial Circuits|circuit]]:
* ![[Pasted image 20260409175756.png|398]]
We can chain these, like we chained [[Full Adder|full adders]] in a [[ripple through carry adder]], to make an $n$ bit **binary** subtractor.


Another way to implement a **binary subtractor** is a **two's complement subtractor**.
* This implements [[Signed Binary Arithmetic|two's complement subtraction]] by flipping all the **bits** of one of the numbers, and then adding $1$, by setting $C_{in}=1$ on our **ripple through carry adder** from before.
Here is the **circuit**:
* ![[Pasted image 20260409180902.png|351]]
