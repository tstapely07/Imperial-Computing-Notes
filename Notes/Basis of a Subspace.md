---
date: 2026-01-25
tags:
  - first-year
  - M40017
---
> [!Abstract] Definition
> A collection of [[Vectors|vectors]] $V=\{\overrightarrow{v_1},\overrightarrow{v_2},\dots,\overrightarrow{v_k}\}$ is said to be a **basis** of a [[Vector Subspaces|subspace]] $U$ if $U=\operatorname{span}\{\overrightarrow{v_1},\overrightarrow{v_2},\dots,\overrightarrow{v_k}\}$ **and** $\{\overrightarrow{v_1},\overrightarrow{v_2},\dots,\overrightarrow{v_k}\}$ are [[Linear Independence|linearly independent]].

Here, the [[Dimension|dimension]] of $U$ is $k$.

We can use [[Gaussian Elimination|Gaussian elimination]] to find a **basis** of a [[Vector Span|span]] of a collection of [[Vectors|vectors]] $V=\{\overrightarrow{v_1},\overrightarrow{v_2},\dots,\overrightarrow{v_k}\}$.
We start with the **augmented** [[Matrices|matrix]] $\begin{bmatrix}\overrightarrow{v_1} & \overrightarrow{v_2} & \dots & \overrightarrow{v_n}\end{bmatrix}$.
We then use the **EROs** to reach [[Row Echelon Form (REF)|REF]].
If the $i^{th}$ column has a [[Pivot|pivot]] then include $\overrightarrow{v_i}$ in the **basis**, otherwise exclude $\overrightarrow{v_i}$.

For **example**:
$$\begin{gather}
U=\operatorname{span}\left\{\begin{bmatrix}1 \\
2 \\
0 \\
\end{bmatrix},
\begin{bmatrix}2 \\
2 \\
0 \\
\end{bmatrix},
\begin{bmatrix}3 \\
2 \\
0 \\
\end{bmatrix},
\begin{bmatrix}-2 \\
3 \\
0 \\
\end{bmatrix}\right\}\\
\text{Now form an augmented matrix:}\\
\begin{bmatrix}
1 & 2 & 3 & -2  \\
2 & 2 & 2 & 3 \\
0 & 0 & 0 & 0
\end{bmatrix}\\
R_2\rightarrow R_2-2R_1\\
\begin{bmatrix}
1 & 2 & 3 & -2  \\
0 & -2 & 4 & 7 \\
0 & 0 & 0 & 0
\end{bmatrix}\\
\text{The pivots are }1\text{ and } -2 \\
\text{So the basis of } U \text{ is:}
\left\{\begin{bmatrix}1 \\
2 \\
0 \\
\end{bmatrix},
\begin{bmatrix}2 \\
2 \\
0 \\
\end{bmatrix}\right\}
\end{gather}$$

We can also note that the **EROs** produce **linear combinations** of rows. 
This means we can change the basis of a vector space using **EROs** as follows:
$$\begin{gather}
\text{Let } U=\operatorname{span}\{\overrightarrow{v_1},\overrightarrow{v_2},\dots,\overrightarrow{v_k}\}\\
\text{Consider the augmented matrix } \begin{bmatrix}\overrightarrow{v_1}^T \\
\overrightarrow{v_2}^T \\
\vdots \\
\overrightarrow{v_k}^T\end{bmatrix} \\
\text{After some sequence of EROs we obtain }\begin{bmatrix}\overrightarrow{w_1}^T \\
\overrightarrow{w_2}^T \\
\vdots \\
\overrightarrow{w_k}^T\end{bmatrix}\\
\text{Then } U=\operatorname{span}\{\overrightarrow{v_1},\overrightarrow{v_2},\dots,\overrightarrow{v_k}\}=\operatorname{span}\{\overrightarrow{w_1},\overrightarrow{w_2},\dots,\overrightarrow{w_k}\}
\end{gather}$$
We can apply this to the **basis** we found in the previous example:
$$\begin{gather}
\text{Basis} =
\left\{\begin{bmatrix}1 \\
2 \\
0 \\
\end{bmatrix},
\begin{bmatrix}2 \\
2 \\
0 \\
\end{bmatrix}\right\}\\
\text{So we form the matrix:}\\
\begin{bmatrix}
1 & 2 & 0 \\
2 & 2 & 0\end{bmatrix}\\
\\R_2\rightarrow R_2-2R_1\\
\begin{bmatrix}
1 & 2 & 0 \\
0 & -2 & 0\end{bmatrix}\\
R_2\rightarrow-\frac{1}{2}R_2\\
\begin{bmatrix}
1 & 2 & 0 \\
0 & 1 & 0\end{bmatrix}\\
R_1\rightarrow R_1\rightarrow 2R_2\\
\begin{bmatrix}
1 & 0& 0 \\
0 & 1 & 0\end{bmatrix}\\
\text{So the simplified basis is }\left\{\begin{bmatrix}1 \\
0 \\
0 \\
\end{bmatrix},
\begin{bmatrix}0\\
1 \\
0 \\
\end{bmatrix}\right\}\\
\text{This confirms that the subspace }U\text{ is precisely the xy-plane}
\end{gather}$$
