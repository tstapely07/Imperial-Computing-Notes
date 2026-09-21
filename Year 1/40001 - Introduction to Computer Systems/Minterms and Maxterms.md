---
date: 2026-04-05
tags:
  - first-year
  - M40001
---
> [!Abstract] Definition
> A **minterm** is a **conjunction** that contains every variable or its **negation** exactly once.
> * For example, with three variables, $A\cdot B\cdot C$ and $A'\cdot B\cdot C'$ are **minterms**, but $AB$ is not.
> * A **minterm** evaluates to $1$ for exactly one of the possible combinations of its input variables, and $0$ for every other combination.
> 

> [!Abstract] Definition
> The [[Canonical Forms|canonical]] **minterm form** of a [[Boolean Algebra|Boolean expression]] is a disjunction of **minterms**.
> * For example, $R = (A \cdot B \cdot C) + (A \cdot B' \cdot C') + (A' \cdot B \cdot C)$

> [!Abstract] Definition
> A **maxterm** is a **disjunction** that contains every variable or its **negation** exactly once. 
> * For example, with three variables, $A+B+C'$.
> * A **maxterm** evaluates to $0$ for exactly one of the possible combinations of its input variables, and $1$ for every other combination.

> [!Abstract] Definition
> The **canonical maxterm form** of a **Boolean expression** is a **conjunction** of **maxterms**.
> * For example, $R=(A+B+C)\cdot (A+B'+C')\cdot (A'+B+C)$

To generate a **canonical minterm form** from a truth table, we find the **minterms** of all the lines where the output is $1$, and OR them together:
* ![[Pasted image 20260405205541.png]]
* Note that when finding the **minterm** for a row, if the input is $1$ we write the letter normally, and if the input is $0$ we write the **negation**.
	* So for a given row of inputs, its **minterm** should always evaluate to $1$.
* $R=A'\cdot B\cdot C+A\cdot B'\cdot C+A\cdot B\cdot C'+A\cdot B \cdot C$
Similarly, to generate a **canonical maxterm form** from a truth table, we find the **maxterms** of all the lines where the output is $0$, and AND them together:
* ![[Pasted image 20260405205752.png]]
* Note that when finding the **maxterm** for a row, if the input is $0$ we write the letter normally, and if the input is $1$ we write the **negation**.
	* So for a given row of inputs, its **maxterm** should always evaluate to $0$.
* $R=(A+B+C)\cdot (A+B+C')\cdot(A+B'+C)\cdot (A'+B+C)$

We can also generate a **canonical form** from any equation.
For the case of **canonical minterm form**, we first use algebraic simplification to get it into a sum of products.
* For example, $X=B\cdot C+A'\cdot B\cdot C$
Now we carry out **augmentation**.
* Since $(A+A')\equiv 1$ and $A\cdot 1\equiv A$, we can write:
	* $X=(A+A')\cdot B\cdot C+A'\cdot B\cdot C$
* And so $X=A\cdot B\cdot C+A'\cdot B\cdot C+A'\cdot B \cdot C$, which simplifies to our final result:
	* $X=A\cdot B\cdot C+A'\cdot B\cdot C$

To generate a **canonical form** from a circuit, we write out its equation by inspection, and then carry out the above steps to reach a **canonical form**.