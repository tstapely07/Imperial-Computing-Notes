---
date: 2026-03-24
tags:
  - first-year
  - M40016
---
> [!Theorem]
> Every [[Cauchy sequence]] in $\mathbb{R}$ is **convergent**.

Let $(a_n)_{n\ge1}$ be a **Cauchy sequence**. 
We already know that [[Cauchy Sequences are Bounded|every Cauchy sequence is bounded]]. 

Because the [[Sequences|sequence]] is **bounded**, we know it has a [[Bounded Sequences have a Convergent Subsequence|convergent subsequence]].
* Let $(a_{n_i})_{i\ge1}$ be this [[Subsequences|subsequence]], and let it converge to a [[Limits|limit]] $A$.

Now we must show that the original **Cauchy sequence** $(a_n)_{n\ge1}$ also **converges** to $a$.
Let $\epsilon\gt0$.
Because $(a_n)_{n\ge1}$ is **Cauchy**, $\exists N\in\mathbb{N}$ such that for all $n,m\gt N$:
$$|a_n-a_m|\lt \frac{\epsilon}{2}$$
Additionally, we just showed that because the **subsequence** converges to $A$, $\exists I_0\in\mathbb{N}$ such that for all $i\gt I_0$:
$$|a_{n_i}-A|\lt \frac{\epsilon}{2}$$
We need a specific **term** from the **subsequence** that satisfies by both conditions. Let $i$ be an index such that $i\gt \max(N,I_0)$.
Because $n_i\ge i$, we also have $n_i\gt N$.
Now for any $n\gt N$, we compare this to the **limit** $A$, and add and subtract the specific **subsequence term** $a_{n_i}$:
$$|a_n-A|=|a_n-a_{n_i}+a_{n_i}-A|$$
Now we apply the [[Triangle Inequality (Calculus)|triangle inequality]]:
$$|a_n-A|\lt|a_n-a_{n_i}|+|a_{n_i}-A|$$
Since both $n$ and $n_i$ are greater than $N$, the first term is $\lt \frac{\epsilon}{2}$. Also, since $i\gt I_0$, the second term is also $\lt \frac{\epsilon}{2}$. Hence:
$$|a_n-A|\lt\frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon$$
Since we have found an $N$ such that for all $n\gt N$, $|a_n-A|\lt \epsilon$, we have proven that the **Cauchy sequence** indeed converges to $A$.
