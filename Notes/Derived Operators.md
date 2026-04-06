---
date: 2026-04-05
tags:
  - first-year
  - M40007
---
**Derived operators** act as a shorthand.
* They are constructed entirely from the five [[primitive operators]].

**Natural join** is **binary operator** that acts as a shorthand for doing a **select** on a **product**.
* $R\bowtie S=\sigma_{R.A_1=S.A_1\land\dots\land R.A_m=S.A_m}(R\times S)$
* It works with any number of common [[attributes]].
> [!Example]
> * ![[Pasted image 20260405114225.png|621]]


**Semi join** is a **binary operator** that is like a **natural join**, but only returns **attributes** that appear in the first table:
* $R \ltimes S=R\bowtie \pi_{Attr(R)\cap Attr(S)}(S)$
> [!Example]
> * ![[Pasted image 20260405114556.png]]


**Equi join** is **binary operator** that carries out a **join** on two specific **attributes** with different names.
* $R\overset{A=B}\bowtie S=\sigma_{R.A=S.B}(R\times S)$

**Theta join** is a **binary operator** that carries out a **join** with any **predicate**.
* $R\overset{\theta}\bowtie S=\sigma_\theta (R\times S)$

**Intersection** is a **binary operator** that works like intersection on sets.
* $R\cap S=R-(R-S)$
* The two [[relations]] must be [[union compatible]].
> [!Example]
> * ![[Pasted image 20260405121055.png|86]]![[Pasted image 20260405121100.png|243]]
> * ![[Pasted image 20260405121116.png|320]]


**Division** ($\div$) is a **binary operator** that returns all **tuples** in $R$ that are associated with every **tuple** in the **extent** of $S$.
* $R\div S=\pi_{Attrs(R)-Attrs(S)}R-\pi_{Attrs(R)-Attrs(S)}((\pi_{Attrs(R)-Attrs(S)}R\times S)-R)$
* Division works by:
	* First we project $R$ to extract only the target **attributes**.
	* Then we take the **Cartesian product**, where this list from $R$ is paired with every **tuple** in $S$.
	* Then subtract the actual **relation** $R$, to be left with the "missing entries".
	* Now we project the target attributes from the missing entries.
	* Then we can again project the target **attributes** from $R$, and subtract these missing **entries** to obtain the final result.
* Note that $Attrs(S)\subset Attrs(R)$ must hold.
> [!Example]
> * ![[Pasted image 20260405121800.png|304]]![[Pasted image 20260405121810.png|187]]
> * ![[Pasted image 20260405121819.png|472]]
> * Here, the result is the names of the customers who have every type of account.

