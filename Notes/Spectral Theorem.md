---
date: 2026-04-14
tags:
  - first-year
  - M40017
---
For a standard **square** [[Diagonalisation|diagonalisable]] [[Matrices|matrix]] $M$, we can write:
$$M=BDB^{-1}$$
* Here $B$ is made up of the [[Eigenvectors and Eigenvalues|eigenvectors]], and $D$ holds the corresponding **eigenvalues** along the diagonal.

The **spectral theorem** states that if a **matrix** $C$ is **symmetric**, i.e. $C^\top=C$, then we get the benefit that the **eigenvalues** of $D$ are **real**.
* Additionally, the **eigenvectors** that make up the **columns** of $B$ are [[Orthonormal Basis|orthonormal]] to each other, which means that $B^{-1}=B^\top$.
* This is because $B^\top B=I$, since the [[inner product]] of two **orthonormal** [[vectors]] is $0$, unless they are the same **vector**, in which case it is $1$.
Therefore we can **diagonalise** $C$ as:
$$C=QDQ^{\top}$$

The proof that all **eigenvalues** are **real** is as follows.
First note that if $a+ib$ is an **eigenvalue**, then so is $a-ib$.
* Also if $\vec d + i\vec f$ is an **eigenvector** corresponding to the **eigenvalue** $a+ib$, then $\vec d - i \vec f$ is also an **eigenvector**, but corresponding to **eigenvalue** $a-ib$.
Let $a+ib$ be an **eigenvalue**, with $\vec d + i \vec f$ as the corresponding **eigenvector**.
So we have:
$$C(\vec d+i \vec f)=(a+ib)(\vec d + i\vec f)\quad \text{and}\quad C(\vec d-i \vec f)=(a-ib)(\vec d - i\vec f)$$
We can form two equations by multiplying each equation by the **conjugate eigenvector** on both sides:
1. $(\vec d - i\vec f)^\top C(\vec d + i \vec f)=(a+ib)(|\vec d|^2+|\vec f|^2)$
2. $(\vec d + i\vec f)^\top C(\vec d - i \vec f)=(a-ib)(|\vec d|^2+|\vec f|^2)$
Now, we take the **transpose** of the first equation, yielding:
$$\left((\vec d - i\vec f)^\top C(\vec d + i \vec f)\right)^\top=(\vec d + i\vec f)^\top C^\top(\vec d - i \vec f)$$
* Note that in general, $(XYZ)^\top=Z^\top Y^\top X^\top$
And now we notice that, since $C^\top=C$, we actually have:
$$\left((\vec d - i\vec f)^\top C(\vec d + i \vec f)\right)^\top=(\vec d + i\vec f)^\top C(\vec d - i \vec f)$$
So by **transposing** the left side of the first equation, we reached the second equation.
* These are both **scalars**, so the **transpose** didn't change the value of the **first equation**.
This means that:
$$(\vec d - i\vec f)^\top C(\vec d + i \vec f)=(\vec d + i\vec f)^\top C(\vec d - i \vec f)$$
But more interestingly, the right hand sides of the equations must also be equal, giving:
$$(a+ib)(|\vec d|^2+|\vec f|^2)=(a-ib)(|\vec d|^2+|\vec f|^2)$$
So $(a+ib)=(a-ib)$. 
* This enforces $b=0$.
Therefore the **eigenvalues** have no **complex component** and are indeed **real**.

We can also prove that for **distinct eigenvalues** $\lambda_1\neq \lambda_2$, the **corresponding eigenvectors** are **perpendicular** using a similar approach.
We start with $C\vec{v}_{\lambda_1} = \lambda_1\vec{v}_{\lambda_1}$, and then multiply both sides by the **transpose** of the second **eigenvector** $(\vec{v}_{\lambda_2})^\top$.
With some simplification, we reach:
$$(\vec{v}_{\lambda_2})^\top C(\vec{v}_{\lambda_1})=\lambda_1(\vec{v}_{\lambda_1}\cdot \vec{v}_{\lambda_2})$$
Of course, the same holds if we swap $\lambda_1$ and $\lambda_2$, giving a second equation:
$$(\vec{v}_{\lambda_1})^\top C(\vec{v}_{\lambda_2})=\lambda_2(\vec{v}_{\lambda_1}\cdot \vec{v}_{\lambda_2})$$
By taking the **transpose** and using the **symmetry** of $C$, we can reach:
$$\left( (\vec{v}_{\lambda_2})^\top C(\vec{v}_{\lambda_1}) \right)^\top = (\vec{v}_{\lambda_1})^\top C^\top \vec{v}_{\lambda_2} = (\vec{v}_{\lambda_1})^\top C \vec{v}_{\lambda_2}$$
And since the left sides of the two equations are equal, so are the right sides, and we have:
$$\lambda_1(\vec{v}_{\lambda_1}\cdot \vec{v}_{\lambda_2})=\lambda_2(\vec{v}_{\lambda_1}\cdot \vec{v}_{\lambda_2})$$
Since $\lambda_1\neq\lambda_2$, we must have:
$$\vec{v}_{\lambda_1}\cdot \vec{v}_{\lambda_2}=0$$
And so we have indeed shown the **eigenvectors** to be **perpendicular**.

Finally we could show that the [[Multiplicities of Eigenvalues|geometric multiplicity]] is the same as the **algebraic multiplicity** for each **eigenvalue**, to confirm that $C$ is **diagonalisable**.
* This proof is omitted for brevity, but it is done by **induction**, and using the [[Gram-Schmidt Process]].