---
date: 2026-01-12
tags:
  - first-year
  - M40017
---
**Gaussian elimination** is a method of **systematically** finding **all solutions** to a **[[Systems of Linear Equations|system of linear equations]]**.
Let's take this **system of linear equations**:
$$\left\{\begin{align}
&2x_1+3x_2=4 \\ \\
&4x_1+5x_2=6
\end{align}\right.$$
Let's write this in the **compact form** with a **matrix**:
$$
\begin{bmatrix}2 & 3 \\ 4 & 5\end{bmatrix}
\begin{bmatrix}x_1 \\ x_2 \end{bmatrix}
= 
\begin{bmatrix} 4 \\ 6 \end{bmatrix}
$$
We can make some observations of what we can do **without changing** the **solution space**:
* We can **swap** two equations/rows 
	* $R_i \leftrightarrow R_j$
* We can **scale** an equation/row with a $\lambda\in\mathbb{R} \setminus {0}$ 
	* $R_i\rightarrow \lambda R_i$.
* We can **add** equations/rows
	* $R_i \rightarrow R_i+R_j$
>[!Info]
>These are known as the **elementary row operations**.
>**Any combination** of these **EROs** does not change the solution space:
>* If $A\overrightarrow{x}=\overrightarrow{b}\rightarrow EROs\rightarrow C\overrightarrow{x}=\overrightarrow{d}$ then the solutions of $A\overrightarrow{x}=\overrightarrow{b}$ and $C\overrightarrow{x}=\overrightarrow{d}$ are the same.

Using these **EROs** we aim to simplify a matrix to [[Row Echelon Form|row echelon form (REF)]].
We can then go a step further, to [[Reduced Row Echelon Form|reduced row echelon form (RREF)]].

Let's work through an **example** [[Systems of Linear Equations||system of linear equations]]:
$$ \begin{gather}
2x+3y-2z=4 \\
x+3y-3z=4 \\
3x-6y+z=-3
\end{gather}$$
It will be useful to convert the system into the compact matrix notation $A\overrightarrow{x}=\overrightarrow{b}$. There is no need to explicitly mention the $x$ variables, so lets build an **augmented matrix**:
$$\left[
\begin{array}{ccc|c}
2  & 3 & -2 & 4 \\
1 & 3 & -3 & 4 \\
3 & -6 & 1 & -3
\end{array}
\right]
$$
Now let's apply some of the **EROs** to reach [[Row Echelon Form|REF]]:
$$
\begin{gather}
R_1 \leftrightarrow R_2  \\
\left[
\begin{array}{ccc|c}
1 & 3 & -3 & 4 \\
2 & 3 & -2 & 4 \\
3 & -6 & 1 & -3
\end{array}
\right]
\\ \\
R_2\rightarrow R_2 -2R_1 \\
R_3 \rightarrow R_3-3R_1 \\
\left[
\begin{array}{ccc|c}
1 & 3 & -3 & 4 \\
0 & -3 & 4 & -4 \\
0 & -15 & 10 & -15
\end{array}
\right]
\\ \\
R_3 \rightarrow R_3-5R-2 \\
\left[
\begin{array}{ccc|c}
1 & 3 & -3 & 4 \\
0 & -3 & 4 & -4 \\
0 & 0 & -10 & 5
\end{array}
\right]
\end{gather}
$$
**REF** has now been reached. 
Let's go further, to [[Reduced Row Echelon Form|RREF]]:
$$
\begin{gather}
R_3 \rightarrow R_3 \times -\frac{1}{10} \\
\left[
\begin{array}{ccc|c}
1 & 3 & -3 & 4 \\
0 & -3 & 4 & -4 \\
0 & 0 & 1 & -\frac{1}{2}
\end{array}
\right]
\\ \\
R_2 \rightarrow R_2-4R_3 \\
R_1\rightarrow R_1+3R_3 \\
\left[
\begin{array}{ccc|c}
1 & 3 & 0 & \frac{5}{2} \\
0 & 1 & 0 & -2 \\
0 & 0 & 1 & -\frac{1}{2}
\end{array}
\right]
\\ \\
R_1 \rightarrow R_1 -3R_2 \\
\left[
\begin{array}{ccc|c}
1 & 0 & 0 & \frac{1}{2} \\
0 & 1 & 0 & -2 \\
0 & 0 & 1 & -\frac{1}{2}
\end{array}
\right]
\end{gather}
$$
In this case, there is a **unique solution**, since $m=n$, and the equations were **linearly independent**.
We can obtain our solution by simply reading off the final column: 
$$ 
\begin{gather}
x=\frac{1}{2} \\
y = \frac{2}{3} \\
z = -\frac{1}{2}
\end{gather}$$

Let's do **another example**, but with **infinite solutions**:
$$
\begin{gather}
2x-3y +2z = -19 \\
5x-9y+2x=-52 \\
-2x+10y+12z=14 \\

\left[
\begin{array}{ccc|c}
2 & -3 & 2 & -19 \\
5 & -9 & 2 & -52 \\
-2 & 10 & 12 & 40
\end{array}
\right]
\\ \\

R_3\rightarrow R_3\times -\frac{1}{2} \\
R_1\leftrightarrow R_3
\left[
\begin{array}{ccc|c}
1 & -5 & -6 & -20 \\
5 & -9 & 2 & -52 \\
2 & -3 & 2 & -19
\end{array}
\right]
\\ \\

R_2\rightarrow R_2-5R_1 \\
R_3\rightarrow R_3-2R_1 \\
\left[
\begin{array}{ccc|c}
1 & -5 & -6 & -20 \\
0 & 16 & 32 & 48 \\
0 & 7 & 14 & 21
\end{array}
\right]
\\ \\

R_2\rightarrow R_2\times \frac{1}{16} \\
R_3\rightarrow R_3\times \frac{1}{7} \\
\left[
\begin{array}{ccc|c}
1 & -5 & -6 & -20 \\
0 & 1 & 2 & 3 \\
0 & 1 & 2 & 3
\end{array}
\right]
\\ \\

R_3\rightarrow R_3-R_2 \\
\left[
\begin{array}{ccc|c}
1 & -5 & -6 & -20 \\
0 & 1 & 2 & 3 \\
0 & 0 & 0 & 0
\end{array}
\right]
\\ \\

R_1\rightarrow R_1+5R_2 \\
\left[
\begin{array}{ccc|c}
1 & 0 & 4 & -5 \\
0 & 1 & 2 & 3 \\
0 & 0 & 0 & 0
\end{array}
\right]
\end{gather}
$$
Now we are in **RREF**.
The row of $0$ indicates that the equations were **linearly dependent**.
Unlike before, we cannot simply read off our solution, since there are infinite, so lets convert back into equations:
$$
\begin{gather}
x+4z=-5 \\
y+2z=3
\end{gather}
$$
Or better:
$$\begin{gather}
x = -5-4z \\
y = 3-2z \\
z = z
\end{gather}$$$z$ is known as a **free variable**, it can take **any** value.
$x$ and $y$ are **dependent variables**, the value they take depends on the value of **other variables**.
We can know state that the solutions to the **system of equations** is:
$$
\begin{gather}
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
= 
\begin{bmatrix} 
-5  \\
3 \\
0
\end{bmatrix}
+ z
\begin{bmatrix}
-4 \\
-2 \\
1
\end{bmatrix}
\end{gather}
$$
If $\overrightarrow{v_0}=\begin{bmatrix}-5 \\ 3 \\ 0\end{bmatrix}$, and $\overrightarrow{v_1}=\begin{bmatrix}-4 \\ -2 \\ 1\end{bmatrix}$, then we can say that the **solution space** is defined by:
$$
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
=
\overrightarrow{v_0}+\lambda\overrightarrow{v_1} \;, \;\lambda\in\mathbb{R}
$$
We can recognise this an equation for a **line** in a **3D space**.
