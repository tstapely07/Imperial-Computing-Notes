---
date: 2026-04-13
tags:
  - first-year
  - M40008
---
> [!Abstract] Definition
> [[P vs NP|Assume]] that $P\ne NP$. If a [[Decision Problems|decision problem]] $D$ is [[NP-hard]], then $D\notin P$. 

Proof:
Assume that $P\neq NP$ and $D$ is **NP-hard**.
Suppose that $D\in P$.
Take any random problem from [[Class NP|NP]], $D'\in NP$. because $D$ is **NP-hard**, $D'\le D$.
Because $D'\le D$ and $D\in P$, the rules of [[Reduction|reduction]] state that $D'\in P.
* Therefore any **problem** in $NP$ is also in [[Class P|P]], and so $NP\subseteq P$.
Since we have $P\subseteq NP$ already, and have just shown that $NP\subseteq P$, this implies $P=NP$, which contradicts our initial assumptions.
Therefore, as desired $D\notin P$.

Therefore, if we can prove a problem is in [[NP-Complete|NPC]], then we know it is **intractable**.
* This assumes $P\neq NP$, which is widely believed, but not yet proven.