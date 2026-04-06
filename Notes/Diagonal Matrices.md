---
date: 2026-02-20
tags:
  - first-year
  - M40017
---
A **diagonal matrix** is a **square** [[Matrices|matrix]] where all the entries outside the main diagonal are $0$.
$$D=\begin{bmatrix}d_1 & 0 & \dots & 0 \\
0 & d_2 & \dots & 0 \\
\vdots & \vdots & \ddots\ & \vdots \\
0 & 0 & \dots & d_n\end{bmatrix}
$$

Multiplying a **diagonal matrix** $D$ by an arbitrary [[Vectors|vector]] $\vec{x}=\begin{bmatrix}x_1\\x_2\\\dots\\x_n\end{bmatrix}$ simply scales each component $x_i$ by the corresponding diagonal entry $d_i$:
$$D\vec{x}=\begin{bmatrix}d_1x_1\\d_2x_2\\\dots\\d_nx_n\end{bmatrix}$$

Consider an arbitrary **matrix** $A=\begin{bmatrix}a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a{22} & \dots & a_{2n} \\  \vdots & \vdots & \ddots & \vdots \\  a_{n1} & a_{n2} & \dots & a_{nn}\end{bmatrix}$.
Multiplying $A$ by $D$ on the **left** scales the **rows** of $A$.
* The $i^{th}$ row of $A$ is multiplied by $d_i$:
$$DA = \begin{bmatrix} d_1 \cdot \text{Row}_1 \\ d_2 \cdot \text{Row}_2 \\ \vdots \\ d_n \cdot \text{Row}_n \end{bmatrix} = \begin{bmatrix} d_1 a_{11} & d_1 a_{12} & \dots & d_1a_{1n}\\ d_2 a_{21} & d_2 a_{22} & \dots & d_2a_{2n}\\ \vdots & \vdots & \ddots  & \vdots \\
d_na_{n1} & d_na_{n2} & \dots & d_na_{nn}\end{bmatrix}$$
Multiplying $A$ by $D$ on the **right** scales the **columns** of $A$.
* The $j^{th}$ column of $A$ is multiplied by $d_j$.
$$DA = \begin{bmatrix} d_1 \cdot \text{Col}_1 & d_2 \cdot \text{Col}_2 & \dots & d_n \cdot \text{Col}_n \end{bmatrix} = \begin{bmatrix} d_1 a_{11} & d_2 a_{12} & \dots & d_na_{1n}\\ d_1 a_{21} & d_2 a_{22} & \dots & d_na_{2n}\\ \vdots & \vdots & \ddots  & \vdots \\
d_1a_{n1} & d_2a_{n2} & \dots & d_na_{nn}\end{bmatrix}$$

To compute the power $k$ of a **diagonal matrix**, we simply raise each diagonal element to the power $k$:
$$D^k=\begin{bmatrix}d_1^k & 0 & \dots & 0 \\
0 & d_2^k & \dots & 0 \\
\vdots & \vdots & \ddots\ & \vdots \\
0 & 0 & \dots & d_n^k\end{bmatrix}$$

The [[Eigenvectors and Eigenvalues|eigenvectors]] are the [[standard ordered basis]] [[vectors]], $\vec{e_1},\vec{e_2},\dots,\vec{e_n}$.
* The corresponding **eigenvalues** are the diagonal entries $d_1,d_2,\dots,d_n$.

> [!Success]
> **Diagonal matrices** are **easy** to work with!

