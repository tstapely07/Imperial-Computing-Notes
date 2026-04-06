---
date: 2026-01-25
tags:
  - first-year
  - M40017
---
There is a **method** to find the **intersection** of two [[Vector Subspaces|vector subspaces]].

Let $U,V$, be subspaces of $\mathbb{R}^n$ such that:
$$\begin{gather}
U=\operatorname{span}\{\overrightarrow{u_1},\overrightarrow{u_2},\dots,\overrightarrow{u_k}\}\\
V=\operatorname{span}\{\overrightarrow{v_1},\overrightarrow{v_2},\dots,\overrightarrow{v_l}\}
\end{gather}$$
So the [[Dimension|dimension]] of $U$ is $k$, and the **dimension** of $V$ is $l$.
To find $U\cap V$, consider some **arbitrary** $\overrightarrow{x}\in U\cap V$ 
$$\begin{gather}
\overrightarrow{x}=\alpha_1\overrightarrow{u_1}+\dots+\alpha_k\overrightarrow{u_k}=-
\beta_1\overrightarrow{v_1}-\dots-\beta_k\overrightarrow{v_k} \\
\Leftrightarrow \overrightarrow\alpha_1\overrightarrow{u_1}+\dots+\alpha_k\overrightarrow{u_k}+
\beta_1\overrightarrow{v_1}+\dots+\beta_k\overrightarrow{v_k}=\overrightarrow{0} \\
\Leftrightarrow\begin{bmatrix}\overrightarrow{u_1} & \dots & \overrightarrow{u_k}\overrightarrow{v_1} & \dots & \overrightarrow{v_l}\end{bmatrix}
\begin{bmatrix}\alpha_1 \\
\vdots \\
\alpha_k \\
\beta_1 \\
\vdots \\
\beta_l\end{bmatrix}=\overrightarrow{0}
\end{gather}$$
Now we solve the **homogenous** [[Systems of Linear Equations|system of linear equations]] to get the **coefficients** $\alpha_i$s and $\beta_j$s.
We can the substitute these into the definition of $\overrightarrow{x}$ to get $U\cap V$.

> [!Warning]
> This approach only works when $\overrightarrow{u_1},\dots,\overrightarrow{u_k}$ is a [[Basis of a Subspace|basis]] of $U$ and $\overrightarrow{v_1},\dots,\overrightarrow{v_l}$ is a [[Basis of a Subspace|basis]] of $V$.


> [!Note]
> It is always true that:
> $$
> \begin{gather}
> \operatorname{dim}(U)+\operatorname{dim}(V)-\operatorname{dim}(U\cap V)\leq \operatorname{dim}(\mathbb{R}^n)\\
> \text{So}\\
> \operatorname{dim}(U\cap V) \geq \operatorname{dim}(U)+\operatorname{dim}(V)-\operatorname{dim}(\mathbb{R}^n)
> \end{gather}$$
> Additionally:
> $$
> \operatorname{dim}(U\cap V) \leq \operatorname{min}\{\operatorname{dim}(U),\operatorname{dim}(V)\}
> $$
> 
> From here, we have found our **greatest lowest bound** and **least upper bound**.
> For $U,V\underset{subspace}\subseteq\mathbb{R}^n;\;\operatorname{dim}(U)=k,\operatorname{dim}(V)=l$
> $\operatorname{max}\{0,k+l-n\}\leq\operatorname{dim}(U\cap V)\leq\operatorname{min}\{k,l\}$
 
>[!Note]
>We can also note that if $\operatorname{dim}(U\cap V)=\operatorname{dim}(U)$ then $U\underset{subspace}\subseteq V$



