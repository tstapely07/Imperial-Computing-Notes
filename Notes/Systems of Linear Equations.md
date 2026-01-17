---
date: 2026-01-12
tags:
  - first-year
  - M40017
---
Here is a single **linear equation**:
$$\begin{aligned}&a_{1}x_1 + a_{2}x_2+\dots+a_{n}x_n=b
\\& x\in\mathbb{R}, i\in\mathbb{N}\end{aligned}$$
**$a_i$ - coefficients**
**$x_i$ - variables**
**$b$ - constant - 'free' coefficient**

A **system** of linear equations consists of **multiple** linear equations:
$$\left\{\begin{aligned}
&a_{11}x_1 + a_{12}x_2+\dots+a_{1n}x_n=b_1 \\
&a_{21}x_1 + a_{22}x_2+\dots+a_{2n}x_n=b_2 \\
&\vdots\\
&a_{m1}x_1 + a_{m2}x_2+\dots+a_{mn}x_n=b_m \\
\end{aligned}\right.$$
We could write this more efficiently, using [[Vectors|vectors]]:
$$x_1\begin{bmatrix} a_{11} \\ a_{21} \\ \vdots \\ a_{m1} \end{bmatrix} + 
x_2\begin{bmatrix} a_{12} \\ a_{22} \\ \vdots \\ a_{m2} \end{bmatrix}
+ 
\dots
+ 
x_1\begin{bmatrix} a_{1n} \\ a_{2n} \\ \vdots \\ a_{mn} \end{bmatrix}
= \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_m  \end{bmatrix} $$
Or even better, using a [[Matrices|matrix]]:
$$\begin{bmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ 
 a_{21} & a_{22} & \dots & a_{2n} \\
\vdots  & \vdots  & \ddots & \vdots\\
a_{m1} & a_{m2} & \dots & a_{mn}\end{bmatrix}
\begin{bmatrix}x_1 \\ x_2 \\ \vdots \\ x_n\end{bmatrix}
= \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_m\end{bmatrix}$$
This can then be written shorter, like so:
$$A\overrightarrow{x}=\overrightarrow{b}$$
Where $A$ is an $m\times n$ matrix, $\overrightarrow{x}$  is a $n\times 1$ vector, and $\overrightarrow{b}$ is an $m\times 1$ vector.
This is the way we will represent **systems of linear equations**.
>[!Info]
>In the special case where $\overrightarrow{b}$ is a **0-vector**, i.e.:
>$$\overrightarrow{b} = \overrightarrow{0} = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0\end{bmatrix}$$
>We call the systemm of linear equations **homogenous**. 
>Here, setting $\overrightarrow{x}=\overrightarrow{0}$ will always be a solution.

The **primary objective** of systems of linear equations, **before** all their applications, is to **find their solutions**, so let's work through some examples.
Our general method to solve them will be [[Gaussian Elimination|Guassian elimination]].
>[!Example]
>When $m=n$, such as:
>$3x=4$ , where $m=1$ and $n=1$
>There is a **single unique solution**, in this case $x=\frac{4}{3}$.
>This is true as long as the equations are **linearly independent**.

>[!Example]
>How about when $m=2$, $n=1$, such as:
>$$\left\{\begin{align} 
>&3x=4 \\
>&4x=5 \end{align}\right.$$
>Here there are **no solutions**.
>In general, if $m>n$, and the equations are **linearly independent**, there are no solutions.

>[!Example]
>How about here:
>$$\left\{\begin{align} 
>&3x=4 \\
>&6x=8 \end{align}\right.$$
>Now, although $m>n$, we do have a solution, $x=\frac{4}{3}$
>Here the equations are **linearly dependent**, since they are **scalar multiples** of each other.

>[!Example]
>Consider $x_1+2x_2=3$, i.e. $m=1$, $n=2$.
>Two **trivial solutions** can be found, by setting $x_1=0$, and obtaining $x_2=3/2$, and inversely setting $x_2=0$, and obtaining $x_1=3$
>In the case where $m<n$, and again, the equations are **linearly independent** there are **infinitely many solutions**.
>
>The proof to this is simple, by **contradiction**, since we can **always** obtain **another** solution by taking the **average** of two known solutions, for example, we could obtain a third solution to our example, where $x_1=\frac{3}{2}$ and $x_2=\frac{3}{4}$.
>
>The solutions lie on an $(m-n)$ dimensional [[Affine Space|affine space]] in $\mathbb{R}^n$.

>[!Info]
>To summarise, for a set of **linearly independent equations**:
>* $m = n$ - **one solution**
>* $m > n$ - **no solutions**
>* $m < n$ - **infinitely many solutions**













