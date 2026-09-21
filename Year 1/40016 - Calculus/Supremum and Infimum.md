---
date: 2026-03-22
tags:
  - first-year
  - "#M40016"
---
> [!Abstract] Definition
> For a **set** $A\subseteq \mathbb{R}$, a number $b$ is an **upper bound** if $\forall a \in A,a\le b$.

> [!Abstract] Definition
> For a **set** $A\subseteq \mathbb{R}$, a number $c$ is a **lower bound** if $\forall a \in A,c\le a$.

> [!Abstract] Definition
> The **supremum** of a **set** $A$ ($\operatorname{sup} A$) is the **least upper bound**.
> For any other **upper bound** of $A$, $b$, $\operatorname{sup} A \le b$. 

> [!Abstract] Definition
> The **infimum** of a **set** $A$ ($\operatorname{inf} A$) is the **greatest lower bound**.
> For any other **lower bound** of $A$, $c$, $c \le \operatorname{inf} A$.
> 

> [!Example] Examples
> For the **set** $A=\set{x\in \mathbb{R} : x^2\lt2}$, a **lower bound** could be -100, and an **upper bound** could be 100. 
> The **supremum** is $\sqrt{2}$, and the **infimum** is $-\sqrt{2}$.
>
For the **set** $B=\set{1,2,3}$, the **supremum** is $3$, and the **infimum** is $1$.

Note that these two **examples** show that the **supremum** and **infimum** may or may not be elements of the set itself.

Here's another way to define the **infimum** and **supremum**:
* Assume $A\neq \emptyset$.
* A number $b=\operatorname{sup} A$ iff:
	1. $b$ is an **upper bound** of $A$.
	2. $\forall \epsilon\gt 0, \exists a\in A \;s.t.\;b-\epsilon\lt a\le b$.
	* This can be proved by **contradiction**:
		* If there is not some $a$, then $b-\epsilon$ would be an **upper bound**, and so $b$ was not the **least upper bound**, and therefore not the **supremum**.
* A number $c=\operatorname{inf} A$ iff:
	1. $c$ is a **lower bound** of $A$.
	2. $\forall \epsilon\gt 0, \exists a\in A \;s.t.\;c\le a\lt c+\epsilon$.
	* This can also be proved by **contradiction** in the same fashion as above.

The **supremum** is **unique**.
* Suppose $a$ and $a'$ are both **supremums** of $A$.
* Since $a$ is a **supremum** and $a'$ is an **upper bound**, $a\le a'$.
* Similarly, since $a'$ is a **supremum** and $a$ is an **upper bound**, $a'\le a$.
* Therefore $a\le a'$ and $a'\le a$, and so $a=a'$.
In the same fashion, we can prove that the **infimum** is also **unique**.