---
date: 2026-03-22
tags:
  - first-year
  - M40016
---
> [!Lemma]
> If a [[Sequences|sequence]] $(a_n)_{n\ge 1}$ converges to $a\in\mathbb{R}$, then it is **bounded**.

The proof goes as follows:
Let $\epsilon=1$. Since $(a_n)_{n\ge 1}$ **converges**, there exists $N\gt 0\;s.t.\;|a_n-a|\lt1\;\forall n\gt N$.
For these $n\gt N$ we now apply the [[Triangle Inequality (Calculus)|triangle inequality]]:
$$|a_n|=|a_n-a+a|\le|a_n-a|+|a|\lt1+|a|$$
To find a **bound** for the entire **sequence**, we must also account for the **finite** number of terms before $N$:
$$k=\max\set{|a_1|,|a_2|\,\dots,|a_N|,1+|a|}$$
Then, $\forall n\ge1$ it holds that $|a_n|\le k$.
And so the **sequence** $(a_n)_{n\ge1}$ is **bounded** by $k$.