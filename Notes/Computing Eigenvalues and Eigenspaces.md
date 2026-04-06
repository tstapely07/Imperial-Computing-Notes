---
date: 2026-02-22
tags:
  - first-year
  - M40017
---
To find the [[Eigenvectors and Eigenvalues|eigenvalues]] and [[eigenspaces]] of some **square** [[Matrices|matrix]] $A_{n\times n}$, we must solve $A\vec{x}=\lambda\vec{x}$ for some non-zero [[Vectors|vector]] $\vec{x}$.
We can rewrite the equation as:
$$A\vec{x}-\lambda\vec{x}=\vec{0}$$
And then factor out $\vec{x}$ to get:
$$(A-\lambda I)\vec{x}=\vec{0}$$

We are looking for non-zero solutions for $\vec{x}$.
* Since $\vec{0}$ would be a **trivial solution**, satisfying the equation for every possible $\lambda$, which would mean every real number is an **eigenvalue**, which would make the concept meaningless.
If the **matrix** $(A-\lambda I)$ was invertible, the only solution would be $\vec{x}=\vec{0}$.
* So we need the [[Determinant|determinant]] to be $0$, that is, $\operatorname{det}(A-\lambda I)=0$.

The expression $\operatorname{det}(A-\lambda I)$ is a **polynomial** in $\lambda$ of degree $n$, and is known as the **characteristic polynomial**.
* The roots of this polynomial are the **eigenvalues**, since they are where the **determinant** is $0$.
For example, if $A$ is a $2\times 2$ **matrix**:
* $A=\begin{bmatrix} a&c\\b&d\end{bmatrix}$
* $\operatorname{det}(A-\lambda I)=\operatorname{det}\begin{bmatrix}a-\lambda&c\\b&d-\lambda\end{bmatrix}$
* $\operatorname{det}(A-\lambda I)=(ad-bc)-(a+d)\lambda+\lambda^2$
* So the roots are $\frac{(a+d)\pm\sqrt{(a+d)^2-4(ad-bc)}}{2}$

For each **eigenvalue** root $\lambda_i$ we find, we substitute it back into the equation:
$$(A-\lambda_i I)\vec{x}=\vec{0}$$
Now we solve this **homogenous** [[Systems of Linear Equations|system of linear equations]].
* The solution set is the **eigenspace** $E_{\lambda_i}$.


Let's do a **worked example**:
$$A=\begin{bmatrix} 2&0&4\\0&2&5\\0&0&6\end{bmatrix}$$
We need to compute $\operatorname{det}(A-\lambda I)$:
$$\operatorname{det}(A-\lambda I)=\operatorname{det}\begin{bmatrix} 2-\lambda&0&4\\0&2-\lambda&5\\0&0&6-\lambda\end{bmatrix}$$
We can use the [[Determinant#^5ad2e0|direct rule]] for a $3\times 3$ **matrix**:
$$\operatorname{det}(A-\lambda I)=((2-\lambda)(2-\lambda)(6-\lambda)+0+0)-(0+0+0)$$
$$\operatorname{det}(A-\lambda I) = (2-\lambda)^2(6-\lambda)$$
This is already factorised, so the roots to $\operatorname{det}(A-\lambda I)=0$, and therefore the **eigenvalues** are $2$ and $6$. 
* Note how that $2$ has [[Multiplicities of Eigenvalues|algebraic multiplicity]] $2$, and $6$ has **algebraic multiplicity** $1$.
Now we must substitute each root back into the equation $(A-\lambda_i I)\vec{x}=\vec{0}$, to find its **eigenspace**:
$$\begin{gather}
(A-2I)\vec{x}=\vec{0}\\
\begin{bmatrix} 2-2&0&4\\0&2-2&5\\0&0&6-2\end{bmatrix}\vec{x}=\vec{0}\\
\left[\begin{array}{ccc|c}0 & 0 & 4 & 0 \\
0 & 0 & 5 & 0 \\
0 & 0 & 4 & 0
\end{array}\right]\\
\sim \left[\begin{array}{ccc|c}0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{array}\right]
\end{gather}$$
So $x_1=x_1$,$x_2=x_2$ and $x_3=0$
So the solution set = $\operatorname{span}\left\{ \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} \right\}$
So our two **eigenvectors** are $\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$ and $\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$.
And again, substituting $6$:
$$\begin{gather}
(A-6I)\vec{x}=\vec{0}\\
\begin{bmatrix} 2-6&0&4\\0&2-6&5\\0&0&6-6\end{bmatrix}\vec{x}=\vec{0}\\
\left[\begin{array}{ccc|c}-4 & 0 & 4 & 0 \\
0 & -4 & 5 & 0 \\
0 & 0 & 0 & 0
\end{array}\right]\\
\sim \left[\begin{array}{ccc|c}1 & 0 & -1 & 0 \\
0 & 1 & -\frac{5}{4} & 0 \\
0 & 0 & 0 & 0
\end{array}\right]
\end{gather}$$
So $x_1=x_3$, $x_2=\frac{5}{4} x_3$, $x_3=x_3$
So the solution set = $\operatorname{span}\left\{\begin{bmatrix}1\\ \frac{5}{4} \\ 1\end{bmatrix}\right\}$ = $\operatorname{span}\left\{\begin{bmatrix}4\\ 5 \\ 4\end{bmatrix}\right\}$

So to conclude, the **eigenvalues** and their respective **eigenspaces** are:
* $\lambda_1=2:E_2=\operatorname{span}\left\{ \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} \right\}$
* $\lambda_2=6:E_6=\operatorname{span}\left\{\begin{bmatrix}4\\ 5 \\ 4\end{bmatrix}\right\}$
And the **eigenvectors** are:
$\vec{v_1}=\begin{bmatrix}1\\0\\0\end{bmatrix},\vec{v_2}=\begin{bmatrix}0\\1\\0\end{bmatrix},\vec{v_3}=\begin{bmatrix}4\\5\\4\end{bmatrix}$
With this information we can visualise how this **matrix** transforms the **domain** by stretching the $xy$-plane uniformly by a factor of $2$, while stretching space along the direction of $\vec{v_3}$ by a factor of $6$.