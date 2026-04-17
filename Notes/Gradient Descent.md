---
date: 2026-04-11
tags:
  - first-year
  - M40016
---
The **gradient** of a [[Multivariable Functions|multivariable function]] $f(x,y)$ is a [[Vectors|vector]] containing its first [[partial derivatives]]:
$$\nabla f = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix}$$
**Gradient descent** is a numerical method, like [[Newton's method]] used to find the **local minimum** of a **surface** $z=f(x,y)$.
* It works by taking iterative steps in the opposite direction of the **gradient**.

Starting from some **initial** guess $\mathbf{x}_0 = (x_0, y_0)$, we find the next point $\mathbf{x}_1=(x_1,y_1)$ by the rule:
$$\mathbf{x}_1 = \mathbf{x}_0 - \eta \nabla f(\mathbf{x}_0)$$
Here, $\eta\gt 0$ is the **learning rate**, and controls how far we move in each step. 

We can prove that this strictly decreases the value of the function by using the **first-order multivariable** [[Taylor series]] **expansion**:
$$f(x_1, y_1) \approx f(x_0, y_0) + (x_1 - x_0)\frac{\partial f}{\partial x} + (y_1 - y_0)\frac{\partial f}{\partial y} $$
Using the [[Inner Product|dot product]], this is equivalent to:
$$f(\mathbf{x}_1)\approx f(\mathbf{x}_0)+(\mathbf{x}_1-\mathbf{x}_0)\cdot \nabla f(\mathbf{x}_0)$$
Now we substitute our rule for $(\mathbf{x}_1 - \mathbf{x}_0)$:
$$f(\mathbf{x}_1) \approx f(\mathbf{x}_0) + \Big(-\eta \nabla f(\mathbf{x}_0)\Big) \cdot \nabla f(\mathbf{x}_0)$$
The **dot product** of any vector with itself is equal to its magnitude squared ($\vec{v}\cdot \vec{v}=|\vec{v}|^2$), which gives us:
$$f(\mathbf{x}_1) \approx f(\mathbf{x}_0) - \eta |\nabla f(\mathbf{x}_0)|^2$$
Since $\eta$ is **positive**, and the squared magnitude must always be positive, the term $-\eta |\nabla f(\mathbf{x}_0)|^2$ is **negative**, and so:
$$f(\mathbf{x}_1) \leq f(\mathbf{x}_0)$$
This proves that, as long as we are close enough to our original guess for the **Taylor series approximation** to hold, every step of **gradient descent** will result in a lower function value, and so we get closer to a **minimum** on every step.
 * The only time $f(\mathbf{x}_1) = f(\mathbf{x}_0)$ is when the **partial derivatives** are all $0$, meaning we have already reached the **minimum**.
* We can ensure sufficient closeness by picking a sufficiently small $\eta$.