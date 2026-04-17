---
date: 2026-04-11
tags:
  - first-year
  - M40016
---
**Newton's method** is a numerical technique used to find the root of a [[Differentiation|differentiable function]] $y=f(x)$.
We begin with an initial guess $x_0$ near to the actual root $x^*$, and **iterate** using the following formula:
$$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$$
* The method fails if we obtain $f'(x_n)=0$ at any point, in this case, we should attempt a different initial guess.

The method is derived from the following formula for a straight line:
$$y-y_0=m(x-x_0)$$
Let the point $(x_0,y_0)$ be our current guess $(x_n, f(x_n))$.
* This means $m=f'(x_n)$.
Now we have the following equation:
$$y - f(x_n) = f'(x_n)(x - x_n)$$
To find the our next guess, we find where this tangent line crosses the x-axis by setting $y=0$:
$$-f(x_n) = f'(x_n)(x_{n+1} - x_n)$$
And this gives the formula for **Newton's method** as desired:
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

We can prove that **Newton's method** converges to the true root $x^*$ using the **second-order** [[Taylor series]].
Let's expand the function, now $f(y)$ to avoid variable clashes, around our current guess $x_n$:
$$f(y) = f(x_n) + f'(x_n)(y - x_n) + \frac{f''(c)}{2!}(y - x_n)^2$$
Note that $c$ is some number between $y$ and $x_n$, as we defined in the **Lagrange remainder**.
Now plugging in $y=x^*$ gives the following, noting that $f(x^*)=0$:
$$0 = f(x_n) + f'(x_n)(x^* - x_n) + \frac{f''(c)}{2}(x^* - x_n)^2$$
Now, assuming $f'(x_n)\neq 0$, we divide through by $f'(x_n)$:
$$0 = \frac{f(x_n)}{f'(x_n)} + (x^* - x_n) + \frac{f''(c)}{2f'(x_n)}(x^* - x_n)^2$$
With some rearranging, we get:
$$(x_n - x^*) - \frac{f(x_n)}{f'(x_n)} = \frac{f''(c)}{2f'(x_n)}(x^* - x_n)^2$$
And now, $x_n-\frac{f(x_n)}{f'(x_n)}$ is exactly $x_{n+1}$, so we can substitute that in:
$$x_{n+1} - x^* = \frac{f''(c)}{2f'(x_n)}(x^* - x_n)^2$$
To simplify the maths, lets define $K$ as the maximum value of $\left| \frac{f''(c)}{2f'(x_n)} \right|$ in the region near the **root**. This gives:
$$|x_{n+1}-x^*|\le K|x_n-x^*|^2$$
This proves that if the error is some fraction, it shrinks to $0$ extremely fast.
* This is known as **quadratic convergence**.
This also tells us that our initial guess, $x_0$ must be within $\frac{1}{K}$ from $x^*$ in order for **Newton's method** to find the **root**.