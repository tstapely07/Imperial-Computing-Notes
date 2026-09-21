---
date: 2026-04-08
tags:
  - first-year
  - M40008
---
> [!Theorem]
> If a [[Decision Problems|decision problem]] is in [[Class P|P]]. then it is in [[Class NP|NP]].
> $$P\subseteq NP$$

Proof:
Take some **problem** $D$ in **P**.
To verify that $D(x)$ holds, we don't need to guess some $y$, we can simply determine $D(x)$ directly.
To formally prove that $D$ is in **NP**, we must define some **verifying function** $E(x,y)$.
* So define $E(x,y)\iff D(x) \land y=\epsilon$. 
* Here, $\epsilon$ is just an empty input, and so $E(x,y)$ simply ignores the guess $y$.
Now we have:
$$D(x)\iff \exists y.E(x,y) \land |y| \le p(|x|)$$
* Since $y$ is an empty input, $|y|\le p(|x|)$ always holds.
Now we just have $D(x)\iff \exists y. E(x,y)$.
* Now there indeed does exist some $y$ if $D(x)$ holds, and so we have formally proved that $D$ is in **NP**.

> [!Note]
> It is **unknown** whether $P=NP$. 
> * In fact, this is one of the **Millennium Problems**, with a $1,000,000 prize for solving it.
> * Most researchers believe that $P\neq NP$.
