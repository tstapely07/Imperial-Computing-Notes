---
date: 2026-01-28
tags:
  - first-year
  - M40017
---
The **intersection** of [[Affine Space|affine spaces]] is obtained using the same technique as the [[Intersection of Vector Subspaces|intersection of vector subspaces]].
$$\begin{gather}
U=\overrightarrow{c_U}+\operatorname{span}\{\overrightarrow{u_1},\overrightarrow{u_2},\dots,\overrightarrow{u_k}\};\overrightarrow{c_U}\notin\operatorname{span}\{\overrightarrow{u_1},\overrightarrow{u_2},\dots,\overrightarrow{u_k}\}\\
V=\overrightarrow{c_V}+\operatorname{span}\{\overrightarrow{v_1},\overrightarrow{v_2},\dots,\overrightarrow{v_l}\};\overrightarrow{c_V}\notin\operatorname{span}\{\overrightarrow{v_1},\overrightarrow{v_2},\dots,\overrightarrow{v_l}\}
\end{gather}$$
To find $U\cap V$, consider an arbitrary $\overrightarrow{x}\in U\cap V$:
$$\begin{gather}
\overrightarrow{x}=\overrightarrow{c_U}+\alpha_1\overrightarrow{u_1}+\dots+\alpha_k\overrightarrow{u_k}=\overrightarrow{c_V}-\beta_1\overrightarrow{v_1}-\dots-\beta_l\overrightarrow{v_l}\\
\iff \alpha_1\overrightarrow{u_1}+\dots+\alpha_k\overrightarrow{u_k}+\beta_1\overrightarrow{v_1}+\dots+\beta_l\overrightarrow{v_l}=\overrightarrow{c_V} - \overrightarrow{c_U}\\
\iff \begin{bmatrix}
\overrightarrow{u_1} & \dots & \overrightarrow{u_k} & \overrightarrow{v_1} & \dots & \overrightarrow{v_l}\end{bmatrix}\begin{bmatrix}\alpha_1 \\
\vdots \\
 \alpha_k \\
\beta_1 \\
\vdots \\
\beta_L\end{bmatrix}=\overrightarrow{c_V}-\overrightarrow{c_U}
\end{gather}$$
We then solve this [[Systems of Linear Equations|system of linear equations]] to get the coefficients $\alpha_i$s and $\beta_j$s.
Substituting these in the definition of $\overrightarrow{x}$ obtains $U\cap V$.

Unlike **vector subspaces**, which were guaranteed to intersect at the **origin**, **affine spaces** do not necessarily intersect.
* This will be indicated by a contradiction while doing [[Gaussian Elimination|Gaussian elimination]] to solve the [[Systems of Linear Equations|system of linear equations]].