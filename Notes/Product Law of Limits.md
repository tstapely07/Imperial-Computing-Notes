---
date: 2026-03-22
tags:
  - first-year
  - M40016
---
> [!Theorem]
> If $\lim_{n\to\infty} a_n=A$ and $\lim_{n\to\infty} b_n=B$ then $\lim_{n\to\infty}(a_nb_n)=AB$

Assume $A\neq 0$, since this would be a trivial case.
Let $\epsilon\gt 0$. 
We require $N\in\mathbb{N}\;s.t.\;\forall n\gt N, |a_nb_n-AB|\lt\epsilon$
Now we can add and subtract $Ab_n$ to obtain:
$$|a_nb_n-AB|=|(a_nb_n-Ab_n)+(Ab_n-AB)|$$
Now we factor the grouped terms and apply the [[Triangle Inequality (Calculus)|triangle inequality]]:
$$\begin{gather}
|(a_nb_n-Ab_n)+(Ab_n-AB)|=|b_n(a_n-A)+A(b_n-B)|\\
\le |b_n(a_n-A)|+|A(b_n-B)|\\
=|b_n||a_n-A|+|A||b_n-B|
\end{gather}$$
Since $(b_n)_{n\ge1}$ is **convergent**, we know it is [[Convergent Sequences are Bounded|bounded]].
We can substitute this into our inequality to obtain:
$$|a_nb_n-AB|\le k|a_n-A|+|A||b_n-B|$$
We need to show that this expression is $\lt\epsilon$, which we can do by showing each half to be less than $\frac{\epsilon}{2}$:
* Since $lim_{n\to\infty}a_n=A$, $\exists N_1\in\mathbb{N}\;s.t.\;\forall n\gt N_1:|a_n-A|\lt \frac{\epsilon}{2k}$
* Since $lim_{n\to\infty}b_n=B$, $\exists N_2\in\mathbb{N}\;s.t.\;\forall n\gt N_2:|b_n-B|\lt \frac{\epsilon}{2|A|}$
Now let $N=\max(N_1,N_2)$, now $\forall n\gt N$:
$$|a_nb_n-AB|\lt k\left( \frac{\epsilon}{2k} \right)+|A|\left( \frac{\epsilon}{2|A|} \right)=\frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon$$
We have shown that $\forall \epsilon \gt 0,\exists N\in\mathbb{N}\;s.t.\;\forall n\gt N:|a_nb_n-AB|\lt\epsilon$, we can conclude that $\lim_{n\to\infty}(a_nb_n)=AB$.

