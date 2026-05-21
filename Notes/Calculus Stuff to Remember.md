# Definitions
**Supremum** - "super" - **upper bound**:
* $b=\sup A$ iff $b$ is an **upper bound** and $\forall \epsilon\gt 0,\exists a\in A\;s.t.\;b-\epsilon\lt a\le b$
**Infimum** - **lower bound**:
* $c=\inf A$ iff $c$ is a **lower bound** and $\forall \epsilon\gt 0, \exists a \in A\;s.t.\;|c \le a \lt c+\epsilon$

**Triangle inequality**:
$$|a+b| \le |a|+|b|$$
And **reverse triangle inequality**:
$$|a-b| \ge ||a|-|b||$$

**Sequence** **converges** to $l$ iff:
$$\forall \epsilon\gt 0,\exists N\in \mathbb{N}\;s.t.\;\forall \gt N :|a_n-l| \lt \epsilon$$
**Converges** to $\infty$ iff:
$$\forall r\in \mathbb{R},\exists N\in \mathbb{N}\;s.t.\;\forall n\ge N, a_n\gt r$$
Lots of arithmetic laws apply to **limits**.



**Sandwich theorem**:
* If $\lim_{n\to\infty}a_n=L$ and $\lim_{n\to\infty}b_n=L$ and $\exists N_0\in \mathbb{N}\;s.t.\;\forall n\gt N_0:a_n\le c_n\le b_n$ then $\lim_{n\to\infty}c_n=L$.

A **subsequence** is obtained by removing some terms from the original **sequence**.

A **sequence** is a **Cauchy sequence** iff:
$$\forall\epsilon\gt 0,\exists N\in\mathbb{N}\;s.t.\;\forall m,n\gt N: |a_n-a_m|\lt \epsilon$$

A set is complete if every **Cauchy sequence** whose terms are in the set has a limit in the set:
* From below, $\mathbb{R}$ is **complete**.
* $A=[0,\infty)$ is **complete**.
* $A=(0,\infty)$ is **not complete** - consider $a_n=\frac{1}{n}$

**Ratio test**:
If $\exists r\in\mathbb{R}\;s.t.\;0\le 1\lt 1\land \forall n:|\frac{a_{n+1}}{a_n}|\le r$, then $\lim_{n\to\infty}a_n=0$.
Also true if $\lim_{n\to\infty}| \frac{a_{n+1}}{a_n}|=r\lt 1$.

**Limits of functions**: $f(x)\to l$ as $x\to x_0$ iff for every **sequence** $(x_n)_{n\ge1}$ that converges to $x_0$, $f(x_n)_{n\ge1}$ converges to $l$.
Equivalently, $f(x)\to l$ as $x\to x_0$ iff for every $\epsilon\gt 0$, exists $\delta$ such that if $|x-x_0|\lt \delta$ then $|f(x)-l|\lt \epsilon$.
* Can show no **limit** by showing two **sequences** that **converge** to $x_0$ but their **sequences** of outputs $f(x_n)_{n\ge1}$ have different **limits**. 

A **function** is **continuous** at $x_0$ if $\lim_{x\to x_0}f(x)=f(x_0)$.
* Which combed with above is iff for every $\epsilon \gt 0$, exists $\delta$ such that $|x-x_0|\lt \delta\implies |f(x)-f(x_0)|\lt \epsilon$.
A **function** is **continuous** in a range if it is continuous at every point within that range.

**Intermediate value theorem** if $f:[a,b]\to\mathbb{R}$ is **continuous** and $s\in\mathbb{R}$ such that $f(a)\lt s\lt f(b)$ then exists $c\in (a,b)$ such that $f(c)=s$.

A **function** is **uniformly continuous** on $I$ if for every $\epsilon \gt 0,\exists \delta\gt 0$ such that $\forall x,x_0\in I$, if $|x-x_0|\lt \delta$ then $|f(x)-f(x_0)|\lt \epsilon$.
* Here, $\delta$ is independent of $x_0$.

An **infinite series** is the **sum** of the **terms** of a **sequence**.
* We consider **partial sums**.
* If the **sequence of partial sums** converges to $a\in\mathbb{R}$ then the **series converges.

