---
date: 2026-04-11
tags:
  - first-year
  - M40016
---
To carry out [[Linear Regression (Calculus)]] for higher dimensions, we need to be able to take [[Differentiation|derivatives]] with respect to [[vectors]].

The [[Partial Derivatives|partial derivative]] of a **linear vector function** with respect to $\vec{x}$ yields the **coefficient vector**:
$$\frac{\partial}{\partial \vec{x}}(\vec{\beta}\cdot \vec{x})=\vec{\beta}$$
A **quadratic form** is a [[Matrix Rank|matrix]] **equation** that produces squared terms, and is written in the form $f(x)=x^TMx$, where $M$ is a **square matrix**.
If $M$ is a **symmetric matrix**, meaning $M=M^T$, then the derivative is:
$$\frac{\partial}{\partial \bar{x}} (x^T M x) = 2Mx$$


We now need to define the **loss function** for higher dimensions.
* We will again use the **sum of squared errors**.
For a data **matrix** $X$, a target vector $\vec{Y}$ and a weight vector $\vec{\beta}$, the **error vector** is $(X\vec{\beta}-\vec{Y})$.
We can find the **sum of squared errors** by taking the [[Inner Product|dot product]], using the **transpose**:
$$L(D,\vec{\beta})=(X\vec{\beta}-\vec{Y})^T(X\vec{\beta}-\vec{Y})$$
We can expand this to:
$$L(\vec{\beta}) = (\vec{\beta}^T X^T - \vec{Y}^T)(X\vec{\beta} - \vec{Y})$$
Multiplying out the brackets then yields:
$$L(\vec{\beta}) = \vec{\beta}^T X^T X \vec{\beta} - \vec{\beta}^T X^T \vec{Y} - \vec{Y}^T X \vec{\beta} + \vec{Y}^T \vec{Y}$$
The two middle terms equal the exact same scalar, so we can group them:
$$L(\vec{\beta}) = \vec{\beta}^T (X^T X) \vec{\beta} - 2(\vec{Y}^T X)\vec{\beta} + \vec{Y}^T \vec{Y}$$
Now to find the minimum, we can take the [[Differentiation|derivative]] with respect to $\vec{B}$ and set it to $0$.
* The first term is a **quadratic form**, which differentiates to $2X^TX\vec{\beta}$.
* The second term is a **linear term**, so its **derivative** is just the **coefficient** $2\vec{Y}^TX$, which is also equivalent to $2X^T\vec{Y}$.
* The third term is just a constant, so **differentiates** to $0$. 
This all gives us:
$$\frac{\partial L}{\partial \vec{\beta}} = 2X^T X \vec{\beta} - 2X^T \vec Y = 0$$
Now we can rearrange to get:
$$X^T X \vec{\beta} = X^T \vec Y$$
And this gives us our final **weight vector**:
$$\vec{\beta} = (X^T X)^{-1} X^T \vec{Y}$$

> [!Example]
> Let's do a worked example for three points in **2D**: $(1,1)$, $(2,2)$, and $(3,2)$.
> Now, the **target vector** $Y$ is just the $y$ values. $X$ contains the $x$ values, and also a column of $1s$ to account for the $y$-intercept:
> $$X = \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}, \quad \vec{Y} = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}$$
> Now we compute $X^TX$ as follows:
> $$X^T X = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix} = \begin{bmatrix} 3 & 6 \\ 6 & 14 \end{bmatrix}$$
> And we can find its inverse to be:
> $$(X^T X)^{-1} = \frac{1}{6} \begin{bmatrix} 14 & -6 \\ -6 & 3 \end{bmatrix} = \begin{bmatrix} 7/3 & -1 \\ -1 & 1/2 \end{bmatrix}$$
> Finally, we compute $X^T\vec{Y}$ as:
> $$X^T \vec{Y} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix} = \begin{bmatrix} 1+2+2 \\ 1+4+6 \end{bmatrix} = \begin{bmatrix} 5 \\ 11 \end{bmatrix}$$
> Now we can find the **weights vector** $\vec\beta$:
> $$\vec{\beta} = (X^T X)^{-1} X^T \vec{Y} = \begin{bmatrix} 7/3 & -1 \\ -1 & 1/2 \end{bmatrix} \begin{bmatrix} 5 \\ 11 \end{bmatrix}$$
> This gives us $\vec\beta=\begin{bmatrix} \frac{2}{3}\\\frac{1}{2}\end{bmatrix}$
> And so our final line is $y=0.5x+\frac{2}{3}$.