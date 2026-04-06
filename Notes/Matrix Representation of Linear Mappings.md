---
date: 2026-02-10
tags:
  - first-year
  - M40017
---

Any [[Linear Mapping|linear mapping]] $f:\mathbb{R}^n\rightarrow\mathbb{R}^m,\;n,m\neq\infty$, there exists an $m\times n$ **matrix** $A_f$, such that $\forall \overrightarrow{x}\in\mathbb{R}^n,A_f\overrightarrow{x}=f(\overrightarrow{x})$.
To obtain $A_f$, we just need to know what $f$ does to the [[Standard Ordered Basis|standard ordered basis]].
* These form the **columns** of $A_f$.
$$
A_f=\begin{bmatrix}
f\left(\begin{bmatrix}1 \\
0 \\
0 \\
\dots \\
0\end{bmatrix}\right) & f\left(\begin{bmatrix}0 \\
1 \\
0 \\
\dots \\
0\end{bmatrix}\right) & \dots & f\left(\begin{bmatrix}1 \\
0 \\
\dots \\
0 \\
1\end{bmatrix}\right)
\end{bmatrix}
$$
The **proof** goes as follows, where $\overrightarrow{e_i}$ is the $i^{th}$  **vector** of the **standard ordered basis**:
$$\begin{gather}
\overrightarrow{x}\in \mathbb{R}^n\\
\overrightarrow{x}=\begin{bmatrix}x_1\\x_2\\\vdots\\x_n\end{bmatrix}=x_1\overrightarrow{e_1}+x_2\overrightarrow{e_2}+\dots+x_n\overrightarrow{e_n}\\
\overrightarrow{x}=\sum_{i=1}^nx_i\overrightarrow{e_i}\\
\text{Using the above: }\\
g(\overrightarrow{x})= g\left(\sum_{i=1}^n{x_i}\overrightarrow{e_i}\right)\\
= \sum_{i=1}^ng\left({x_i}\overrightarrow{e_i}\right)\text{ since LM preserves vector addition}\\
= \sum_{i=1}^n{x_i}\cdot g\left(\overrightarrow{e_i}\right)\text{ since LM preserves scalar multiplication}\\
= \sum_{i=1}^{n}x_i\overrightarrow{a_i}\\
= \begin{bmatrix}\overrightarrow{a_1} & \overrightarrow{a_2} & \dots & \overrightarrow{a_n}\end{bmatrix}\begin{bmatrix}x_1 \\
x_2 \\
\vdots \\
x_n\end{bmatrix}\\
= A\overrightarrow{x}

\end{gather}$$


Let's do a **worked example**, finding $\operatorname{Im}(A),\operatorname{Ker}(A),\operatorname{Im}(A^T),\operatorname{Ker}(A^T)$:
$$
\text{Let }A = \begin{bmatrix}1 & 2 & 3 & 4  \\
5 & 6 & 7 & 8 \\
9 & 10 & 11 & 13\end{bmatrix}
$$
Now we carry out [[Gaussian Elimination|Gaussian elimination]], to reach [[Reduced Row Echelon Form (RREF)|RREF]]
This is simple, so we will just skip to the **RREF**:
$$A=\begin{bmatrix}
1 & 0 & -1 & 0 \\
0 & 1 & 2 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}$$
Now, by taking the vectors of the columns that correspond to pivots we can find the [[Image|image]] of $A$ to be:
$$span\left\{\begin{bmatrix}1 \\
5 \\
9\end{bmatrix},\begin{bmatrix}2 \\
6 \\
10\end{bmatrix},\begin{bmatrix}4 \\
8 \\
13\end{bmatrix}\right\}$$
This has [[Dimension|dimension]] $3$, so [[Matrix Rank|rank]] $3$.
If we finish solving $A\overrightarrow{x}=\overrightarrow{0}$, we get:
$$\begin{gather}
x_1=x_3\\
x_2=-2x_3\\
x_3=x_3\\
x_4=0
\end{gather}
$$
So the solution set and therefore the [[Kernel|kernel]] is:
$$\lambda\begin{bmatrix}1 \\
-2 \\
1 \\
0\end{bmatrix}$$
Or equivalently:
$$\operatorname{span}\left\{\begin{bmatrix}1 \\
-2 \\
1 \\
0\end{bmatrix}\right\}$$
One **free variable** means [[Matrix Nullity|nullity]] $1$.
Now lets consider the **image** and **kernel** of $A^T$.
Recall that $\operatorname{rank}(M)=\operatorname{rank}(M^T)$, and that the [[Rank Nullity Theorem]] states $\operatorname{Rank}(M)+\operatorname{Nullity}(M)=\text{number of columns in }M$.
Now, we know that $\operatorname{rank}(A^T)=3$ and $\operatorname{nullity}(A_T)=3-3=0$.
Looking at $A_T$:
$$
\begin{bmatrix}
1 & 5 & 9 \\
2 & 6 & 10 \\
3 & 7 & 11 \\
4 & 8 & 13
\end{bmatrix}$$There are $3$ columns, and so the **rank** is just the [[Vector Span|span]] of **all** the columns, that is:
$$
\operatorname{span}\left\{
\begin{bmatrix}1 \\
2 \\
3 \\
4
\end{bmatrix},\begin{bmatrix}5 \\
6 \\
7 \\
8
\end{bmatrix},\begin{bmatrix}9 \\
10 \\
11 \\
13
\end{bmatrix}\right\}
$$There are no free variables, so the solution space, has dimension $0$, meaning the **kernel** is just $\overrightarrow{0}$.

So to **summarise** what we have found:
$$\operatorname{Im}(A)=span\left\{\begin{bmatrix}1 \\
5 \\
9\end{bmatrix},\begin{bmatrix}2 \\
6 \\
10\end{bmatrix},\begin{bmatrix}4 \\
8 \\
13\end{bmatrix}\right\}$$
$$\operatorname{Ker}(A)=\operatorname{span}\left\{\begin{bmatrix}1 \\
-2 \\
1 \\
0\end{bmatrix}\right\}$$
$$\operatorname{Im}(A^T)=\operatorname{span}\left\{
\begin{bmatrix}1 \\
2 \\
3 \\
4
\end{bmatrix},\begin{bmatrix}5 \\
6 \\
7 \\
8
\end{bmatrix},\begin{bmatrix}9 \\
10 \\
11 \\
13
\end{bmatrix}\right\}$$
$$\operatorname{Ker}(A^T)=\overrightarrow{0}$$
