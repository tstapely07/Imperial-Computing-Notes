---
date: 2026-03-10
tags:
  - first-year
  - M40017
---
The **Cayley-Hamilton  Theorem** states that every **square** [[Matrices|matrix]] satisfies its own **characteristic polynomial**.

Consider a **square matrix** $A_{n\times n}$. 
As mentioned when [[Computing Eigenvalues and Eigenspaces|computing eigenvalues]], its **characteristic polynomial** is:
$$p(\lambda)=det(A-\lambda I)=a_0+a_1\lambda+a_2\lambda^2+\dots+a_n\lambda^n$$
We can substitute the matrix $A$ in place of $\lambda$, and this yields the **zero matrix**:
$$p(a)=a_0I+a_1A+a_2A^2+\dots+a_nA^n=0_{n\times n}$$

This allows us to find $A^n$ and $A^{-1}$ in terms of lower powers: $I, A, A^2,\dots,A^{n-1}$.
* In general, for any power $k$, the **matrix** $A^k$ will always be some [[Linear Combination of Vectors|linear combination]] of $I, A,A^2,\dots,A^{n-1}$.

The proof relies on the fact that there exists a sequence of [[Diagonalisation|diagonalisable]] **square matrices**, $A_1, A_2, \dots, A_k,\dots$ that converges to $A$.
* These **matrices** can contain **complex numbers**, so the proof is outside the scope of this course.