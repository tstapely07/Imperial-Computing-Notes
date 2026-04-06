---
date: 2026-03-25
tags:
  - first-year
  - M40016
---
> [!Abstract] Definition
> An **infinite series** is the **sum** of the **terms** of a [[Sequences|sequence]] $(a_n)_{n\ge1}$:
> $$\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + \dots + a_n + \dots$$

Since we cannot compute an **infinite addition**, we look at its **partial sums**:
> [!Abstract] Definition
> The $n$-th **partial sum**, $S_n$ is the **sum** of the first $n$ **terms**:
> $$S_n = \sum_{i=1}^{n} a_i = a_1 + a_2 + \dots + a_n$$

We can now form a new **sequence**, the **sequence** of **partial sums** $(S_n)_{n\ge1}$.

Let $\sum_{i=1}^\infty a_i$ be the **series** determined by the **sequence** $(a_n)_{n\ge1}$:
* The series is **convergent** to a [[Limits|limit]] $a \in \mathbb{R}$ if the **sequence** of **partial sums** $(S_n)_{n\ge1}$ **converges** to $a$.
* Otherwise, if the **limit** does not exist, or is $\pm\infty$, the **series** **diverges**.

> [!Example]
> Let $a_n=d^n$ where $d\in\mathbb{R}$. 
> This defines a **geometric series**:
> $$\sum_{n=1}^{\infty} d^n = d + d^2 + d^3 + \dots$$
> We define the **partial sum** $S_n=d+d^2+\dots+d^n$, which, for $d\neq 1$, simplifies to:
> $$S_n= \frac{d(1-d^n)}{1-d}$$
> To determine if the **series** **converges**, we examine $\lim_{n\to\infty} S_n$.
> * If $|d|\lt 1$ then $d^n\to 0$, and the **sequence** of **partial sums** converges to $\frac{d}{1+d}$, and so the **series** also **converges**.
> * Otherwise, if $|d|\ge 1$, then $d^n\to\pm\infty$, and so $S_n$ does not **converge** to a real **limit**, and the **series** **diverges**.

> [!Theorem]
> If the **series** $\sum_{n\ge1}a_n$ **converges**, then the **sequence** of its **terms** must **converge** to $0$ ($\lim_{n \to \infty} a_n = 0$)

Proof:
We can examine the **term** $a_n$, since:
$$a_n=S_n-S_{n-1}$$
Since the **series** **converges**, its **sequence** of **partial sums** must also **converge** to some limit $L$.
Therefore, as $n\to\infty$, both $S_n\to L$ and $S_{n-1}\to L$.
So, taking the **limit** of the earlier equation gives:
$$\lim_{n \to \infty} a_n = \lim_{n \to \infty} (S_n - S_{n-1}) = L - L = 0$$

> [!Note]
> Usefully, this tells us that if $a_n\not\to 0$, then the **series** definitely **diverges**.
> However, although $a_n\to 0$ is a **necessary** condition for the series to **converge**, it is not **sufficient**.
> * One example of it not being **sufficient** is the [[Harmonic Series]].




