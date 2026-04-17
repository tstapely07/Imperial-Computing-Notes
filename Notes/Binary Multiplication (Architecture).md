---
date: 2026-04-16
tags:
  - first-year
  - M40005
---
In [[RISC-V Architecture|RISC-V]] the instructions that involve **multiplication** include:
* `mul` - multiply - stores the bottom $32$-[[Binary|bits]].
* `mulh` - multiply high - stores the top $32$-**bits**.
These also have **unsigned** versions, with a `u` suffix.

Throughout these notes, we will only consider **unsigned arithmetic**, for simplicity.

The core **multiplication algorithm** is as follows:
* We shift the **multiplicand** to the left one bit at a time, and if the corresponding **multiplier** **bit** is a $1$ we add it to the total, otherwise we add $0$.
This is known as the **conditional shift and add** method:
* ![[Pasted image 20260416184917.png|271]]
* Note here we do not add the **purple** `0010`, since it corresponded to a $0$ in the **multiplier**.

We can implement this in hardware with:
* A $64$-**bit** **multiplier** [[Registers|register]].
* A $128$-**bit** **multiplicand** **register** which begins with the $64$-bit **multiplicand** in the right half.
* A $128$-**bit** **product** **register** which starts at $0$.
* A $128$-**bit** [[Arithmetic and Logic Unit (ALU) (Architecture)|ALU]].
This gives the following circuit diagram:
* ![[Pasted image 20260416185723.png|435]]
In each of the $64$ iterations, we look at the **LSB** of the multiplier. 
* If it is a $1$, we add the contents of the **multiplicand** **register** to the product. 
* If it is a $0$, we do nothing.
* We then shift the **multiplicand** left by $1$-**bit**, shift the **multiplier** right by $1$-**bit**, and repeat.
We represent this by the following flow chart:
* ![[Pasted image 20260416185428.png|356]]
Here's an example, but for $4$ **bits**, rather than $64$:
* ![[Pasted image 20260416185443.png|383]]
* This computes $3\times 2$, and the result is indeed $6$.

The previous hardware approach worked, but it is very inefficient.
* Now, instead of shifting the **multiplicand** left, to align with the **product**, we instead shift the **product** right. 
* Now, the **ALU** and **multiplicand register** can both be shrunk down to $64$ **bits**, with the **ALU** **output** wired to the top-half of the **product register**.
This gives the following circuit diagram:
* ![[Pasted image 20260416185735.png|487]]
The logical flow is similar to before, except the shifts are of course different, as illustrated in this flow chart:
* ![[Pasted image 20260416185818.png|370]]
And here's the same $3\times 2$ example, again reaching $6$:
* ![[Pasted image 20260416185843.png|479]]

Finally, we can observe that both the **multiplier register** and the **product register** are shifting to the **right**.
* The right half of the **product register** starts empty and is gradually populated.
* At the same time, the **multiplier register** leaves empty space behind as it shifts.
* In fact, we can initialise the right half of the **product register** to the **multiplier**, and eliminate the need for a **multiplier register** entirely.
This is shown in this diagram:
* ![[Pasted image 20260416190051.png|405]]
Again, here's a flow chart, and the same example of $3\times 2= 6$:
* ![[Pasted image 20260416190124.png|425]]
* ![[Pasted image 20260416190138.png|432]]
