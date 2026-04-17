---
date: 2026-04-14
tags:
  - first-year
  - M40017
---
The **PageRank algorithm** is used by **Google** to rank **webpages**.
Let $x_i$ be the **importance score** of some **page** $i$, and let $N_i$ be the total number of **outbound links** form **page** $i$.
* **Page** $i$ shares its **importance score** equally between all the **pages** that it **link** to.
Thus the importance of a some **page** $i$ is the **sum** of the **value** of all **incoming links**:
$$x_i=\sum \frac{x_j}{N_j}$$

> [!Example]
> Consider this simplified **web**:
> * ![[Pasted image 20260414184415.png|157]]
> The **importance scores** are given by the following equations:
> * $x_1=x_3+\frac{x_4}{2}$
> * $x_2=\frac{x_1}{3}$
> * $x_3=\frac{x_1}{3}+\frac{x_2}{2}+\frac{x_4}{2}$
> * $x_4=\frac{x_1}{3}+\frac{x_2}{2}$
> This is a [[Systems of Linear Equations|system of linear equations]], and so can be rewritten as a [[Matrices|matrix]]:
> $$\begin{bmatrix}x_1\\x_2\\x_3\\x_4\end{bmatrix}=
> \begin{bmatrix}0 & 0 & 1 & \frac{1}{2}\\ \frac{1}{3}&0 & 0 & 0\\ \frac{1}{3}& \frac{1}{2} & 0 & \frac{1}{2}\\ \frac{1}{3} & \frac{1}{2} & 0 & 0\end{bmatrix}
> \begin{bmatrix}x_1\\x_2\\x_3\\x_4\end{bmatrix}$$

In general, we can represent the **importance scores** as a **matrix** **vector** multiplication:
$$\vec x= A\vec x$$
* $\vec x$ is the **importance vector**, containing each **page's importance score**.
* $A$ is the **link matrix**, where $a_{ij}$ is defined as:
$$a_{ij}=\begin{cases} \frac{1}{N_j} & \text{if page } j\text{ links to page } i \\ \\
0 & \text{otherwise}\end{cases}$$
Note that finding $\vec x$ is equivalent to finding the [[Eigenvectors and Eigenvalues|eigenvector]] of $A$ corresponding to the **eigenvalue**  $\lambda = 1$.

> [!Example]
> For the same example as before, we end up with:
> $$E_1=\operatorname{span}\left\{\begin{bmatrix}12\\4\\9\\6\end{bmatrix}\right\}$$
> And so the **PageRank** is $P_1\gt P_3\gt P_4\gt P_2$.

If $1$ is not an **eigenvalue** of $A$, then we would find $E_1=\operatorname{span}\set \vec 0$, which is clearly useless.
Fortunately, unless a **page** has no **out links**, $A$ is a [[column-stochastic matrix]], and therefore is guaranteed to have an **eigenvalue** of $1$.

For **PageRank** to give us a definitive ranking, we must get a unique **importance vector**, and so the [[Eigenspaces|eigenspace]] for $\lambda=1$ must have **dimension** $1$, and therefore only give a **single eigenvector**.

