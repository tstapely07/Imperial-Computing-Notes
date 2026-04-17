---
date: 2026-04-11
tags:
  - first-year
  - M40016
---
> [!Abstract] Definition
> For a [[Multivariable Functions|multivariable function]] $f(x,y)$, a [[Critical Points|critical point]] only exists when the slope is zero in **all directions**.
> Therefore a point $(x_0,y_0)$ is a **critical point** iff:
> $$\frac{\partial f}{\partial x} = 0 \quad \text{and} \quad \frac{\partial f}{\partial y} = 0$$

> [!Example]
> For $f(x,y)=x^2-xy+y^2$, we set:
>  $$\frac{\partial f}{\partial x} =2x-y= 0 \quad \text{and} \quad \frac{\partial f}{\partial y} = -x+2y =0$$
>  We can solve this [[Systems of Linear Equations|system of linear equations]] to get the only solution, and therefore the only **critical point** as $(0,0)$.

Just like in **1D**, the rules for determining the nature of **2D critical points** come directly from the [[Taylor series]].
The **2D** **Taylor series** for a **function** around a point $(x_0,y_0)$ is:
$$f(x,y)=f(x_0,y_0)+\frac{\partial f}{\partial x}(x-x_0)+\frac{\partial f}{\partial y}(y-y_0)+\frac{1}{2}\left[\frac{\partial^2f}{\partial x^2}(x-x_0)^2+2\frac{\partial^2f}{\partial x\partial y}(x-x_0)(y-y_0)+\frac{\delta^2 f}{\delta y^2}(y-y_0)^2\right]+\dots$$
At a **critical point**, the first two values are exactly $0$, and so the **function** is dictated by the **second derivative**, and so we examine when this term equals $0$:
$$\frac{\partial^2 f}{\partial x^2}(x-x_0)^2 + 2\frac{\partial^2 f}{\partial x \partial y}(x-x_0)(y-y_0) + \frac{\partial^2 f}{\partial y^2}(y-y_0)^2 = 0$$
To solve this, we divide through by $(x-x_0)^2$:
$$\frac{\partial^2 f}{\partial x^2} + 2\frac{\partial^2 f}{\partial x \partial y} \left( \frac{y-y_0}{x-x_0} \right) + \frac{\partial^2 f}{\partial y^2} \left( \frac{y-y_0}{x-x_0} \right)^2 = 0$$
Now if we set $t=\frac{y-y_0}{x-x_0}$, we end up with a **quadratic** in $t$:
$$\left(\frac{\partial^2 f}{\partial y^2}\right) t^2 + 2\left(\frac{\partial^2 f}{\partial x \partial y}\right) t + \left(\frac{\partial^2 f}{\partial x^2}\right) = 0$$
Letting $a = \frac{\partial^2 f}{\partial y^2}$, $b = \frac{\partial^2 f}{\partial x \partial y}$, and $c = \frac{\partial^2 f}{\partial x^2}$, we get:
$$at^2+2bt+c=0$$
Now we are only interested in the number of roots, so we can consider the **sign** of the **discriminant**:
$$\Delta = (2b)^2 - 4(a)(c)=4b^2-4ac$$
Since we only care about the sign, we simply consider:
$$\Delta=b^2-ac$$
* If $\Delta \lt 0$ there are no roots, and the surface curves in the same direction everywhere, and so we have a **local maximum** or **minimum**.
	* $a$ and $c$ must have the same sign, and so we can consider either of them.
	* If $a\gt 0$ we have a **local minimum**.
	* If $a\lt 0$ we have a **local maximum**.
* If $\Delta \gt 0$ there are two roots, and the surface curves up in one direction and down in another, giving a **saddle point**.
* If $\Delta = 0$ then the test is **inconclusive**.

> [!Example]
> Let $f(x,y)=x^2-xy+y^2$. 
> * We already found a **critical point** at $(0,0)$, so lets determine its **nature**:
> 
>We first find the **second partial derivatives**:
> * $a = \frac{\partial^2 f}{\partial x^2} = 2$
> * $b = \frac{\partial^2 f}{\partial x \partial y} = -1$
> * $c = \frac{\partial^2 f}{\partial y^2} = 2$
> 
> We then find the **discriminant**:
> $$\Delta=b^2-ac=(-1)^2-(2)(2)=-3$$
> Since $\Delta \lt 0$ and $a \gt 0$, the point $(0,0)$ is a **local minimum**.

> [!Example]
> Let $f(x,y)=xy-x^3-y^2$.
> We must first find the **critical points**, so we find the **first derivatives** and set them to zero:
> * $\frac{\partial f}{\partial x}=y-3x^2=0$
> * $\frac{\partial f}{\partial y}=x-2y=0\implies x=2y$
> We can then **substitute** $x=2y$ into the first equation:
> $$y - 3(2y)^2 = 0 \implies y - 12y^2 = 0 \implies y(1 - 12y) = 0$$
> This gives $y=0$ or $y=\frac{1}{12}$
> And so our **critical points** are $(0,0)$ and $\left( \frac{1}{6}, \frac{1}{12} \right)$
> Now we find the **second partial derivatives**:
> * $a = \frac{\partial^2 f}{\partial x^2} = -6x$
> * $b = \frac{\partial^2 f}{\partial x \partial y} = 1$
> * $c = \frac{\partial^2 f}{\partial y^2} = -2$
> 
> For the point $(0,0)$:
> * $a=0,b=1,c-2$
> * This gives the **discriminant** $\Delta =b^2-ac=1^2-(0)(-2)=1$
> * Since $\Delta \gt 0$, the point $(0,0)$ is a **saddle point**.
> 
> For the point $\left( \frac{1}{6}, \frac{1}{12} \right)$:
> * $a=-1,b=1,c-2$
> * This gives the **discriminant** $\Delta =b^2-ac=1^2-(-1)(-2)=-1$
> * Since $\Delta \lt 0$ and $a\lt 0$, the point $\left( \frac{1}{6}, \frac{1}{12} \right)$ is a **local maximum**.

When we have a **saddle point**, it means the surface is crossing the **horizontal tangent plane**. 
* We can actually find these **lines of intersection**, by calculating the roots of the **quadratic equation**, and using the fact that $t=\frac{y}{x}$.
Note that for a function with powers higher than $2$, away from the **critical point** the surface will warp.
* In these cases, the **lines** obtained are only **instantaneous tangents**.

> [!Example]
> For $f(x,y)=x^2-y^2$ at ($0,0$), we have:
> * $a=2,b=0,c=-2$, and so $\Delta=4\gt 0$, confirming we have a **saddle**.
> We get the solutions for $t=\pm1$, and so $y=\pm x$ gives the two lines where the **surface** crosses the **plane.**
> 
> This image makes this easier to visualise:
> * ![[Pasted image 20260411122519.png|246]]

