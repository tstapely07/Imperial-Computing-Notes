---
date: 2026-01-21
tags:
  - first-year
  - M40017
---
Let $V=\left\{\begin{bmatrix}1 \\ 0 \\ 0 \end{bmatrix},\begin{bmatrix}0 \\ 1 \\ 0 \end{bmatrix}\right\}$.
The [[Vectors|vector]] $s_1=\begin{bmatrix}x \\y \\0\end{bmatrix}$ can be written as $\begin{bmatrix}x \\y \\0\end{bmatrix}=x\begin{bmatrix}1 \\0 \\0\end{bmatrix}+y\begin{bmatrix}0 \\1 \\0\end{bmatrix}$
This means that $s_1$ is **linearly dependent** on $V$. 

The vector $s_2=\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$ cannot be written using any [[Linear Combination of Vectors|linear combination]] of $V$, i.e. $\begin{bmatrix}1 \\ 2 \\ 3\end{bmatrix}\neq \lambda\begin{bmatrix}1 \\0 \\0\end{bmatrix}+\mu\begin{bmatrix}0 \\1 \\0\end{bmatrix}$so $s_2$ is **linearly independent** of $V$. 


Now let's extend this idea to a collection of **linearly independent** vectors:
Let $V=\{\overrightarrow{v_1},\overrightarrow{v_2},\dots,\overrightarrow{v_n}\}$
If $\forall i\;.\;\overrightarrow{v_i}$ is **linearly independent** of $V\setminus\{\overrightarrow{v_i}\}$ then $V$ is a **set of linearly independent vectors**.
But this is **difficult to write**.

Let's say, without **loss of generality**, that $\overrightarrow{v_1}$ is **dependent** on the rest of the **vectors**.
This means that $-\lambda_1\overrightarrow{v_1}=\lambda_2\overrightarrow{v_2}+\lambda_3\overrightarrow{v_3}+\dots+\lambda_n\overrightarrow{v_n}$ such that $\begin{bmatrix}\lambda_1\\\lambda_2\\\vdots\\\lambda_n\end{bmatrix}\neq\overrightarrow{0}$, i.e. at least one coefficient is **non-zero**.

This is equivalent to $\begin{bmatrix}\overrightarrow{v1} & \overrightarrow{v_2} & \dots & \overrightarrow{v_n}\end{bmatrix}\begin{bmatrix}\lambda_1\\\lambda_2\\\vdots\\\lambda_n\end{bmatrix}\neq\overrightarrow{0}$


Conversely, when $\begin{bmatrix}\overrightarrow{v1} & \overrightarrow{v_2} & \dots & \overrightarrow{v_n}\end{bmatrix}\begin{bmatrix}\lambda_1\\\lambda_2\\\vdots\\\lambda_n\end{bmatrix}=\overrightarrow{0}$, we have **linear independence**.
There is a nicer way to write the definition for **linear independence**:
> [!Abstract] Definition
> $\{\overrightarrow{v_1},\overrightarrow{v_2},\dots,\overrightarrow{v_n}\}$ are **linearly independent** if:
> $$(\lambda_1\overrightarrow{v_1}+\lambda_2\overrightarrow{v_2}+\dots+\lambda_n\overrightarrow{v_n}=\overrightarrow{0})\implies(\lambda_1=\lambda_2=\dots=\lambda_n=0)$$


We can check for **linear independence** of a set of [[Vectors|vectors]] by using [[Gaussian Elimination|Gaussian elimination]].
For **vectors** $\{\overrightarrow{v_1},\overrightarrow{v_2},\dots,\overrightarrow{v_n}\}$, we create a [[Matrices|matrix]] by **augmenting** the **vectors**: $\begin{bmatrix}\overrightarrow{v_1}\quad\overrightarrow{v_2}\quad\dots\quad\overrightarrow{v_n}\end{bmatrix}$.
If the [[Row Echelon Form (REF)|REF]] has a column **without** a [[Pivot|pivot]], than the [[Systems of Linear Equations|system of equations]] is **linearly dependent**.
Therefore, if all columns have a **pivot**, then the **system** is **linearly independent**.

For example:
$$\begin{gather}
x_1=\begin{bmatrix}2 \\ -1 \\ 3\end{bmatrix},\;x_2=\begin{bmatrix}1 \\ 1 \\ -2\end{bmatrix},\;x_3=\begin{bmatrix}3 \\ -3 \\ 8\end{bmatrix} \\
V=\begin{bmatrix} 
2 & 1 & 3 \\
-1 & 1 & -3 \\
3 & -2 & 8
\end{bmatrix}\\
R_2\rightarrow R_2+\frac{1}{2}R_1\\
R_3\rightarrow R_3-\frac{3}{2}R_1\\
V=\begin{bmatrix} 
2 & 1 & 3 \\
0 & \frac{3}{2} & -\frac{3}{2} \\
0 & -\frac{7}{2} & \frac{7}{2}
\end{bmatrix}\\
R_3\rightarrow R_3+\frac{7}{3}R_2 \\
V=\begin{bmatrix} 
2 & 1 & 3 \\
0 & \frac{3}{2} & -\frac{3}{2} \\
0 & 0 & 0
\end{bmatrix}\\
\end{gather}$$
The third column has **no pivot**, meaning $V\overrightarrow{\lambda}=\overrightarrow{0}$ has a **non-zero solution**, so the system is **linearly dependent**.
