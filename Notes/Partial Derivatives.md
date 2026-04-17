---
date: 2026-04-11
tags:
  - first-year
  - M40016
---
> [!Abstract] Definition
> When taking the [[Differentiation|derivative]] of a [[Multivariable Functions|function with multiple variables]], such as $z=f(x,y)$, we **differentiate** with respect to one variable, while treating all the other **variables** as **constants**.
> * $\frac{\partial f}{\partial x}$ is the **partial derivative** with respect to $x$.
> * $\frac{\partial f}{\partial y}$ is the **partial derivative** with respect to $y$.

> [!Example]
> For $z=x^2-xy+y^2$:
> * $\frac{\partial z}{\partial x}=2x-y$
> * $\frac{\partial z}{\partial x}=-x+2y$
> 

We can also take the **partial derivative** multiple times, with respect to the same or different **variables**:
* $\frac{\partial^2 f}{\partial x^2} = \frac{\partial}{\partial x}(\frac{\partial f}{\partial x})$
* $\frac{\partial^2 f}{\partial x^2} = \frac{\partial}{\partial x}(\frac{\partial f}{\partial x})$

If the **mixed partial derivatives** exist and are [[Continuity|continuous]] in a disk around a point, they are equal:
$$\frac{\partial^2 f}{\partial x\partial y} =\frac{\partial^2f}{\partial y\partial x}$$

Continuing from the previous example for $z=x^2-xy+y^2$, we find:
* $\frac{\partial^2z}{\partial x^2}=2$
* $\frac{\partial^2z}{\partial y^2}=2$
* $\frac{\partial^2 z}{\partial x\partial y} =\frac{\partial^2z}{\partial y\partial x}=-1$

