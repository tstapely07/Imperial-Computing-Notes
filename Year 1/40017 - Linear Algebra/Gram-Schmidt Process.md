---
date: 2026-03-11
tags:
  - first-year
  - M40017
---
The **Gran-Schmidt process** is an iterative algorithm used to convert any standard basis $\set{\vec{v_1},\vec{v_2},\dots,\vec{v_k}}$ into an [[orthonormal basis]] $\set{\vec{c_1},\vec{c_2},\dots,\vec{c_k}}$.

For the first [[Vectors|vector]], we **normalise** it, by dividing by its magnitude, to obtain the first **unit vector**:
$$\vec{c_1}=\frac{\vec{v_1}}{|\vec{v_1}|}$$

For any subsequent vector $i$, we must first separate it from the [[Vector Subspaces|subspace]] [[Vector Span|spanned]] by all the previously established **orthonormal vectors** ($\operatorname{span}\set{\vec{c_1},\dots,\vec{c_{i-1}}}$), to find the component of the **vector** in the **direction** **perpendicular** to all the other **vectors**.
* We do this by first computing its **component** in the same direction of each existing **vector**, its **projection**, and then subtracting this. 
Its **projection** is given by the following formula:
$$\vec{p}_i = \begin{bmatrix} \vec{c}_1 &  \dots & \vec{c}_{i-1} \end{bmatrix} \begin{bmatrix} \vec{c}_1 \cdot \vec{v}_i  \\ \vdots \\ \vec{c}_{i-1} \cdot \vec{v}_i \end{bmatrix} = (\vec{c}_1 \cdot \vec{v}_i)\vec{c}_1  + \dots + (\vec{c}_{i-1} \cdot \vec{v}_i)\vec{c}_{i-1}$$
* Note that this is equivalent to the standard [[Orthogonal Projection Matrix|projection matrix]], $P_U=C(C^\top C)^{-1}C^\top$, but with the simplification that, since the **vectors** are all **orthonormal**, we have $C^\top C=I$, and so $P_U\vec v_i=CC^\top\vec v_i$. 
The same formula in **sum notation** is:
$$p_i=\sum_{j=1}^{i-1}(\vec{v_i}\cdot \vec{c_j})\vec{c_j}$$
We then subtract this **projection** from the original **vector**:
$$\vec{o_i}=\vec{v_i}-\vec{p_i}$$
And finally we **normalise**:
$$\vec{c_i}=\frac{\vec{o_i}}{|\vec{o_i}|}$$

> [!Example]
> Let's find an **orthonormal basis** for these three **vectors** in $\mathbb{R}^3$:
> $$\vec{v}_1 = \begin{bmatrix} 2 \\ 2 \\ 1 \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 0 \\ 3 \\ 3 \end{bmatrix}, \quad \vec{v}_3 = \begin{bmatrix} 1 \\ 1 \\ 5 \end{bmatrix}$$
> We can find $|v_1|=\sqrt{2^2+2^2+1^2}=\sqrt{9}=3$, and so:
> $$\vec{c}_1 = \frac{\vec{v}_1}{|\vec{v}_1|} = \begin{bmatrix} \frac{2}{3} \\ \frac{2}{3}\\ \frac{1}{3} \end{bmatrix}$$
> Now to find $\vec{c_2}$ we first find:
> $$p_2=\left(\begin{bmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{bmatrix}\cdot \begin{bmatrix} 0 \\ 3 \\ 3 \end{bmatrix}\right)\begin{bmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{bmatrix}=\begin{bmatrix} 2\\2\\1\end{bmatrix}$$
> So:
> $$\vec o_2=\begin{bmatrix} 0\\3\\3\end{bmatrix}-\begin{bmatrix} 2\\2\\1\end{bmatrix}=\begin{bmatrix} -2\\1\\2\end{bmatrix}$$
> And **normalising** gives us:
> $$\vec{c}_2 = \frac{\vec{o}_2}{|\vec{o}_2|} = \begin{bmatrix} -\frac{2}{3} \\ \frac{1}{3} \\ \frac{2}{3} \end{bmatrix}$$
> Similarly, for $\vec c_3$ we first find:
> $$p_3=\left(\begin{bmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{bmatrix}\cdot \begin{bmatrix} 1 \\ 1 \\ 5 \end{bmatrix}\right)\begin{bmatrix} \frac{2}{3} \\ \frac{2}{3} \\ \frac{1}{3} \end{bmatrix}+\left(\begin{bmatrix} -\frac{2}{3} \\ \frac{1}{3} \\ \frac{2}{3} \end{bmatrix}\cdot \begin{bmatrix} 1 \\ 1 \\ 5 \end{bmatrix}\right)\begin{bmatrix} -\frac{2}{3} \\ \frac{1}{3} \\ \frac{2}{3} \end{bmatrix}=\begin{bmatrix}2\\2\\1\end{bmatrix}+\begin{bmatrix}-2\\1\\2\end{bmatrix}=\begin{bmatrix}0\\3\\3\end{bmatrix}$$So: 
> $$\vec o_3=\begin{bmatrix}1\\1\\5\end{bmatrix}-\begin{bmatrix}0\\3\\3\end{bmatrix}=\begin{bmatrix}1\\-2\\2\end{bmatrix}$$
> And **normalising** gives:
> $$\vec{c}_3 = \frac{\vec{o}_3}{|\vec{o}_3|} = \begin{bmatrix} \frac{1}{3} \\ -\frac{2}{3} \\ \frac{2}{3} \end{bmatrix}$$
> And we now have our final **orthonormal basis**:
> $$\left\{ \begin{bmatrix} 2/3 \\ 2/3 \\ 1/3 \end{bmatrix}, \begin{bmatrix} -2/3 \\ 1/3 \\ 2/3 \end{bmatrix}, \begin{bmatrix} 1/3 \\ -2/3 \\ 2/3 \end{bmatrix}\right\}$$
