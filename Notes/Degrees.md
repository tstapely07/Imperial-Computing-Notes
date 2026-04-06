---
date: 2026-01-16
tags:
  - first-year
  - M40008
---

> [!Abstract] Definition
> The **degree** of a [[Nodes|node]] is the number of [[Arcs|arcs]] **incident** on it - i.e. the number of **arcs** which have that **node** as an endpoint.

Each arc contributes **twice** to then total of all the degrees - once for each endpoint.
* ![[Pasted image 20260116120055.png|400]]
* This means that here, $C$ has degree $3$.

>[!Theorem]
>The **sum** of the **degrees** of all the **nodes** of a [[Graphs|graph]] is **twice** the number of **arcs**, and therefore **even**.
>
>The number of **nodes** with **odd degree** is even:
>* This can be shown by **contradiction**, if it was **odd**, then the **sum** would be **odd** - a **contradiction**.

In a [[Directed Graphs|directed graph]], we must split the **degrees** of  **node** into the **indegrees** and **outdegrees**.

> [!Abstract] Definition
> The **indegree** of a **node** $x$ is the number of **arcs** entering $x$.

> [!Abstract] Definition
> The **outdegree** of a **node** $x$ is the number of **arcs** leaving $x$.
