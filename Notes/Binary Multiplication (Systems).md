---
date: 2026-04-09
tags:
  - first-year
  - M40001
---
In general for a $2$-digit number, **long multiplication** has the following form:
$$a_1a_0\times b_1b_0=a_1\times b_1\times 10^2+a_0\times b_1\times 10+a_1\times b_0\times 10+a_0\times b_0$$
We can implement this for **binary**, replacing the $\times$ with [[Logic Gates|AND]], and using a [[Shift Registers|left shift]] to multiply by $2$:
$$a_1a_0\times b_1b_0=(a_1\cdot b_1)\Leftarrow 2+(a_0\cdot b_1)\Leftarrow1+(a_1\cdot b_0)\Leftarrow 1+a_0\cdot b_0$$
We can construct this [[Combinatorial Circuits|circuit]] by wiring [[Half Adder|half adders]] as follows:
* ![[Pasted image 20260409181305.png|384]]

Although not as cleanly as with the [[ripple through carry adder]], we can use [[functional design]] and chain this $2$-**bit** to make a $4$-**bit** multiplier****:
* ![[Pasted image 20260409194744.png|390]]
Of course, we can then repeat this process for $8$ and $32$-**bit** multipliers.


