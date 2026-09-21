---
date: 2026-04-10
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> **Attributes** hold data about [[ER Modelling|ER]] [[ER Entities|entities]].
> 

There are three types of **attributes**.

A **mandatory attribute** $E.A$ is a **function** that maps from entity set $E$ to value $V$.
* $E.A\subseteq \set{\langle e,v\rangle | e\in E \land v \in V}$
	* $E.A$ is a **subset** of all possible pairings between **entities** and **values**.
* **Attributes** are **unique**, so $\langle e, v_1\rangle \in E.A \land \langle e,v_2\rangle \in E.A \implies v_1=v_2$.
	* If the same **entity** maps to two **values**, those values must be the same.
* **Mandatory attributes** being **mandatory** means that $E=\set{e | \langle e,v\rangle \in E.A}$.
	* The set of all **entities** is equal to the set of **entities** that hold this **mandatory attribute**.
**Mandatory attributes** are denoted by text attached to an **entity**.

An **optional attribute** is like a **mandatory attribute**, without the final **mandatory property**.
**Optional attributes** are denoted by a `?` suffix.

Certain **mandatory attributes** $E.A_1\dots E.A_n$ of $E$ are **key attributes**.
* This means that $E=\set{\langle v_1,\dots,v_n\rangle|\langle e,v_1\rangle \in E.A_1\land \dots \land \langle e,v_n\rangle \in E.A_n}$
	* The set of **entities** can be represented by the set of values of the **key attributes**.
* These are like the [[SQL Keys|primary key]] in [[SQL Data Manipulation Language (DML)|SQL]].
**Key attributes** are **underlined**.


> [!Example]
> Here, a `person` has a `name`, and is identified by their `salary_number`. They may optionally have a `bonus` figure recorded:
> * ![[Pasted image 20260410125817.png|281]]

When mapping [[ER Modelling|ER]] to a [[relational schema]]:
* Each [[ER Attributes|attribute]] $E.A$ maps to an [[Attributes|attribute]] or **column** $C_A$ of $R_E$.
	* If $A$ is an **optional attribute** then $C_A$ is **nullable**, otherwise $C_A$ is not **nullable**.
	* $\vec{K}$ are **key attributes**, then $\vec{C_K}$ forms a **key** of $R_E$.

> [!Example]
> ![[Pasted image 20260410150230.png|607]]