For positive terms, if for all $n\ge 1$, $\frac{a_{n+1}}{a_n}\le l\lt 1$ then $\sum a_n$ **converges**.
Similarly, if for all $\lim_{n\to\infty} \frac{a_{n+1}}{a_n}=L$:
* $L\lt 1\implies$ **converges**.
* $L\gt 1\implies$ **diverges**.
* $L= 1\implies$ **inconclusive**.

**Comparison test** is self explanatory, need to show **inequality** starts from a certain point.
**Limit comparison test** works by sequence/convergent or divergent/sequence. If the limit exists, then behaviour matches.

**Absolutely converges** if **sum** of **absolute values converges**.
* **Convergent but not absolutely convergent** - **conditionally convergent**.

**Limit superior** is the **greatest** **limit** of any **subsequence**.
**Limit inferior** is the **least** **limit** of any **subsequence**.
* The **standard limit** exists iff the $\liminf$ and $\limsup$ are equal.

The **root test** is like the **limit ratio test**, but we instead test:
$$L=\limsup_{n\to\infty}\sqrt[n]{|a_n|}$$
* $L\lt 1\implies$ **converges absolutely**.
* $L\gt 1\implies$ **diverges**.
* $L= 1\implies$ **inconclusive**.
If we can evaluate $\lim_{n\to\infty}\sqrt[n]{|a_n|}$ directly, then the $\limsup$ must equal this.

**Lower integral** is **supremum** of all **lower sums**:
$$\underline\int_a^bf(x)\;dx=\underset{P}\sup S^l(f,p)$$
**Upper integral** is **infimum** of **upper sums**.
Integrable iff upper and lower integral are same.

**Partition** is just a finite sequence that divides interval into subintervals.
Lower and upper sums are sums across a partition:
$$S^l(f,P)=\sum_{i=1}^n(r_i-r_{i-1})\underset{x\in [r_{i-1},r_i]}\inf f(x)$$
Similar for upper sum just with $\sup$.

Improper integrals are just done using limits - standard.

Integral test for series - requires function to be strictly positive, and strictly decreasing.

Derivative given by limit.

To be differentiable, must be continuous, but this is not sufficient.

Rolle's theorem states if $f$ is continuous and differentiable and $f(a)=f(b)$ then there must be a $c$ such that $f'(c)=0$.
* Proof by considering minimum and maximum.

Mean value theorem states:
$$f'(c)=\frac{f(b)-f(a)}{b-a}$$
Which also gives $f(x)=f(x_0)+f'(c)(x-x_0)$

Fundamental theorem of calculus states that for:
$$g(x)=\int_a^xf(t)\;dt$$
* $g'(x_0)=f(x_0)$

We can also define an integral using general sample points, where $c_i$ is any point in the subinterval:
$$S(f,P)=\sum_{i=1}^n(r_i-r_{i-1})f(c_i)$$
* As $||P||\to 0$, the sum will converge to the same value, the value of the integral.

Expanding the mean value theorem we get:
$$f(x)=f(x_0)+(x-x_0)f'(x_0)+\frac{(x-x_0)^2}{2!}f''(x_0)+\dots+\frac{(x-x_0)^{n-1}}{(n-1)!}f^{(n-1)}(x_0)+R_n(x)$$
Where $R_n(x)=\frac{(x-x_0)^n}{n!}f^{(n)}(x^*)$
$$f(x)\sum_0^\infty \frac{(x-x_0)^n}{n!}f^{(n)}(x_0)$$
Maclaurin series is Taylor series at $x_0=0$.

L'Hôpital's rule - if indeterminate form, can differentiate top and bottom.

Power series is general term for Taylor series and Maclaurin series (and others).
* Within radius of convergence, we can manipulate power series like standard polynomials.
* New radius of convergence is minimum of previous one.

Smooth functions are differentiable everywhere, infinitely many times.
* Analytic functions have a valid Taylor series expansion that perfectly represents them, for some radius of convergence $R\neq 0$.

By differentiating term by term we can solve differential equations using power series.

In a partial derivative, we treat all other variables as constant.

