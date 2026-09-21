---
date: 2026-04-17
tags:
  - first-year
  - M40018
---
[[Mathematical induction]] allows the **inductive step** ($k+1$) to refer to the direct predecessor ($k$).
* **Strong induction** allows the **inductive step** ($k+1$) to refer to **any** predecessor, e.g. to $k$, $k-1$, or $k-2$.

The **principle of strong induction** is as follows:
*$$P()\;\land\;\forall k:\mathbb{N}.[\forall j\in [0..k].P(j)\to P(k+1)]\quad\longrightarrow\quad \forall n:\mathbb{N}.P(n)$$
* Note that $j\in[m..n]$ is shorthand for $m\le j\le n$ and $j\in [m..n)$ is shorthand for $m\le j\lt n$.

> [!Example]
> We now prove that this function satisfies the property $\forall n:\mathbb{N}. g\;n=3^n-2^n$:
> * ![[Pasted image 20260417131914.png|530]]
> Applying the **strong induction principle** gives us:
> * ![[Pasted image 20260417131936.png|479]]
> The [[Semi-Structured Proofs|proof]] is then as follows:
> * ![[Pasted image 20260417132105.png|454]]
> * ![[Pasted image 20260417132121.png|472]]
> * ![[Pasted image 20260417132155.png|476]]
> * Note that we add to consider $k=0$ separately, since otherwise $k-1$ would not be defined.
> * Cases like these are where **strong induction** can yield **false** **proofs** if we are not careful.

> [!Note]
> **Strong induction** is actually **equivalent** to **mathematical induction**:
> * **Strong induction** is trivially powerful enough to prove a statement that can be proved by **mathematical induction**.
> * **Mathematical induction** can **simulate** **strong induction** by using some predicate $Q(n)$ that represents "$P$ is true for all values up to $n$".


  