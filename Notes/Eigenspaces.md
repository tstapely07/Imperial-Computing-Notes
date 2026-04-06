---
date: 2026-02-22
tags:
  - first-year
  - M40017
---
The set of all [[Eigenvectors and Eigenvalues|eigenvectors]] corresponding to a fixed [[Eigenvectors and Eigenvalues|eigenvalue]] $\lambda_0$ form a  [[Vector Subspaces|vector subspace]] of $\mathbb{R}^n$ called the **eigenspace**, $E_{\lambda_0}$.
The proof for **eigenspace** being a **subspace** is as follows:
* Proof of closure under **scalar multiplication**:
	* If $\vec{x}$ is an **eigenvector** ($A\vec{x}=\lambda_0\vec{x}$), and $\alpha$ is a scalar:
	* $A(\alpha\vec{x})$=$\alpha(A\vec{x})$ - [[Linear Transformations|linearity]] of **matrix multiplication**.
	* $=\alpha(\lambda_0\vec{x})$ - definition of **eigenvector**.
	* $=\lambda_0(\alpha\vec{x})$ - **commutativity** of scalars.
	* Since $A(\alpha\vec{x})=\lambda_0(\alpha\vec{x})$, the scaled vector is also in the **eigenspace**.
* Proof of closure under **vector addition**:
	* If $x,y\in E_{\lambda_0}$.
	* $A(\vec{x}+\vec{y})=A\vec{x}+A\vec{y}$ - **linearity** of **matrix multiplication**.
	* $=\lambda_0\vec{x}+\lambda_0\vec{y}$ - definition of **eigenvectors**.
	* $=\lambda_0(\vec{x}+\vec{y})$ - factorising.
	* Since $A(\vec{x}+\vec{y})=\lambda_0(\vec{x}+\vec{y})$, the **vector sum** is also in the **eigen space**.

> [!Note]
> See also - [[Computing Eigenvalues and Eigenspaces]]
