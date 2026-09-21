---
date: 2026-04-13
tags:
  - first-year
  - M40008
---
**Reduction** gives us a formal way to categorise a problem as "harder" than another.

> [!Abstract] Definition
> Suppose $D$ and $D'$ are two [[decision problems]]. We say that $D$ **(many-one) reduces** to $D'$, written $D\le D'$ if there is a [[Class P|p-time]] computable **function** $f$ such that:
> $$D(x)\iff D'(f(x))$$
> * $f$ can be a **many-one function**, i.e. reducing many $x$ to the same output.

> [!Proposition]
> Suppose $D\le D'$ and $D'\in P$. Then $D\in P$.

Proof:
Suppose we have some **algorithm** $A'$ which decides $D'$ in $p'(n)$ time. We also have $f$, which runs in $p(n)$ time.
We can now construct an **algorithm** $A$ which decides $D$ by first computing $f(x)$, and then running $A'$ on $f(x)$ and returning the result.
* Since we know **composition** of **p-time** functions is **p-time**, we can conclude that $A$ runs in **p time**, and so indeed $D\in P$.

> [!Proposition]
> Suppose $D\le D'$ and $D'\in NP$. Then $D\in NP$.

Proof:
We have $E'(x,y)\in P$ and some **polynomial** $p'(n)$ such that $D'(x) \iff \exists y.E'(x,y)$, and if $E'(x,y)$ then $|y|\le p'(|x|)$.
* We also have $D(x) \iff D'(f(x))$ by **reduction**, and so we obtain $f(x)\iff \exists y.E'(f(x),y)$.
We now define $E(x,y)\iff E'(f(x),y)$ and so $D(x)\iff \exists y.E(x,y)$. 
* We have $E\in P$ by **composition** of **p-time** **functions**.
We must check that $E$ is **p-balanced**, i.e. $y$ is **bounded** by a **polynomial function** of $x$.
* We know $|y|\le p'(|f(x)|)$
* We also know $|f(x)|\le q(|x|)$ 
* Therefore $|y|\le p'(q(|x|))$.
* Since the **composition** of **p-time functions** is a **p-time** function, $E$ is indeed **p-balance**.
And so indeed $D\in NP$.

Reduction has a few more **properties**:
* **Reflexive** - $D\le D$.
* **Transitive** - if $D\le D'$ and $D'\le D''$ then $D\le D''$.
* If $D\le D'$ and $D'\le D$ we write $D\sim D'$.