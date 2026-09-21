---
date: 2026-04-09
tags:
  - first-year
  - M40001
---
To be able to use [[functional design]] principles to build a [[binary]] **adder**, we need to improve our [[half adder]] with a way to propagate a **carry** from a previous **bit**.
The **full adder** achieves this, with the following **truth table**:
* ![[Pasted image 20260409164312.png|258]]
After some simplification, we get the following [[Boolean Algebra|Boolean expressions]]:
* $SUM=A\oplus B\oplus C$
* $C_{out}=C\cdot(A\oplus B)+A\cdot B$
Which results in the following [[Combinatorial Circuits|circuit]]:
* ![[Pasted image 20260409164425.png|356]]
