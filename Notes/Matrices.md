---
date: 2026-01-15
tags:
  - first-year
  - M40017
---
**Matrices** are an **ordered collection** of [[Vectors|vectors]].
$$
\begin{bmatrix}
\overrightarrow{a_1}  & \overrightarrow{a_2} & \dots & \overrightarrow{a_n}
\end{bmatrix}
$$
We can think of each **column** as a **mapping** of the standard ordered bases by $A$.
>[!Example]
>$$\overrightarrow{a_1}=f_A\left(\begin{bmatrix}1 \\ 0 \\ \dots \\ 0\end{bmatrix}\right),\dots,\overrightarrow{a_n}=f_A\left(\begin{bmatrix}0 \\ \dots \\ 0 \\ 1\end{bmatrix}\right)$$



We can also think of a **matrix** as a [[Functions|function]] $f_A:\mathbb{R}^n\rightarrow\mathbb{R}^m$, such that $f_A(\overrightarrow{x})=A\overrightarrow{x}$.
As a function, a **matrix** **maps** all the **vectors** in the $\mathbb{R}^n$ space to the $\mathbb{R}^m$ space.

**Matrix multiplication** is simply the **composition** of the underlying functions:
$$AB\cong f_A \circ f_B$$
This properties of **matrix multiplication** therefore stem from the properties of **composition of functions**.
* $(AB)C=A(BC)$, since $(f\circ g)\circ h=f\circ(g\circ h)$
* $AB\not=BA$, since $f\circ g \not=g\circ f$
* $IA=AI=A$, since $1\times x=x\times 1=x$
* 

The [[Inverse of a Matrix|inverse of a matrix]], $A^{-1}$ is then the matrix which represents the inverse of the function $f_A$.
As for all functions, the inverse exists if $f_A$ is a bijection.