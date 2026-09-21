---
date: 2026-04-14
tags:
  - first-year
  - M40017
---
> [!Abstract] Definition
> A [[Matrices|matrix]] $M$ is **column-stochastic** if:
> * Every single entry is **non-negative** - $a_{ij}\ge 0$.
> * The **sum** of the entries in every **column** is exactly $1$ - $\forall j\;\;\sum_{i}a_{ij}=1$.

Any **column-stochastic matrix** $M$ will have $1$ as an [[Eigenvectors and Eigenvalues|eigenvalue]].
* Note that **transposing** a **matrix** does not change its [[determinant]].
* Hence the **eigenvalues** of $M$ and $M^T$ are the **same**:
$$\operatorname{det}(M-\lambda I)=\operatorname{det}(M^\top-\lambda I)$$
Since $M$ is **column-stochastic**, we have $M^\top \vec1=\vec1$.
* Therefore $1$ is an **eigenvalue** of $M^\top$, and so $1$ is an **eigenvalue** of $M$.