---
date: 2026-04-05
tags:
  - first-year
  - M40001
---
> [!Note]
> **Two's complement** is the standard [[Signed Integers|representation]] used for **signed binary arithmetic**.

**Addition**:
* Add the values column-by-column, and discard the carry-out bit.
	* Discarding this carry-out bit is standard, and does not necessarily indicate an overflow.
* **Overflow** occurs if two numbers of the same sign are added, and the result is of the opposite sign, such as:
	* $(+A)+(+B)=-C$
	* $(-A)+(-B)=+C$
* **Overflow** never occurs when adding operands of opposite signs.
**Subtraction**:
* The second number (the **subtrahend**) is **negated**, and then **added** to the first number (the **minuend**).
* Any carry-out bit is discarded.
* Overflow occurs if two numbers of opposite signs are added, and the result has the same sign as the **subtrahend**, i.e.: 
	* $(+A)-(-B)=-C$
	* $(-A)-(+B)=+C$
	* These cases are identical to the cases for **addition** once the signs are simplified.

**Multiplication** and **division** cannot be achieved efficiently for **signed** numbers using the standard techniques.

