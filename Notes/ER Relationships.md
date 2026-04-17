---
date: 2026-04-10
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> An [[ER Modelling|ER]] **relationship** represents a set of **tuples** of objects where each **tuple** is some type of conceptual association between [[ER Entities|entities]] $E_1$ and $E_2$:
> $$R\subseteq \set{\langle e1, e2\rangle\;|\;e_1\in E_1\land e_2\in E_2 }$$

These are usually **verbs**, such as `works in`.
**Relationships** are represented by **diamonds** connecting **rectangles** in **ER diagrams**.

> [!Example]
> ![[Pasted image 20260410124152.png]]

The way we map some **relationship** $R$ between [[ER Entities|entities]] $E_1$ and $E_2$ to a [[relational schema]] depends on the [[ER Cardinality|cardinality]] of the **relationship**.
* Assume that the **entities** $E_1,E_2$ are mapped to the [[relations]] $R_1,R_2$, with [[Relational Keys|keys]] $K_1,K_2$.

If $R$ is a **many-many relationship** then it maps to:
* A **table** $R_{R_1R_2}(\vec{K_1},\vec{K_2})$ with a [[Foreign Keys|foreign key]] $R_{R_1R_2}(\vec{K_1})\overset{fk}\Rightarrow R_1(\vec{K_1})$ and a **foreign key** $R_{R_1R_2}(\vec{K_2})\overset{fk}\Rightarrow R_2(\vec{K_2})$.

If $R$ is a **one-many relationship** then it maps to:
* A **column** $\vec{K_2}$ in $R_1$, with a **foreign key** $R_1(\vec{K_2})\overset{fk}\Rightarrow(\vec{K_2})$

If $R$ is a **one-many relationship**, but with $0:N$ then it is like the case for $1:N$, but $\vec{K_2}$ is an [[ER Attributes|optional attribute]] of $R_1$.

If $R$ is a **one-one relationship**, we treat it like a **one-many relationship** and just pick a direction.

> [!Example]
> Here are some **ER models**, and the resulting **schema**.
> **One-many relationship**:
> * ![[Pasted image 20260410133227.png|609]]
> **Optional one-many relationship**:
> * ![[Pasted image 20260410133250.png|613]]
> **Many-many relationship**:
> * ![[Pasted image 20260410133310.png|615]]
> 