If the **web** is **strongly connected**, then the **dimension** is indeed $1$.
* Let $A$ be the **link matrix** for the **web**, consisting of $n$ **pages**.
* The $ij$-th entry of $A^k$ will be $\gt 0$ if there is a path from **page** $i$ to **page** $j$ in exactly $k$ steps.
* Because $A$ is **column-stochastic**, so is $A^k$.
* We can define $B$ as follows:
$$B=\frac{1}{n}(I+A+A^2+\dots+A^{n-1})$$
* As an average of **column-stochastic matrices**, $B$ is also **column-stochastic**.
We can prove all **eigenvectors** corresponding to the **eigenvalue** $1$ have the **same sign** by **contradiction**.
* Let $\vec x$ have **entries** of **mixed sign** such that $\vec x = B \vec x$.
* Let $B_i$ give the $i$-th **row** of $B$.
* Any entry $x_i=B_i\vec x=\sum_j b_{ij}x_j$.
Since the **entries** of $\vec x$ have mixed signs, but $b_{ij}\gt 0$, the terms that **sum** to $x_i$ must have **mixed signs**:
* $\set{b_{i1}x_1,b_{i2}x_2,\dots,b_{in}x_n}$ have **mixed signs**.
We can then reach the following **strict inequality**, since some terms must cancel out:
* $|x_i|=|\sum_{j=1}^nb_{ij}x_j|\lt\sum_{j=1}^nb_{ij}|x_j|$
By **summing** the **left** and **right** side, we get:
$$\sum_i |x_i|\lt \sum_i\sum_j b_{ij}|x_j|=\sum_j\left(\sum_i b_{ij}\right)|x_j|$$
But, $\sum_i b_{ij}$ is the **sum** of the **entries** in the $j$-th **column** of $B$.
* Since $B$ is **column-stochastic**, we have $\sum_i b_{ij}=1$.
So by only considering the left and right terms of this new **inequality** we end up with:
$$\sum_i |x_i|\lt \sum_j|x_j|$$
* These terms are **equal**, so we have a **contradiction**.
Therefore the **eigenvectors** of $B$ must have **entries** of the **same sign**.
We can now prove that $\operatorname{dim}(E_1(B))=1$:
* For **contradiction**, assume $\operatorname{dim}(E_1(B))\gt1$
* So there must be some **plane** that is a [[Vector Subspaces|subspace]] of $E_1(B)$.
* Any **2D** plane passing through the **origin** must cross into different **quadrants**, and so must contain **vectors** with **mixed signs**.
* However we know any **eigenvector** of $B$ must not contain **mixed signs**, and so we have a **contradiction**.
Therefore $\operatorname{dim}(E_1(B))$ is indeed $1$.
Finally, we can show that if $\vec x\in E_1(A)$ then $\vec x\in E_1(B)$:
* Because $\vec x = A\vec x$, we have:
$$\begin{gather}B\vec x=\frac{1}{n}(I+A+A^2+\dots+A^{n-1})\vec x=\frac{1}{n}(I\vec x+A\vec x + A^2\vec x+\dots+A^{n-1}\vec x)=\\
\frac{1}{n}(\vec x+\vec x+\dots + \vec x)= \frac{1}{n}(n\vec x)=\vec x\end{gather}$$
* And so since $B\vec x = \vec x$, we have $\vec x \in E_1(B)$.
And now we have:
$$0\lt \operatorname{dim}(E_1(A))\lt \operatorname{dim}(E_1(B))=1$$
And so $\operatorname{dim}(E_1(A))$ is indeed $1$, and we have a **unique** **eigenvector** and a **unique ranking**.

However, the **web** in reality is **disconnected**, and so we need a solution to achieve a **unique ranking**.
We define a new **matrix** $C$ where every entry is $1/n$, with $n$ being the **total** number of **pages** on the **web**.
* This represents a **fully connected web**, where every **page** links to every other **page** equally.
We now calculate the final **matrix** as:
$$M=(1-d)A+dC$$
* Where $0\lt d\lt 1$ is some **damping factor**. **Google** originally used $d=0.15$.
The only other issue is when a **page** has zero **out links**:
* To solve this, we set every **entry** in its **column** to $\frac{1}{n}$.
* This could be achieved by setting $d=1$ for these specific **columns**.
We now have a **matrix** $M$ that is **column-stochastic** and suitable to run the **PageRank** algorithm on.

However, since the **web** features **billions** of **pages**, computing the **eigenspace** $E_1(M)+\operatorname{ker}(M-I)$ is unfeasible, and so we must find a faster way.
Every other **eigenvalue** is less **dominant** than the **eigenvalue** $1$.
* i.e. $|\lambda|\lt 1$.
We show this by **contradiction**. 
* Assume there exists some **eigenvalue** $\lambda \gt 1$.
* Since the [[determinant]] of a **matrix** and its **transpose** is the same, and therefore the **characteristic polynomial** is the same, $\lambda$ is also an **eigenvalue** of $M^\top$. Let $\vec x$ be the corresponding **eigenvector**.
* So we have:
$$M^\top \vec x=\lambda \vec x$$
Now let $x_{max}$ be the greatest **entry** in $\vec x$. 
* Therefore the **maximum entry** in the **vector** $\lambda \vec x$ is $\lambda x_{max}\gt x_{max}$.
* But, with $R_i=\begin{bmatrix}r_{i1}&r_{i2}&\dots&r_{in}\end{bmatrix}$ being the $i$-th **row** of $M^\top$, we have:
$$M^T\vec x=\begin{bmatrix}R_1\vec x\\R_2\vec x\\\vdots \\R_n\vec x\end{bmatrix}$$
* Since $M^\top$ is **column stochastic**, we have $r_{ij}\gt 0$, and $\sum_j r_{ij}=1$, and so $R_i\vec{x}$ is a **convex sum** and cannot be greater than $x_{max}$.
Since the **maximum entry** in $M^\top \vec x_{max}$ is $\le x_{max}$ this **contradicts** with our $\lambda x_{max}\gt x_{max}$, and so $1$ must indeed be the **dominant eigenvalue**.

Now, according to the **power convergence theorem**, from any **arbitrary vector**, $\vec x$, repeated multiplication by $M$ will cause $\vec{x}$ to **converge** towards some **eigenvector** corresponding to the **dominant eigenvalue** of $M$.
In our case, with $1$ as the **dominant eigenvalue**, we have:
$$\lim_{k\to\infty}M^k\vec{x}\in E_1$$
And since $E_1$ is of **dimension** $1$, $\lim_{k\to\infty}M^k\vec x$ converges perfectly to our **importance vector** and therefore our **ranking**.