---
date: 2026-04-05
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> A **key** of a [[Relations|relation]] $R(AB\dots)$  is  **subset** of the [[attributes]] for which the values in any **extent** are unique across all tuples.

Every **relation** has at least one key, the **set** of all the **attributes**.
A key is **violated**, if there are two **tuples** in the **extent** with the same values for the **attributes** that make up the **key**.
If $A$ is a **key**, then $AB$ must also be a **key**.

> [!Abstract] Definition
> A **minimal key** is a **set** of **attributes** $AB\dots$ for which no **subset** of the **attributes** is also a **key**.

> [!Abstract] Definition
> The **primary key** is one of the **keys** of the **relation**.
> * It serves as the default key, when no other key is explicitly stated.

