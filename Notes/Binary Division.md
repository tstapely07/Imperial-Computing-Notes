---
date: 2026-04-16
tags:
  - first-year
  - M40005
---
[[Binary]] **division** is essentially like **long division**.
* Unlike [[Binary Multiplication (Architecture)|multiplication]], division works from left-to-right (**MSB** to **LSB**).

The **algorithm** is as follows, noting that we store the **dividend** in the **remainder register**.
* The [[Arithmetic and Logic Unit (ALU) (Architecture)|ALU]] subtracts the **divisor** from the **remainder**.
* If the result is positive, then the **divisor** "fit", so we **left** **shift** the **quotient**, setting the new **bit** to a $1$.
* If the result is negative, then we must **restore** the original value, by adding the **divisor** back to the **remainder**.
	* In this case, we **left** **shift** the **quotient**, and set the new **bit** to a $0$.
* Either way, we then **right** **shift** the **divisor**.
We can implement this naïvely with the following circuit diagram:
* ![[Pasted image 20260416192505.png|523]]
We have the following flowchart:
* ![[Pasted image 20260416192526.png|401]]
And here's an example, showing $\frac{7}{2}=3\text{ remainder }1$, or $7=3*2+1$:
* ![[Pasted image 20260416192617.png|333]]
As in our initial **multiplication implementation**, this **implementation** wastes space, by using $128$ **bit** **registers** to store $64$ **bit** numbers.
* We can optimise the **division hardware**, by changing what we shift, allowing us to shrink some of then [[registers]] and the [[Arithmetic and Logic Unit (ALU) (Architecture)|ALU]].
