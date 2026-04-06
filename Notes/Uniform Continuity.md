---
date: 2026-03-24
tags:
  - first-year
  - M40016
---
> [!Abstract] Definition
> Let $f:I\to\mathbb{R}$ be a **function** defined on an (open or closed) **interval** $I$.
> $f$ is **uniformly continuous** on $I$ if for every $\epsilon\gt 0$, there exists a $\delta \gt 0$ such that for all $x,x_0\in I$, if $|x-x_0|\lt\delta$, then $|f(x)-f(x_0)|\lt\epsilon$.

Essentially, this means that $\delta$ is **independent** of $x_0$, unlike standard [[continuity]].

> [!Example]
> Claim: The **function** $f(x)=\frac{1}{x}$ is **continuous** on the **open interval** $(0,1)$ but it is not **uniformly continuous**.
> Proof:
> Set $\epsilon=1$.
> Let $\delta\gt 0$.
> Because the **function** tends to $\infty$ as it approaches $0$, regardless how small $\delta$ is, there are always two points $x,x_0\in(0,1)$ such that $|x-x_0|\lt\delta$, but $|f(x)-f(x_0)|\ge 1$, since the **slope** is near vertical close to the $y$-axis. 
> Therefore $f(x)=\frac{1}{x}$ is not **uniformly continuous**.

Claim: $f(x)=x^2$ is **uniformly continuous** on $[a,b]$.
Proof:
Let $\epsilon\gt 0$.
We need to examine the difference $|x^2-x_0^2$|. By factoring, this becomes:
$$|x-x_0||x+x_0|$$
By the [[Triangle Inequality (Calculus)|triangle inequality]], we know:
$$|x+x_0|\le |x|+|x_0|$$
Since both $x$ and $x_0$ are **bounded** within $[a,b]$, their absolute values cannot exceed some maximum value $M=\max(|a|,|b|)$. Therefore:
$$|x+x_0|\le 2M$$
Substituting this bound gives:
$$|x^2-x_0^2|\le |x-x_0|(2M)$$
Now we define $\delta=\frac{\epsilon}{2M}$. This means for any $|x-x_0|\lt\delta$ it follows that:
$$|x^2 - x_0^2| \le |x - x_0|(2M) < \left(\frac{\epsilon}{2M}\right)(2M) = \epsilon$$
This matches our definition, so $f(x)=x^2$ is indeed **uniformly continuous**.
* The chosen $\delta$ depended solely on $\epsilon$ and the **interval**, it was entirely independent of $x_0$.


> [!Theorem]
> If a **function** is **uniformly continuous** on an **interval**, it is **continuous** on every point inside that **interval**.


> [!Theorem]
> If a **function** is **continuous** on a **closed interval**, $[a,b]$, it is **uniformly continuous** on $[a,b]$.

Proof by **contradiction**:
Assume that some **function** $f$ is **continuous** on $[a,b]$, but is not **uniformly continuous**.
This means that there is some $\epsilon\gt 0$ such that for any arbitrarily small $\delta$, say $\delta=\frac{1}{n}$, there exists a pair of points $x_n$ and $y_n$ inside $[a,b]$ such that:
$$|x_n - y_n| < \frac{1}{n} \quad \text{but} \quad |f(x_n) - f(y_n)| \ge \epsilon$$
Because the [[Sequences|sequence]] $(x_n)_{n\ge1}$ is **bounded** within $[a,b]$, it must have a [[Bounded Sequences have a Convergent Subsequence|convergent subsequence]]:
* We call this [[Subsequences|subsequence]] $(x_{n_k})_{k\ge1}$, with [[Limits|limit]] $L$.
* Since the **interval** is **closed**, $L\in[a,b]$.
Because the distance $|x_n-y_n|$ collapses to $0$ as $n\to\infty$, the **subsequence** $(y_{n_k})_{k\ge1}$ must also **converge** to the same **limit** $L$.
Since $f$ is **continuous** in $[a,b]$, both **output sequences** must **converge** to the same value:
$$\lim_{k \to \infty} f(x_{n_k}) = f(L) \quad \text{and} \quad \lim_{k \to \infty} f(y_{n_k}) = f(L)$$
And therefore:
$$\lim_{k \to \infty} |f(x_{n_k}) - f(y_{n_k})| = 0$$
Now since $\epsilon\gt 0$, we know that $0\lt \epsilon$, which contradicts our assumption, giving us a **contradiction**.
Therefore the **function** is indeed **uniformly continuous**.

