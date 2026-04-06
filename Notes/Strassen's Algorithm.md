---
date: 2026-03-03
tags:
  - first-year
  - M40008
---
The standard way to multiply two $n\times n$ [[matrices]] is as follows:
$$\begin{gather} AB=C\\ \begin{bmatrix}a_{11} & a_{12}\\a_{21} & a_{22}\end{bmatrix}\begin{bmatrix}b_{11} & b_{12}\\b_{21} & b_{22}\end{bmatrix}=\begin{bmatrix}a_{11}b_{11}+a_{12}b_{21} & a_{11}b_{12}+a_{12}b_{22}\\a_{21}b_{11}+a_{22}b_{21} & a_{21}b_{12}+a_{22}b_{22}\end{bmatrix} \end{gather}$$
* This takes 8 multiplications, and 4 additions.

**Strassen** found a way to multiply two $2\times 2$ **matrices** in only 7 multiplications.
* This does require 18 additions, but since these are much less computationally expensive than multiplications, we can ignore them.
$$C=\begin{bmatrix}x_1+x_4-x_5+x_7 & x_3+x_5  \\
x_2+x_4 & x_1+x_3-x_2+x_6\end{bmatrix}$$
* Where:
	* $x_1=(a_{11}+a_{22})\cdot(b_{11}+b_{22})$
	* $x_2=(a_{21}+a_{22})\cdot b_{11}$
	* $x_3=a_{11}\cdot (b_{12}-b_{22})$
	* $x_4=a_{22}\cdot (b_{21}-b_{11})$
	* $x_5=(a_{11}+a_{12})\cdot b_{22}$
	* $x_6=(a_{21}-a_{11})\cdot (b_{11}+b_{12})$
	* $x_7=(a_{12}-a_{22})\cdot (b_{21}+b_{22})$

Crucially, **Strassen's** formulas do not rely on the commutativity of multiplication.
* This means that we can generalise to **matrices**.

Suppose that $n=2^k$.
Divide up the **matrices** into four quadrants, each $\frac{n}{2}\times \frac{n}{2}$:
$$\begin{bmatrix}A_{11} & A_{12}\\A_{21} & A_{22}\end{bmatrix}\begin{bmatrix}B_{11} & B_{12}\\B_{21} & B_{22}\end{bmatrix}=\begin{bmatrix}C_{11} & C_{12}\\C_{21} & C_{22}\end{bmatrix}$$
* Now we recursively compute each $C_{ij}$ by further subdividing the matrices, until we reach the base case of $n=2$.
* If $n$ is not a power of 2 ($n\neq 2^k$), then we can simply add extra rows and columns of 0s to allow for perfect subdivision.
	* The desired result is obtained by stripping off these rows and columns at the end.

At each recursive step of **Strassen's** algorithm, we need to add/subtract $18$ **matrices** of dimension $\frac{n}{2}\times \frac{n}{2}$ and recursively perform $7$ multiplications of $\frac{n}{2}\times \frac{n}{2}$ **matrices**.
* The number of arithmetic operations $A(k)$ for $n=2^k$ is therefore given by the recurrence relation:
	* $A(0)=1$
	* $A(k)=7A(k-1)+18(\frac{n}{2})^2$
* We can solve this by repeated expansion, and then summing the resulting geometric progression, to obtain:
	* $A(k)=7\cdot 7^k-6\cdot 4^k$
	* $=7\cdot 7^{\log_2 n}-6n^2$
	* $=7\cdot n^{\log_2 7}-6n^2$
	* $\approx7\cdot n^{2.807}-6n^2$
Since the highest power dominates, **Strassen's** matrix multiplication algorithm is exactly $\Theta(n^{\log_2 7})$.

