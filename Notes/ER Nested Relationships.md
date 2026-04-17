---
date: 2026-04-10
tags:
  - first-year
  - M40007
---
In [[ER modelling]], we can define **nested relationships**, where a [[ER Relationships|relationship]] connects to at least one **other relationship**.

If the **relationship** to which a **nested relationship** connects to is **mandatory** and **unique** with **entity** $E$, then we can instead connect the **nested relationship** to $E$:
* ![[Pasted image 20260410153259.png|582]]

> [!Example]
> Here, a `person` works in at least one `departments`, and they may work on any number of `projects` with a some `role`. A `person` can take a different `role` on the project for each `department` that they work in:
> * ![[Pasted image 20260410153449.png|348]]

To map **nested relationships** to a [[relational schema]], if $R$ connects to a relationship $S$, then we map $S$ as normal, and when mapping $R$ we treat $S$ as if it were an **entity**, and again apply the normal rules.

> [!Example] Examples
> Here's an example for a **one-many relationship** connecting to a **many-many relationship**:
> * ![[Pasted image 20260410161201.png|557]]
> And here's an example for a **many-many relationship** connecting to another **many-many relationship**
> * ![[Pasted image 20260410161238.png|459]]