Let's do an **example**:
$$\begin{gather}
\text{Compute the intersection } S\cap U\text{ where}\\
U=\operatorname{span}\left\{\begin{bmatrix}1 \\
2 \\
3 \\
4\end{bmatrix},
\begin{bmatrix}5 \\
6 \\
7 \\
8\end{bmatrix},
\begin{bmatrix}4 \\
4 \\
4 \\
4\end{bmatrix}\right\}
\text{ and }
S=\operatorname{span}\left\{\begin{bmatrix}1 \\
-2 \\
1 \\
0\end{bmatrix},
\begin{bmatrix}2 \\
-3 \\
0 \\
1\end{bmatrix}\right\}\\
\text{Let's first find the basis of }S\text{ by building the augmented matrix}\\
\begin{bmatrix}
1 & 5 & 4 \\
2 & 6 & 4 \\
3 & 7 & 4 \\
4 & 8 & 4\end{bmatrix}\\
R_2\rightarrow R_2-2R_1\\
R_3\rightarrow R_3-3R_1\\
R_4\rightarrow R_4-4R_1\\
\begin{bmatrix}
1 & 5 & 4 \\
0 & -4 & -4 \\
0 & -8 & -8 \\
0 & -12 & -12\end{bmatrix}\\
R_3\rightarrow R_3-2R_2\\
R_4\rightarrow R_4-3R_2\\
\begin{bmatrix}
1 & 5 & 4 \\
0 & -4 & -4 \\
0 & 0 & 0 \\
0 & 0 & 0\end{bmatrix}\\
\text{The pivots are in columns 1 and 2, so the basis of }U \text{ is }\\
B_U=\left\{\begin{bmatrix}1 \\
2 \\
3 \\
4\end{bmatrix},
\begin{bmatrix}
5 \\
6 \\
7 \\
8\end{bmatrix}\right\}\\
S\text{ is already a basis, since the vectors are linearly independent}\\
\text{We set up the equation}\\
\alpha_1\begin{bmatrix}1 \\
2 \\
3 \\
4 \\
\end{bmatrix}+\alpha_2\begin{bmatrix}5\\
6 \\
7 \\
8 \\
\end{bmatrix}+\beta_1\begin{bmatrix}1 \\
-2 \\
1 \\
0 \\
\end{bmatrix}+
\beta_2\begin{bmatrix}2 \\
-3 \\
0 \\
1 \\
\end{bmatrix}=\begin{bmatrix}0 \\
0 \\
0 \\
0\end{bmatrix}\\
\text{Now we build and solve the augmented matrix }\\
\left[\begin{array}{cccc|c}1 & 5 & 1 & 2 & 0 \\
2 & 6 & -2 & -3 & 0 \\
3 & 7 & 1 & 0 & 0 \\
4 & 8 & 0 & 1 & 0\end{array}\right]\\
R_2\rightarrow R_2-2R_1\\
R_3\rightarrow R_3-3R_1\\
R_4\rightarrow R_4-4R_1\\
\left[\begin{array}{cccc|c}1 & 5 & 1 & 2 & 0 \\
0 & -4 & -4 & -7 & 0 \\
0 & -8 & -2 & -6 & 0 \\
0 & -12 & -4 & -7 & 0\end{array}\right]\\
R_3\rightarrow R_3-2R_2 \\
R_4\rightarrow R_4-3R_2 \\
\left[\begin{array}{cccc|c}1 & 5 & 1 & 2 & 0 \\
0 & -4 & -4 & -7 & 0 \\
0 & 0 & 6 & 8 & 0 \\
0 & 0 & 8 & 14 & 0\end{array}\right]\\
R_4\rightarrow R_4-\frac{4}{3}R_3\\
\left[\begin{array}{cccc|c}1 & 5 & 1 & 2 & 0 \\
0 & -4 & -4 & -7 & 0 \\
0 & 0 & 6 & 8 & 0 \\
0 & 0 & 0 & \frac{10}{3} & 0\end{array}\right]\\
\text{The only solution to this system is }\alpha_1=\alpha_2=\beta_1=\beta_2=0\\
\text{Substituing this back in to our definition for }\overrightarrow{x} \text{ gives us } \overrightarrow{x}=\overrightarrow{0}\\
\text{So the intersection } S\cap U=\{\overrightarrow{0}\}\\
\text{This means the subspaces only intersect at the origin, and the dimension of their intesection is 0}
\end{gather}$$

And **another example**:
$$\begin{gather}
U=\operatorname{span}\left\{\begin{bmatrix}1 \\
0 \\
0 \\
0\end{bmatrix},
\begin{bmatrix}0 \\
1 \\
0 \\
0\end{bmatrix}\right\},
V=\operatorname{span}\left\{\begin{bmatrix}0 \\
0 \\
1 \\
0\end{bmatrix},
\begin{bmatrix}0 \\
0 \\
0 \\
1\end{bmatrix}\right\}\\
U\text{ and } V\text{ are both a basis, since their vectors are clearly linearly independent}\\
\text{Let's set up the equation, and solve it}
\end{gather}$$
