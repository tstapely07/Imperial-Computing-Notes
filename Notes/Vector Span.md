---
date: 2026-01-21
tags:
  - first-year
  - M40017
---
> [!Abstract]  Definition
> The **span** of a set of [[Vectors|vectors]] $V=\{\overrightarrow{v_1},\overrightarrow{v_2},\dots,\overrightarrow{v_n}\}$ is the set of **all possible** [[Linear Combination of Vectors|linear combinations]] of $V$.

For **example**:
$\operatorname{span}\left\{\begin{bmatrix}1 \\ 0 \\ 0 \end{bmatrix},\begin{bmatrix} 0 \\ 1 \\0 \end{bmatrix}\right\}$ would be the $x,y$ plane. It is also a [[Vector Subspaces|subspace]] of $\mathbb{R}^3$. 
Interestingly, $\operatorname{span}\left\{\begin{bmatrix}1 \\ 1 \\ 0 \end{bmatrix},\begin{bmatrix} -1 \\ 1 \\0 \end{bmatrix}\right\}$ would be the **same subspace**. This ties into [[Linear Independence|linear independence]].


$\operatorname{span} \left\{\overrightarrow{v_1},\overrightarrow{v_2},\dots,\overrightarrow{v_n}\right\}$, where each $\overrightarrow{v_i}\in\mathbb{R}^n$, is a [[Vector Subspaces|subspace]] of the $\mathbb{R}^n$ [[Vector Spaces|vector space]] - so every **span** is a **subspace**.
For example, $\operatorname{span}\left\{\begin{bmatrix}1 \\ 1 \\ 0 \end{bmatrix},\begin{bmatrix} -1 \\ 1 \\0 \end{bmatrix}\right\}$ is equivalent to the **subspace** $S=\left\{\begin{bmatrix}x \\ y \\ z \end{bmatrix}\in \mathbb{R}^3 \;\bigg| \; z = 0\right\}$


Likewise, there is an **algorithm** to go from some **subspace** $S$ to the span of a set of [[Vectors|vectors]]:
* We start with an empty set of vectors, $V=\emptyset$
* Now we look at $S$. Is there a **vector** in $S$ that is **not** covered by the **span** of $V$?
* If there is, then we add that **vector** to $V$.
* We repeat this **iteratively**.
* **Stop** when the **span** of $V$ equals $S$.

Finally, we can construct a [[Matrices|matrix]] $A$ such that $A\overrightarrow{v_1}=\overrightarrow{0},A\overrightarrow{v_2}=\overrightarrow{0},\dots,A\overrightarrow{v_n}=\overrightarrow{0}$
This means our **subspace**, which is equivalent to the **span** of a set of **vectors**, is also equivalent to the set of solutions to the [[Systems of Linear Equations|equation]] $A\overrightarrow{x}=\overrightarrow{0}$.



