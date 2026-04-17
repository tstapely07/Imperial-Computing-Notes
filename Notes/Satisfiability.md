---
date: 2026-04-13
tags:
  - first-year
  - M40008
---
> [!Problem] SAT Problem
> Given a **formula** $\phi$ in **conjunctive normal form**, is $\phi$ **satisfiable**.

It would seem that **SAT** is not decidable in [[Class P|p-time]], since we would have to try all possible assignments, which is **exponential**.
* Of course this cannot be guaranteed, since $P\overset{?}=NP$.

However **SAT** does belong to [[Class NP|NP]].

Let $Ver\text{-}SAT(\phi,v) \iff \phi\text{ is in CNF and }v\text{ satisfies }\phi$.
Then we have:
* $SAT(\phi)\iff \exists v.Ver\text{-}SAT(\phi,v)$
* If $Ver\text{-}SAT(\phi,v)$ then $|v|\le |\phi|$.
	* $Ver\text{-}SAT$ is **p-balanced**.