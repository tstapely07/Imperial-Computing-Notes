---
date: 2026-04-17
tags:
  - first-year
  - M40018
---
**Induction** can be used to prove statements of the form:
$$\forall x : S.P(x)$$
* Where $S$ is an **enumerable set**, and $P\subseteq S$.

For example:
* $\forall n: \mathbb{N}.(7^n+5\text{ is exactly divisible by } 5)$
* $\forall xs: [a].\forall ys: [a]. length(xs++ys)=length(xs)+length(ys)$
	* ([[Haskell]] [[lists]] are **enumerable sets**).
Note that $\mathbb{R}$ is **not enumerable**.

We formally define the **principle of mathematical induction** for any $P\subseteq \mathbb{N}$ as:
$$P(0)\;\land \;\forall k:\mathbb{N}.[P(k)\to P(k+1)]\quad \longrightarrow \quad\forall n:\mathbb{N}.P(n)$$

For example, let's write a [[Semi-Structured Proofs|proof]] using **mathematical induction** over $n$ that:
$$\forall n: \mathbb{N}.\sum_{i=0}^1=\frac{n\cdot(n+1)}{2}$$

> [!Example]
> **Base case**: 
> To show $\sum_{i=0}^0i=\frac{0\cdot(0+1)}{0}$
> $$\begin{align}
> &\sum_{i=0}^0i\\
> &=0 \text{ -- by definition of } \sum\\
> &=\frac{0\cdot (1)}{2} \text{ -- by arithmetic}\\
> &=\frac{0\cdot (0+1)}{2} \text{ -- by arithmetic}
> \end{align}$$
> **Inductive step**:
> Take arbitrary $k\in\mathbb{N}$
> Inductive hypothesis: $\sum_{i=0}^k i = \frac{k\cdot(k+1)}{2}$
> To show: $\sum_{i=0}^{k+1}i=\frac{(k+1)\cdot (k+1+1)}{2}$
> $$\begin{align}
> &\sum_{i=0}^{k+1}i\\
> &=\sum_{i=0}^{k}i+(k+1) \text{ -- by definition of }\sum\\
> &=\left(\frac{k\cdot(k+1)}{2}\right)+(k+1) \text{ -- by inductive hypothesis}\\
> &=\frac{k^2+k+2k+2}{2}\text{ -- by arithmetic}\\
> &=\frac{k^2+3k+2}{2}\text{ -- by arithmetic}\\
> &=\frac{(k+1)\cdot (k+2)}{2}\text{ -- by arithmetic}\\
> &=\frac{(k+1)\cdot (k+1+1)}{2}\text{ -- by arithmetic}\\
> \end{align}$$

> [!Warning]
> We must be aware of the cases when **induction** can fail:
> * Essentially, this can occur when we assume an **induction hypothesis** which is not **true** for everything we say it is **true** for.


What if we wanted to prove that, for the following function $\forall n\ge 1 . f \;n=\frac{n}{n+1}$:
* ![[Pasted image 20260417130421.png|436]]
* The term $f\;0$ is **undefined**, and so we cannot simply apply our **mathematical induction principle**.

In fact, we can use a **technique** that allows us to start from any number.
The principle is as follows, for any $P\subseteq\mathbb{Z}$ and any $m\in \mathbb{Z}$:
$$P(m)\;\land\; \forall k\ge m.[P(k)\to P(k+1)]\quad\longrightarrow\quad \forall n\ge m.P(n)$$
* Note that for any $Q\subseteq \mathbb{Z}$, we use $\forall j\ge m.Q(j)$ as a shorthand for $\forall j:\mathbb{Z}.[j\ge m \rightarrow Q(j)]$.

Now our proof for $\forall n\ge 1 . f \;n=\frac{n}{n+1}$ can be as follows:
* ![[Pasted image 20260417130514.png|387]]
* ![[Pasted image 20260417130532.png|385]]
* Note the additional **assumption**.

In fact, the original **principle** and this **technique** are logically **equivalent**:
* We can prove something that requires the **technique** by defining a new predicate $Q(n)=P(n+m)$, and using **induction** on $Q$ to prove $P$.