---
date: 2026-04-10
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> In [[ER modelling]], in addition to the other types of [[attributes]], we also have **multi-valued attributes**.
> * These remove the property of **uniqueness**.
> * A **multi-valued attribute** may or may not be **optional**.

**Optional multi-valued attributes** are suffixed with a `*`, to indicate $0$ or more values.
**Mandatory multi-valued attributes** are suffixed with a `+`, to indicate $1$ or more values.

For example, a `person` may have any number of `cars` registered to them:
* ![[Pasted image 20260410154107.png|446]]

To map **multi-valued attributes** of some **entity** $E$ to a [[relational schema]], we map $E$ to $R$, and store each **multi-valued attribute** $E.A_v$ in its own [[Relations|table]] $RA_v$, together with the [[Relational Keys|key attributes]] of $R$ used to represent the **entity** $R$.
* All **attributes** of $RA_v$ form its **key**, and there is a [[Foreign Keys|foreign key]] from $RA_v$ to $R$.
* We cannot efficiently represent the `+` constraint.

> [!Example]
> ![[Pasted image 20260410161710.png]]
