---
date: 2026-01-12
tags:
  - first-year
  - M40017
---
An **affine space** is like a [[Vector Subspaces|subspace]], except it does **not** have to pass through the **origin**.

It is equivalent to adding some offset $\overrightarrow{c}\neq\overrightarrow {0}$ to every point in the **subspace**.

Like there is an **equivalence** between the solution set to a **homogenous** [[Systems of Linear Equations|system of linear equations]], a [[Vector Subspaces|subspace]], and the [[Vector Span|span]] of some vectors, there is also an **equivalence** between:
* An **affine space**.
* $\overrightarrow{c}+\operatorname{span}\{\overrightarrow{v_1},\dots,\overrightarrow{v_k}\},\; \overrightarrow{c}\notin\operatorname{span}\{\overrightarrow{v_1},\dots,\overrightarrow{v_k}\}$
* The solution set to a **non-homogenous** [[Systems of Linear Equations|system of linear equations.]]

Be careful when trying to find $\operatorname{dist}(\text{Affine},\overrightarrow{0})$, it is not just $\overrightarrow{c}$.
* Instead, we must find a **normal vector**, and measure that length.
