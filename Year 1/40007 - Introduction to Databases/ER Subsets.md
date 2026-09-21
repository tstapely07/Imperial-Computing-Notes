---
date: 2026-04-10
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> In [[ER Modelling|ER]], sometimes the **instances** of one [[ER Entities|entity]] $E_s$ are a **subset** of another **entity** $E$, we may add a **subset** constraint:
> $$E_s\subseteq E$$

A **subset** is denote by an **arrow** from $E_s$ to $E$.

> [!Abstract] Example
> Here, some `persons` are `managers`, and they have a `mobile_number`:
> * ![[Pasted image 20260410131222.png|487]]

To map some **subset**$E_s\subseteq E$ to a [[relational schema]], we the [[ER Entities|entities]] $E$ and $E_S$ to [[Relations|tables]]  $R_s$ and $R$, and additionally:
* Add a [[Relational Keys|key]] $\vec{K}$ in $R_s$, where $\vec{K}$ is also the key of $R$.
* Add a [[Foreign Keys|foreign key]] $R_s(\vec{K})\overset{fk}\Rightarrow R(\vec{K})$

> [!Example]
> Here's the **schema** generated from this example model with a **subset**:
> * ![[Pasted image 20260410133649.png|491]]