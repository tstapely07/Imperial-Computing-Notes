---
date: 2026-03-23
tags:
  - first-year
  - M40016
---
> [!Abstract] Definition
> A **term** $a_k$ is a **peak** of the [[Sequences|sequence]] $(a_n)_{n\ge1}$ if:
> $$a_k\ge a_m\; \text{for all }m\gt k$$

> [!Theorem]
> For any **sequence** $(a_n)_{n\ge1}$ there exists a [[Subsequences|subsequence]] $(a_{n_i})_{i\ge1}$ that is **monotonic**.

Proof:
We can examine the parent sequence and split it into two **mutually exclusive** cases:
Case 1 - the sequence has infinitely many **peaks**.
Let the **peaks** be located at indices $n_1\lt n_2\lt n_3\lt\dots$
Consider the **subsequence** formed entirely by these peaks: $(a_{n_i})_{i\ge1}$.
By the definition of a **peak**, every **peak** must be greater than or equal to everything that comes after it.
And so $a_{n_1}\ge a_{n_2}\ge a_{n_3}\ge\dots$. This **subsequence** is **decreasing** and therefore **monotonic**.

Case 2 - the sequence as finitely many **peaks**.
Since there are only finitely many **peaks**, let $K$ be the index of the final **peak**.
* If there are zero **peaks**, let $K=0$.
For all $n\gt K$, the **term** $a_n$ is not a **peak**.
Let $n_1=K+1$. Because $a_{n_1}$ is not a **peak**, there must exist some **term** after it that is larger. 
* We call this **term** $a_{n_2}$, where $n_2\gt n_1$. We have $a_{n_1}\lt a_{n_2}$.
Now look at $a_{n_2}$, similarly, since it is also not a **peak**, there must exist some $n_3\gt n_2$ such that $a_{n_2}\lt a_{n_3}$.
We can repeat this process infinitely, creating a **subsequence** $a_{n_1}\lt a_{n_2}\lt a_{n_3}\lt\dots$.
This **subsequence** is strictly **increasing**, and therefore **monotonic**.

Since every **sequence** falls into one of the two cases, every **sequence** indeed contains a **monotonic subsequence**.

