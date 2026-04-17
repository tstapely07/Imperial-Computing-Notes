---
date: 2026-04-10
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> In [[ER Modelling|ER modelling]], an **n-ary** **relationship** $H$ represents a set of **tuples** between **objects** where each **tuple** is some type of conceptual association between [[ER Entities|entities]] $E_1,\dots,E_n$, where $n\gt 2$:
> $$H\subseteq \set{\langle e_1,\dots,e_n\rangle | e_1 \in E\land \dots \land e_n\in E_n}$$

An **n-ary relationship** is the proper representation of a [[ER Weak Entities|"weak entity"]] with $n$ [[ER Relationships|relationships]] and no [[Relational Keys|key]] [[attributes]].

> [!Example]
> Here, a `person` may work in multiple `departments`, and for each `department`, the `person` will be assigned a `manager`:
> * ![[Pasted image 20260410152551.png|456]]

We map an **n-ary relationships** to a [[relational schema]] just like mapping normal **relationships**, just multiple times.
Let $R$ be a **n-ary relationship** between **entities** $E_1,E_2\dots,E_n$, which each map to $T_1,T_2,\dots,T_n$ with [[relational keys|keys]] $\vec{K_1},\vec{K_2},\dots,\vec{K_n}$
If $R$ is a **many-many relationship**, then it maps to:
* A table $R_{E_1E_2\dots E_n}(\vec{K_1},\vec{K_2},\dots,\vec{K_n}$ 
* A [[Foreign Keys|foreign key]] $R_{E_1E_2\dots E_n}(\vec{K_i})\overset{fk}\Rightarrow T_i(\vec{K_i})$ for each $i\in [1..n]$.
If $R$ is a **one-many relationship** then it maps to:
 * **Columns** $\vec{K_2},\dots, \vec{K_n}$ in $T_1$.
* A [[Foreign Keys|foreign key]] $T_1(\vec{K_i})\overset{fk}\Rightarrow T_i(\vec{K_i})$ for each $i\in [2..n]$.

> [!Example]
> Here's an example for a **many-many relationship**:
> * ![[Pasted image 20260410160719.png|492]]