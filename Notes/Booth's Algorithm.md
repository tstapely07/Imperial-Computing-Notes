---
date: 2026-04-16
tags:
  - first-year
  - M40005
---
The [[Binary Multiplication (Architecture)|multiplication]] circuit we derived is good, but it is slow if there are lot of consecutive ones.
We can optimise this using the properties of a **geometric** [[series]] by recognising that:
$$m+2m+\dots+2^{k-1}m=-m+2^km$$
* This replaces $k-1$ **additions** by $1$ **addition** and $1$ **subtraction**. 

**Booth's algorithm** works by looking at two [[Binary|bits]] at a time, although we still only **shift** $1$ at a time:
* If we see a $11$ we are in the **middle** of a block of $1$s, and so do nothing.
* If we see a $00$, we are **between** blocks, so again, do nothing.
* If we see a $10$, we are at the **start** of a block of $1$s, so we **subtract** the **multiplicand** from the **product**.
	* This is equivalent to the $-m$ of the formula.
* If we see a $01$, we are at the **end** of a block of $1$s, so we add the **multiplicand** to the **product**.
	* This is equivalent to the $+2^km$, since the **shifting** accounts for the $2^k$.

Lets compare our original method to **Booth's algorithm**, for :
* ![[Pasted image 20260416190957.png|517]]
* The **benefit** is much more apparent for larger numbers.

> [!Success]
> Additionally, **Booth's algorithm** works on [[signed integers]] without any modifications.