---
date: 2026-03-22
tags:
  - first-year
  - M40016
---
> [!Abstract] Definition
> We say a [[Sequences|sequence]] $(a_n)_{n\ge 1}$ **converges** to a **limit** $l$ (written $\lim_{n\to\infty} a_n=l$) iff:
> $$\forall \epsilon > 0, \exists N\in\mathbb{N} \text{ such that } \forall n > N : |a_n - \ell| < \epsilon$$
> 

> [!Abstract] Definition
> A **sequence** **converges** to $\infty$ (written $\lim_{n\to\infty}a_n=\infty$) if f $\forall r\in \mathbb{R},\exists N\in\mathbb{N}\;s.t.\;\forall n\ge N, a_n\gt r$.
> 

> [!Abstract] Definition
> A **sequence** **converges** to $-\infty$ (written $\lim_{n\to\infty}a_n=-\infty$) if f $\forall r\in \mathbb{R},\exists N\in\mathbb{N}\;s.t.\;\forall n\ge N, a_n\lt r$.
> 

> [!Abstract] Definition
> A **sequence** **diverges** if it does not **converge** to a real number or $\pm\infty$.

As an example, lets prove the limit for a **convergent** geometric series:
Prove that $\lim_{n\to\infty} ar^n=0$ given $|r|\lt 1$.
Let $\epsilon\gt 0$. We need $N\in \mathbb{N}$ such that for all $n\gt N$:
$$|ar^n-0|\lt \epsilon$$
This is equivalent to $|a||r|^n\lt \epsilon$

We split this into two cases:
If $a=0$ then $|0|\lt \epsilon$ is true for all $\epsilon\gt 0$, so we can choose $N=1$.
Otherwise, if $a\neq 0$ we can divide by $|a|$ to get:
$$|r|^n\lt \frac{\epsilon}{|a|}$$
Taking logs gives:
$$n\ln|r|\lt ln\left(\frac{\epsilon}{|a|}\right)$$
Now we divide by $\ln|r|$. Note that this is negative, since $|r|\lt 1$, so we flip the sign:
$$n\gt \frac{\ln\left( \frac{\epsilon}{|a|} \right)}{\ln|r|}$$
So we take $N=\left\lceil \frac{\ln\left( \frac{\epsilon}{|a|} \right)}{\ln|r|}\right\rceil$

For another example, let's prove that $(a_n)_{n\ge1}$ converges to $\infty$:
Let $r\in\mathbb{R}$ be given. We require $N$ such that for all $n\gt N,a_n\gt r$.
So we require:
$$\sqrt{n}\gt r$$
Squaring both sides yields:
$$n\gt r^2$$
So we choose $N=\lceil r^2 \rceil$.
For all $n\gt N$ it follows that $n\gt r^2$, and so $\sqrt{n}\gt r$.
Since we can find an $N$ for any arbitrary $r$, we conclude that $\lim_{n\to\infty}\sqrt{n}=\infty$.

There are many useful **laws** of **limits**, including:
* [[Addition Law of Limits]] - $\lim_{n\to\infty}(a_n+b_n)=\lim_{n\to\infty}a_n+\lim_{n\to\infty}b_n$
* [[Negation Law of Limits]] - $\lim_{n\to\infty}(-a_n)=-\lim_{n\to\infty}a_n$
* [[Subtraction Law of Limits]] - $\lim_{n\to\infty}(a_n-b_n)=\lim_{n\to\infty}a_n-\lim_{n\to\infty}b_n$
* [[Product Law of Limits]] - $\lim_{n\to\infty}(a_nb_n)=\lim_{n\to\infty}a_n\times\lim_{n\to\infty}b_n$
* [[Reciprocal Law of Limits]] - $lim_{n\to\infty}\left( \frac{1}{a_n} \right)=\frac{1}{\lim_{n\to\infty}a_n}$
* [[Quotient Law of Limits]] - $\lim_{n\to\infty} (\frac{a_n}{b_n})=\frac{\lim_{n\to\infty}a_n}{\lim_{n\to\infty}b_n}$

Limits are **unique**.
This means that if $lim_{n\to\infty}a_n=l$ and $lim_{n\to\infty}a_n=l'$, then $l=l'$.
We can prove this by contradiction:
* Suppose $l\neq l'$.
* Let $\epsilon=\frac{|l-l'|}{2}\gt 0$.
* Because $a_n\to l, \exists N_1\;s.t.\;\forall n\gt N_1,|a_n-l|\lt \frac{|l-l'|}{2}$.
* Also, because $a_n\to l, \exists N_2\;s.t.\;\forall n\gt N_2,|a_n-l|\lt \frac{|l-l'|}{2}$.
* For $n\gt \max(N_1,N_2)$, both inequalities must hold, but since we took $\epsilon$ as the midpoint of the two limits, $a_n$ cannot be sufficiently close to both simultaneously, so we have a contradiction.
We could also prove this directly:
* Let $\epsilon\gt 0$.
* $\exists N_1\;s.t.\;\forall n\gt N_1,|a_n-l|\lt \frac{\epsilon}{2}$
* $\exists N_2\;s.t.\;\forall n\gt N_2,|a_n-l|\lt \frac{\epsilon}{2}$
* Let $n\gt \max(N_1,N_2)$, using the [[Triangle Inequality (Calculus)|triangle inequality]]:
$$\begin{gather}|l-l'|=|l-a_n+a_n-l'|\\
\le |l-a_n|+|a_n-l'|\\
\lt \frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon
\end{gather}$$
* Since $|l-l'|\lt \epsilon$ for any **arbitrary** $\epsilon\gt 0$, the distance between them must be $0$, and so $l=l'$.
