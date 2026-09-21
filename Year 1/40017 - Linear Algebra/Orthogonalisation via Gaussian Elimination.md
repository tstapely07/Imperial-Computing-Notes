---
date: 2026-04-14
tags:
  - first-year
  - M40017
---
To obtain an [[orthonormal basis]] from a standard [[Basis of a Subspace|basis]], we can also use [[Gaussian elimination]] as an alternative to the [[Gram-Schmidt Process]].

For some **basis** $\set{\vec v_1,\dots,\vec v_k}$, we construct:
$$A = \begin{bmatrix}\vec{v}_1 & \dots  & \vec{v}_k\end{bmatrix}$$
We can then form the **augmented matrix**:
$$\left[\begin{array}{c|c}A^\top A & A^\top\end{array}\right]$$
We now perform **Gaussian elimination**, but only using the $R_i\to R_i+\lambda R_j$ **ERO** until the left side is in **row echelon form**.
* At this point, the rows on the right side of the **augmented matrix** will be the [[orthogonal basis]] [[vectors]], $\set{\vec{d}_1, \dots, \vec{d}_k}$.
* We then normalise each $\vec{d_i}$ to obtain the **orthonormal basis** $\set{\vec c_1,\dots,\vec c_k}$.

> [!Example]
> Let's compute the **orthonormal basis** for these [[Vectors|vectors]] in $\mathbb{R}^3$:
> $$\vec{v}_1 = \begin{bmatrix} 2 \\ 2 \\ 1 \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 0 \\ 3 \\ 3 \end{bmatrix}, \quad \vec{v}_3 = \begin{bmatrix} 1 \\ 1 \\ 5 \end{bmatrix}$$
> We construct $A$, and then $A^\top$, as follows:
> $$A = \begin{bmatrix} 2 & 0 & 1 \\ 2 & 3 & 1 \\ 1 & 3 & 5 \end{bmatrix}, \quad A^\top = \begin{bmatrix} 2 & 2 & 1 \\ 0 & 3 & 3 \\ 1 & 1 & 5 \end{bmatrix}$$
> We also compute $A^\top A$ like this:
> $$A^\top A = \begin{bmatrix} 2 & 2 & 1 \\ 0 & 3 & 3 \\ 1 & 1 & 5 \end{bmatrix} \begin{bmatrix} 2 & 0 & 1 \\ 2 & 3 & 1 \\ 1 & 3 & 5 \end{bmatrix} = \begin{bmatrix} 9 & 9 & 9 \\ 9 & 18 & 18 \\ 9 & 18 & 27 \end{bmatrix}$$
> We can now form our **augmented matrix**:
> $$\left[ \begin{array}{ccc|ccc} 9 & 9 & 9 & 2 & 2 & 1 \\ 9 & 18 & 18 & 0 & 3 & 3 \\ 9 & 18 & 27 & 1 & 1 & 5 \end{array} \right]$$
> We can now do **Gaussian elimination**:
> * First we do $R_2\to R_2-R_1$ and $R_3\to R_3-R_1$ to obtain:
> $$\left[ \begin{array}{ccc|ccc} 9 & 9 & 9 & 2 & 2 & 1 \\ 9 & 18 & 18 & 0 & 3 & 3 \\ 9 & 18 & 27 & 1 & 1 & 5 \end{array} \right]$$
> We then do $R_3\to R_3-R_2$ to get:
> * $$\left[ \begin{array}{ccc|ccc} 9 & 9 & 9 & 2 & 2 & 1 \\ 0 & 9 & 9 & -2 & 1 & 2 \\ 0 & 0 & 9 & 1 & -2 & 2 \end{array} \right]$$
> Now the right hand side gives us our **orthogonal vectors**:
> $$\vec{d}_1 = \begin{bmatrix} 2 \\ 2 \\ 1 \end{bmatrix}, \quad \vec{d}_2 = \begin{bmatrix} -2 \\ 1 \\ 2 \end{bmatrix}, \quad \vec{d}_3 = \begin{bmatrix} 1 \\ -2 \\ 2 \end{bmatrix}$$
> And we can **normalise** to get the **orthonormal basis**:
> $$\left\{ \begin{bmatrix} 2/3 \\ 2/3 \\ 1/3 \end{bmatrix}, \begin{bmatrix} -2/3 \\ 1/3 \\ 2/3 \end{bmatrix}, \begin{bmatrix} 1/3 \\ -2/3 \\ 2/3 \end{bmatrix}\right\}$$