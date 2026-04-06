---
date: 2026-04-05
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> A **foreign key** $R(\vec{X})\overset{fk}\Rightarrow S(\vec{Y})$ of a [[Relations|relation]] $R(AB\dots)$ is a **subset** $\vec{X}\in AB\dots$ of the [[attributes]] for which the **values** in the extent of $R$ also appear as **values** of **attributes** $\vec{Y}$ in the **extent** of $S$.
> Additionally, $\vec{Y}$ must be a [[Relational Keys|key]] of $S$.

> [!Example] 
> In this **schema**, we have the **foreign key** $account(sortcode)\overset{fk}\Rightarrow branch(sortcode)$:
> * ![[Pasted image 20260405104943.png|337]]![[Pasted image 20260405104950.png|253]]


