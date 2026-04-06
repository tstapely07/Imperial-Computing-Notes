---
date: 2026-01-21
tags:
  - first-year
  - M40017
---
A **vector space** is a **4-tuple** $(V,\oplus,\otimes,\overrightarrow{0})$, where:
* $V$ is a **set**.
* If $\overrightarrow{x},\;\overrightarrow{y}\in V$ then $\overrightarrow{x}\oplus\overrightarrow{y}\in V$ - **closed under vector addition**.
* If $\lambda\in \mathbb{R},\;\overrightarrow{x}\in V$ then $\lambda \otimes \overrightarrow{x}\in V$ - **closed under scalar multiplication**. 
* $\overrightarrow{0} \in V$ such that $\overrightarrow{0}\oplus\overrightarrow{x}=\overrightarrow{x}\oplus\overrightarrow{0}=\overrightarrow{x}$ - **additive identity**.

>[!Info]
>The **Euclidean space** $(\mathbb{R}^n,+,\times,\overrightarrow{0})$ is an obvious example of a **vector space**.


Let's look at some other examples of **vector spaces**:
$$(\mathbb{R}^+,\times,exp,1)$$
Let's prove that this is a **vector space**:
$$\begin{gather}
x,y\in\mathbb{R}^+\\\\
x\oplus y = x\times y \\
x\times y\in\mathbb{R}^+\text{ so closed under vector addition} \\\\
\lambda\otimes x = x^\lambda\\
\text{a positive number to any power is} \\\text{positive, so closed under scalar multiplication} \\
x\times 1 = 1\times x = 1 \text{ so satisfies additive identity} \\
\\\text{so we have a valid vector space}
\end{gather}$$

Here's another:
$P = \{a_0+a_1x+a_2x^2+\dots+a_nx^n\;|\;\forall i.a_i\in\mathbb{R},n\in\mathbb{Z}^+\}$ is the set of **all polynomials** of **any degree**.
$(P,+,\times,0)$ is a **vector space**.
* $\operatorname{dim}(P)=\infty$, this can be proved by **contradiction**.
* Assume $\operatorname{dim}(P)=l$, where $l$ is **finite**. We can then create $l+1$ [[Linear Independence|linearly indepedent]] **polynomials**, which is a **contradiction**.

> [!Note]
> See also [[Vector Subspaces]]

