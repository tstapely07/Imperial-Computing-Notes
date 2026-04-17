---
date: 2026-04-07
tags:
  - first-year
  - M40008
---
> [!Abstract] Definition
> A [[Decision Problems|decision problem]] $D(x)$ is in the [[Orders of Complexity|complexity]] **class P** if it can be decided within **polynomial time** $p(n)$, where $n=|x|$. 
> 

We say that a **problem** in class P can be solved in **p-time**.

> [!Abstract] Definition
> A **problem** that cannot be solved in **p-time** is called **intractable**.

**Arithmetic operations** are **p-time**.
* They are **polynomial** in $|n|=\log n$.
* This is because a number $n$ is represented by $\log n$ digits, so the **input size** is $\log n$

> [!Theorem]
> If $f$ is some **p-time** function, then its **output size** $|f(x)|$ is **polynomially bounded** in the **input size** $|x|$. For some **polynomial** $p(n)$:
> $$|f(x)|\le p(|x|)$$
> * This is because there is simply no **time** to construct a larger **output**.

> [!Theorem]
> If $f$ and $g$ are two **p-time computable** functions, then $g\circ f$ is also **p-time computable**.

Proof:
Suppose $f(x)$ is **computed** by **algorithm** $A$ within time $p(n)$, where $n=|x|$.
Suppose $g(y)$ is **computed** by **algorithm** $B$ within time $q(m)$, where $m=|y|$.
Take some input $x$ with $|x|=n$.
We compute $g(f(x))$ by first running $A$ on $x$ to obtain $f(x)$, and then running $B$ on $f(x)$ to get $g(f(x))$.
Running $A$ on $x$ takes $\le p(n)$ steps.
* Since $f(x)$ is built in $\le p(n)$ steps, $|f(x)|$ must be **polynomially bounded** in $n$, so $|f(x)|\le p'(n)$ for some **polynomial** $p'(n)$.
Now $B$ runs in $q(p'(n))$ steps.
The total running time is therefore $p(n)+q(p'(n))$, which is indeed a **polynomial** in $n$.