---
date: 2026-04-14
tags:
  - first-year
  - M40007
---
To determine which [[Concurrent Execution|concurrent executions]] of [[transactions]] should be allowed, we look at **serialisability** and **recoverability**.

> [!Abstract] Definition
> A **concurrent execution** of **transactions** is **serialisable** (**SR**) if there is some [[serial execution]] of the **same transactions** which reaches the same **final result**.

> [!Abstract] Definition
> A **concurrent execution** of **transactions** is **recoverable** (**RC**) if no **transaction commits** depend on data that has been produced by another **transaction** that has yet to **commit**.

For the **set** $H$ of all possible **histories**, we have the following **Venn diagram**:
* ![[Pasted image 20260414101711.png]]

![[Pasted image 20260414102210.png]]
* Here, $H_x$ is **recoverable**, but it is not **serialisable**, since the changes to $b_{34}$ by **transaction** $1$ are lost.
![[Pasted image 20260414102320.png]]
* Here, $H_y$ is both **serialisable** and **recoverable**.
![[Pasted image 20260414102346.png]]
* Here, $H_z$ is **serialisable**, but it is not **recoverable**, since **transaction** $1$ **commits** depending on data that **transaction** $2$ is yet to **commit**.