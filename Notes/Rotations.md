---
date: 2026-04-14
tags:
  - first-year
  - M40017
---
In $\mathbb{R}^n$ [[Vector Spaces|space]] with [[standard ordered basis]] $E=(\vec{e_1},\vec{e_2},\dots,\vec{e_n})$, a rotation by $\theta$ **anti-clockwise** in the 
$e_i$-$e_j$ plane is represented by the [[Linear Transformations|transformation]] [[Matrices|matrix]] $R_{ij}(\theta)$ where:
* The $i$-th **column** has $\cos\theta$ in the $i$-th **row** and $\sin\theta$ in the $j$-th **row**.
* The $j$-th **column** has $-\sin\theta$ in the $i$-th **row** and $\cos\theta$ in the $j$-th **row**
* All other entries are $1$ on the **diagonal** and $0$ elsewhere.

A **rotation** in the $x$-$y$ **plane** by $\theta$ **anti-clockwise** is given by the [[Matrices|matrix]]:
$$R_{12}(\theta) = \left[ \begin{array}{ccc} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{array} \right]$$

**Rotation** is **commutative** in the same **2D plane**, but this does not hold for different **planes**:
* $R_{ij}(\theta)R_{ij}(\phi)=R_{ij}(\theta+\phi)=R_{ij}(\phi)R_{ij}(\theta)$
* $R_{ij}(\theta)R_{kl}(\phi)\neq R_{kl}(\phi)R_{ij}(\theta)$

For any **rotation matrix**, the [[Determinant|determinant]] is $1$:
* $\operatorname{Det}(R)=1$
* This means **rotation** preserves **volume**.

The columns of $R$ form an [[orthonormal basis]] of $\mathbb{R}^n$, so we have $RR^\top=R^\top R=I$, and so:
$$R^\top=R^{-1}$$
If a [[Vectors|vector]] $\vec x$ is **stationary**, then $R\vec x = \vec x$, and so to find all **stationary vectors**, we must solve:
$$(R-I)\vec x= \vec 0$$
* For a **rotation matrix**, the **stationary vectors** are the [[Eigenvectors and Eigenvalues|eigenvectors]]. 
* Since $\operatorname{Det}(R)=0$, these all have **eigenvalue** of $1$.
Equivalently, the **axis of rotation** is given by the [[Eigenspaces|eigenspace]] $E_1=\operatorname{Ker}(R-A)$.
* For a typical rotation, we have $\operatorname{dim}(\operatorname{Ker}(R-I)) = n-2$.
* In a **3D space**, the **axis of rotation** is a **line**, whereas in a **4D space** it is a **plane**.