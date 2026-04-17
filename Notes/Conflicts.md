---
date: 2026-04-14
tags:
  - first-year
  - M40007
---
A **conflict** occurs between two **operations** if:
* They belong to different [[transactions]].
* They access the same **data item**.
* At least one of the operations is a **write**.

If there is some **third operations** between a **pairs** of **conflicting operations** that **conflicts** with **both**, then we ignore the **original conflict**:
* For example, if we had $T_1\to T_2$, but also $T_1\to T_3$ and $T_3\to T_2$, then we now **ignore** the **original** $T_1\to T_2$.

> [!Example]
> Here are some **examples** of **conflicts**:
> * ![[Pasted image 20260414111637.png|544]]