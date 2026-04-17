---
date: 2026-04-11
tags:
  - first-year
  - M40016
---
**Linear regression** uses [[Multivariable Functions|multivariable]] calculus to find the line of best fit for a set of **data points** $D=\set{(x_1,y_1),(x_2,y_2),\dots,(x_n,y_n)}$.

We need some **loss function**, that gives the error between our line, and the actual data points.
The **sum of squared errors** is one such **loss function**, and is defined as:
$$L(D,m,c)=\sum_{i=1}^n(mx_i+c-y_i)^2$$

If we force the line through the origin, giving $c=0$, then the function is simply:
$$L=\sum_{i=1}^n(mx_i-y_i)^2$$
We can then take the [[Differentiation|derivative]] with respect to $m$, and set it equal to $0$:
$$\frac{dL}{dm}=2\sum_{i=1}^nx_i(mx_i-y_i)=0$$
This then simplifies to:
$$m\sum x_i^2 - \sum x_i y_i = 0$$
Which, using the [[Inner Product|dot product]] simplifies to:
$$m = \frac{x \cdot y}{x \cdot x}$$


To solve for both $m$ and $c$ we must instead consider when both [[partial derivatives]] are $0$.
For $c$, we have:
$$\frac{\partial L}{\partial c} = 2\sum (mx_i + c - y_i) = 0$$
Which simplifies to:
$$m\sum x_i + nc - \sum y_i = 0$$
Dividing through by $n$ gives us: 
$$m\frac{\sum x_i}{n} + c - \frac{\sum y_i}{n} = 0$$
We now recognise these terms as the **mean** of $x$ and $y$, giving us our formula for $c$ as:
$$c=\bar{y}-m\bar{x}$$
We can now substitute this formula for $c$ into our **partial derivative** with respect to $m$:
$$\frac{\partial L}{\partial m} = 2\sum x_i(mx_i + c - y_i) = 0$$
With some rearranging, we obtain our final formula for the **gradient**:
$$m = \frac{x \cdot y - n\bar{x}\bar{y}}{x \cdot x - n\bar{x}^2}$$


For larger datasets, where $y_i=\beta_0+\beta_1 x_i$ we can use [[matrices]] to represent the **data** as:
$$\begin{bmatrix} 1 & x_1 \\ 1 & x_2 \\ \vdots & \vdots \\ 1 & x_n \end{bmatrix} \begin{bmatrix} \beta_0 \\ \beta_1 \end{bmatrix} = \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix}$$