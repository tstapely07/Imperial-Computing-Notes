---
date: 2026-04-14
tags:
  - first-year
  - M40017
---
In **linear regression**, we aim to find some **linear equation** that predicts some **output** $y$ based on $n$ **inputs** $(x_1,x_2,\dots,x_n)$:
$$y = \hat{w}_0 + \hat{w}_1x_1 + \hat{w}_2x_2 + \dots + \hat{w}_nx_n$$
Given some **dataset** with $l$ **datapoints** of the form $d_i=(y_i,x_{1,i},x_{2,i},\dots,x_{n,i})$, we aim to find the **weights** ($\hat{w}_0, \hat w_1\dots, \hat{w}_n$) that **minimise** the following **loss function**:
$$L(w_0, \dots, w_n) = \sum_{i=1}^{l} \left( (w_0 + w_1x_{1,i} + \dots + w_nx_{n,i}) - y_i \right)^2$$
* In [[40016 - Calculus|Calculus]], we achieved this using [[differentiation]], however that is not necessary.

Let us first define a [[Vectors|vector]] of **weights** $\vec w$, a **vector** of **inputs** $\vec x_i$ and a **vector** of **outputs**:
$$\vec w=\begin{bmatrix} w_0\\w_1\\\vdots\\w_n\end{bmatrix}_{(n+1)\times 1};\quad \vec x_i=\begin{bmatrix}1\\x_{1,i}\\\vdots\\x_{n,i}\end{bmatrix}_{(n+1)\times 1};\quad \vec y = \begin{bmatrix} y_1\\y_2\\\vdots \\y_l\end{bmatrix}_{l\times 1}$$
* Note the first element in $\vec x_i$ being a $1$ to handle the **constant term**.
Now, the **loss function** can be written:
$$L(w_0,w_1,\dots,w_n)=\sum_{i=1}^l((\vec x_i\cdot\vec w)-y_i)^2=\sum_{i=1}^l(\vec x_i^\top\vec w-y_i)^2$$
We can define a [[Matrices|matrix]] $X$ as:
$$X=\begin{bmatrix}\vec x_1^\top\\\vec x_2^\top\\\vdots\\\vec x_n^\top\end{bmatrix}_{l\times (n+1) }$$
* Each **row** is now one of the **input vectors**.
And now the **loss function** is even simpler:
$$L(w_0,w_1,\dots,w_n)=|X\vec w - \vec y|^2$$
Of course, $X\vec w$ must be in the [[image]] of $X$, which itself is a [[Vector Subspaces|subspace]] of $\mathbb{R}^l$:
$$X\vec w\in \operatorname{Im}(X)\subseteq \mathbb{R}^l$$
* Also, $\vec y$ is of course in $\mathbb{R}^l$.
When we minimise **loss**, we are trying to find the vector $\hat{\vec w}$ such that $X\hat{\vec w}$ is as close as possible to $\vec y$.
* This means that $X\vec w$ is **exactly** the [[Orthogonal Projection Matrix|orthogonal projection]] of $\vec y$ onto $\operatorname{Im}(X)$:
$$X\hat{\vec w}=\underset{\operatorname{Im}(X)}{\operatorname{Pr}}(\vec y)$$
And so:
$$X\hat{\vec w}=X(X^\top X)^{-1} X^\top \vec y$$
Therefore we can define the **weights** as:
$$\hat{\vec w}=(X^\top X)^{-1} X^\top \vec y$$

Note that fitting a **polynomial curve** to training data still counts as **linear regression**, since the **inputs** $x,x^2,\dots x^n$ are treated as **constants** when we populate the **matrix** $X$.
* So the equation $y = w_0 + w_1x + w_2x^2 + \dots + w_nx^n$ is still **linear** with respect to the **weights**, and we can use **linear regression**.

