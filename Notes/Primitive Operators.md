---
date: 2026-04-05
tags:
  - first-year
  - M40007
---
All **operators** take [[relations]] as their **input**, and produce a single **relation** as their **output**.

There are **5** **primitive operators**.

**Project** ($\pi$) is  **unary operator** that returns all of the [[attributes]] that are specified as **subset**.
* Removing **attributes** may result in **duplicate tuples**, but these are automatically removed.
* Project can also **rename** **attributes**, using $\pi_\text{oldName as newName}$ to make them [[union compatible]], e.g. $\pi_{\text{sortcode as id}}account$).
> [!Example]
> * ![[Pasted image 20260405111607.png]]
> * ![[Pasted image 20260405111623.png]]![[Pasted image 20260405111629.png|170]]
> 


**Select** ($\sigma$) is a **unary operator** that returns all of the **tuples** that satisfy a given **predicate**.
> [!Example]
> * ![[Pasted image 20260405111737.png|488]]
> * ![[Pasted image 20260405111749.png]]


**Product** ($\times$) is a **binary operator** that takes two **relations** and computes their **Cartesian product**.
* The [[Relational Keys|key]] of the output **relation** is simply made up of the **primary keys** from both **relations**.
* Identical **attribute** names in the two input **relations** are permitted, since they can be distinguished by their **parent relation**.
* If a **product** followed by a **select** is carried out, we say that a **join** has been performed.
> [!Example]
> * ![[Pasted image 20260405111819.png|316]]![[Pasted image 20260405111826.png|451]]
> * ![[Pasted image 20260405111851.png|578]]


**Union** ($\cup$) is a **binary operator** that combines all **unique tuples** from two **relations** into a single **relation**.
* The **relations** must be [[union compatible]].
> [!Example]
> * ![[Pasted image 20260405112404.png|239]]![[Pasted image 20260405112408.png|125]]
> * ![[Pasted image 20260405112413.png]]


**Difference** ($-$) is a **binary operator** that returns **tuples** that are present in the **extent** of the first **relation**, but not the second.
* The **relations** must be [[union compatible]].
> [!Example]
> * ![[Pasted image 20260405112454.png]]![[Pasted image 20260405112459.png]]
> * ![[Pasted image 20260405112506.png]]

