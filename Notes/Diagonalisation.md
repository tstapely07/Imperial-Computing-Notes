---
date: 2026-02-24
tags:
  - first-year
  - M40017
---
A square [[Matrices|matrix]] $A_{n\times n}$ is **diagonalisable** if there is some [[basis change|basis change matrix]] $B$ such that $D=B^{-1} A B$ is a [[Diagonal Matrices|diagonal matrix]]:
$$B^{-1}AB=D=\begin{bmatrix}\lambda_1 & 0 & \dots & 0 \\
0 & \lambda_2 & \dots & 0 \\
\vdots & \vdots & \ddots\ & \vdots \\
0 & 0 & \dots & \lambda_n\end{bmatrix}$$
* This is equivalently written as $I_{VE}A_{EE}I_{EV}=A_{VV}$.

A **matrix** is **diagonalisable** iff it has $n$ [[Linear Independence|linearly independent]] [[Eigenvectors and Eigenvalues|eigenvectors]].
* In terms of [[eigenspaces]], this means the sum of the [[Multiplicities of Eigenvalues|geometric multiplicities]] must equal $n$:
$$\sum_{i=1}^k\operatorname{dim}(E_{\lambda_i})=n$$
* This means that if $\operatorname{dim}(E_{\lambda_i})<AM(\lambda_i)$ for any **eigenvalue**, the matrix is **not diagonalisable**.

To diagonalise a matrix $A$, we first find **basis change matrix** $B=I_{EV}$, and the resulting **diagonal matrix** $D=A_{VV}$.
* We first compute the **spectrum** $\{\lambda_1,\lambda_2,\dots,\lambda_n\}$, and find $n$ **linearly independent eigenvectors** $\vec{v_1},\vec{v_2}\dots,\vec{v_2}$.
* We use **eigenvectors**, since they act as the "natural axes" of the **transformation**, turning the **transformation** into a set of independent scaling operations along each axis - the **diagonal matrix**.
* We construct the matrix $B=I_{EV}$ like any other **basis change**, by putting the **basis eigenvectors** as the **columns** of $B$:
$$B=\begin{bmatrix}\vec{v_1} & \vec{v_2} & \dots & \vec{v_n} \end{bmatrix}$$
* Now we can compute the **diagonal matrix** $D$:
$$D=B^{-1}AB=\begin{bmatrix}\lambda_1 & 0 & \dots & 0 \\
0 & \lambda_2 & \dots & 0 \\
\vdots & \vdots & \ddots\ & \vdots \\
0 & 0 & \dots & \lambda_n\end{bmatrix}$$
* Here, each $\lambda_i$ is the **eigenvalue** corresponding to the **eigenvector** $\vec{v_i}$.
	* **Eigenvalues** may repeat if their **eigenspaces** have [[dimension]] $\geq 2$.

We can use **diagonalisation** to compute $A^k$ for any **diagonalisable matrix** $A$.
* Since $D=B^{-1}AB$, we can rearrange this to $A=BDB^{-1}$.
* So now we have:
$$A^k=(BDB^{-1})^k=(BDB^{-1})(BDB^{-1})\dots(BDB^{-1})$$
Note that $B\cdot B^{-1}=I$ and $B^{-1}\cdot B=I$, so internal terms cancel:
$$A^k=BD^kB^{-1}$$

Here's a **worked example**:
To save work, we can follow on from our previous example for [[computing eigenvalues and eigenspaces]].
Here, we found that the matrix:
$$A=\begin{bmatrix} 2&0&4\\0&2&5\\0&0&6\end{bmatrix}$$
Has **eigenvalues** and **eigenspaces** of:
 * $\lambda_1=2:E_2=\operatorname{span}\left\{ \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} \right\}$
* $\lambda_2=6:E_6=\operatorname{span}\left\{\begin{bmatrix}4\\ 5 \\ 4\end{bmatrix}\right\}$
Since we have $3$ [[Linear Independence|independent]] **eigenvectors** for a $3\times 3$ **matrix**, it is indeed diagonalisable.
We construct $B$ by placing the **eigenvectors** as **columns**:
$$B=I_{EV}=\begin{bmatrix} 1 & 0 & 4 \\ 0 & 1 & 5 \\ 0 & 0 & 4 \end{bmatrix}$$
Then the **diagonal matrix** $D$ is found by placing the corresponding **eigenvalues** on the main diagonal:
$$D=B^{-1}AB=\begin{bmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 6 \end{bmatrix}$$

