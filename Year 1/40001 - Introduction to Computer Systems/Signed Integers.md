---
date: 2026-04-05
tags:
  - first-year
  - M40001
---
For any representation of **signed and unsigned integers**, desirable properties include:
* Unique patterns for each value.
* Symmetrical range about $0$.
* Maximum range of values achieved, for a given number of bits.
* No gaps in the range.
* Simple hardware implementation for arithmetic.

**Sign and Magnitude**:
* The **MSB** represents the **sign**:
	* $0=+$
	* $1=-$
* The remaining **bits** represent the magnitude.
* Range for $n$ **bits** is $-(2^{n-1}-1)\le x \le +(2_{n-1}-1)$
> [!Success] Pros
> Simplest for humans to understand.

> [!Warning] Cons
> Two representations for zero - $+0$ and $-0$.
> Costly to implement.

**One's Complement**:
* Negative numbers are the **complement** of their positive equivalent.
	* i.e. the **bits** are **flipped**.
* Range for $n$ **bits** is $-(2^{n-1}-1)\le x \le +(2_{n-1}-1)$

> [!Success] Pros
> Cheap to implement.

> [!Warning] Cons
> Unintuitive to humans.
> Two representations of zero - $0\dots 0$ and $1\dots 1$.

**Two's Complement**:
* Negative numbers are the **complement** of their positive equivalent, plus $1$.
	* e.g. $3_{10}=0011$, so $-3_{10}=1101_2$ 
	* This can be achieved by flipping all **bits**, but leaving the rightmost $1$.
* Range for $n$ **bits** is $-2^{n-1} \leq x \leq 2^{n-1}-1$

> [!Success] Pros
> $X-Y=X+(-Y)$ is satisfied, so subtraction can be implemented by an adder.
> Unique representation for zero.

> [!Warning] Cons
> The range is slightly asymmetric, since there is $1$ extra negative value.

**Excess-n (Bias-n)**: ^d3d41b
* A range is chosen, e.g. $-4\to 3$.
	* $0\dots 0$ represents the lowest number in the range.
	* $1\dots 1$ represents the greatest number in the range.
* For example, if the range is $-4\to 3$ then:
	* $-4_{10}=000_2$
	* $3_{10}=111_2$
	* $1_{10}=101_2$

> [!Success] Pros
> Sorting values is easy.

> [!Warning] Cons
> Unintuitive to humans.
> Arithmetic is costly to implement.

**Binary Coded Decimal**:
* Each decimal digit is encoded by a fixed number of bits, normally $4$.
* For example, $981$ would be $1001\;1000\; 0001$.

> [!Success] Pros
> Intuitive for humans to understand.

> [!Warning] Cons
> Very inefficient use of space.