In a single-variable function, a critical point occurs when the $f'(x)=0$.
* We categorise it using the first non zero higher order derivative
* If $n$ is odd then we have a point of inflection.
* If $n$ is even then we look at the sign to determine minimum or maximum.

For multivariable functions, we use the 2D Taylor series, but essentially just consider $b^2-ac$. if $\gt 0$ two roots, so surface curves up in one direction and down in another, giving a saddle.
* If $\lt 0$ we look at $a$. $a\gt 0$ means minimum, $a\lt 0$ means maximum.
* $b^2-ac=0$ is inconclusive.

From solutions of $at^2+2bt+c=0$, with $t=\frac{y}{x}$ we can find the lines where the surface crosses the tangential plane.

The Hessian is another way to classify critical points, and extends up to multiple dimensions.

Multivariable chain rule is a thing.
Here $z$ depends on $u_1$ and $u_2$, which in turn depend on $x$ and $y$.
* $\frac{\partial z}{\partial x} = \frac{\partial z}{\partial u_1} \frac{\partial u_1}{\partial x} + \frac{\partial z}{\partial u_2} \frac{\partial u_2}{\partial x}$
* $\frac{\partial z}{\partial y} = \frac{\partial z}{\partial u_1} \frac{\partial u_1}{\partial y} + \frac{\partial z}{\partial u_2} \frac{\partial u_2}{\partial y}$

Newton's method is given by:
$$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$$

Gradient descent uses $\nabla f = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix}$ and states that:
$$\mathbf{x}_1=\mathbf x_0-\eta\nabla f(\mathbf x_0)$$

To show a metric space we need to show:
* $d(x,y)=0\iff x=y$
* $d(x,y)=d(y,x)$
* $d(x,z)\le d(x,y)+d(y,z)$
This enforces $d(x,y)\ge 0$ (consider $d(x,x)\le d(x,y)+d(y,x)$)

Linear regressions requires us to minimise:
$$L(D,m,c)=\sum_{i=1}^n(mx_i+c-y_i)^2$$
We do this using **partial derivatives** and obtain:
* $c=\bar y -m \bar x$
* $m=\frac{x\cdot y-n\bar x\bar y}{x\cdot x-n \bar x^2}$

Or for multidimensional data sets, where $X$ is the $x$ values and $Y$ is the $Y$ values:
$$\vec \beta=(X^\top X)^{-1}X^\top\vec Y$$
To get the constant value, the first column of $X$ should be $1$s.
E.g. for the points $(1,1),(2,2),(3,2)$ we would have:
$$X = \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}, \quad \vec{Y} = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}$$
Computing $\vec\beta$ gives $\vec\beta = \begin{bmatrix} \frac{2}{3}\\\frac{1}{2}\end{bmatrix}$ so our line is $y=0.5x+\frac 2 3$.


# Facts
**Convergent sequences are bounded.**

**If a sequence converges to a non-zero limit its term are eventually strictly bounded away from 0.**

**Every subsequence converges to the same limit as its parent sequence.**

**Every sequence has a monotonic subsequence** - consider peaks.

**Bounded sequences have a convergent subsequence** - consider monotonic subsequence, which is also bounded.

**Cauchy sequences are bounded.**

**Every non-empty subset** $A\subseteq\mathbb{R}$ **with an upper bound has a supremum in** $\mathbb{R}$**.**

**Every Cauchy sequence in** $\mathbb{R}$ **is convergent** - consider bounded and so convergent subsequence.

**Convergent sequences are Cauchy**.

**Continuous functions are bounded** - by contradiction, and bounded sequences having a convergent subsequence, so using continuity to reach a contradiction.

**If a function is continuous on a closed interval then it obtains its supremum and infimum.**

**If a function is uniformly continuous on an interval, it is continuous on every point inside that interval.**

**If a function is continuous on a closed interval, it is uniformly continuous on that closed interval.**

**If a series converges, the sequence of its terms must converge to** $0$**.**

**A series with non-negative terms converges iff its sequence of partial sums is bounded above.**

**Absolute convergence implies convergence.**

**Continuous functions are integrable.**

**A bounded function is integrable iff its set of discontinuities is countable.**

**A limit can be pushed inside a continuous function.** 