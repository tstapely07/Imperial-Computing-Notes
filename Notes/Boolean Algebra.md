---
date: 2026-04-05
tags:
  - first-year
  - M40001
---
**Boolean algebra** provides a formal representation for logical operations.
* The truth values are replaced by [[binary]] numbers:
	* True is $1$.
	* False is $0$.
* The propositions are replaced by variables.
* The operators are replaced by symbols:
	* NOT is $'$
	* AND is $\cdot$
	* OR is $+$
	* Note that, read top to bottom, this is the symbols' order of precedence.

There are various laws that allow simplification of expressions:
* Associative law:
	* $(A\cdot B)\cdot C\equiv A\cdot (B\cdot C)$
	* $(A+ B)+ C\equiv A+ (B+ C)$
* Commutative law:
	* $A\cdot B\equiv B\cdot A$
	* $A+B\equiv B+A$
* Distributive law:
	* $A\cdot(B+C)=A\cdot B+A\cdot C$
	* $A+(B\cdot C)=(A+B)\cdot (A+C)$
* Idempotent law:
	* $A\cdot A=A$
	* $A+A=A$
* Laws with $0$ or $1$:
	* $A\cdot 0=0$
	* $A\cdot 1 = A$
	* $A+0=A$
	* $A+1=1$
* Absorption law:
	* $A+A\cdot B=A$
	* $A\cdot(A+B)=A$
* De Morgan's Theorem:
	* $(A+B)'=A'\cdot B'$
	* $(A\cdot B)'=A'+B'$
	* Note that this theorem applies for any number of variables.

Every **Boolean equation** has a dual, which is found by swapping every **AND** for **OR**, and vice versa.
* We also swap $1$ and $0$.
* If expressions $E_1$ and $E_2$ are equal, then their duals are also equal.

We can also take the **complement** of both sides of a **Boolean equation**.