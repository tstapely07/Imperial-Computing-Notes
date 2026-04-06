---
date: 2026-03-24
tags:
  - first-year
  - M40016
---
> [!Theorem]
> If a **function** $f:[a,b]\to\mathbb{R}$ is [[Continuity|continuous]] on the **closed interval** $[a,b]$, then it attains its [[Supremum and Infimum|supremum]] and [[Supremum and Infimum|infimum]].
> 

We will prove the case for the **supremum**, that there exists some input $c\in[a,b]$, where $f(c)=\sup\set{f(x):x\in[a,b]}$.
* The proof for the **infimum** is almost identical.
Proof:
Since $f$ is **continuous**, we know the set of its outputs is [[Continuous Functions are Bounded|bounded]].
By the [[Completeness Axiom]], this set must have a **supremum**.
* Let $M=\sup\set{f(x):x\in[a,b]}$.
Since $M$ is the **least upper bound**, if we decrease it by $\frac{1}{n}$, it is no longer an **upper bound**.
* Therefore, for every integer $n\ge1$, there must exist some input $x_n\in[a,b]$ that outputs a value strictly higher than the decreased **upper bound**:
$$M-\frac{1}{n}\lt f(x_n)\le M$$
This gives us a [[Sequences|sequence]] of inputs $(x_n)_{n\ge1}$. 
* Because all these inputs are from the **set** $[a,b]$, the sequence is clearly **bounded**.
We know that [[bounded sequences have a convergent subsequence]].
* Let $(x_{n_k})_{k\ge1}$ be this **subsequence** that **converges** to a [[Limits|limit]] $c$.
Because the **interval** is **closed**, $c\in[a,b]$.
Because $f$ is **continuous** everywhere, in $[a,b]$, including at $c$, it must be true that $\lim_{k\to\infty} f(x_{n_k})=f(c)$.
Now, looking at the inequality from before, as $k\to\infty$, $\frac{1}{n_k}\to0$, so by the squeeze theorem, $\lim_{k\to\infty}f(x_{n_k})=M$.
Now since this **limit** equals both $f(c)$ and $M$, by transitivity, $f(c)=M$. 
Therefore the **function** does indeed attain its **supremum**.