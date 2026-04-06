---
date: 2026-02-23
tags:
  - first-year
  - M40017
---
Once we have computed the [[Computing Eigenvalues and Eigenspaces|characteristic polynomial]], we can define the **multiplicities** of each [[Eigenvectors and Eigenvalues|eigenvalue]].

**Algebraic multiplicity**:
* For an $n\times n$ [[Matrices|matrix]] $A$, the **characteristic polynomial** can be factorised as:
$$(\lambda-\lambda_1)^{p_1}(\lambda-\lambda_2)^{p_2}\dots(\lambda-\lambda_k)^{p_k}$$
* The exponent $p_i$ is the **algebraic multiplicity** of the **eigenvalue** $\lambda_i$.
* The **sum** of these **multiplicities** must satisfy $p_1+p_2+\dots+p_k=n$, since the **characteristic polynomial** is of **degree** $n$.

**Geometric multiplicity**:
* The dimension of the **eigenspace** $E_{\lambda_i}$ is called the **geometric multiplicity** of the **eigenvalue** $\lambda_i$.

> [!Note]
> The **geometric multiplicity** of an **eigenvalue** is always less than or equal to its **algebraic multiplicity**.
> $$GM\leq AM$$