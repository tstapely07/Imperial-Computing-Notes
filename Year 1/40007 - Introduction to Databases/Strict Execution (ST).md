---
date: 2026-04-14
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> A [[Transactions|transaction history]] is a **strict execution** (**ST**) if **transactions** are blocked from **reading** and **writing** to a **data item** until the previous **transaction** that wrote to it has **committed** or **aborted**.
> * A **strict execution** has no [[Dirty Read|dirty reads]] or [[Dirty Write|dirty writes]].

For **example**, this **history** is [[Avoids Cascading Aborts (ACA)|ACA]], but not **ST**:
* ![[Pasted image 20260414120131.png|451]]