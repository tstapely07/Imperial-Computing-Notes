---
date: 2026-04-10
tags:
  - first-year
  - M40007
---
Sometimes in [[ER modelling]], an [[ER Entities|entity's]] attributes are not sufficient to uniquely identify itself, and a [[ER Relationships|relationship]] also makes up part of the **entity's** [[Relational Keys|keys]].
* This is a **weak entity**.

> [!Abstract] Definition
> Formally, a **weak entity** has a **key** comprising of one or more [[attributes]] $A_1,\dots$ and one or more $1:1$ **relationships** $R_1,\dots$ such that:
> $$W=\set{\langle v_1,v_2,\dots\rangle|\langle w,v_1\rangle\in W.A_1\land \langle w,v_2\rangle \in R_1\land \dots}$$

Beware of the following cases, which aren't actually **weak entities**.
A **weak entity** with one **key relationship** but no **key attributes** is just a [[ER Subsets|subset]]:
* ![[Pasted image 20260410151744.png|447]]
A **weak entity** with more than one **key relationship** but no **key attributes** is just a **many-many relationship**:
* ![[Pasted image 20260410151902.png|481]]
	* Note the final `dname` is cut off.
A **weak entity** with no **key relationships** is just a normal **entity**:
* ![[Pasted image 20260410151936.png|501]]

> [!Example]
> Here's an example of a **weak entity**, where `swipe_card` depends on the `person` it is issued to:
> * ![[Pasted image 20260410152053.png|563]]

To map a **weak entity** $E_W$ of $E$, with a key $k$, to a [[relational schema]], we map $E_W$ to the [[Relations|relation]] $R_W$, and also use the [[Foreign Keys|foreign key]] **column** $K$ of $E_W$ in the [[Relational Keys|key]] of $R_W$:

> [!Example]
> ![[Pasted image 20260410155710.png]]
> * Here, if `swipe_card` wasn't a **weak entity**, then the only change would be to un-underline `salary_number`, since it is no longer part of the **key**.

