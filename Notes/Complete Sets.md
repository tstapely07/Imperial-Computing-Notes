---
date: 2026-03-24
tags:
  - first-year
  - M40016
---
We know from the [[Completeness Axiom]] that the entire set of real numbers ($\mathbb{R}$) is **complete**.
* We can also consider **subsets** inside $\mathbb{R}$.

> [!Abstract] Definition
> Let $A\subseteq \mathbb{R}$. $A$ is **complete** if every [[Cauchy sequence]] whose terms are entirely in $A$ has a limit that is also in $A$.

> [!Example] Examples
> * $A=\mathbb{Q}$ is **not complete**. As seen before, we can construct a **Cauchy sequence** of fractions that tends to $\sqrt{2}$. Although the sequence exists entirely inside $\mathbb{Q}$, the limit is outside of $\mathbb{Q}$.
> * $A=[0,\infty)$ is **complete**. Any **Cauchy sequence** of non-negative numbers will eventually **converge**. 
> * $A=(0,\infty)$ is **not complete**. For example the sequence $a_n=\frac{1}{n}$ consists of **positive terms**, within $A$, yet $\lim_{n\to\infty} \frac{1}{n}=0$, and $0\not\in A$.
> 