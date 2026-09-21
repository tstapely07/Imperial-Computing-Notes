---
date: 2026-04-05
tags:
  - first-year
  - M40001
---
[[Boolean Algebra|Boolean]] functions can be represented using symbols:
* AND:
	* ![[Pasted image 20260405195244.png|153]]
* OR:
	* ![[Pasted image 20260405195256.png|154]]
* NOT:
	* ![[Pasted image 20260405195306.png]]
Adding a circle to any gate results in its inverted equivalent:
* NAND:
	* ![[Pasted image 20260405195353.png|270]]
* NOR:
	* ![[Pasted image 20260405195405.png|272]]

> [!Abstract] Definition
> A set of **Boolean functions** $f_1,f_2,\dots$ is **complete** if any other **Boolean function** can be represented by these functions.
> 

NAND alone is **complete**.
* For this reason, it is often called the **universal gate**.
* Here are some gates, made using only NAND:
	* NOT:
		* ![[Pasted image 20260405195601.png]]
	* AND:
		* ![[Pasted image 20260405195617.png|277]]
	* OR:
		* ![[Pasted image 20260405195628.png|279]]

The XOR gate is true iff the inputs are different:
* $R=A\oplus B = A\cdot B'+A'\cdot B$
* ![[Pasted image 20260405200059.png|201]]
* Again, it can be constructed using NAND gates:
	* ![[Pasted image 20260405200124.png|345]]

The gates themsleves have different relative physical sizes, approximately, these are:
* NOT - 3.
* NAND/NOR - 4.
* AND/OR - 6.
* XOR/XNOR - 8.
By replacing AND and OR gates with NAND and NOR gates, and then using De Morgan's theorem to move the NOT gates through the circuit, a smaller physical representation for a circuit can be obtained.