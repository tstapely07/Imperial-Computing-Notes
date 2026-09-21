---
date: 2026-02-20
tags:
  - first-year
  - M40017
---
The **determinant** of a square [[matrices|matrix]] $A$, $\operatorname{det}(A)$ or $|A|$, has a **geometric** interpretation.
* The [[standard ordered basis]] forms the **edges** of a unit square in $\mathbb{R}^2$, or more generally a **unit** [[Dimension|n-dimensional cube]] in $\mathbb{R}^n$.
* A **matrix** $A$ transforms this **unit n-dimensional cube** to some **n-dimensional parallelopiped** in $\mathbb{R}^n$, where the edges of the **n-dimensional parallelopiped** are the columns of $A$.
* $\operatorname{det}(A)$ is the **signed** **n-dimensional volume** of the **n-dimensional parallelopiped**.

The **volume** is **zero** iff the **parallelopiped** is embedded into a **lower dimension**.
* This means that $\operatorname{det}(A)=0\iff \operatorname{rank}(A)<n$.
* $\iff \operatorname{nullity}(A)>0$
* $\iff$ the columns of $A$ were [[Linear Independence|linearly dependent]].
* $\iff$ $\operatorname{ker}(A)\neq\{\vec{0}\}$.
Likewise , $\operatorname{det}(A)\neq 0$ also has meaning:
* $\operatorname{det}(A)\neq0\iff \operatorname{rank}(A)=n$
* $\iff \operatorname{nullity}(A)=0$
* $\iff$ the columns of $A$ were **linearly independent**.
* $\iff$ $\operatorname{ker}(A)=\{\vec{0}\}$.

To compute the **determinant**, we use [[Gaussian elimination]] to reach [[Row Echelon Form (REF)|REF]], which is an [[Triangular Matrices|upper triangular matrix]].
For any [[Diagonal Matrices|diagonal]] or [[Triangular Matrices|triangular]] **matrix**, the determinant is the **product** of the diagonal entries:
$$\begin{gather}A=\begin{bmatrix}a_1 & b & \dots & c \\
0 & a_2 & \dots & d\\
\vdots & \vdots & \ddots\ & \vdots \\
0 & 0 & \dots & a_n\end{bmatrix}\\
\operatorname{det}(A)=\prod_{i=1}^na_i\end{gather}
$$
Note that applying the **EROs** can change the **determinant**.
Let $A\to_{ERO} B$:
* **Row swap** ($R_i\leftrightarrow R_j$): $\operatorname{det}(B)=-\operatorname{det}(A)$
	* Geometrically, we are simply swapping the axes, so changing the orientation.
* **Row scaling** ($R_i\to\lambda R_i$): $\operatorname{det}(B)=\lambda\operatorname{det}(A)$
	* Geometrically, we are stretching the **parallelopiped** along one axis.
* **Row addition** ($R_i\to R_i + R_j$): $\operatorname{det}(B)=\operatorname{det}(A)$
	* Geometrically, we are shearing the **parallelopiped**, but preserving its volume.
	* Note that the **determinant** also doesn't change for an operation of the form $R_i\to R_i+\lambda R_j$.
Our procedure to calculate $\operatorname{det}(A)$ of some **matrix** $A$ is as follows:
* Reduce $A$ to **REF** using **Gaussian elimination**.
* Multiply the diagonal entries of the **REF**.
* Adjust the result based on the **EROs** performed.

Another method of computing the determinant is the **cofactor method**.
* This is usually slower, especially for larger **matrices**, but can be efficient for **matrices** with lots of $0$ entries.
We break an $n\times n$ **matrix** into a combination of the **determinants** of smaller $(n-1)\times (n-1)$ **matrices**, these are called **minors** ($M_{ij}$).
* $M_{ij}$ is obtained by taking $M$, and removing the $i^{th}$ row and the $j^{th}$ column.
We fix one **row** or **column** to expand along:
* Fix row $i$ and sum across all columns $j$: $\det(A) = \sum\limits_{j=1}^n (-1)^{i+j} a_{ij} \det(M_{ij})$
* Fix column $j$ and sum down all rows $i$: $\det(A) = \sum\limits_{i=1}^n (-1)^{i+j} a_{ij} \det(M_{ij})$
* The $(-1)^{i+j}$ term creates a checkerboard-like pattern of signs: $\begin{bmatrix} +  & - & + & -  & \dots \\ - & + & - & + & \dots \\  +  & - & + & -  & \dots \\ - & + & - & + & \dots \\  \\ \vdots & \vdots & \vdots & \vdots & \ddots\end{bmatrix}$
For example:
$$\begin{gather}\left|\begin{array}{ccc}a & b & c \\
d & e & f \\
g & h & i\end{array}\right|=a\left|\begin{array}{cc}e & f  \\ h & i\end{array}\right| - b\left|\begin{array}{cc}d & f\\g & i\end{array}\right|+c\left|\begin{array}{cc}d & e\\g & h\end{array}\right|
\end{gather}$$

The finally method computing the **determinant** is by using direct rules:
* For a $1\times 1$ **matrix**, $|a|=a$.
* For a $2\times 2$ **matrix**, $\left|\begin{array}{cc}a&b\\c&d\end{array}\right|=ad-bc$
* For a $3\times 3$ **matrix** $A=\left[\begin{array}{ccc}a & b & c \\d & e & f \\g & h & i\end{array}\right]$, we repeat the first two columns to get something like $\left(\begin{array}{ccccc}a & b & c  & a & b\\d & e & f & d & e \\g & h & i & g & h\end{array}\right)$, and then subtract the sum of the upward diagonal products from the sum of the downward diagonal products, to get $\operatorname{det}(A)=(aei+bfg+cdh)-(ceg+afh+bdi)$ ^5ad2e0

