---
date: 2026-04-05
tags:
  - first-year
  - M40001
---
A **Karnaugh map**, or **K-map**, is like a truth table, but laid out such that only one variable changes between adjacent columns or rows.
Here are two examples:
* ![[Pasted image 20260405212625.png|301]]
* ![[Pasted image 20260405212631.png|301]]

We aim to draw **circles** that only cover $1$s. The **circle's** size must be a power of two.
* We aim to draw the largest circles possible, even if they overlap other circles.
For example:
* ![[Pasted image 20260405212733.png]]
* For the **upper circle**, $A$ is always $0$ and $B$ is always $1$, giving the condition $A'\cdot B=1$
* For the **lower circle**, we have $A\cdot C=1$.
* We then AND these together for our final circuit: $A'\cdot B+A\cdot C$
In a **K-map**, we can think of opposite edges as being adjacent, and so circles can wrap around the grid:
* ![[Pasted image 20260405213046.png|216]]


We could also draw **circles** around $0s$, but with a few changes, identically to the differences between finding [[minterms and maxterms]].
* ![[Pasted image 20260406121439.png|219]]


Sometimes, certain input combinations are impossible, or will never occur.
* We call these "don't cares", and denote them using an "x".
* We can then consider these don't cares as a $1$ or a $0$, whichever is more convenient.
* For example:
	* ![[Pasted image 20260405213144.png|466]]