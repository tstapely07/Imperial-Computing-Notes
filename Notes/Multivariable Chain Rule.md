---
date: 2026-04-11
tags:
  - first-year
  - M40016
---
When a [[Multivariable Functions|multivariable function]]  $z$ depends on **intermediate variables** $u_1$ and $u_2$, which in turn depend on **independent variables** $x$ and $y$, we can use the **multivariable chain rule** to find the [[partial derivatives]]:
* $\frac{\partial z}{\partial x} = \frac{\partial z}{\partial u_1} \frac{\partial u_1}{\partial x} + \frac{\partial z}{\partial u_2} \frac{\partial u_2}{\partial x}$
* $\frac{\partial z}{\partial y} = \frac{\partial z}{\partial u_1} \frac{\partial u_1}{\partial y} + \frac{\partial z}{\partial u_2} \frac{\partial u_2}{\partial y}$

Let $z=\sin(u_1)+6\cos(u_2)$ with $u_1=3x+5y$ and $u_2=2x-y$.
To find $\frac{\partial z}{\partial x}$ we first find the **partial derivatives** of $z$ with respect to the **intermediates**:
* $\frac{\partial z}{\partial u_1} = \cos(u_1)$
* $\frac{\partial z}{\partial u_2} = -6 \sin(u_2)$
We then find the **partial derivatives** of the **intermediates** with respect to $x$:
* $\frac{\partial u_1}{\partial x} = 3$
* $\frac{\partial u_2}{\partial x} = 2$
We then combine our results to obtain $\frac{\partial z}{\partial x}$:
$$\frac{\partial z}{\partial x} = (\cos u_1 \cdot 3) + (-6 \sin u_2 \cdot 2)=3\cos(u_1)-12\sin(u_2)$$
Or equivalently:
$$\frac{\partial z}{\partial x} =3\cos(3x+5y)-12\sin(2x-y)$$