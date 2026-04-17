---
date: 2026-04-11
tags:
  - first-year
  - M40016
---
Instead of using the **determinant** of the **quadratic term** of the [[Taylor series]] to classify the **nature** of the [[Multivariable Critical Points|critical points]] of a [[Multivariable Functions|multivariable]] function, we evaluate the the [[Partial Derivatives|second partial derivatives]]:
* $a=\frac{\delta^2f}{\delta x^2}(x_0,y_0)$
* $b=\frac{\delta^2f}{\delta x\delta y}(x_0,y_0)$
* $c=\frac{\delta^2f}{\delta y^2}(x_0,y_0)$
We can then organise these into a [[Matrices|matrix]] known as the **Hessian matrix**:
$$H = \begin{bmatrix} a & b \\ b & c \end{bmatrix} = \begin{bmatrix} \frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\ \frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2} \end{bmatrix}$$
The **nature** of the point $(x_0,y_0)$ is given by the [[determinant]] of the **Hessian**, $det(H)=ac-b^2$.
* If $ac-b^2\gt 0$ and $a\gt0$ we have a **local minimum**.
* If $ac-b^2\gt 0$ and $a\lt0$ we have a **local maximum**.
* If $ac-b^2\lt 0$ we have a **saddle point**.
* If $ac-b^2=0$ the test is **inconclusive**.

The power of the **Hessian matrix** is that, unlike the simple **determinant** of the **quadratic** method, we can extend it up to higher **dimensions**.
